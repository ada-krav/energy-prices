# Energy prices scraper

## Installation:
It`s assumed that Python3 is already installed:

```shell
git clone https://github.com/ada-krav/energy-prices.git
cd energy-prices
python -m venv venv
venv\Scripts\activate (on Windows) or venv/Scripts/activate (depends on system settings)
source venv/bin/activate (on macOS)
pip install -r requirements.txt
python app.py (to run Flask)
python script/scraper.py (to run script)
```


## Prices Scraper:
It's recommended to schedule script execution once a day around 12:00 to get info as fast as possible.
* Recursive execution every 5 minutes until data is available.
* Selenium and BeautifulSoup for data fetching
* SQLite as database engine

## Flask API endpoint

* Access to information in db through Flask API endpoint
* Database is included, so you can test Flask app straight from the box
