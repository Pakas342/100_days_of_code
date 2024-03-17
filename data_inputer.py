import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


def data_submitter(url, properties):
    """Submits the data to a Google forms"""

    # Setting the no closing tab
    edge_options = webdriver.EdgeOptions()
    edge_options.add_experimental_option(name="detach", value=True)

    # Going to the Google forms

    driver = webdriver.Edge(options=edge_options)

    for property in properties:
        # Go to the beginning web
        driver.get(url)
        sleep(1)

        # Get the inputs to fulfill with data based on their position on the forms

        inputs = driver.find_elements(By.CSS_SELECTOR, value='''div[role="list"] input''')
        address_input = inputs[0]
        price_input = inputs[1]
        link_input = inputs[2]

        # Fulfill every input
        address_input.click()
        address_input.send_keys(property["address"])
        price_input.click()
        price_input.send_keys(property["price"])
        link_input.click()
        link_input.send_keys(property["link"])

        # get the send button and click it and wait
        send_button_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span'
        send_button = driver.find_element(By.XPATH, value=send_button_xpath)
        send_button.click()
        sleep(1)
