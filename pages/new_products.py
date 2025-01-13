import streamlit as st

def new_product_development_page():
    st.title("新品开发")
    st.text_input("创意名称")
    st.text_area("概念描述")
    st.text_area("开发时间线")
    st.file_uploader("上传原型图片")
    st.button("提交开发计划")

new_product_development_page()