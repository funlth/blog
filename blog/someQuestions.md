# 读取静态文件显示404 77 错误  
    [25/Feb/2023 21:56:14] "GET /static/layer/layer.js HTTP/1.1" 404 77
    [25/Feb/2023 21:56:23] "GET /static/ckeditor/ckeditor/skins/moono-lisa/dialog.css?t=I3I8 HTTP/1.1" 404 77
    [25/Feb/2023 21:56:23] "GET /static/ckeditor/ckeditor/plugins/codesnippet/dialogs/codesnippet.js?t=I3I8 HTTP/1.1" 404 77
    起步
    线上部署时因设置了 settings.DEBUG = False 会导致静态文件都是 404 的情况。
    主要原因是应为关闭DEBUG模式后，Django 便不提供静态文件服务了。
    runserver 的启动
    如果运行是通过 runserver 命令的方式，那简单，
    在启动 runserver 指令后追加 --insecure 选项能参数强制 django 处理静态文件。
    解决方案：
        将django中setting文件中的 DEBUG = FALES 改为 DEBUG = TRUE 。
        在Terminal中输入指令 py manage.py runserver --insecure
        未完全解决！
        存在问题：表情无法使用，插入代码无法使用



# 所需要增加及改善的功能内容
    为所设定标签添加相对应的按钮属性---
    增加我的喜爱
    分类列表
    推荐
    将最新和最近分开编写
    markdown权属内容使用不完全
    更新界面设计
    登录，注册完善--存在登录界面表单提交错误
    添加数据分析页面   
    
    
    --文章列表存在作者属性为完全使用，需要增加文章列表索引作者进行显示

# 存在问题 邮箱无法正常使用 存在端口占用问题 
邮箱注册未实现
2023.3.16.2.29邮箱功能存在问题依旧未解决
邮箱问题解决成功，未采取验证登录等方式。   
数据分析功能copy未实现   




[django-allahth详细讲解](http://www.opcoder.cn/article/2/#signup)
[markdown个人教程--作者：卷不动的小白](https://blog.csdn.net/qq_40818172/article/details/126260661)  
[杜塞的个人博客](https://www.dusaiphoto.com/)  
[RUNOOB](https://www.runoob.com/)   
[gitee](https://gitee.com/)    
[github](https://github.com/)


项目启动方式
# 首先创建虚拟空间（需先下载虚拟空间库vir..）
python -m venv venv 
# 进入虚拟空间
venv\Scripts\activate
# 下载所需库文件
pip install -r tip.txt
# 数据库映射
py manage.py makemigrations
py manage.py migrete
# 完成以上内容后如无报错，则启动程序
py manage.py runserver
