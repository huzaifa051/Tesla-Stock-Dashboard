import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from plotly import express as px

# Set the page configuration (must be at the top)
st.set_page_config(page_title="Tesla Stock Analysis", layout="wide", page_icon="📈")

# Load the dataset
data_path = "Tesla Stock Data.csv"  # Ensure this file is in the same directory
df = pd.read_csv(data_path)

# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Custom CSS for styling
st.markdown(
    """
    <style>
    .main { background-color: #f5f5f5; }
    .stButton>button { background-color: #0066cc; color: white; border-radius: 8px; padding: 8px 16px; }
    .stSidebar { background-color: #e6f7ff; }
    </style>
    """,
    unsafe_allow_html=True
)

# App Title and Description
st.title("📊 Tesla Stock Data Visualization Dashboard")
st.markdown("Analyze and visualize Tesla stock data with interactive charts and insights.")

# Sidebar for user input
st.sidebar.header("🔧 Options")
st.sidebar.markdown("Use the controls below to customize your experience.")

selected_columns = st.sidebar.multiselect(
    "Select Columns for Overview:", df.columns, default=["Date", "Open", "Close", "Volume"]
)

# Display Dataset and Statistics
st.header("📁 Dataset Overview")
if selected_columns:
    st.dataframe(df[selected_columns], use_container_width=True)
else:
    st.warning("Please select columns to display.")

st.subheader("📈 Summary Statistics")
st.write(df.describe())

# Visualization Functions
def plot_line_chart():
    st.subheader("📈 Line Chart: Closing Prices Over Time")
    fig = px.line(df, x='Date', y='Close', title="Tesla Closing Prices Over Time", labels={'Close': 'Closing Price'})
    st.plotly_chart(fig, use_container_width=True)

def plot_bar_chart():
    st.subheader("📊 Bar Chart: Trading Volume")
    fig = px.bar(df[:50], x='Date', y='Volume', title="Trading Volume (First 50 Days)", labels={'Volume': 'Volume'})
    st.plotly_chart(fig, use_container_width=True)

def plot_histogram():
    st.subheader("📊 Histogram: Adjusted Closing Prices")
    fig = px.histogram(df, x='Adj Close', nbins=20, title="Distribution of Adjusted Closing Prices")
    st.plotly_chart(fig, use_container_width=True)

def plot_box_plot():
    st.subheader("📦 Box Plot: Stock Prices")
    fig = px.box(df, y=['Open', 'High', 'Low', 'Close'], title="Box Plot of Stock Prices")
    st.plotly_chart(fig, use_container_width=True)

def plot_scatter_plot():
    st.subheader("🌟 Scatter Plot: High vs Low Prices")
    fig = px.scatter(df, x='High', y='Low', title="High vs Low Prices", labels={'High': 'High Prices', 'Low': 'Low Prices'})
    st.plotly_chart(fig, use_container_width=True)

def plot_pie_chart():
    st.subheader("🍰 Pie Chart: Volume Proportion (First 10 Days)")
    fig = px.pie(df[:10], values='Volume', names=df['Date'][:10].dt.date, title="Volume Proportion (First 10 Days)")
    st.plotly_chart(fig, use_container_width=True)

def plot_heatmap():
    st.subheader("🔥 Heatmap: Correlations")
    corr = df.corr()
    fig = px.imshow(corr, text_auto=True, title="Correlation Heatmap", color_continuous_scale=px.colors.diverging.RdBu)
    st.plotly_chart(fig, use_container_width=True)

def plot_area_chart():
    st.subheader("📈 Area Chart: Adjusted Closing Prices")
    fig = px.area(df, x='Date', y='Adj Close', title="Area Chart of Adjusted Closing Prices", labels={'Adj Close': 'Adjusted Closing Price'})
    st.plotly_chart(fig, use_container_width=True)

def plot_pair_plot():
    st.subheader("🔗 Pair Plot: Numeric Columns")
    pairplot_fig = sns.pairplot(df[['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']])
    plt.title("Pair Plot of Numeric Columns")
    st.pyplot(pairplot_fig.fig)

def plot_moving_average():
    st.subheader("📈 Moving Average (30 Days): Closing Prices")
    df['30 Day MA'] = df['Close'].rolling(window=30).mean()
    plt.figure(figsize=(10, 6))
    plt.plot(df['Date'], df['Close'], label='Closing Price', alpha=0.5)
    plt.plot(df['Date'], df['30 Day MA'], label='30 Day MA', color='orange')
    plt.title("30-Day Moving Average of Closing Prices")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    st.pyplot(plt)

# Display Graphs
st.markdown("---")
st.header("📊 Interactive Visualizations")
plot_line_chart()
plot_bar_chart()
plot_histogram()
plot_box_plot()
plot_scatter_plot()
plot_pie_chart()
plot_heatmap()
plot_area_chart()
plot_moving_average()

# Footer
st.sidebar.markdown("---")
st.sidebar.info("Created by Samar Murtaza, Samiullah, and Huzaifa Rehman Qureshi.")
