import streamlit as st
import pandas as pd
import plotly.express as px

def store_management_page():
    st.title("店铺管理")
    st.text_input("店铺名称")
    st.text_area("店铺描述")
    st.number_input("产品总数", min_value=0, step=1)
    st.text_input("店铺经理")
    st.button("更新店铺信息")
    st.subheader("店铺销售概览")
    sales_data = {
        "月份": ["一月", "二月", "三月", "四月"],
        "销售额": [12000, 15000, 14000, 16000]
    }
    df = pd.DataFrame(sales_data)
    fig = px.bar(df, x="月份", y="销售额", title="月度销售概览")
    st.plotly_chart(fig)

store_management_page()