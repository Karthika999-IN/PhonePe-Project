import os
import subprocess
import pymysql

# Define paths and repository URL
repo_url = "https://github.com/PhonePe/pulse.git"
repo_path = os.path.join(os.getcwd(), "phonepe_pulse")

# ✅ Ensure Git is installed and use full path
git_path = r"C:\Program Files\Git\cmd\git.exe"

try:
    # Clone the repository if it doesn't exist
    if not os.path.exists(repo_path):
        subprocess.run([git_path, "clone", repo_url, repo_path], check=True)
        print("Repository cloned successfully.")
    else:
        print("Repository already exists.")
except Exception as e:
    print(f"Error cloning repository: {e}")
  
import os
import pandas as pd
import mysql.connector

# MySQL connection details
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mythili11$",  # Your MySQL password
)

mycursor = mydb.cursor()

# Step 1: Create database if it does not exist
mycursor.execute("CREATE DATABASE IF NOT EXISTS karphonepe;")
print("✅ Database 'karphonepe' is ready.")

# Step 2: Switch to the correct database
mycursor.execute("USE karphonepe;")

# Step 3: Create the required table
create_table_sql = """
CREATE TABLE IF NOT EXISTS Aggregated_transaction (
    State VARCHAR(255),
    Year INT,
    Quarter INT,
    Transaction_type VARCHAR(255),
    Transaction_count INT,
    Transaction_amount DECIMAL(15, 2)
);
"""
mycursor.execute(create_table_sql)
print("✅ Table 'Aggregated_transaction' is ready.")

# Step 4: Load the CSV file into a pandas DataFrame
csv_file_path = r"C:\Users\USER\OneDrive\Desktop\phonepe_kar\phonepe_transaction_data.csv"

# Check if the file exists
if not os.path.exists(csv_file_path):
    print("❌ CSV file not found. Check the file path.")
else:
    # Load CSV
    Agg_Trans = pd.read_csv(csv_file_path)

    # Print column names to verify
    print("CSV Columns:", Agg_Trans.columns)

    # Step 5: Insert data into MySQL
    def insert_data_into_mysql(dataframe, table_name):
        for i, row in dataframe.iterrows():
            row_data = tuple(row[["State", "Year", "Quarter", "Transaction_type", "Transaction_count", "Transaction_amount"]])
            
            sql = f"""
            INSERT INTO {table_name} (State, Year, Quarter, Transaction_type, Transaction_count, Transaction_amount)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            
            mycursor.execute(sql, row_data)

        mydb.commit()
        print(f"✅ {mycursor.rowcount} rows inserted into {table_name}.")

    # Call function to insert data
    insert_data_into_mysql(Agg_Trans, "Aggregated_transaction")

# Close MySQL connection
mycursor.close()
mydb.close()
print("✅ Database connection closed.")

import os
import pandas as pd
import mysql.connector

# MySQL connection details
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mythili11$",  # Your MySQL password
)

mycursor = mydb.cursor()

# Step 1: Use existing database
mycursor.execute("USE karphonepe;")
print("✅ Using Database 'karphonepe'.")

# Step 2: Create the Insurance table
create_table_sql = """
CREATE TABLE IF NOT EXISTS Aggregated_insurance (
    State VARCHAR(255),
    Year INT,
    Quarter INT,
    Insurance_type VARCHAR(255),
    Insurance_count INT,
    Insurance_amount DECIMAL(15, 2)
);
"""
mycursor.execute(create_table_sql)
print("✅ Table 'Aggregated_insurance' is ready.")

# Step 3: Load the CSV file into a pandas DataFrame
csv_file_path = r"C:\Users\USER\OneDrive\Desktop\phonepe_kar\insurance_data.csv"

# Check if the file exists
if not os.path.exists(csv_file_path):
    print("❌ CSV file not found. Check the file path.")
else:
    # Load CSV with correct column names
    columns = ["State", "Year", "Quarter", "Insurance_type", "Insurance_count", "Insurance_amount"]
    Agg_Ins = pd.read_csv(csv_file_path, names=columns, header=0)  # Set header=0 if first row has column names

    # Print column names to verify
    print("CSV Columns:", Agg_Ins.columns)

    # Step 4: Insert data into MySQL
    def insert_data_into_mysql(dataframe, table_name):
        for i, row in dataframe.iterrows():
            row_data = tuple(row[["State", "Year", "Quarter", "Insurance_type", "Insurance_count", "Insurance_amount"]])
            
            sql = f"""
            INSERT INTO {table_name} (State, Year, Quarter, Insurance_type, Insurance_count, Insurance_amount)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            
            mycursor.execute(sql, row_data)

        mydb.commit()
        print(f"✅ {mycursor.rowcount} rows inserted into {table_name}.")

    # Call function to insert data
    insert_data_into_mysql(Agg_Ins, "Aggregated_insurance")

# Close MySQL connection
mycursor.close()
mydb.close()
print("✅ Database connection closed.")

import os
import pandas as pd
import mysql.connector

# MySQL connection details
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mythili11$",  # Your MySQL password
)

mycursor = mydb.cursor()

# Step 1: Use existing database
mycursor.execute("USE karphonepe;")
print("✅ Using Database 'karphonepe'.")

# Step 2: Create the Aggregated User table
create_table_sql = """
CREATE TABLE IF NOT EXISTS Aggregated_user (
    Brand VARCHAR(255),
    Transaction_count INT,
    Percentage DECIMAL(5, 2),
    State VARCHAR(255),
    Year INT,
    Quarter INT
);
"""
mycursor.execute(create_table_sql)
print("✅ Table 'Aggregated_user' is ready.")

# Step 3: Load the CSV file into a pandas DataFrame
csv_file_path = r"C:\Users\USER\OneDrive\Desktop\phonepe_kar\user_data.csv"

# Check if the file exists
if not os.path.exists(csv_file_path):
    print("❌ CSV file not found. Check the file path.")
else:
    # Load CSV with correct column names
    columns = ["Brand", "Transaction_count", "Percentage", "State", "Year", "Quarter"]
    Agg_User = pd.read_csv(csv_file_path, names=columns, header=0)  # Set header=0 if first row has column names

    # Print column names to verify
    print("CSV Columns:", Agg_User.columns)

    # Step 4: Insert data into MySQL
    def insert_data_into_mysql(dataframe, table_name):
        for i, row in dataframe.iterrows():
            row_data = tuple(row[["Brand", "Transaction_count", "Percentage", "State", "Year", "Quarter"]])
            
            sql = f"""
            INSERT INTO {table_name} (Brand, Transaction_count, Percentage, State, Year, Quarter)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            
            mycursor.execute(sql, row_data)

        mydb.commit()
        print(f"✅ {mycursor.rowcount} rows inserted into {table_name}.")

    # Call function to insert data
    insert_data_into_mysql(Agg_User, "Aggregated_user")

# Close MySQL connection
mycursor.close()
mydb.close()
print("✅ Database connection closed.")

import os
import pandas as pd
import mysql.connector

# MySQL connection details
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mythili11$",  # Your MySQL password
)

mycursor = mydb.cursor()

# Step 1: Use existing database
mycursor.execute("USE karphonepe;")
print("✅ Using Database 'karphonepe'.")

# Step 2: Create the Map_Transaction table
create_table_sql = """
CREATE TABLE IF NOT EXISTS Map_Transaction (
    District VARCHAR(255),
    Transaction_count INT,
    Transaction_amount DECIMAL(15, 2),
    State VARCHAR(255),
    Year INT,
    Quarter INT
);
"""
mycursor.execute(create_table_sql)
print("✅ Table 'Map_Transaction' is ready.")

# Step 3: Load the CSV file into a pandas DataFrame
csv_file_path = r"C:\Users\USER\OneDrive\Desktop\phonepe_kar\transaction_data.csv"

# Check if the file exists
if not os.path.exists(csv_file_path):
    print("❌ CSV file not found. Check the file path.")
else:
    # Load CSV with correct column names
    columns = ["District", "Transaction_count", "Transaction_amount", "State", "Year", "Quarter"]
    Map_Trans = pd.read_csv(csv_file_path, names=columns, header=0)  # Set header=0 if first row has column names

    # Print column names to verify
    print("CSV Columns:", Map_Trans.columns)

    # Step 4: Insert data into MySQL
    def insert_data_into_mysql(dataframe, table_name):
        for i, row in dataframe.iterrows():
            row_data = tuple(row[["District", "Transaction_count", "Transaction_amount", "State", "Year", "Quarter"]])
            
            sql = f"""
            INSERT INTO {table_name} (District, Transaction_count, Transaction_amount, State, Year, Quarter)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            
            mycursor.execute(sql, row_data)

        mydb.commit()
        print(f"✅ {mycursor.rowcount} rows inserted into {table_name}.")

    # Call function to insert data
    insert_data_into_mysql(Map_Trans, "Map_Transaction")

# Close MySQL connection
mycursor.close()
mydb.close()
print("✅ Database connection closed.")

import os
import pandas as pd
import mysql.connector

# MySQL connection details
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mythili11$",  # Your MySQL password
)

mycursor = mydb.cursor()

# Step 1: Use existing database
mycursor.execute("USE karphonepe;")
print("✅ Using Database 'karphonepe'.")

# Step 2: Create the Map_Insurance table
create_table_sql = """
CREATE TABLE IF NOT EXISTS Map_Insurance (
    District VARCHAR(255),
    Insurance_count INT,
    Insurance_amount DECIMAL(15, 2),
    State VARCHAR(255),
    Year INT,
    Quarter INT
);
"""
mycursor.execute(create_table_sql)
print("✅ Table 'Map_Insurance' is ready.")

# Step 3: Load the CSV file into a pandas DataFrame
csv_file_path = r"C:\Users\USER\OneDrive\Desktop\phonepe_kar\insurance_map_data.csv"

# Check if the file exists
if not os.path.exists(csv_file_path):
    print("❌ CSV file not found. Check the file path.")
else:
    # Load CSV with correct column names
    columns = ["District", "Insurance_count", "Insurance_amount", "State", "Year", "Quarter"]
    Map_Insurance = pd.read_csv(csv_file_path, names=columns, header=0)  # Set header=0 if first row has column names

    # Print column names to verify
    print("CSV Columns:", Map_Insurance.columns)

    # Step 4: Insert data into MySQL
    def insert_data_into_mysql(dataframe, table_name):
        for i, row in dataframe.iterrows():
            row_data = tuple(row[["District", "Insurance_count", "Insurance_amount", "State", "Year", "Quarter"]])
            
            sql = f"""
            INSERT INTO {table_name} (District, Insurance_count, Insurance_amount, State, Year, Quarter)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            
            mycursor.execute(sql, row_data)

        mydb.commit()
        print(f"✅ {mycursor.rowcount} rows inserted into {table_name}.")

    # Call function to insert data
    insert_data_into_mysql(Map_Insurance, "Map_Insurance")

# Close MySQL connection
mycursor.close()
mydb.close()
print("✅ Database connection closed.")

import os
import pandas as pd
import mysql.connector

# MySQL connection details
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mythili11$",  
)

mycursor = mydb.cursor()

# Use existing database
mycursor.execute("USE karphonepe;")
print("✅ Using Database 'karphonepe'.")

# Create Table
create_table_sql = """
CREATE TABLE IF NOT EXISTS Map_User (
    District VARCHAR(255),
    RegisteredUser INT,
    AppOpens INT,
    State VARCHAR(255),
    Year INT,
    Quarter INT
);
"""
mycursor.execute(create_table_sql)
print("✅ Table 'Map_User' is ready.")

# Load CSV
csv_file_path = r"C:\Users\USER\OneDrive\Desktop\phonepe_kar\user_map_data.csv"
if not os.path.exists(csv_file_path):
    print("❌ CSV file not found.")
else:
    columns = ["District", "RegisteredUser", "AppOpens", "State", "Year", "Quarter"]
    Map_User = pd.read_csv(csv_file_path, names=columns, header=0)

    def insert_data(dataframe, table_name):
        for _, row in dataframe.iterrows():
            row_data = tuple(row)
            sql = f"INSERT INTO {table_name} VALUES (%s, %s, %s, %s, %s, %s)"
            mycursor.execute(sql, row_data)

        mydb.commit()
        print(f"✅ {mycursor.rowcount} rows inserted into {table_name}.")

    insert_data(Map_User, "Map_User")

# Close connection
mycursor.close()
mydb.close()
print("✅ Database connection closed.")

import os
import pandas as pd
import mysql.connector

# MySQL connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mythili11$",
)

mycursor = mydb.cursor()

# Use the database
mycursor.execute("USE karphonepe;")
print("✅ Using Database 'karphonepe'.")

# Create Table for Top_Transaction
create_table_sql = """
CREATE TABLE IF NOT EXISTS Top_Transaction (
    Pincode INT,
    Transaction_count INT,
    Transaction_amount DECIMAL(15, 2),
    State VARCHAR(255),
    Year INT,
    Quarter INT
);
"""
mycursor.execute(create_table_sql)
print("✅ Table 'Top_Transaction' is ready.")

# Load CSV File
csv_file_path = r"C:\Users\USER\OneDrive\Desktop\phonepe_kar\top_transaction_data.csv"

if not os.path.exists(csv_file_path):
    print("❌ CSV file not found. Check the file path.")
else:
    # Read CSV
    columns = ["Pincode", "Transaction_count", "Transaction_amount", "State", "Year", "Quarter"]
    Top_Transaction = pd.read_csv(csv_file_path, names=columns, header=0)

    # 🔹 **Fix NaN values**
    Top_Transaction.fillna({
        "Pincode": 0,
        "Transaction_count": 0,
        "Transaction_amount": 0.0,
        "State": "Unknown",
        "Year": 0,
        "Quarter": 0
    }, inplace=True)

    # Convert data types (to ensure compatibility)
    Top_Transaction["Pincode"] = Top_Transaction["Pincode"].astype(int)
    Top_Transaction["Transaction_count"] = Top_Transaction["Transaction_count"].astype(int)
    Top_Transaction["Transaction_amount"] = Top_Transaction["Transaction_amount"].astype(float)
    Top_Transaction["Year"] = Top_Transaction["Year"].astype(int)
    Top_Transaction["Quarter"] = Top_Transaction["Quarter"].astype(int)

    # Function to insert data
    def insert_data(dataframe, table_name):
        for _, row in dataframe.iterrows():
            row_data = tuple(row)
            sql = f"INSERT INTO {table_name} VALUES (%s, %s, %s, %s, %s, %s)"
            mycursor.execute(sql, row_data)

        mydb.commit()
        print(f"✅ {mycursor.rowcount} rows inserted into {table_name}.")

    # Insert data into MySQL
    insert_data(Top_Transaction, "Top_Transaction")

# Close connection
mycursor.close()
mydb.close()
print("✅ Database connection closed.")

import os
import pandas as pd
import mysql.connector

# MySQL Connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mythili11$",
)

mycursor = mydb.cursor()

# Use the database
mycursor.execute("USE karphonepe;")
print("✅ Using Database 'karphonepe'.")

# Create Table for Top_Insurance
create_table_sql = """
CREATE TABLE IF NOT EXISTS Top_Insurance (
    Pincode INT,
    Transaction_count INT,
    Transaction_amount DECIMAL(15, 2),
    State VARCHAR(255),
    Year INT,
    Quarter INT
);
"""
mycursor.execute(create_table_sql)
print("✅ Table 'Top_Insurance' is ready.")

# Load CSV File
csv_file_path = r"C:\Users\USER\OneDrive\Desktop\phonepe_kar\top_insurance_data.csv"

if not os.path.exists(csv_file_path):
    print("❌ CSV file not found. Check the file path.")
else:
    # Read CSV
    columns = ["Pincode", "Transaction_count", "Transaction_amount", "State", "Year", "Quarter"]
    Top_Insurance = pd.read_csv(csv_file_path, names=columns, header=0)

    # 🔹 **Fix NaN values**
    Top_Insurance.fillna({
        "Pincode": 0,
        "Transaction_count": 0,
        "Transaction_amount": 0.0,
        "State": "Unknown",
        "Year": 0,
        "Quarter": 0
    }, inplace=True)

    # Convert data types (to ensure compatibility)
    Top_Insurance["Pincode"] = Top_Insurance["Pincode"].astype(int)
    Top_Insurance["Transaction_count"] = Top_Insurance["Transaction_count"].astype(int)
    Top_Insurance["Transaction_amount"] = Top_Insurance["Transaction_amount"].astype(float)
    Top_Insurance["Year"] = Top_Insurance["Year"].astype(int)
    Top_Insurance["Quarter"] = Top_Insurance["Quarter"].astype(int)

    # Function to insert data
    def insert_data(dataframe, table_name):
        for _, row in dataframe.iterrows():
            row_data = tuple(row)
            sql = f"INSERT INTO {table_name} VALUES (%s, %s, %s, %s, %s, %s)"
            mycursor.execute(sql, row_data)

        mydb.commit()
        print(f"✅ {mycursor.rowcount} rows inserted into {table_name}.")

    # Insert data into MySQL
    insert_data(Top_Insurance, "Top_Insurance")

# Close connection
mycursor.close()
mydb.close()
print("✅ Database connection closed.")

import os
import pandas as pd
import mysql.connector

# MySQL Connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mythili11$",
)

mycursor = mydb.cursor()

# Use the database
mycursor.execute("USE karphonepe;")
print("✅ Using Database 'karphonepe'.")

# Create Table for Top_Users
create_table_sql = """
CREATE TABLE IF NOT EXISTS Top_Users (
    Pincode INT,
    RegisteredUser INT,
    State VARCHAR(255),
    Year INT,
    Quarter INT
);
"""
mycursor.execute(create_table_sql)
print("✅ Table 'Top_Users' is ready.")

# Load CSV File
csv_file_path = r"C:\Users\USER\OneDrive\Desktop\phonepe_kar\top_user_data.csv"

if not os.path.exists(csv_file_path):
    print("❌ CSV file not found. Check the file path.")
else:
    # Read CSV
    columns = ["Pincode", "RegisteredUser", "State", "Year", "Quarter"]
    Top_Users = pd.read_csv(csv_file_path, names=columns, header=0)

    # 🔹 **Fix NaN values**
    Top_Users.fillna({
        "Pincode": 0,
        "RegisteredUser": 0,
        "State": "Unknown",
        "Year": 0,
        "Quarter": 0
    }, inplace=True)

    # Convert data types (to ensure compatibility)
    Top_Users["Pincode"] = Top_Users["Pincode"].astype(int)
    Top_Users["RegisteredUser"] = Top_Users["RegisteredUser"].astype(int)
    Top_Users["Year"] = Top_Users["Year"].astype(int)
    Top_Users["Quarter"] = Top_Users["Quarter"].astype(int)

    # Function to insert data
    def insert_data(dataframe, table_name):
        for _, row in dataframe.iterrows():
            row_data = tuple(row)
            sql = f"INSERT INTO {table_name} VALUES (%s, %s, %s, %s, %s)"
            mycursor.execute(sql, row_data)

        mydb.commit()
        print(f"✅ {mycursor.rowcount} rows inserted into {table_name}.")

    # Insert data into MySQL
    insert_data(Top_Users, "Top_Users")

# Close connection
mycursor.close()
mydb.close()
print("✅ Database connection closed.")

import streamlit as st
import mysql.connector
import pandas as pd
import plotly.express as px

# Connect to MySQL
def get_data():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Mythili11$",
            database="karphonepe"
        )
        mycursor = mydb.cursor()

        # Fetch data (use correct column names)
        query = "SELECT state, year, quarter, transaction_count, transaction_amount FROM Aggregated_transaction;"
        mycursor.execute(query)
        data = mycursor.fetchall()

        # Get column names
        column_names = [i[0] for i in mycursor.description]

        # Convert to DataFrame
        df = pd.DataFrame(data, columns=column_names)

        return df

    except mysql.connector.Error as err:
        st.error(f"Database Error: {err}")
        return None

# Load Data
df = get_data()

st.title("📊 PhonePe Transaction Analysis")

if df is not None:
    st.write("✅ Data Loaded Successfully!")
    st.write(df.head())  # Show first few rows

    # Bar Chart
    st.subheader("Transaction Amount by State")
    fig_bar = px.bar(df, x="state", y="transaction_amount", color="state", title="Transaction Amount by State")
    st.plotly_chart(fig_bar)
else:
    st.error("⚠️ No data available. Please check the database connection.")

import streamlit as st
import mysql.connector
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Database connection function
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Mythili11$",
        database="karphonepe"
    )

# Fetch data function
def fetch_data(query):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns=[desc[0] for desc in cursor.description])
    cursor.close()
    conn.close()
    return df

# Streamlit UI
st.title("PhonePe Data Analysis Dashboard")

# Sidebar for Case Study Selection
case_study = st.sidebar.selectbox("Select a Case Study", [
    "Decoding Transaction Dynamics",
    "Device Dominance and User Engagement",
    "Insurance Penetration and Growth",
    "Transaction Analysis for Market Expansion",
    "User Engagement and Growth Strategy"
])

# Query and visualization based on case study
if case_study == "Decoding Transaction Dynamics":
    st.header("Transaction Trends Across States")
    df = fetch_data("SELECT State, Year, Quarter, Transaction_type, Transaction_count, Transaction_amount FROM Aggregated_transaction")
    
    # Bar Chart
    fig = px.bar(df, x="State", y="Transaction_count", color="Transaction_type", barmode="group",
                 title="Transactions by State and Type")
    st.plotly_chart(fig)
    
    # Heatmap
    pivot_df = df.pivot_table(values="Transaction_amount", index="State", columns="Quarter", aggfunc="sum")
    fig, ax = plt.subplots()
    sns.heatmap(pivot_df.astype(float), annot=True, cmap="coolwarm", fmt=".0f", linewidths=0.5)
    st.pyplot(fig)

elif case_study == "Device Dominance and User Engagement":
    st.header("User Engagement Across Devices")
    
    # Fetch data with correct column names
    df = fetch_data("SELECT Brand, State, Transaction_count, Percentage FROM Aggregated_user")
    
    # Pie Chart
    fig = px.pie(df, values="Transaction_count", names="Brand", title="Device Brand Market Share")
    st.plotly_chart(fig)
    
    # Bar Chart
    fig = px.bar(df, x="Brand", y="Transaction_count", color="State", title="Transactions by Device Brand & State")
    st.plotly_chart(fig)


elif case_study == "Insurance Penetration and Growth":
    st.header("Insurance Adoption Across States")
    df = fetch_data("SELECT State, Year, Quarter, Insurance_type, Insurance_count, Insurance_amount FROM Aggregated_insurance")
    
    # Choropleth Map
    fig = px.choropleth(df, locations="State", locationmode="geojson-id", color="Insurance_amount",
                         title="Insurance Transactions Across States")
    st.plotly_chart(fig)

elif case_study == "Transaction Analysis for Market Expansion":
    st.header("Market Expansion Insights")
    df = fetch_data("SELECT State, Year, Quarter, Transaction_count, Transaction_amount FROM Top_transaction")
    
    # Bar Chart
    fig = px.bar(df, x="State", y="Transaction_count", color="Transaction_amount",
                 title="Transactions by State")
    st.plotly_chart(fig)

elif case_study == "User Engagement and Growth Strategy":
    st.header("User Growth Trends")
    df = fetch_data("SELECT State, Year, Quarter, RegisteredUser, AppOpens FROM Map_user")
    
    # Line Chart
    fig = px.line(df, x="Quarter", y="RegisteredUser", color="State",
                  title="User Registration Trends Over Quarters")
    st.plotly_chart(fig)

st.sidebar.write("Developed by Karthika")




