
# Serverless Image Uploader

## Prerequisites

- Python3 (3.9 is recommended).
- NodeJS and Npm (14.18 and 6.14)
- The AWS CDK (1.132)
- An AWS Account with your Access Key and Secret Access Key.

## Project architecture

```
serveless-image-uploader
|   README.md
|---front-app # The Front-End React App
|---lambda
|   |---file_to_ddb.py
|   |---hello_world.py
|   |---list_files.py
|   |---upload-file.py
|---scripts # You can run this script to populate example images
|   |---upload_images.py
|   |---assets # The example assets
|---serveless_image_uploader # Your AWS infra lives here
```

## AWS Infrastructure

![The services used for this project](./serverless-images-uploader.drawio.png)


## Using the AWS CDK

- `npm install -g aws-cdk`: Install the AWS CDK.


To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

Then bootstrap your environnement.
```
$ cdk bootstrap
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

Finally deploy the project:

```
$ cdk deploy
```

Before you go try upload images, copy the output of the deploy command, it
looks like this one: **https://4ooi3ccx66.execute-api.us-east-1.amazonaws.com/prod**

Copy and paste this link in the following files:
- `scripts/upload_images.py` - It's the BASE_URL
- `front-app/src/constants.ts`

## Run the Front-end project

- `cd front-app` - Go the Front-end directory project
- `yarn` - Install the dependencies
- `yarn start` - Launch the React project

## Useful commands 


### With the AWS CDK:

* `cdk ls`          list all stacks in the app
* `cdk synth`       emits the synthesized CloudFormation template
* `cdk deploy`      deploy this stack to your default AWS account/region
* `cdk diff`        compare deployed stack with current state
* `cdk docs`        open CDK documentation

### With Python

- `python scripts/upload_images.py` - Upload example images.


