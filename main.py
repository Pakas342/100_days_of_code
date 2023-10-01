import pandas
import smtplib
import datetime as dt
import os
import random

# 1. Update the birthdays.csv

# DONE

# 2. Check if today matches a birthday in the birthdays.csv

BIRTHDAY_CSV_DIRECTORY = "birthdays.csv"
LETTERS_DIRECTORY = "letter_templates/"
MY_EMAIL = "jcbp1999@gmail.com"
PASSWORD = "cwch ujti nmni lohz"

letters = os.listdir(LETTERS_DIRECTORY)

now = dt.datetime.now()
now_day = now.day
now_month = now.month
birthday_data = pandas.read_csv(BIRTHDAY_CSV_DIRECTORY).to_dict(orient="records")
for birthday in birthday_data:
    if birthday["month"] == now_month and birthday["day"] == now_day:
        letter = random.choice(letters)
        with open(f"{LETTERS_DIRECTORY}{letter}", mode="r") as template:
            birthday_template = template.read()
        birthday_letter = birthday_template.replace("[NAME]", birthday["name"])
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=birthday["email"],
                                msg=f"Subject: Happy birthday!\n\n{birthday_letter}")


# 4. Send the letter generated in step 3 to that person's email address.
