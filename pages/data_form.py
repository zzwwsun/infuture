import streamlit as st

def amazon_data_input_page():
    with st.form(key='data_form_amazon', clear_on_submit=True):
        st.title("Amazon 数据填报")
        st.text_input("产品名称")
        st.text_area("描述")
        st.number_input("价格", min_value=0.0, step=0.01)
        st.number_input("库存", min_value=0, step=1)
        st.text_input("类别")
        st.text_input("ASIN (Amazon 标准识别码)")
        st.date_input("上线日期")
        st.file_uploader("上传产品图片")
        st.form_submit_button(label='提交', type='primary')

amazon_data_input_page()