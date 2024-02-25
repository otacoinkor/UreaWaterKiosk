# main.py

import streamlit as st
import pandas as pd
import pymysql
import config

st.set_page_config(
    layout="wide",
    page_title="Main")

st.title("요소수 키오스크 매니저")


connection = pymysql.connect(
    host=config.host,
    user=config.user,
    password=config.password,
    database=config.database
)

print('connected')

cursor = connection.cursor()
cursor.execute("Select * from _PickPic_Log_Magok")
data = cursor.fetchall()
column_names = [desc[0] for desc in cursor.description]
# print(column_names)

dataset = pd.DataFrame(data, columns=column_names)
