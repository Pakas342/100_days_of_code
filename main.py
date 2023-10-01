import smtplib
import datetime as dt
import random

my_email = "jcbp1999@gmail.com"
password = "cwch ujti nmni lohz"

day_of_week = dt.datetime.now().weekday()

print(day_of_week)

if day_of_week == 6:
    with open(file="quotes.txt", mode="r") as file:
        quotes = file.readlines()
        quote = random.choice(quotes)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject: Monday Motivation\n\n{quote}")
