import streamlit as st
import pandas as pd

def product_management_page():
    st.title("产品管理")
    st.text_input("搜索产品")
    st.dataframe(pd.DataFrame({
        "产品": ["A", "B", "C"],
        "库存": [50, 30, 100],
        "价格": [10.0, 15.0, 5.0]
    }))
    cols = st.columns(spec=[1,1, 3])
    cols[0].button("添加新产品")
    cols[1].button("移除产品")

product_management_page()