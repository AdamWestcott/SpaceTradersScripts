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

class FactionStats:
    faction_table = [] 
    faction_row = []
    faction_trait_table = [] 
    faction_trait_row = []
    space_trader_factions_url = "https://api.spacetraders.io/v2/factions"


    internalnetworks = []

    faction_list = requests.get(space_trader_factions_url)
    print(faction_list)
    print(faction_list.json())
    factions = faction_list.json()


    faction_data = factions["data"]

    for faction in faction_data:
        faction_row.append(faction["name"])
        faction_row.append(faction["symbol"])
        faction_row.append(faction["description"])
        faction_row.append(faction["headquarters"])
        print(faction["name"])
        if "traits" in faction:
            faction_traits = faction["traits"]
            for trait in range(len(faction_traits)):
                faction_trait = faction_traits[trait]
                print(faction_trait)
                faction_trait_row.append(faction["name"])
                faction_trait_row.append(faction_trait["symbol"])
                faction_trait_row.append(faction_trait["name"])
                faction_trait_row.append(faction_trait["description"])
                faction_trait_table.append(faction_trait_row)
                faction_trait_row = []
        faction_table.append(faction_row)
        faction_row = []

    faction_table_df = pd.DataFrame(faction_table, columns = ['Name', 'Symbol', 'Description','Headquarters Location'])

    faction_trait_table_df = pd.DataFrame(faction_trait_table, columns = ['Name', 'Trait Symbol', 'Trait Name','Trait Description'])

class viewFactionContracts:
    def __init__(self, Authorization):

        agent_header = {
            'Authorization': 'Bearer '+Authorization
        }
        
        space_trader_agent_contracts_url = "https://api.spacetraders.io/v2/my/contracts"

        space_trader_agent_contracts_data = requests.get(space_trader_agent_contracts_url, headers = agent_header)
        print(space_trader_agent_contracts_data)
        print(space_trader_agent_contracts_data.json())

    

