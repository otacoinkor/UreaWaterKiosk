# main.py

import streamlit as st
import pandas as pd
import pymysql
import config


st.set_page_config(
    layout="wide",
    page_title="Main")

st.title("OTACO TEST")

connection = pymysql.connect(
    host=config.host,
    user=config.user,
    password=config.password,
    database=config.database
)

print('connected')
