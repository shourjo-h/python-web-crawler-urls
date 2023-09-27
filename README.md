## Python Web Crawler Program to Find URLs

**Overview**

This Python web crawler program can be used to find URLs that match a given set of criteria, such as primary category, secondary category, geography, and date range. The program crawls the web using Google Search and extracts the URLs from the search results. The URLs are then written to a CSV file.

**Features**

* Crawls the web using Google Search
* Extracts URLs from the search results
* Writes the URLs to a CSV file
* Customizable to meet your specific needs

**Installation**

To install the program, simply run the following command in a terminal:

```
pip install requests beautifulsoup4 csv
```

**Usage**

To use the program, simply download the '.py' file and run the following command in a terminal:

```
python web_crawler.py
```

The program will then prompt you for the following input parameters:

* **Primary Category:** The primary category of the content, such as "Medical Journal", "Blog", or "News".
* **Secondary Category:** The secondary category of the content, such as "Orthopedic" or "Gynecology".
* **Geography:** The geographic location of the content, such as "India", "US", or "Europe".
* **Date Range:** The date range of the content, such as "2022", "2022-23", or "Sep 22".

Once you have provided the input parameters, the program will crawl the web to find URLs that match the given criteria and write them to a CSV file. The CSV file will be named `urls_{primary_category}_{secondary_category}_{geography}_{date_range}.csv` and will be saved in the same directory as the program.

**Example**

To find URLs for medical journals in the United States that were published in 2022, you would run the program with the following input parameters:

```
Primary Category: Medical Journal
Secondary Category:
Geography: United States
Date Range: 2022
```

The program would then crawl the web to find URLs for medical journals in the United States that were published in 2022 and write them to a CSV file named `urls_Medical_Journal__United_States_2022.csv`.

**Customization**

The program can be customized to meet your specific needs. For example, you can change the search engine that the program uses to crawl the web, or you can add additional filters to the search criteria.

To customize the program, you can edit the `web_crawler.py` file. The file is well-documented and easy to understand.

**Conclusion**

This Python web crawler program is a powerful tool for finding URLs that match a given set of criteria. The program is easy to use and can be customized to meet your specific needs.
