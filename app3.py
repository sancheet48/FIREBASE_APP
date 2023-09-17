import streamlit as st
import pandas as pd


df = pd.read_csv("titanic.csv")
imp_cols = ['Survived', 'Pclass', 'Sex', 'Embarked']

st.title("Titanic Survivor Predictor")

nav = st.sidebar.selectbox(
    "What would you like to do?",
    ("1. Read the Data", "2. Use Chatbot", "3. Update the data")
)

output_df = None 

def nav_1():
    choice = dict.fromkeys(imp_cols)

    for key in choice:
        choice[key] = "No Value Selected"

    with st.form("filter_form"):
        for ele in imp_cols:
            column_name = ele
            unique_values = ["No Value Selected"] + list(df[column_name].unique())
            selected_value = st.selectbox(column_name, unique_values)
            if selected_value != "No Value Selected":
                choice[ele] = selected_value

        submitted = st.form_submit_button("Submit")

    if submitted:
        # Create a DataFrame based on the selected values
        filtered_df = df
        for key, value in choice.items():
            if value != "No Value Selected":
                filtered_df = filtered_df[filtered_df[key] == value]

       
        st.write("Selected Values:")
        st.write(choice)

        st.write("Filtered DataFrame:")
        st.write(filtered_df)

        return filtered_df

@st.cache_data
def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')  

def download_output(output_df):
    # Add a button to download the filtered data as CSV
    if output_df is not None and not output_df.empty:
        csv = convert_df(output_df)
        st.download_button(
            label="Download data as EXCEL",
            data=csv,
            file_name='Filtered_Output.csv',
            mime='text/csv',
        )


def chatbot():
    pass


# Display the form or other content based on user choice
if nav == "1. Read the Data":
    st.write("Welcome to Reading the Data")

    output_df = nav_1()
    download_output(output_df)

if nav == "2. Use Chatbot":
    st.write("Welcome to Using the Chatbot")

if nav == "3. Update the data":
    st.write("Welcome to Updating the Data")
