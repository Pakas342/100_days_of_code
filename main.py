import requests
from twilio.rest import Client


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCKS_API_KEY = "A76BMJL7HW2GH365"
STOCKS_URL = "https://www.alphavantage.co/query"
NEWS_API = "ba46054299c94aa2b1d223bcca2d9476"
NEWS_URL = "https://newsapi.org/v2/everything"
account_sid = "AC1f1163b6a1912e80338e7b03b11cba10"
SMS_API_KEY = "596894dd16824f5a61c1d732b1936e0d"
client = Client(account_sid, SMS_API_KEY)

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stocks_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCKS_API_KEY
}

stocks_response = requests.get(url=STOCKS_URL, params=stocks_params)
stocks_response.raise_for_status()
stocks_data = stocks_response.json()
tesla_stock_days = [day for day in stocks_data["Time Series (Daily)"]]
last_day_tesla_info = stocks_data["Time Series (Daily)"][tesla_stock_days[0]]
last_day_variation = (float(last_day_tesla_info["4. close"]) - float(last_day_tesla_info["1. open"])) / float(last_day_tesla_info["1. open"])

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

if abs(last_day_variation) > 0.02:
    if last_day_variation < 0:
        title = f"TSLA:🔻{round(last_day_variation * 100)}%"
    else:
        title = f"TSLA:🔺{round(last_day_variation * 100)}%"
    news_params = {
        "apiKey": NEWS_API,
        "q": COMPANY_NAME,
        "from": tesla_stock_days[2],
        "language": "en",
        "sortBy": "relevancy",
        "pageSize": 3,
    }
    news_response = requests.get(url=NEWS_URL, params=news_params)
    news_response.raise_for_status()
    news_tesla_data = news_response.json()
    print(title)
    for new_data in news_tesla_data["articles"]:
        print(new_data["title"])
        print(new_data["description"])
        message = client.messages.create(
            from_="+12566002734",
            body=f"{title}\n"
                 f"Headline: {new_data['title']}\n"
                 f"Brief: {new_data['description']}",
            to='+573222261835'
       )


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

