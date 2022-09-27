#authentication for td ameritrade api, uses config file access tokens
#and redirect urls, initiates instance of client which is the api
#object used in pulling data

from tda import auth, client
import json
import sys
# sys.path.append(r'C:\Users\Owner\Desktop\backtrader_v2\data_feeds\td_ameritrade\authentication')
# import config
from td_ameritrade.authentication import config

def get_client():
    try:
        #if log api has been accessed in past 30 days the token stored at the given
        #path is used for faster access to the api
        client = auth.client_from_token_file(config.token_path, config.api_key)

    except FileNotFoundError:
        #if token is not found traditional access is initiated using selenium and 
        #the chromedriver
        #webdriver set up using 4.0.0 updated (service object now required)
        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service
        serv_object = Service(config.driver_path)
        driver = webdriver.Chrome(service=serv_object)
        #initiating instance of client object to be used to access api
        client = auth.client_from_login_flow(driver, config.api_key, config.redirect_url, config.token_path)

    return client
