import boto3
import json

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    """
    This function copies an object from an S3 source bucket to a target bucket.

    Args:
        event (dict): The event object containing information about the S3 event that triggered the function.
        context (object): AWS Lambda context object.

    Returns:
        dict: A dictionary containing the status code and a message indicating success.
    """

    # Get the source bucket and object key from the event
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    source_object_key = event['Records'][0]['s3']['object']['key']  # Corrected variable name

    # Define the target bucket name
    target_bucket = 'real-estate-data-intermediate-zone'

    # Define the copy source object
    copy_source = {'Bucket': source_bucket, 'Key': source_object_key}

    # Wait for the object to exist in the source bucket before copying
    waiter = s3_client.get_waiter('object_exists')
    waiter.wait(Bucket=source_bucket, Key=source_object_key)

    # Copy the object to the target bucket
    s3_client.copy_object(Bucket=target_bucket, Key=source_object_key, CopySource=copy_source)

    # Return a success message
    return {
        'statusCode': 200,
        'body': json.dumps('Copy completed successfully')
    }
