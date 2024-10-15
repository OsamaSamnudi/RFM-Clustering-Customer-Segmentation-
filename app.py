import streamlit as st
import pandas as pd

# Assuming rfm_df and new_df are defined DataFrames
# Replace this with your actual data loading code
# Example:
rfm_df = pd.read_csv('rfm_data.csv')
new_df = pd.read_csv('new_data.csv')


pd.options.display.float_format ='{:,.2f}'.format
st.set_page_config (page_title = 'RFM' , layout = "wide" , page_icon = 'Z')
st.title("RFM analysis")

# Sidebar
brief = st.sidebar.checkbox(":red[Brief about Project]")
Planning = st.sidebar.checkbox(":green[About Project]")
About_me = st.sidebar.checkbox(":green[About me]")

if brief:
    st.sidebar.header(":red[Brief about Project]")
    st.sidebar.write("""
    * RFM analysis (Recency, Frequency, Monetary) is a proven marketing model for customer segmentation. 
    * It helps businesses understand and segment their customers based on their purchasing behavior. 
    * By applying clustering algorithms to RFM data, businesses can more precisely group customers into different segments, 
    * which allows for more targeted marketing strategies and personalized communication.
    * :red[So let us see the insights 👀.]
    """)
# Planning
if Planning :
    st.sidebar.header(":green[About Project]")
    st.sidebar.subheader ('RFM analysis')
    st.sidebar.write("""
    * This project during my Intership @ Epsilon AI (https://www.epsiloneg.com/). 

    """)
    st.sidebar.write("""
    * Features Used during Project :
        * CustomerID	
        * MerchantName	
        * Category	
        * TransactionRank	
        * TransactionRedeemedPoints	
        * TransactionValue	
        * TransactionFrom(days)	
        * CustomerLastTransactionFrom(days)	
        * Recency	
        * Frequency	
        * Monetary	
        * RecencyScore	
        * FrequencyScore	
        * MonetaryScore	
        * Cluster	
        * RFM_Score
    """)
# Aboutme
if About_me :
    st.sidebar.header(":green[About me]")
    st.sidebar.write("""
    - Osama SAAD
    - Certified Data Science - Epsilon AI
    - Infor EAM Master Data and Assets Control Section Head @Ibnsina Pharma
    - LinkedIn: 
        https://www.linkedin.com/in/ossama-ahmed-saad-525785b2
    - Github : 
        https://github.com/OsamaSamnudi
    """)

tab1, = st.tabs(['🧠Prediction🤖'])

with tab1:
    with st.container():
        st.header("🧠 Prediction🤖")
            # Define your Cut_Merch function
        def Cut_Merch(x):
            Cust_Cluster = float(rfm_df[rfm_df['CustomerID'] == x]['Cluster'].iloc[0])
        
            # Get top categories and their details
            Top_Cat = new_df[new_df.Cluster == Cust_Cluster].groupby(['Category'])['RFM_Score'].mean().nlargest(2).index.tolist()
            Top_Cat_Details = new_df[new_df.Cluster == Cust_Cluster].groupby(['Category'])['RFM_Score'].mean().nlargest(2).reset_index()
        
            # Get top merchants and their details
            Top_Merchants = new_df[(new_df.Cluster == Cust_Cluster) & (new_df.Category.isin(Top_Cat))].groupby(['MerchantName'])['RFM_Score'].mean().nlargest(3).index.tolist()
            Top_Merchants_Details = new_df[(new_df.Cluster == Cust_Cluster) & (new_df.Category.isin(Top_Cat))].groupby(['MerchantName'])['RFM_Score'].mean().nlargest(3).reset_index()
        
            # Streamlit output
            st.write(f"Customer Code: {x}\n")
            
            st.write("Top Categories:")
            st.dataframe(Top_Cat_Details)  # Display category details in a table
            
            st.write(f"Top Merchants: {Top_Merchants}")
            st.dataframe(Top_Merchants_Details)  # Display merchant details in a table
        
        # Streamlit interface
        st.title("Customer Recommendation App")
        
        # Text input for "Customer Code"
        customer_code = st.text_input("Enter Customer Code:")
        
        # Check if the user has input a value
        if customer_code:
            try:
                # Convert the input to an integer
                customer_code_int = int(customer_code)
                # Call the function with the provided customer code
                Cut_Merch(customer_code_int)
            except ValueError:
                st.error("Please enter a valid Customer Code (numeric).")
