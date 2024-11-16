import streamlit as st
import pandas as pd


distance=int


st.title("Restaurant Finder Zurich")
st.write(
    "This app will help you find your favorite restaurant in zurich!"
)
# requesting the users location, choise of cuisine, price-range and preferred rating
location =  st.text_input("Location:", 
                        placeholder="Please write your location here"
                        )

cuisine =   st.selectbox("What type of cuisine are you looking for?",
                        ("Asian", "French", "Italian","suprise me"),
                        index=None,
                        placeholder="Select Cuisine",
                        )

price =     st.selectbox("In what price-range should the restaurant fall?",
                        ("cheap","average","expensive","very expensive"),
                        index=None,
                        placeholder="Select price-range"
                        )

#making sure the user gives an input to all requirements for the search
if cuisine!=None and location!=0 and price!=None: 
        
    distance = st.slider(
                        "Select the maximum distance to the restaurant", 0, 20, step=5
                        )                        
        
rating = st.slider("Rating", 0, 5)
        
st.write("Looking for", cuisine, "restaurants", distance,"near", location,"with a rating of", rating,"or above")
        
if st.button("Search", icon="🔎"):
               st.write("database.location")
# database.location is just a placeholder the map and a short review of the restaurants that meet the search critiria will be displayed here
else:
        st.write("Please fill out the attributes of the kind of restauraunt you are looking for!")
        
