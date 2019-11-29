# Part One of The Term Project

##### PLEASE THOROUGHLY READ THIS README BEFORE BEGIN TO USE

This part provides a simple tool to help you to create and manage instances on your Google Cloud Platform. It is based on the document from Google Cloud Client Libraries for Python https://cloud.google.com/compute/docs/tutorials/python-guide. 

For more information about Google Cloud Platform, please refer to https://cloud.google.com/. Click `Console` on the upper right corner to enter your Google Cloud Platform Console. 

## Set up your environment

If you have not installed Python, please install Python first. (Python 3 recommended)

Install Anaconda: https://www.anaconda.com/distribution/

Or just install Python: https://www.python.org/downloads/

Set up Python development environment by referring to https://cloud.google.com/python/setup. 

Login to Google Cloud Platform Dashboard, create a project, remember the Project ID. Then go to Storage part, create a storage bucket, remember the bucket name. 

Create a service account key by referring to https://cloud.google.com/docs/authentication/getting-started. Create a json key file is recommended. 

## Just Before You Run

Download all the files under this folder, modify ```credential_path``` at Line 7 to the path where your service account key file locate. 

## Run

### Parameters:

All these parameters except [Project ID] and [Bucket Name] have default parameters. 

[Project ID] is the Google Cloud Project ID. 

[Bucket Name] is the Google Cloud Storage Bucket Name. 

[ZONE] is where you want your instance deploy, for more information about zone, please refer to https://cloud.google.com/compute/docs/regions-zones/. Default is 'us-central1-a'. 

[INSTANCE NAME] is the new instance name. Default is 'instance-1'. 

[SOURCE IMAGE PROJECT] and [SOURCE IMAGE FAMILY] are the images you want to deploy on the instance, for more information about source images, please refer to https://cloud.google.com/compute/docs/images. Default of [SOURCE IMAGE PROJECT] is 'debian-cloud', and default of [SOURCE IMAGE FAMILY] is 'debian-9'. 

[DISK SIZE IN GB] is the disk size of the instance, it should at least be 10. Default is '10'.

[MACHINE TYPE] is the machine type of the instance, for more information about machine type, please refer to https://cloud.google.com/compute/docs/machine-types. Default is 'n1-standard-1'. 

### Run Scripts

To create an instance:

```
python create.py [Project ID] [Bucket Name] --zone [ZONE] --name [INSTANCE NAME] --image_proj [SOURCE IMAGE PROJECT] --image_family [SOURCE IMAGE FAMILY] --disk_size [DISK SIZE IN GB] -- machine [MACHINE TYPE]
```

To list instances in a zone:

```
python create.py [Project ID] --zone [ZONE]
```

To delete an instance:

```
python delete.py [Project ID] --zone [ZONE] --name [INSTANCE NAME]
```

To access the created instance through ssh:

```
gcloud compute ssh --project [PROJECT_ID] --zone [ZONE] [INSTANCE_NAME]
```

To copy files to the created instance from local machine: 

Please refer to https://cloud.google.com/sdk/gcloud/reference/compute/scp. 

For more information about how to use Google Cloud SDK, please refer to https://cloud.google.com/sdk/, and click on either `View quickstart` or `View documentation`. 
