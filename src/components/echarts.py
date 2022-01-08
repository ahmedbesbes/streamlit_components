import streamlit as st
from streamlit_echarts import st_echarts


def display_echarts():
    selected_value = st.sidebar.slider(
        "Select a value", min_value=0, max_value=100, value=50, step=1
    )

    columns = st.columns(3)

    options = {
        "tooltip": {"formatter": "{a} <br/>{b} : {c}%"},
        "series": [
            {
                "name": "Pressure",
                "type": "gauge",
                "progress": {"show": "true"},
                "detail": {"valueAnimation": "true", "formatter": "{value}"},
                "data": [{"value": selected_value, "name": "Pressure"}],
            }
        ],
    }

    events = {
        "click": "function(params) { console.log(params.name); return params.name }",
        "dblclick": "function(params) { return [params.type, params.name, params.value] }",
    }

    with columns[0]:
        value = st_echarts(options=options, width="100%", key="0", events=events)

        st.write(value)
