# Energy prices scraper

## Installation:
It`s assumed that Python3 is already installed:

```shell
git clone https://github.com/ada-krav/energy-prices.git
cd energy-prices
python -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
pip install -r requirements.txt
python app.py 
python script/scraper.py
```


## Features:

*  Repeated execution to fetch current data
*  Access to information in db through Flask API endpoint
* Database with included, so you can test Flask app straight from the box

## Additional info:
It's recommended to schedule script execution once a day around 12:00.