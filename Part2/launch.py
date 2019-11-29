import argparse
import os
import time

import googleapiclient.discovery

credential_path = "./MyProject.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

def create_instance(compute, project_id, zone, name, bucket, image_family, image_proj,
    disk_size, machine):
    image_response = compute.images().getFromFamily(
        project=image_proj, family=image_family).execute()
    source_disk_image = image_response['selfLink']

    machine_type = "zones/%s/machineTypes/%s" % (zone, machine)
    startup_script = open(
        os.path.join(
            os.path.dirname(__file__), 'startup-script.sh'), 'r').read()
    image_url = "http://storage.googleapis.com/gce-demo-input.photo.jpg"
    image_caption = "Ready for dessert?"

    config = {
        'name': name,
        'machineType': machine_type,

        'disks': [
            {
                'boot': True,
                'autoDelete': True,
                'initializeParams': {
                    'sourceImage': source_disk_image,
                    'diskSizeGb': disk_size,
                }
            }
        ],

        'networkInterfaces': [{
            'network': 'global/networks/default',
            'accessConfigs': [
                {'type': 'ONE_TO_ONE_NAT', 'name': 'External NAT', "natIP": '*.*.*.*'}
            ]
        }],

        'serviceAccounts': [{
            'email': 'default',
            'scopes': [
                'https://www.googleapis.com/auth/devstorage.read_write',
                'https://www.googleapis.com/auth/logging.write'
            ]
        }],

        'metadata': {
            'items': [{
                'key': 'startup-script',
                'value': startup_script
            }, {
                'key': 'url',
                'value': image_url
            }, {
                'key': 'text',
                'value': image_caption
            }, {
                'key': 'bucket',
                'value': bucket
            }]
        }
    }

    return compute.instances().insert(
        project=project_id,
        zone=zone,
        body=config).execute()

def wait_for_operation(compute, project, zone, operation):
    print('Waiting for creation to finish...')
    while True:
        result = compute.zoneOperations().get(
            project=project,
            zone=zone,
            operation=operation).execute()

        if result['status'] == 'DONE':
            print('Finished creation. ')
            if 'error' in result:
                raise Exception(result['error'])
            return result

        time.sleep(1)

def main(project_id, zone, name, bucket, image_family, image_proj, disk_size, machine):
    compute = googleapiclient.discovery.build('compute', 'v1')

    print('Creating instance.')

    operation = create_instance(compute, project_id, zone, name, bucket, image_family,
        image_proj, disk_size, machine)
    wait_for_operation(compute, project_id, zone, operation['name'])

    print("""
Instance created.
It will take minutes for the instance to complete work.
Check this URL: http://storage.googleapis.com/{}/output.png
    """.format(bucket))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('project_id', help='Google Cloud Project ID')
    parser.add_argument('bucket_name', help='Google Storage Bucket Name')
    parser.add_argument('--zone', default='us-central1-a', help='Zone of the instance to deploy')
    parser.add_argument('--name', default='instance-1', help='Instance name')
    parser.add_argument('--image_proj', default='debian-cloud', help='Source Image Project. For public images, please refer to https://cloud.google.com/compute/docs/images')
    parser.add_argument('--image_family', default='debian-9', help='Source Image Series')
    parser.add_argument('--disk_size', default='10', help='Disk Size in GB, at least 10')
    parser.add_argument('--machine', default='n1-standard-1', help='Machine Type. For predefined machine types, please refer to https://cloud.google.com/compute/docs/machine-types')

    args = parser.parse_args()

    main(args.project_id, args.zone, args.name, args.bucket_name, args.image_family,
        args.image_proj, args.disk_size, args.machine)
