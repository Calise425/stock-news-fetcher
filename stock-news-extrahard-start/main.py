import requests
from datetime import date, timedelta

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY = "56Q1HLB9H90EH7B9"


def check_stock():
    today = date.today()
    yesterday = today - timedelta(days=1)

    parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": API_KEY
    }
    response = requests.get("https://www.alphavantage.co/query", params=parameters)
    data = response.json()

    opening_price_today = float(data["Time Series (Daily)"][f"{today}"]["4. close"])
    opening_price_yesterday = float(data["Time Series (Daily)"][f"{yesterday}"]["4. close"])

    if (opening_price_today/opening_price_yesterday) < 0.95 or (opening_price_today/opening_price_yesterday) > 1.05:
        print("Get News")
    else:
        print("No big changes")

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file
by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the
coronavirus market crash.
or
TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file
by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the
coronavirus market crash.
"""

check_stock()
