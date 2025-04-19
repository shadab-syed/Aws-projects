import boto3
from PIL import Image
import os
import io
import urllib.parse


# Define the destination bucket name
DEST_BUCKET = 'your-thumbnail-bucket-name'
THUMBNAIL_SIZE = (128, 128)

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    encoded_key = event['Records'][0]['s3']['object']['key']
    object_key = urllib.parse.unquote_plus(encoded_key)
    
    try:
        # Download the image from source bucket
        response = s3_client.get_object(Bucket=source_bucket, Key=object_key)
        image_data = response['Body'].read()
        
        # Open image with Pillow
        image = Image.open(io.BytesIO(image_data))
        image.thumbnail(THUMBNAIL_SIZE)
        
        # Save thumbnail to memory buffer
        buffer = io.BytesIO()
        image_format = image.format if image.format else 'JPEG'
        image.save(buffer, image_format)
        buffer.seek(0)
        
        # Define thumbnail key (same filename, in 'thumbnails/' folder)
        thumbnail_key = f"thumbnails/{os.path.basename(object_key)}"

        # Upload to destination bucket
        s3_client.put_object(
            Bucket=DEST_BUCKET,
            Key=thumbnail_key,
            Body=buffer,
            ContentType=f'image/{image_format.lower()}'
        )
        
        print(f"Thumbnail created and uploaded to {DEST_BUCKET}/{thumbnail_key}")
        return {
            'statusCode': 200,
            'body': f"Thumbnail uploaded to {DEST_BUCKET}/{thumbnail_key}"
        }
    
    except Exception as e:
        print(f"Error processing file {object_key}: {e}")
        return {
            'statusCode': 500,
            'body': str(e)
        }
