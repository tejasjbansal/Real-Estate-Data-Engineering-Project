import boto3
import json
import pandas as pd

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    """
    Lambda function that transforms JSON data from S3 and uploads the transformed data as CSV to another S3 bucket

    Args:
        event (dict): Lambda function event object
        context (object): Lambda function context object

    Returns:
        dict: API Gateway response with status code and message
    """

    # Extract source bucket and object key from the event
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']

    # Define target bucket and filename for transformed data
    target_bucket = 'real-estate-transformed-data'
    target_file_name = object_key[:-5]  # Remove ".json" extension

    # Wait for object to be available in source bucket
    waiter = s3_client.get_waiter('object_exists')
    waiter.wait(Bucket=source_bucket, Key=object_key)

    # Download JSON data from source S3 bucket
    response = s3_client.get_object(Bucket=source_bucket, Key=object_key)
    data = response['Body'].read().decode('utf-8')
    data = json.loads(data)

    # Extract records from JSON data and convert to pandas DataFrame
    records = data["results"]
    df = pd.DataFrame(records)

    # Select specific columns for transformation
    selected_columns = ['bathrooms', 'bedrooms', 'city', 'homeStatus',
                        'homeType', 'livingArea', 'price', 'rentZestimate', 'zipcode']
    df = df[selected_columns]

    # Convert DataFrame to CSV format
    csv_data = df.to_csv(index=False)

    # Upload CSV data to target S3 bucket
    s3_client.put_object(Bucket=target_bucket, Key=f"{target_file_name}.csv", Body=csv_data)

    # API Gateway response
    return {
        'statusCode': 200,
        'body': json.dumps('CSV conversion and S3 upload completed successfully')
    }
