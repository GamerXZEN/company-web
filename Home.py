import streamlit as sl
import pandas as pd

sl.title("The Best Company")
content = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""
sl.info(content)

sl.subheader("Our Team")

data = pd.read_csv("data1.csv")

col1, col2, col3 = sl.columns(3)

with col1:
	for index, row in data[:4].iterrows():
		sl.subheader(f"{row['first name'].title()} {row['last name'].title()}")
		sl.write(row["role"])
		sl.image("images/" + row["image"])

with col2:
	for index, row in data[4:8].iterrows():
		sl.subheader(f"{row['first name'].title()} {row['last name'].title()}")
		sl.write(row["role"])
		sl.image("images/" + row["image"])

with col3:
	for index, row in data[8:12].iterrows():
		sl.subheader(f"{row['first name'].title()} {row['last name'].title()}")
		sl.write(row["role"])
		sl.image("images/" + row["image"])
