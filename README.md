# evernote_remove_duplicates
印象笔记去重
## 关注主线
1. 访问以下网站获取 token，填入 py 文件的 token 处  
https://app.yinxiang.com/api/DeveloperToken.action
2. 打开 IDE 运行 py 文件
## 注意事项
1. 笔记本**不可重名**
2. 每个笔记本内的笔记**数目不得多于 250 个**
## 方法
#### get_notebook_list
调用 API，获得**笔记本数据集**
#### search_note
接受笔记本名称，获得该笔记本下的**笔记数据集**
#### get_note_list
接受**笔记本数据集**，获得**笔记数据集**
#### writer_to_excel
导出备查 excel
## 数据结构
#### 笔记本数据集
columns = ['tag', 'name', 'guid']
#### 笔记数据集
columns=['name', 'guid']
## 参考文献
1. 印象笔记开发者文档  
https://dev.yinxiang.com/doc/  
2. 使用 Python 操作 Evernote - 简书  
https://www.jianshu.com/p/bda26798f3b3  
3. Github / EvernoteController  
https://github.com/littlecodersh/EasierLife/tree/master/Programs/Evernote  
