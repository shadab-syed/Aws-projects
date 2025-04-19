# S3 Thumbnail Generator Using AWS Lambda
# Serverless Image Processing Pipeline

A serverless project that automatically generates thumbnails from images uploaded to an S3 bucket using AWS Lambda and Pillow (Python). The thumbnail is saved to another destination S3 bucket.

## 🚀 Features

- Triggered on S3 PUT (new image upload)
- Generates thumbnail (128x128)
- Uploads thumbnail to a separate S3 bucket
- Written in Python using Pillow library
- Fully serverless and event-driven

## 🛠️ Architecture

1. User uploads image to Source S3 bucket  
2. S3 triggers a Lambda function  
3. Lambda reads the image, creates a thumbnail  
4. Thumbnail is uploaded to a Destination S3 bucket under /thumbnails

## 📦 Technologies Used

- AWS Lambda (Python 3.9)
- Amazon S3 (Event trigger + storage)
- AWS IAM (for permissions)
- Pillow (image processing)
- boto3 (AWS SDK for Python)


## Step 1 : Create Two S3 buckets
- Source bucket (eg: uploadbucket12345)
- Destination bucket (eg: outputbucket12345)


## Step 2 : Create Lambda Function
- Login to your Aws management console and open "Amazon Lambda"
- Click on "create Function".
- Click "Author From Scratch" and scroll down and name the function (eg: my lambda function)
- Under Runtime Select Python 3.9
- Under change default execution role create a role and select it.(Role is in iam role for lambda.json, edit it and give your bucket names)
- Create Function


## Step 3 : Deploy Python Code to AWS Lambda as .zip Package (For Code with Dependencies like PIL/Pillow)
### Since this code uses Pillow (a third-party library), you need to bundle it with your code:
#### Go to your local linux machine in amazon linux
#### give commands as given below

- mkdir thumbnail-lambda      (to create a directory)
- cd thumbnail-lambda
- nano lambda_function.py   ( create a python file. paste the python lambda function code from #lambda_function.py# file as given above and save it)
- sudo yum -y install python-pip (to install pip)
- pip install pillow -t .
- zip -r function.zip .

#### Download this function.zip file

- Go to Lambda Console → Your function
- Choose "Upload from" > ".zip file" under "Code source"
- Upload function.zip file

- In code (lambda_function.py) replace "your-thumbnail-bucket-name" with your destination bucket name
- Click deploy



## Step 4 : Adding trigger to your lambda function
- In your Lambda Function click "Add Trigger"
- set source trigger as "S3 Bucket"
- select your source bucket and click "Add"


# Now try uploading any image to source bucket you will get the Image Thumbnail in Destination Bucket
If any Error try increasing the timeout time (Go to the General Configuration of Lambda and edit it. Increase it to 20sec)
because some large images takes time for execution.


