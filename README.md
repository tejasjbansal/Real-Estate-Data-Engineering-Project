# Real Estate Data Engineering Project

## Overview

This project involves building an end-to-end Python ETL pipeline to extract real estate property information from the Zillow Rapid API and process it on the AWS Cloud. The data pipeline includes data extraction, loading, transformation, and visualization, all orchestrated using Apache Airflow.

## Project Architecture

![Zillow Data Engineering Project Pipeline](https://github.com/tejasjbansal/Real-Estate-Data-Engineering-Project/assets/56173595/6cf80872-716a-4426-9aec-720665acb2f7)

## Requirements

- **Python** (version 3.7 or later)
- **AWS Account** with access to the following services:
  - Amazon S3
  - AWS Lambda
  - Amazon Redshift
  - Amazon EC2
  - Amazon QuickSight
  - Apache Airflow (running on an EC2 instance)
- **Zillow Rapid API** access credentials

## Project Structure

1. **Data Extraction**:
   - Connect to the Zillow Rapid API.
   - Extract real estate property information.
   - Load the extracted data into an Amazon S3 bucket (Landing Zone).

2. **Data Loading and Transformation**:
   - Trigger a Lambda function to copy data from the Landing Zone to an intermediate S3 bucket.
   - Trigger another Lambda function to transform the data.
   - Load the transformed data into another S3 bucket.

3. **Data Storage and Visualization**:
   - Load the transformed data into an Amazon Redshift cluster.
   - Use Amazon QuickSight for data visualization.

4. **Orchestration**:
   - Use Apache Airflow running on an Amazon EC2 instance to orchestrate the entire pipeline.

## Step-by-Step Instructions

### 1. Data Extraction

1. **Connect to Zillow Rapid API**:
   - Obtain API credentials from Zillow Rapid API.
   - Write a Python script to connect to the API and extract real estate property information.

2. **Load Data into Amazon S3 (Landing Zone)**:
   - Use the AWS SDK for Python (Boto3) to upload the extracted data to the S3 bucket (Landing Zone).

### 2. Data Loading and Transformation

1. **Trigger Lambda Function for Data Copy**:
   - Set up an S3 event notification to trigger a Lambda function whenever new data is uploaded to the Landing Zone.
   - Write a Lambda function to copy the data from the Landing Zone to an intermediate S3 bucket.

2. **Trigger Lambda Function for Data Transformation**:
   - Set up another S3 event notification to trigger a second Lambda function when data is copied to the intermediate S3 bucket.
   - Write a Lambda function to transform the data (e.g., cleaning, normalization).
   - Load the transformed data into another S3 bucket.

### 3. Data Storage and Visualization

1. **Load Data into Amazon Redshift**:
   - Write a Python script or use AWS Glue to load the transformed data from the S3 bucket into an Amazon Redshift cluster.

2. **Visualize Data with Amazon QuickSight**:
   - Connect Amazon QuickSight to the Redshift cluster.
   - Create interactive dashboards and visualizations.

### 4. Orchestration with Apache Airflow

1. **Set Up Apache Airflow**:
   - Launch an Amazon EC2 instance and install Apache Airflow.
   - Configure Airflow to orchestrate the entire ETL pipeline.

2. **Create Airflow DAG**:
   - Define a Directed Acyclic Graph (DAG) in Airflow to manage the tasks:
     - Data extraction from Zillow Rapid API.
     - Uploading data to the Landing Zone.
     - Triggering Lambda functions for data copy and transformation.
     - Loading data into Amazon Redshift.
     - Refreshing Amazon QuickSight dashboards.

## Getting Started

### Prerequisites

- Ensure you have all required AWS services set up and API credentials from Zillow Rapid API.
- Install necessary Python packages:
  ```bash
  pip install -r requirements.txt
  ```

### Running the Pipeline

1. **Clone the Repository**:
   ```bash
   git clone [<repository-url>](https://github.com/tejasjbansal/Real-Estate-Data-Engineering-Project.git)
   cd Real-Estate-Data-Engineering-Project
   ```

2. **Configure the AWS Credentials**:
    ```bash
    aws congfigure
    ```
3. **Set Up Environment Variables**:
   - Create a `config.json` file with your Zillow API key:
     ```bash
     ZILLOW_API_KEY=<your-zillow-api-key>
     ```

4. **Create Lambda Functions and Schedule the trigger**

5. **Run the Script/Dag**:
   ```bash
   python zillowanalytics.py
   ```

6. **Monitor the Pipeline in Apache Airflow**:
   - Access the Airflow web interface to monitor and manage the DAGs.
   
7. **Connect to Amazon Redshift**

8. **Visualize Data with Amazon QuickSight**

