import streamlit as st
import requests

st.set_page_config(page_title="Customer Review", layout="centered")

st.title("📝 Customer Review Form")

name = st.text_input("Your Name")
review = st.text_area("Write your review")

submit = st.button("Submit")

if submit:
    if name == "" or review == "":
        st.error("Please fill all fields")
    else:
        payload = {
            "name": name,
            "review": review
        }

        # رابط Webhook من n8n
        webhook_url = "https://casen-troublous-undeterminably.ngrok-free.dev/webhook/2ebf9bdf-cb4f-4790-90b1-9a613c1cb1f4"

        response = requests.post(webhook_url, json=payload)

        if response.status_code == 200:
            st.success("✅ Review submitted successfully")
        else:
            st.error("❌ Something went wrong")
