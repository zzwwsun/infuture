import streamlit as st
import sqlite3
from streamlit_extras.stylable_container import stylable_container


# 数据库初始化
def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                password TEXT
                )''')
    conn.commit()
    conn.close()


init_db()


# 用户注册/登录函数
def register_user(username, password=123):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    try:
        c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        conn.close()
        return False


def login_user(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = c.fetchone()
    conn.close()
    return user


# 注册成功
@st.dialog(title='注册成功')
def sign_up_ok(username, password):
    st.success(f"登录成功！欢迎{username}！登录密码：{password}")
    st.write('登录成功 跳转中。。。')
    st.session_state['logged_in'] = username
    import time
    time.sleep(3)
    # 设置 cookie
    from cookies import cookie_setAndremove
    cookie_setAndremove(sign='设置', cookies=username)
    # 重置
    st.rerun(scope='app')


def auth_page():
    st.title("用户认证")
    tab1, tab2 = st.tabs(["登录", "注册"])

    with tab1:
        cols = st.columns([16, 9])
        with cols[0]:
            st.header("登录")
            username = st.text_input("用户名", key="login_user")
            password = st.text_input("密码", type="password", key="login_pass")
            if st.button("登录"):
                if login_user(username, password):
                    st.success("登录成功！")
                    st.session_state['logged_in'] = True
                else:
                    st.error("用户名或密码错误")
        with cols[1]:
            with stylable_container(
                    key='tourist_login_style',
                    css_styles='''
                        button {
                            height: 300px;
                            width: 100%;
                            border: 1px solid #ddd;
                            border-radius: 8px;
                            background-color: rgb(255,75,75);
                            color: #FFFFFF;
                            cursor: pointer;
                            transition: all 0.3s ease;
                        }
                        button:hover {
                            color: inherit !important;
                            background-color: inherit !important;
                        }
                    '''
            ):
                if st.button(
                        label='游客登录',
                        key='tourist_login',
                        icon=':material/flutter_dash:',
                        use_container_width=True
                ):
                    from datetime import datetime
                    username = f"用户{datetime.now().strftime('%Y%m%d%H%M%S')}"
                    password = 123
                    if register_user(username, password):
                        sign_up_ok(username, password)

    with tab2:
        st.header("注册")
        username = st.text_input("用户名", key="register_user")
        password = st.text_input("密码", type="password", key="register_pass")
        if st.button("注册"):
            if register_user(username, password):
                sign_up_ok(username, password)
            else:
                st.error("用户名已存在")
