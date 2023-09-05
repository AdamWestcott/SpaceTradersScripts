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




class CreateAgent:
    def __init__(self, symbol, faction):

        data = {
            "symbol": symbol,
            "faction": faction
        }
        
        space_trader_agent_creation_url = "https://api.spacetraders.io/v2/register"

        space_trader_agent = requests.post(space_trader_agent_creation_url, json=data)
        print(space_trader_agent)
        print(space_trader_agent.json())

class AgentDetails:
    def __init__(self, Authorization):

        agent_header = {
            'Authorization': 'Bearer '+Authorization
        }
        
        space_trader_agent_data_url = "https://api.spacetraders.io/v2/my/agent"

        space_trader_agent_data = requests.get(space_trader_agent_data_url, headers = agent_header)
        print(space_trader_agent_data)
        print(space_trader_agent_data.json())

class ViewLocation:
    def __init__(self, Authorization,systemSymbol,waypointSymbol):

        agent_header = {
            'Authorization': 'Bearer '+Authorization
        }
        
        space_trader_agent_location_url = "https://api.spacetraders.io/v2/systems/"+str(systemSymbol)+"/waypoints/"+str(waypointSymbol)

        space_trader_location_data = requests.get(space_trader_agent_location_url, headers = agent_header)
        print(space_trader_location_data)
        print(space_trader_location_data.json())



