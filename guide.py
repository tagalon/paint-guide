import streamlit as st
import json
from streamlit import components

def custom_multiselect(options_dict):
    frontend_location = "frontend/"
    
    selected_colors = components.v1.html(
        open("index.html", "r").read(),
        args={"optionsWithColors": [{"Name": key, "RGB": value} for key, value in options_dict]},
        height=300
    )
    
    return selected_colors

def convert_json(file_path):
    with open(file_path, 'r') as file:
    # Load the JSON content from file
        data = json.load(file)
    return data
# Test
if __name__ == "__main__":
    
    color_dict = convert_json('data.json')
    selected = custom_multiselect(color_dict)
    if selected:
        st.write("Selected Colors:", selected)
    else:
        st.write("No colors selected yet.")
