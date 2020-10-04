# Just-Dial-Scraper
#### Step #1
Create an environment for scraping using Python. You can use whichever environment manager you prefer. 
To create a conda environment, use `conda create --name scrape`. After creating the environment, activate it by typing `conda activate scrape`.

Install the requirements by using 
`pip install -r Just-Dial-Scraper/requirements.txt`

#### Step #2

Search in Google What is `what is my user agent`, copy the top result.
Open Just-Dial-Scraper/product_scraper.py with a text editor. Replace the copied result in scrape function: `your_user_agent`.

#### Step #3
Run the following commands:
1. `cd Just-Dial-Scraper/justdial`
2. `scrapy crawl justdial_spider -o restaurant_unformatted.csv`
It will generate a restaurant_unformatted.csv file

2. `python Just-Dial-Scraper/replacing_numbers.py`
This will create a Restaurant_details.csv file where the extracted data is present of 500 records.


#### Voila! Data  is scraped!
