# Energy prices scraper

## Installation:
It`s asumed that Python3 is already installed:

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

## Additional info:
It's reccomended to schedule script execution once a day around 12:00.