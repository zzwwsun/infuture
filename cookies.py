import streamlit as st
from streamlit_cookies_controller import CookieController

# 初始化 cookie 管理器
controller = CookieController(key='cookies')

@st.fragment
def cookie_setAndremove(sign, cookies=None):
    match sign:
        case '设置':
            # 设置 cookie
            controller.set(name='name', value=cookies)
        case '删除':
            # 删除指定 cookie
            controller.remove(name='name')
            st.rerun(scope='app')
        case '查询':
            # 获取指定 cookie
            cookie = controller.get(name='name')
            if cookie:
                st.session_state['logged_in'] = cookie
                return False
            else:
                return True
