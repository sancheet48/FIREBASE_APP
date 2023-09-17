import streamlit as st
import re
import pandas as pd

# Load the Titanic dataset
df = pd.read_csv("titanic.csv")

# Function to extract attributes from input text
def extract_attributes(input_text, attribute_patterns):
    extracted_attributes = {}
    
    for attribute, pattern in attribute_patterns.items():
        match = pattern.search(input_text)
        if match:
            extracted_attributes[attribute] = match.group(1)
        else:
            extracted_attributes[attribute] = "No Value Entered"
    
    return extracted_attributes

# Define attribute patterns and their corresponding names
attribute_patterns = {
    "sex": re.compile(r'sex is (\w+)', re.IGNORECASE),
    "pclass": re.compile(r'pclass is (\d+)', re.IGNORECASE),
    "siblings": re.compile(r'siblings is (\d+)', re.IGNORECASE)
}

# Get user input
input_text = st.text_input("Enter text")

# Submit button to trigger filtering
if st.button("Submit"):
    # Extract attributes
    extracted_attributes = extract_attributes(input_text, attribute_patterns)

    st.write(extracted_attributes)
    # Initialize the filtered DataFrame
    filtered_df = df.copy()

    for key, value in extracted_attributes.items():
            key = key.capitalize()
            value = value.capitalize()
            if value != "No Value Selected" and key in df.columns:
                filtered_df = filtered_df[filtered_df[key] == value]



    st.write("Filtered DataFrame:")
    st.write(filtered_df)






# .\env\Scripts\Activate ; cd .\TITANIC\   ; streamlit run app4.py  

