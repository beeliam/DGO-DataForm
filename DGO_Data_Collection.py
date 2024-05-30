from datetime import date
import streamlit as st
import pandas as pd

today = date.today()
st.header(today.strftime("%B %d, %Y"))

st.text('Device Information')

device_information = pd.read_csv('device_information.csv')

st.data_editor(device_information)

st.button("submit")
