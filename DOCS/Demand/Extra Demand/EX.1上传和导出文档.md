# 额外需求EX.1 上传和导出文档
#### 用户可以上传本地文档；翻译完成后，用户可以导出并下载文档。
## 场景EX.1.1 文档格式兼容
#### 前提
系统处于开始界面，显示“请选择要翻译的文档”。
#### 正常状态
用户可以上传各种格式的文档，包括.docx、.pdf、.txt等，系统兼容这些格式的文档，并能从文档中提取只保留缩进的文本，忽略文档中的图片等内容。
#### 可能的问题
- EX.1.1.1用户上传的文件中包含表格、流程图等特殊格式的文本<br>
  系统提示“检测到特殊文本”并询问是否翻译每一类的特殊文本
#### 其他活动
#### 结束状态
系统跳转到翻译界面。
