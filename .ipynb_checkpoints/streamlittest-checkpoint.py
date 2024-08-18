# importing the libraries

import streamlit as st
import json
import os

# Defining the Streamlit app layout

# Streamlit app title
st.title("Company Announcements")

# Directory where my .txt files (one for each ticker) are stored
directory = os.path.join(os.path.dirname(__file__), 'Data')

# Initialize an empty dictionary to store the data of each ticker
# key: ticker, value: announcements

company_data = {}

# Loop through all the files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.txt'):
        
        # Extract the company name from the filename (without the .txt extension)
        company_name = filename.replace('.txt', '')

        # Open the .txt file and read its content
        with open(os.path.join(directory, filename), 'r') as file:
            
            # Load the content as a JSON object
            content = json.load(file)
            
            # Store the content in the dictionary with the company name as the key
            company_data[company_name] = content

# This function prints the announcements of ticker (chosen from drop down menu)
# The input to the function is one of the 5 tickers

def specifc_company(option):

    st.subheader("Latest Announcements")

    # Retrieve the data for the selected company
    announcements = company_data[option].get('data', [])
    
    if announcements:

        # if the user wants to view only those announcements that have 'Trading Halt' in their header
        
        if halt_option == 'YES':
            for announcement in announcements:
                if 'Trading Halt' in announcement.get('header', ''):
            
                    st.write(f"**ID:** {announcement.get('id', 'No ID')}")
                    st.write(f"**Document Release Date:** {announcement.get('document_release_date', 'No Release Date')}")
                    st.write(f"**Document Date:** {announcement.get('document_date', 'No Document Date')}")
                    st.write(f"**Header:** {announcement.get('header', 'No Header')}")
                    st.write(f"**Issuer:** {announcement.get('issuer_full_name', 'No Issuer Name')} ({announcement.get('issuer_code', 'No Issuer Code')})")
                    st.write(f"**Market Sensitive:** {'Yes' if announcement.get('market_sensitive', False) else 'No'}")
                    st.write(f"**Number of Pages:** {announcement.get('number_of_pages', 'No Page Info')}")
                    st.write(f"**Size:** {announcement.get('size', 'No Size Info')}")
                    st.write("---")

        # if the user wants to view all the announcements
        
        else:
            
            for announcement in announcements:
                
                    st.write(f"**ID:** {announcement.get('id', 'No ID')}")
                    st.write(f"**Document Release Date:** {announcement.get('document_release_date', 'No Release Date')}")
                    st.write(f"**Document Date:** {announcement.get('document_date', 'No Document Date')}")
                    st.write(f"**Header:** {announcement.get('header', 'No Header')}")
                    st.write(f"**Issuer:** {announcement.get('issuer_full_name', 'No Issuer Name')} ({announcement.get('issuer_code', 'No Issuer Code')})")
                    st.write(f"**Market Sensitive:** {'Yes' if announcement.get('market_sensitive', False) else 'No'}")
                    st.write(f"**Number of Pages:** {announcement.get('number_of_pages', 'No Page Info')}")
                    st.write(f"**Size:** {announcement.get('size', 'No Size Info')}")
                    st.write("---")


# a drop down list is created in the app that allows user to select their desired ticker

option = st.selectbox(
    "Which company announcement would you like to see?",
    ("AEE", "REZ", "1AE", "1MC", "NRZ"),
)

# displays the option the user has selected

st.write("You selected:", option)

# a drop down list is created in the app that allows user to either view announcements with header as 'Trading Halt' or
# view all the announcements

halt_option = st.selectbox(
    "Do you only want to see Trading Halt announcements?",
    ("YES", "NO"),
)

# calling the function

specifc_company(option)