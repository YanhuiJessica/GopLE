
<img src="logo.png" width=550px>

# Current Plan👿

## 需求分析🧐

该应用是一个基于 Web 的数据库应用，这个应用是一个查询关于电影数据库的数据，数据部分信息经过了脱密处理，数据及相关数据文档由教师指定。开发的基本功能需求如下：

- [x] 搜索任务🔍
  - [x] 根据用户 ID，搜索用户所看的电影名字和评分，按时间从新到旧排序，给出电影的前三个标签及关联度评分
  - [x] 根据输入的关键词，查询电影名字里有关键词的电影
  - [x] 查询某一风格最受欢迎的 20 部电影（请给出你的最受欢迎的定义，风格数据处理较难，需要精心设计）
  - [x] 根据性别推荐最受欢迎的电影 20 部电影
- 界面规范📱
  - 界面上应该有录入用户 ID, 检索关键词、风格等的文本框和不同任务的提交按钮，风格最好提供选择框。搜索结果要在网页上或客户端图形 UI 展示，超过一页的要有滚动条。
- 用户希望界面友好，查询响应速度快
- 系统可以支持未来数据量的大幅增加
- 各组尽可能地做查询速度的优化，并在最后提交的文档中包含测试结果

## 开发架构选择😊

- [Django+MongoDB](https://django-mongodb-engine.readthedocs.io/en/latest/)

## 开发时间计划📌

时间 | 计划
-|-
4月23日|组建队伍
5月7日|选定数据库，确定人物分工，上报相关文档
5月28日|方案提交设计
6月11日|中期检查(开发进度，分工工作完成情况，未按计划实施原因，改进措施)
6月25日|提交完整文档，系统开发报告与演示