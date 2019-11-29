import argparse
import os
import time

import googleapiclient.discovery

credential_path = "/home/$USER/MyProject.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

def delete_instance(compute, project_id, zone, name):
    return compute.instances().delete(
        project=project_id,
        zone=zone,
        instance=name).execute()

def wait_for_operation(compute, project, zone, operation):
    print('Waiting for delete operation to finish...')
    while True:
        result = compute.zoneOperations().get(
            project=project,
            zone=zone,
            operation=operation).execute()

        if result['status'] == 'DONE':
            print('Deletion has done. ')
            if 'error' in result:
                raise Exception(result['error'])
            return result

        time.sleep(1)

def main(project, zone, instance_name):
    compute = googleapiclient.discovery.build('compute', 'v1')

    print('Deleting instance.')

    operation = delete_instance(compute, project, zone, instance_name)
    wait_for_operation(compute, project, zone, operation['name'])

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('project_id', help='Google Cloud Project ID')
    parser.add_argument('--zone', default='us-central1-a', help='Zone of the instance to delete')
    parser.add_argument('--name', default='instance-1', help='Instance name')

    args = parser.parse_args()

    main(args.project_id, args.zone, args.name)
