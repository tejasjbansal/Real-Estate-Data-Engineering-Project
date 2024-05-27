#!/bin/bash

# Update the package list
sudo apt update

# Install pip for Python 3
sudo apt install -y python3-pip

# Install the Python 3.10 venv module
sudo apt install -y python3.10-venv

# Create a virtual environment
python3 -m venv zillow_venv

# Activate the virtual environment
source zillow_venv/bin/activate

# Install necessary Python packages
pip install pandas boto3 awscli apache-airflow apache-airflow-providers-amazon

# Verify Airflow installation
airflow version

# Verify Python installation
python3 --version

# Start Airflow in standalone mode
airflow standalone