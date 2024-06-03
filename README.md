# About carbon_trading

## Overview

### Data Scraping

Crafted a Python script `carbon.py` to initiate the web scraping process. Modify the script to specify the endpoints of the web pages of National Renewable Energy Certification Center from which data needs to be scraped.
- Scope: Data from 2020 to 2024, including certification trading (transaction/remaining number of certifications), supply number.
- Method: Scraped using Selenium, loaded and written to CSV files.

### Data Processing

1. Datasets: World Bank Carbon Pricing
- Content: Compliance gen_info, details, revenues, emissions, Crediting details, issuances, etc.
- Update: Data updated on 1 April 2024

2. National Renewable Energy Certification Center
- Content: Supplier, Buyer, Trans_num, Remaining_num, etc.
- Update: Data Scraped on 30 May 2024
- Range: Data from 2020 to 2024

### Data Visualisation

1. Utilised libraries such as Matplotlib, Seaborn, or Plotly within Python to create visualisations based on the processed data.
2. Implement appropriate visualisation techniques such as line plots, bar charts, heatmaps, etc., to effectively communicate insights and trends present in the data.

## Technologies Used

- Python
- MySQL
- HTML

## Project Structure

The project is organised into distinct modules, each dedicated to a specific aspect of the overall objective. The clear segmentation allows for modularity and ease of maintenance.

### Data Scarping Module

- Code files: carbon.py
- Documentation: The data scraping process is primarily executed using the `selenium` package in Python, which facilitates automated web browsing and data extraction from dynamic web pages.
  - Detailed documentation explaining the implementation of Selenium within the `carbon.py` script is provided within the script itself as comments.
  - Key functionalities covered include:
    - Setting up the Selenium webdriver.
    - Navigating to target websites and interacting with web elements.
    - Extracting relevant data from web pages.
    - Handling dynamic content loading and pagination.
    - Storing scraped data in structured formats for further analysis.
  - For additional guidance on using Selenium and understanding its capabilities, refer to the official Selenium documentation and relevant online tutorials.

### Data Processing and Visualisation Module

- Code files: carbon.ipynb
- Database: MySQL
- Documentation: The data processing module involves the `carbon.ipynb` Jupyter Notebook, which serves as the primary environment for data analysis, transformation, and exploration.
  - Detailed documentation and explanatory comments are provided within the notebook itself, guiding users through each step of the data processing pipeline.
  - Key functionalities covered include:
    - Loading scraped data from the data source(s).
    - Cleaning and preprocessing the raw data to address missing values, inconsistencies, and outliers.
    - Performing exploratory data analysis (EDA) to gain insights into the dataset's structure and characteristics.
    - Transforming the data into a suitable format for storage and analysis.
    - Utilising MySQL as the database management system (DBMS) to store processed data and facilitate efficient data retrieval and manipulation.
    - Integration with MySQL database using packages like `config` and establishing a connection through MAMP for Mac users.
  - For additional guidance on data processing techniques, MySQL database management, and establishing connections with MAMP, relevant online tutorials and documentation resources are recommended.

## Acknowledgments

Include any acknowledgments or credits for libraries, frameworks, or data sources used in the project.

## License

This project is licensed under the [LICENSE.md](LICENSE.md) - see the [LICENSE.md](LICENSE.md) file for details.

The code and associated files in the "carbon_trading" project are the intellectual property of Hsin Pai. All rights are reserved by the copyright holder. This code is intended for the exclusive viewing of potential employers to assess the coding and analytical skills of Hsin Pai.

Unauthorised use, reproduction, or distribution of this code, in whole or in part, without the written permission of Hsin Pai is strictly prohibited.

© Hsin Pai, 2024
