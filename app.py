import streamlit as st


def main():
    pages = {
        "导航": [
            st.Page(r"pages/home.py", title="小智洞界未来", icon=":material/home:"),
        ],
        "小智财经": [
            st.Page(r"pages/store_management.py", title="乐福天地", icon=":material/empty_dashboard:"),
            st.Page(r"pages/new_product_operations.py", title="金融属性", icon=":material/empty_dashboard:"),
        ],
        "小智健康": [
            st.Page(r"pages/product_management.py", title="饮食规律", icon=":material/empty_dashboard:"),
            st.Page(r"pages/new_products.py", title="体育运动", icon=":material/empty_dashboard:"),
        ],
        "小智随笔": [
            st.Page(r"pages/data_analysis.py", title="灵光一现", icon=":material/monitoring:"),
            st.Page(r"pages/data_form.py", title="信息体系", icon=":material/empty_dashboard:"),
        ],
        "小智科技": [
            st.Page(r"pages/system_settings.py", title="Ai工具箱", icon=":material/desktop_cloud:"),
        ]
    }

    pg = st.navigation(pages, expanded=False)
    pg.run()
    with st.sidebar:
        st.caption(body=f'用户：{st.session_state.logged_in}')
        if st.button(label='注销', key='log_off', type='secondary', use_container_width=True):
            st.session_state.clear()
            from cookies import cookie_setAndremove
            cookie_setAndremove(sign='删除')


# 用来重置侧边导航栏
def empty_sidebar():
    pass


if __name__ == "__main__":
    if 'logged_in' not in st.session_state:
        from cookies import cookie_setAndremove

        state = cookie_setAndremove(sign='查询')
        # 如果未登录
        if state:
            from pages.login_register import auth_page

            auth_page()
            # 重置streamlit导航
            pg = st.navigation([st.Page(empty_sidebar)], expanded=False, position='hidden')
            pg.run()
        else:
            main()
    else:
        main()
