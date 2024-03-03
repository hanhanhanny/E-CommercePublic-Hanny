import streamlit as st
import matplotlib.pyplot as plt
from datetime import datetime
import seaborn as sns
import pandas as pd
sns.set(style='dark')

all_df = pd.read_csv("https://raw.githubusercontent.com/hanhanhanny/E-CommercePublic-Hanny/main/dashboard/main_data.csv")
datetime_columns = ["order_purchase_timestamp", "order_delivered_customer_date"]
all_df.sort_values(by="order_purchase_timestamp", inplace=True)
all_df.reset_index(inplace=True)

for column in datetime_columns:
    all_df[column] = pd.to_datetime(all_df[column])

#membuat filter dari datetime
min_date = all_df["order_purchase_timestamp"].min()
max_date = all_df["order_delivered_customer_date"].max()

def create_daily_orders_df(all_df):
    daily_orders_df = df.resample(rule='D', on='order_date').agg({
        "order_id": "nunique",
        "total_price": "sum"
    })
    daily_orders_df = daily_orders_df.reset_index()
    daily_orders_df.rename(columns={
        "order_id": "order_count",
        "total_price": "revenue"
    }, inplace=True)
    
    return daily_orders_df

with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://github.com/hanhanhanny/E-CommercePublic-Hanny/blob/main/assets/logo.jpg")
    
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Date',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

    st.header('E-Commerce Dashboard :sparkles:')

    st.caption('Made by Hanny (2023)')