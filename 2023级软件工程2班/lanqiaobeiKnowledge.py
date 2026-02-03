from pyvis.network import Network

# 创建知识图谱
net = Network(height="700px", width="100%", bgcolor="#ffffff", font_color="black")

# 添加节点，设置字体大小与重要性关联
nodes = [
    {"name": "Python基础", "importance": 5, "desc": "核心基础"},
    {"name": "数据类型", "importance": 4, "desc": "基础数据结构"},
    {"name": "函数", "importance": 4, "desc": "代码组织"},
    {"name": "模块导入", "importance": 3, "desc": "代码复用"}
]

for node in nodes:
    net.add_node(
        node["name"],
        label=node["name"],
        # 字体大小与重要性成正比
        font={"size": node["importance"] * 4 + 12},  # 基础12px，每级+4px
        title=node["desc"]
    )

# 添加关系
net.add_edge("Python基础", "数据类型", weight=0.8)
net.add_edge("Python基础", "函数", weight=0.8)
net.add_edge("函数", "模块导入", weight=0.6)

# 生成HTML文件
net.write_html("/workspace/2023级软件工程2班/knowledge_graph.html")