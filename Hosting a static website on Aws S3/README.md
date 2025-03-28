# Hosting a static website on Aws S3

This beginner project will guide you through setting up a personal website using Amazon S3 and connecting it with a custom domain through Route 53 and hostinger

## Step 1 : Design your own website
- Design your own website or download an existing template.which has index.html file and other files
- I personally have designed my portfolio to host as static website
  
## Step 2 : Set up Amazon S3 bucket
- Login to your Aws management console and open Amazon S3
- Click on "create bucket" and enter a unique name for your bucket. Must be unique globally.
- Untick Block all public access and create the bucket.
- In the properties tab of the bucket enable "static website hosting" and specify index document as index.html and save.
- upload the website files into the bucket.
- Go to the permissions section of the bucket and give the bucket policy to get objects. policy is in the above file.

## Step 3 : Purchase a Custom Domain through Amazon Route53 or other Domain Registrar(hostlinger)
### -Custom domain through Amazon Route53

- Open the Amazon Route 53 console.
- Choose "Domain registration" and then "Register domain".
- Follow the prompts to purchase your custom domain.
- Create Hosted zone for the Domain name and create a new record set.
- Enter your S3 bucket's endpoint as the alias target

### -Custom domain through Hostinger Domain Registrar
#### I personally have used Hostinger for Domain Registration

- Go to the Domain Registration of Hostinger and Register your custom Domain
- Now go to the Hosted zone in Route53 and Create the Public Hosted Zone.
- Now go to the Hosted Zone Details you find Four Name Servers of Hosted zone.
- Copy the All Four Name Servers of hosted zone.
- Go to the Hostinger and Edit DNS/Name Servers and paste All the Four NameServers of the Hosted zone. This points the Domain name to the Hostedzone(It usually takes around 24hrs for NameServers to be changed in Domain Registrar.

## You Have Successfully Hosted A Static Website On Amazon S3

## Project Completion Time
-30 minutes to 1 hour if you have an existing template.
-For Customizing the website you need more time depends on the website design. 
