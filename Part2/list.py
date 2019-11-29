import argparse
import os
import time

import googleapiclient.discovery

credential_path = "./MyProject.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

def list_instances(compute, project, zone):
    result = compute.instances().list(project=project, zone=zone).execute()
    return result['items'] if 'items' in result else None

def main(project, zone):
    compute = googleapiclient.discovery.build('compute', 'v1')

    instances = list_instances(compute, project, zone)

    print('Instances in project %s and zone %s: ' % (project, zone))
    print(' - instance name \t instance status')
    for instance in instances:
        print(' - ' + instance['name'] + ' \t\t' + instance['status'] )

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('project_id', help='Google Cloud Project ID')
    parser.add_argument('--zone', default='us-central1-a', help='Zone of the instances locate')

    args = parser.parse_args()

    main(args.project_id, args.zone)
