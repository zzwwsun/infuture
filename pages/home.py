import streamlit as st
from streamlit_extras.stylable_container import stylable_container
import random


def load_amazon_news():
    """
    加载亚马逊新闻
    :return:
    """
    return [
        {"title": "亚马逊宣布2024年新政策更新",
         "content": "亚马逊将在2024年推出新的仓储费用政策，这将影响许多卖家的运营模式。",
         "image": "https://cdn.pixabay.com/photo/2021/06/13/08/15/laptop-6332546_1280.jpg"},
        {"title": "畅销产品排行榜发布", "content": "本月电子产品成为亚马逊畅销榜首位，销售额增长了25%。",
         "image": "https://cdn.pixabay.com/photo/2019/04/26/07/14/store-4156934_1280.png"},
        {"title": "卖家扶持计划", "content": "亚马逊推出新计划，帮助新卖家快速启动并优化运营。",
         "image": "https://cdn.pixabay.com/photo/2018/09/17/12/40/business-3683769_1280.jpg"},
        {"title": "亚马逊 Prime 会员日", "content": "即将到来的Prime会员日将提供大量折扣，预计会大幅提升销售量。",
         "image": "https://cdn.pixabay.com/photo/2017/03/29/00/50/amazon-2183855_1280.png"},
        {"title": "仓储中心扩建", "content": "亚马逊计划在明年扩建多个仓储中心，提高配送效率。",
         "image": "https://cdn.pixabay.com/photo/2023/04/13/07/48/door-7921956_1280.jpg"}
    ]


def render_home_page():
    # 今日头条
    news_data = load_amazon_news()
    headline = random.choice(news_data)

    st.subheader("今日头条")
    col1, col2 = st.columns([2, 3])
    with col1:
        st.image(headline['image'], width=150)
    with col2:
        st.write(f"### {headline['title']}")
        st.write(headline['content'])

    # 分类新闻
    st.subheader("分类新闻")
    categories = ["畅销产品", "卖家支持", "物流动态"]
    for category in categories:
        st.markdown(f"#### {category}")
        cols = st.columns(2)
        for i, col in enumerate(cols):
            news = random.choice(news_data)
            with col:
                st.image(news['image'], width=100)
                st.write(f"**{news['title']}**")
                st.caption(news['content'])

    # 热门新闻
    st.subheader("热门新闻")
    hot_news = random.sample(news_data, 3)
    for news in hot_news:
        st.image(news['image'], width=150)
        st.write(f"### {news['title']}")
        st.write(news['content'])


def hover_card():
    with stylable_container(
            key='sty',
            css_styles='''
            {
                position: fixed; /* 让容器固定在页面顶部 */
                top: 3.6rem; /* 距顶部距离 */
                left: 0;  /* 距左边界距离 */
                width: 100%; /* 宽度 */
                background: #ffeb3b; /* 背景 #FFFFFF */
                z-index: 1000; /* 确保容器层级高于其他内容 */
                padding: 0 0; /* 内边距 */
                box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1); /* 投影效果 */
            }
        '''
    ):
        with st.container(height=50, border=False):
            st.markdown("""
                <div style="background-color: #FFFFFF; padding: 10px; text-align: center; font-size:14px;">
                    🌟 最新消息：我们的产品现已在全球范围内上市！
                </div>
            """, unsafe_allow_html=True)


def home_page():
    hover_card()
    st.title("应用仪表盘")
    cols = st.columns(spec=[1, 1, 1], gap='medium', vertical_alignment='top', border=True)
    cols[0].metric(label="总销售额", value="¥50,000", delta="5%")
    cols[1].metric(label="活跃用户数", value="1,200", delta="+100")
    cols[2].metric(label="产品数量", value="350", delta="-10")
    st.text_input("搜索", placeholder="这只是一个摆设...")
    render_home_page()


home_page()
