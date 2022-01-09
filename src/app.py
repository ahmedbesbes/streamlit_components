import streamlit as st
from components.echarts import main as main_echarts

st.set_page_config(layout="wide")

component = st.sidebar.radio(
    "Select a component",
    options=["echarts", "streamlit_tags", "streamlit_aggrid", "st_ace"],
)


if component == "echarts":
    main_echarts.render_echarts()
