import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def test_toast():
    import time
    data = [
        ('🔥', '最近更新 2024-12-19', '产品 A 销售额增长了 10%。'),
        ('🔀', '最近更新 2024-12-20', '新增类别 【电子产品】。'),
        ('⚠️', '最近更新 2024-12-21', '系统维护计划于下周进行。'),
    ]
    for dt in data:
        st.toast('  \n'.join([dt[1], f'**{dt[2]}**']), icon=dt[0])
        time.sleep(1)


# 模拟数据
def get_amazon_data():
    return pd.DataFrame({
        "产品名称": ["产品A", "产品B", "产品C", "产品D", "产品E"],
        "类别": ["电子", "家居", "服装", "电子", "家居"],
        "价格": [199.99, 89.99, 29.99, 249.99, 99.99],
        "销量": [150, 200, 300, 100, 250],
        "评分": [4.5, 4.0, 3.5, 5.0, 4.8],
        "库存": [50, 20, 100, 10, 40],
        "销售额": [29998.5, 17998.0, 8997.0, 24999.0, 24997.5]
    })


# Amazon 数据分析页面
def amazon_data_analysis_page():
    st.title("Amazon 数据分析")

    # 数据加载
    df = get_amazon_data()
    st.subheader("Amazon 数据表")
    st.dataframe(df)

    cols = st.columns([1, 1])
    with cols[0]:
        # 可视化 1: 销量柱状图
        st.subheader("各产品销量对比")
        fig_sales = px.bar(df, x="产品名称", y="销量", color="类别", text="销量", title="销量柱状图")
        st.plotly_chart(fig_sales)
    with cols[1]:
        # 可视化 2: 销售额饼图
        st.subheader("各产品销售额占比")
        fig_pie = px.pie(df, names="产品名称", values="销售额", title="销售额饼图")
        st.plotly_chart(fig_pie)

    # 可视化 3: 评分与价格的散点图
    st.subheader("评分与价格的关系")
    fig_scatter = px.scatter(df, x="评分", y="价格", size="销量", color="类别", title="评分与价格的关系",
                             hover_name="产品名称")
    st.plotly_chart(fig_scatter)

    # 可视化 4: 库存和销量的气泡图
    st.subheader("库存与销量的关系")
    fig_bubble = px.scatter(df, x="库存", y="销量", size="销售额", color="类别", title="库存与销量的关系",
                            hover_name="产品名称")
    st.plotly_chart(fig_bubble)

    # 可视化 5: 类别销售额堆叠柱状图
    st.subheader("不同类别的销售额分布")
    fig_stacked = px.bar(df, x="类别", y="销售额", color="产品名称", text="销售额", title="类别销售额堆叠柱状图")
    st.plotly_chart(fig_stacked)

    # 可视化 6: 销量和销售额的双轴图
    st.subheader("销量与销售额的对比")
    fig_dual = go.Figure()
    fig_dual.add_trace(go.Bar(x=df["产品名称"], y=df["销量"], name="销量", marker_color='rgb(55, 83, 109)'))
    fig_dual.add_trace(go.Line(x=df["产品名称"], y=df["销售额"], name="销售额", marker_color='rgb(26, 118, 255)'))
    fig_dual.update_layout(title="销量与销售额对比", barmode='group')
    st.plotly_chart(fig_dual)

    # 可视化 7: 价格箱线图
    st.subheader("不同类别产品价格分布")
    fig_box = px.box(df, x="类别", y="价格", color="类别", title="价格箱线图")
    st.plotly_chart(fig_box)

    # 可视化 8: 热力图
    st.subheader("数据相关性热力图")
    corr = df[["价格", "销量", "评分", "库存", "销售额"]].corr()
    fig_heatmap = px.imshow(corr, text_auto=True, title="数据相关性热力图")
    st.plotly_chart(fig_heatmap)

    # 可视化 9: 销售额时间序列（模拟数据）
    st.subheader("月度销售额趋势")
    trend_data = pd.DataFrame({
        "月份": ["一月", "二月", "三月", "四月", "五月"],
        "销售额": [10000, 15000, 20000, 25000, 30000]
    })
    fig_line = px.line(trend_data, x="月份", y="销售额", title="月度销售额趋势")
    st.plotly_chart(fig_line)

    # 可视化 10: 评分分布直方图
    st.subheader("产品评分分布")
    fig_hist = px.histogram(df, x="评分", nbins=5, title="评分分布直方图")
    st.plotly_chart(fig_hist)


amazon_data_analysis_page()
test_toast()
