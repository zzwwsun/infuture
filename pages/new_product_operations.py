
import streamlit as st

def new_product_operations_page():
    st.title("新品运营")
    st.text_input("新品名称")
    st.text_area("营销策略")
    st.date_input("上线日期")
    st.number_input("初始库存", min_value=0, step=1)
    st.text_input("目标用户群体")
    st.button("保存运营计划")

new_product_operations_page()