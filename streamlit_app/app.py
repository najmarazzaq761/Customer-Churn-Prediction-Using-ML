import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Title of Dashboard
st.title("Customer Data Analysis Dashboard")

# Upload CSV File
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # Convert Date Columns to DateTime format for proper analysis
    df['invoice_date'] = pd.to_datetime(df['invoice_date'], errors='coerce')
    df['dob'] = pd.to_datetime(df['dob'], errors='coerce')
    df['age'] = (pd.Timestamp.now() - df['dob']).dt.days // 365  # Calculate age from Date of Birth
    
    # Sidebar Filters for interactive analysis
    st.sidebar.header("Filters")
    selected_city = st.sidebar.selectbox("Select City", ['All'] + list(df["city"].dropna().unique()))
    selected_gender = st.sidebar.selectbox("Select Gender", ['All'] + list(df["gender"].dropna().unique()))
    selected_age = st.sidebar.slider("Select Age Range", int(df["age"].min()), int(df["age"].max()), (int(df["age"].min()), int(df["age"].max())))
    
    # Apply Filters to the dataset based on user selection
    filtered_df = df.copy()
    if selected_city != 'All':
        filtered_df = filtered_df[filtered_df["city"] == selected_city]
    if selected_gender != 'All':
        filtered_df = filtered_df[filtered_df["gender"] == selected_gender]
    filtered_df = filtered_df[(filtered_df["age"] >= selected_age[0]) & (filtered_df["age"] <= selected_age[1])]
    
    # Key Metrics Calculation
    total_sales = filtered_df["price"].sum()
    total_customers = filtered_df["customer_id"].nunique()
    avg_purchase_value = filtered_df["price"].mean()
    churn_rate = (filtered_df["is_churned"].sum() / total_customers) * 100 if total_customers else 0
    
    # Display Key Metrics in a table format
    matrix_data = pd.DataFrame({
        "Metric": ["Total Sales", "Total Customers", "Avg Purchase Value", "Churn Rate"],
        "Value": [f"${total_sales:,.2f}", total_customers, f"${avg_purchase_value:.2f}", f"{churn_rate:.2f}%"]
    })
    st.table(matrix_data)
    
    # Sales Trend Over Time Visualization
    df["month"] = df["invoice_date"].dt.to_period("M").astype(str)  # Convert invoice date to month
    sales_trend = df.groupby("month")["price"].sum().reset_index()
    sales_trend["month"] = pd.to_datetime(sales_trend["month"])
    
    st.subheader("Sales Trend Over Time")
    fig = px.line(sales_trend, x="month", y="price", markers=True, title="Sales Trend Over Time")
    st.plotly_chart(fig)
    
    # Customer Age Distribution (Bar Graph)
    st.subheader("Customer Age Distribution")
    age_distribution = df["age"].value_counts().reset_index()
    age_distribution.columns = ["Age", "Count"]
    fig = px.bar(
        age_distribution, 
        x="Age", 
        y="Count", 
        title="Customer Age Distribution", 
        color="Count",
        color_continuous_scale=px.colors.sequential.Viridis
    )
    fig.update_traces(marker=dict(color=age_distribution["Count"], colorscale="Viridis"))
    st.plotly_chart(fig)
    
    # Sales by Category Visualization
    st.subheader("Sales by Category")
    category_sales = df.groupby("category")["price"].sum().reset_index()
    fig = px.bar(category_sales, x="category", y="price", title="Sales by Category", color="price")
    st.plotly_chart(fig)
    
    # Top Selling Products Visualization
    st.subheader("Top Selling Products")
    top_products = df.groupby("item")["price"].sum().nlargest(10).reset_index()
    fig = px.bar(top_products, x="item", y="price", title="Top 10 Selling Products", color="price")
    st.plotly_chart(fig)
    
    # World Map Visualization for Sales Distribution
    st.subheader("Sales Distribution (World Map)")
    map_df = df.groupby(["city", "country"], as_index=False)["price"].sum()
    fig = px.scatter_geo(
        map_df, 
        locations="country", 
        locationmode="country names",
        hover_name="city",
        size="price",
        title="Sales Distribution by Location",
        template="plotly_dark"
    )
    st.plotly_chart(fig)
    
    
    # Download Cleaned Data Button
    st.subheader("Download Cleaned Data")
    st.download_button("Download CSV", filtered_df.to_csv(index=False), file_name="cleaned_data.csv", mime="text/csv")
    
# Display message to guide users on uploading CSV file
st.info("Upload your CSV file to analyze customer data!")
