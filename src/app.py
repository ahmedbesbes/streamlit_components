import streamlit as st
from components.echarts import display_echarts
from components.ace import display_ace

st.set_page_config(layout="wide")

component = st.sidebar.radio(
    "Select a component",
    options=["echarts", "streamlit_tags", "streamlit_aggrid", "st_ace"],
)


if component == "echarts":
    display_echarts()

elif component == "st_ace":
    content = display_ace()
