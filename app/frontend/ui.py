import streamlit as st
import requests
import os
from app.config.settings import settings
from app.common.logger import get_logger
from app.common.custom_exception import CustomException
from urllib.parse import urljoin


logger = get_logger(__name__)

st.set_page_config(page_title="Multi AI Agent", layout="centered")
st.title("Multi AI Agent")

system_prompt = st.text_area("Define your AI Agent: ", height=70)

selected_model = st.selectbox("Select your AI model: ", settings.ALLOWED_MODEL_NAMES)

allow_web_search = st.checkbox("Allow Web Search")

user_query = st.text_area("Enter your query: ", height=150)

API_URL = urljoin(settings.API_URL, "chat")

if st.button("Ask Agent") and user_query.strip():
    payload = {
        "model_name": selected_model,
        "system_prompt": system_prompt,
        "messages": [user_query],
        "allow_search": allow_web_search
    }

    try:
        logger.info("Sending request to backend")
        with st.spinner("Thinking..."):                     
            response = requests.post(API_URL, json=payload)

        if response.status_code == 200:
            agent_response = response.json().get("response", "")
            logger.info("Succesfully recieved response from backend")

            st.subheader("Agent Response")
            st.markdown(agent_response.replace("\n", "<br>"), unsafe_allow_html=True)

        else:
            logger.error("Backend error")
            st.error("Error with backend")
            # st.error(f"Backend error: {response.status_code} - {response.json().get('detail', 'Unknown error')}")

    except Exception as e:
        logger.error("Error occured while sending request to backend")
        st.error(str(CustomException("failed to communicate with backend")))