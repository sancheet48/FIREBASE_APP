
import pandas as pd
import streamlit as st

df = pd.read_csv('titanic.csv')
df = df.head(10)

@st.cache_data
def convert_df(df):
    return df.to_csv(index=False).encode('utf-8') 
def download_output(output_df):
    # Add a button to download the filtered data as CSV
    if output_df is not None and not output_df.empty:
        csv = convert_df(output_df)
        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='Filtered_Output.csv',
            mime='text/csv',
        )

st.title("Echo Bot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = df[prompt]
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.dataframe(response)
        download_output(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response.to_markdown()})

    # Scroll to the bottom of the chat container using JavaScript
    scroll_js = """
    <script>
    var chatContainer = document.querySelector('.stContainer');
    chatContainer.scrollTop = chatContainer.scrollHeight;
    </script>
    """
    st.markdown(scroll_js, unsafe_allow_html=True)