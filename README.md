# Project Documentation

## Overview

This project focuses on the backend processes involved in extracting fitness-related data from Garmin and Wahoo devices, followed by conversion of the raw data into usable formats. Additionally, this documentation provides a brief demonstration of how Google Cloud Platform (GCP) is used within the process.

## Table of Contents
- [Documentation](#documentation)
- [Garmin - LoginDemo](#garmin---logindemo)
- [Wahoo API - Data Extraction](#wahoo-api---data-extraction)
- [FIT Conversion Scripts](#fit-conversion-scripts)
- [Process Overview](#process-overview)
- [Redback Fit Backend](#redback-fit-backend)
- [Glossary](#glossary)


## Documentation

This section outlines the backend process for extracting data from fitness APIs and how GCP services are utilized to manage and process this data. It includes the following steps:

1. **Garmin API and Wahoo API Integration:** Establish connections to fitness APIs.
2. **Data Storage:** Store raw data using GCP services such as Google Cloud Storage.
3. **Data Conversion:** Use conversion scripts to process raw data into formats suitable for analysis.
4. **Processing and Analysis:** Use GCP services (BigQuery, Compute Engine, etc.) for data analysis and insights.

The backend code interacts with Garmin and Wahoo APIs to extract fitness data (steps, heart rate, cycling data, etc.) and converts this data from the proprietary formats to CSV for further analysis.

## Garmin - LoginDemo

**Garmin - LoginDemo** is a module designed to extract fitness data from Garmin's API. The login process authenticates the user and accesses the Garmin API to retrieve relevant fitness data such as steps, heart rate, GPS data, etc.

### Features:
- User authentication via Garmin API.
- Extraction of fitness-related metrics.
- Secure storage of API keys and access tokens.
  
The extracted data is processed and stored in raw format (e.g., FIT files) for further conversion and analysis.

## Wahoo API - Data Extraction

**Wahoo API - Data Extraction** is responsible for retrieving data from the Wahoo ecosystem, including cycling and heart rate data.

### Features:
- Seamless connection to the Wahoo API.
- Extracts workout data such as cycling distance, time, and performance metrics.
- Handles API authentication and token management.
  
Similar to the Garmin extraction process, raw data from the Wahoo API is stored and prepared for conversion into a more usable format, such as CSV files.

## FIT Conversion Scripts

The **FIT Conversion Scripts** are responsible for converting data from proprietary FIT files (used by Garmin and Wahoo) to CSV files. This allows for easy data manipulation and integration into analysis tools such as Excel or Python-based data processing frameworks.

### Features:
- Converts raw FIT files into CSV format.
- Extracts relevant metrics such as GPS coordinates, heart rate, and performance data.
- Ensures compatibility with various data analysis platforms.

## Process Overview
This document details the pipelining of the data flow and shows how it can be converted to be utilised in GCP process, so it can be stored and accessed securely for Data Analysis usage.




## Redback Fit Backend

This is the backend API for the Redback Fit application, built with Flask.

### Project Structure

redback_cms/
│
├── app/
│ ├── init .py
│ ├── models.py
│ ├── routes/
│ │ ├── init .py
│ │ ├── auth.py
│ │ 
│ └── utils.py
│
├── config.py
├── requirements.txt
└── run.py


### Setup and Installation

1. Clone the repository:
git clone https://github.com/Pr3views/Redback-Operations-Backend.git




2. Activate the virtual environment:
- On Windows: `env\Scripts\activate`
- On macOS and Linux: `source env/bin/activate`

3. Install the required packages:
pip install -r requirements.txt


4. Set up environment variables:
Create a `.env` file in the project root with the following content:


FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///redback_fit.db # in developmenthttps://github.com/Redback-Operations/redback-cms.git





### Running the Application

To run the application, use the following command:


python run.py


The API will be available at `http://127.0.0.1:5000/`.

### API Endpoints

#### Authentication

- Register a new user:
  - POST `/auth/register`
  - Body: `{"username": "string", "email": "string", "password": "string"}`

- Login:
  - POST `/auth/login`
  - Body: `{"username": "string", "password": "string"}`



### Database Models

#### User
- id: Integer, primary key
- username: String, unique
- email: String, unique
- password_hash: String
