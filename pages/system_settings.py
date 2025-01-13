import streamlit as st

def system_settings_page():
    st.title("系统设置")
    st.checkbox("启用通知")
    st.checkbox("自动备份")
    st.text_input("管理员邮箱")
    st.button("保存设置")

system_settings_page()