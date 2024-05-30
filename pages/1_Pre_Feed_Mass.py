import streamlit as st
import pandas as pd

#left_column, middle_column, right_column = st.columns(3)

st.write ("PRE-FEED MASS")
serial_df = pd.read_csv('device_information.csv', usecols = [0])
grafana_name = []


serial_number = serial_df.tolist()
print(serial_number)
st.sidebar.text('Record Device Empty')


# pre-feed mass inputs
st.text_input (serial_number[0], key ="pre-feed_" + str(serial_number[0]))
st.text_input (serial_number[1], key ="pre-feed_" + str(serial_number[1]))
st.text_input (serial_number[2], key ="pre-feed_" + str(serial_number[2]))
st.text_input (serial_number[3], key ="pre-feed_" + str(serial_number[3]))
st.text_input (serial_number[4], key ="pre-feed_" + str(serial_number[4]))
st.text_input (serial_number[5], key ="pre-feed_" + str(serial_number[5]))
st.text_input (serial_number[6], key ="pre-feed_" + str(serial_number[6]))
#sidebar "empty" tab

with st.sidebar:
    st.checkbox('Emptied ' + str(serial_number[0]))
    st.checkbox('Emptied ' + str(serial_number[1]))
    st.checkbox('Emptied ' + str(serial_number[2]))
    st.checkbox('Emptied ' + str(serial_number[3]))
    st.checkbox('Emptied ' + str(serial_number[4]))
    st.checkbox('Emptied ' + str(serial_number[5]))
    st.checkbox('Emptied ' + str(serial_number[6]))

