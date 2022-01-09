import random
import streamlit as st
from streamlit_echarts import st_echarts


def get_gauge_options(value, name, color):
    options = {
        "tooltip": {"formatter": "{a} <br/>{b} : {c}%"},
        "series": [
            {
                "name": "Pressure",
                "type": "gauge",
                "color": color,
                "axisLine": {
                    "lineStyle": {
                        "width": 10,
                    },
                },
                "progress": {"show": "true", "width": 10},
                "detail": {"valueAnimation": "true", "formatter": "{value}"},
                "data": [{"value": value, "name": name}],
            }
        ],
    }
    return options


def render_gauge_chart():
    columns = st.columns(3)

    selected_value_1 = random.randint(1, 99)
    selected_value_2 = random.randint(1, 99)
    selected_value_3 = random.randint(1, 99)

    events = {
        "click": "function(params) { console.log(params.name); return params.name }",
        "dblclick": "function(params) { return [params.type, params.name, params.value] }",
    }

    options_1 = get_gauge_options(selected_value_1, "Temperature", "red")
    options_2 = get_gauge_options(selected_value_2, "Pressure", "green")
    options_3 = get_gauge_options(selected_value_3, "Humidity", "orange")

    with columns[0]:
        st_echarts(options=options_1, width="100%", events=events, key=0)

    with columns[1]:
        st_echarts(options=options_2, width="100%", events=events, key=1)

    with columns[2]:
        st_echarts(options=options_3, width="100%", events=events, key=2)
