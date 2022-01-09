import streamlit as st
from .gauge import render_gauge_chart
from .pie import render_pie_chart


def render_echarts():
    plot_type = st.sidebar.selectbox(
        "Select plot type",
        options=["Gauge", "Bar chart", "Scatter plot", "Pie chart"],
    )

    if plot_type == "Gauge":
        render_gauge_chart()
    if plot_type == "Pie chart":
        render_pie_chart()
