import pygsheets
import numpy as np
import os

CREDENTIALS_FILE_PATH = os.path.dirname(os.path.abspath(__file__)) + "/service_account_credentials.json"

def fetch_sheet():
    gc = pygsheets.authorize(service_file=CREDENTIALS_FILE_PATH)
    sh = gc.open('Tea Tracking')
    return sh[0]
