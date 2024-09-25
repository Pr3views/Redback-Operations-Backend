# Project Documentation

## Overview

This project focuses on the backend processes involved in extracting fitness-related data from Garmin and Wahoo devices, followed by conversion of the raw data into usable formats. Additionally, this documentation provides a brief demonstration of how Google Cloud Platform (GCP) is used within the process.

## Table of Contents
- [Documentation](#documentation)
- [Garmin - LoginDemo](#garmin---logindemo)
- [Wahoo API - Data Extraction](#wahoo-api---data-extraction)
- [FIT Conversion Scripts](#fit-conversion-scripts)
- [Process Overview](#process-overview)
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

## Glossary

- **Documentation:** Refers to the complete process of backend development, including the extraction of data from fitness APIs (Garmin and Wahoo), data processing, and the utilization of GCP services for storing, converting, and analyzing the data. The documentation also provides a brief overview of the GCP services used in the process, such as Cloud Storage for storing raw files and BigQuery for data analysis.
  
- **Garmin - LoginDemo:** A backend component that handles user authentication and data extraction from the Garmin API. It retrieves various fitness metrics (e.g., steps, heart rate, GPS data) and stores them in raw formats like FIT files.

- **Wahoo API - Data Extraction:** A backend module that connects to Wahoo's API, allowing for the extraction of cycling, heart rate, and other performance metrics from Wahoo fitness devices. Like Garmin, data is pulled in a raw format and processed for conversion.

- **FIT Conversion Scripts:** A set of scripts designed to convert proprietary FIT files (Flexible and Interoperable Data Transfer files) into CSV format. These scripts facilitate the transformation of raw fitness data into a format that is more accessible for analysis, reporting, and visualization purposes.
