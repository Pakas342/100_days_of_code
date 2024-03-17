from web_scrapper import scrapper
from data_inputer import data_submitter

URL = "https://appbrewery.github.io/Zillow-Clone/"
FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSdo3o3UmQotMag1W2opSQcNux9GLMfTt95RkBSHBMn9HFyDqw/viewform"


data = scrapper(URL)
data_submitter(FORM_URL, data)


