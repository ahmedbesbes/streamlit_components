import streamlit as st
from streamlit_echarts import st_echarts


def get_pie_options():

    options = {
        "tooltip": {"trigger": "item"},
        "legend": {"top": "5%", "left": "center"},
        "series": [
            {
                "name": "Access From",
                "type": "pie",
                "radius": ["40%", "70%"],
                "avoidLabelOverlap": False,
                "itemStyle": {
                    "borderRadius": 10,
                    "borderColor": "#fff",
                    "borderWidth": 2,
                },
                "label": {
                    "show": False,
                    "position": "center",
                },
                "emphasis": {
                    "label": {"show": True, "fontSize": "20", "fontWeight": "bold"}
                },
                "labelLine": {"show": False},
                "data": [
                    {"value": 1048, "name": "Search Engine"},
                    {"value": 735, "name": "Direct"},
                    {"value": 580, "name": "Email"},
                    {"value": 484, "name": "Union Ads"},
                    {"value": 300, "name": "Video Ads"},
                ],
            }
        ],
    }
    return options


def render_pie_chart():
    columns = st.columns(2)
    options = get_pie_options()

    with columns[0]:
        st_echarts(options=options, key=0, width=500, height=500)
