from tda import auth, client
import json
from td_ameritrade.authentication import config

def get_client():
    try:
        client = auth.client_from_token_file(config.token_path, config.api_key)

    except FileNotFoundError:
        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service
        serv_object = Service(config.driver_path)
        driver = webdriver.Chrome(service=serv_object)
        token_path = config.token_path
        client = auth.client_from_login_flow(driver, config.api_key, config.redirect_url, config.token_path)

    return client

