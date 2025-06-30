import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go

st.set_page_config(page_title="Adidas US Sales Dashboard", layout="wide")
st.title("👟 Adidas US Sales Data Dashboard")

adidas = pd.read_csv("https://raw.githubusercontent.com/myoh0623/dataset/refs/heads/main/adidas_us_sales_datasets.csv", encoding='utf-8')

