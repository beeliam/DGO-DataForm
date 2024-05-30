import streamlit as st
import pandas as pd

#left_column, middle_column, right_column = st.columns(3)

st.write ("PRE-FEED MASS")

#pull this information from CSV file
serial_number = ["SN1", "SN2", "SN3", "SN4", "SN5", "SN6", "SN7"]
grafana_name = []


# post-feed mass inputs
st.text_input (serial_number[0], key ="post-feed_" + str(serial_number[0]))
st.text_input (serial_number[1], key ="post-feed_" + str(serial_number[1]))
st.text_input (serial_number[2], key ="post-feed_" + str(serial_number[2]))
st.text_input (serial_number[3], key ="post-feed_" + str(serial_number[3]))
st.text_input (serial_number[4], key ="post-feed_" + str(serial_number[4]))
st.text_input (serial_number[5], key ="post-feed_" + str(serial_number[5]))
st.text_input (serial_number[6], key ="post-feed_" + str(serial_number[6]))


