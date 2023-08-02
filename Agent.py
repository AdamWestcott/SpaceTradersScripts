import csv
from io import StringIO
import json
import math
import os
import time
import requests
from datetime import datetime
from pathlib import Path
import pandas as pd
from time import sleep
#from PIL import Image
import keys
import streamlit as st
import factionList

headers = {
    'Authorization': 'Basic '
}



class CreateAgent:
    def __init__(self, symbol, faction):

        data = {
            "symbol": symbol,
            "faction": faction
        }
        
        space_trader_agent_creation_url = "https://api.spacetraders.io/v2/register"

        space_trader_agent = requests.get(space_trader_agent_creation_url, json=data)
        print(space_trader_agent)
        print(space_trader_agent.json())


