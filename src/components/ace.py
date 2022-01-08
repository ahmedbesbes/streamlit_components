from streamlit_ace import st_ace


def display_ace():
    content = st_ace(language="python", theme="dracula")
    return content
