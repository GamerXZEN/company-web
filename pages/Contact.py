import streamlit as sl
from send_email import send_email as se
import pandas as pd


sl.header("Contact Me")

data = pd.read_csv("topics.csv")

with sl.form(key="email_form", clear_on_submit=True):
	email = sl.text_input("Your email address", placeholder="Enter email address. Ex: youwho@gnpmail.com")
	topic = sl.selectbox("What topic do you want to discuss", data)
	feedback = sl.text_area("Text", placeholder="Enter your feedback")
	feedback = f"""\
Subject: {topic}
{feedback}
From {email}"""
	button = sl.form_submit_button("Submit")
	if button:
		sl.info("Success: email sent")
		se(message=feedback)
