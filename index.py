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

st.write("Faction Table")
st.table(factionList.FactionStats.faction_table_df)

st.write("Faction Trait Table")
st.table(factionList.FactionStats.faction_trait_table_df)