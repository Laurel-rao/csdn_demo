
# 数据库

## 代码创建

1. 创建 连接类，一般在配置文件（config.py）中写入

   ```python
        import os
        
        BASE_DIR = os.path.abspath(os.path.dirname(__file__))
        
        # database
        host = "localhost"
        port = 3306
        username = "root"
        password = "root"
        database = "myflask"
        
        class Config(object):
    
            #格式为mysql+pymysql://数据库用户名:密码@数据库地址:端口号/数据库的名字?数据库格式
            SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{}:{}@{}:{}/{}?charset=utf8'.\
                format(username, password, host, port, database)
            SQLALCHEMY_TRACK_MODIFICATIONS = False
   ```

2. 在创建 app 的文件中，创建db对象

    ```python
        from flask_migrate import Migrate
        from flask_sqlalchemy import SQLAlchemy
    
        from config import Config

        app.config.from_object(Config)
        db = SQLAlchemy(app)
        migrate = Migrate(app, db)
        from .models import *
    ```
3. 在models 中创建模型类

    ```python
    from View import db
    
    
    class User(db.Model):
        __tablename__ = 'user'
        id = db.Column(db.Integer,primary_key=True)
        username = db.Column(db.String(64),index=True,unique=True)
        email = db.Column(db.String(120),index=True,unique=True)
        password_hash = db.Column(db.String(128))
    
        def __repr__(self):
            return '<用户名:{}>'.format(self.username)
    ```

## 数据库初始化

1. 创建代码后 ,运行 `flask db init`
    - 文件夹中无 app.py 或 wsgi.py 会报错
    ```
    Usage: flask db init [OPTIONS]
    
    Error: Failed to find Flask application or factory in module "app". Use "FLASK_APP=app:name to specify one.
    ```
    - 在文件目录中打开命令行，指定该文件
    ```
        set FLASK_APP=manage.py # windows
        export FLASK_APP=manage.py # linux
        flask db init
    ```
    - 这样就解决了

2. 运行 flask db migrate
    - 报错 
    ```
    Warning: (1366, "Incorrect string value: '\\xD6\\xD0\\xB9\\xFA\\xB1\\xEA...'
    ```
    - 解决， 安装mysql-connector, `pip install mysql-connector`
    - 在 config 改成 
    ```
        SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{}:{}@{}:{}/{}?charset=utf8'
    ```
    - 运行后发现结果是这样
        ```
            INFO  [alembic.runtime.migration] Context impl MySQLImpl.
            INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
            INFO  [alembic.env] No changes in schema detected.
        ```
    - 说明没有导入成功，因为没有找到models 文件
        - 检查 manage.py 中有没有导入 models文件
        - `from View import models`, 我放在靠后的部分
        
    
3. 将数据库文件导入到数据库中 `flask db upgrade`

4. 每次改动数据库后，都运行下面两句

    ```
        # 在 migrations/versions.py 中生成文件
        flask db migrate
        # 将文件导入到数据库中
        flask db upgrade
    ```

## 常见报错 

1. ImportError: cannot import name "db"
   
    - 将 register_blueprint 放在db的后面，就像这样
        ```
        db = SQLAlchemy(app)
        migrate = Migrate(app, db)
        from View.urls import urlAPI
        app.register_blueprint(urlAPI, url_prefix="/all")
        from .models import *
        ```
    - 顺序很重要，因为导入蓝图时，找不到相应的db
    
## 数据增删改查

1. 查看官网 <a href="http://flask-sqlalchemy.pocoo.org/2.3/">flask-sqlalchemy</a>
2. 查看官网 <a href="https://www.sqlalchemy.org/">sqlalchemy</a>

### 增

1. 增加一条记录
    ```
        u = User(username="zhang", email="zhang@123")
        db.session.add(u)    # 提交到缓存
        db.session.commit()  # 提交到数据库 
    ```
    ```
        s = User()
        s.username = "zhang"
        s.email = "zhang@123"
        db.session.add(u)
        db.session.commit()
    ```
    
2. 添加多条数据   

    ```
        u1 = User(username="zhang1", email="zhang@123")
        u2 = User(username="zhang2", email="zhang@123")
        u3 = User(username="zhang3", email="zhang@123")
        db.session.add(u1)    # 提交到缓存
        db.session.add(u2)    # 提交到缓存
        db.session.add(u3)    # 提交到缓存
        db.session.commit()  # 提交到数据库 
    ```
    ```
        u1 = User(username="zhang1", email="zhang@123")
        u2 = User(username="zhang2", email="zhang@123")
        u3 = User(username="zhang3", email="zhang@123")
        user_lists = []
        user_lists.append(u1)
        user_lists.append(u2)
        user_lists.append(u3)
        db.session.add_all(user_lists)
        db.session.commit()
    ```

### 查

1. all()

    ```
        users = User.query.all()
        print(users) # 所有User对象的列表，一行数据代表一个对象
        # <user1 :obj > <user2 :obj > <user3 :obj >
    ```
    
2. get()
    1. 未找到时，get() 返回 None
    ```
        user = User.query.get(1)
        print(user) # 一个user对象
        # <user1 :obj>
    ```
    
#### filter()  # 综合查询函数

1. filter 和 filter_by 函数 得到的都是 <class 'flask_sqlalchemy.BaseQuery'>
2. 该对象可继续进行其他操作(排序等)，完成复杂的检索
3. 该对象可遍历，取详细数据，使用 all(), first(), 取出 User 对象
4. 详情请看 `https://blog.csdn.net/weixin_42750983/article/details/82431257`

    ``` 
        # 通过id查找
        User.query.filter(User.id==1)
        User.query.filter_by(id=1)
        # 模糊查找
    
    ```

5. 模糊查询
    1. 通过模糊查询得到的结果都是字节对象`<用户名:bytearray(b'zhang')>`
    
    
    ```
        语法:filter(模型名.属性.运算符('xx'))
        运算符:
            contains：包含
            startswith：以什么开始
            endswith：以什么结束
            in_：在范围内
            like：模糊  '%' 代表任意字符 ， "_" 代表一个字符
            __gt__: 大于
            __ge__：大于等于
            __lt__：小于
            __le__：小于等于
            
        # 举例
        User.query.filter(User.id.in_([1, 2]))
        User.query.filter(User.username.like("%han%"))
    ```
    
6. 多条件逻辑查询

    1. _and, 查询姓名包含zhan，且年龄大于16的人
       
        `User.query.filter(_and(User.username.contains("zhan"), User.age.__gt__(16)))`
    2. _not, 查询不叫zhang的所有人
        `User.query.filter(_not(User.username=="zhang"))`
    3. _or， 查询姓名包含zhan，或者年龄大于16的人
        `User.query.filter(_or(User.username.contains("zhan"), User.age.__gt__(16)))`

7. 筛选
   
    1. limit()
    2. order_by()
    3. offset()
    4. 示例: `User.query.filter(User.id.in_([1, 2])).order_by("age")`
    
### 改

1. 通过对象.update 设置
   
    ```
    User.query.filter_by(id=3).update({"username":"zhang123"})
    db.session.commit()
    ```
    
2. 通过对象直接更改

    ```
        use1 = User.query.filter_by(id=3)
        use1.username = "zhang123"
        db.session.commit()
    ```
    
### 删除

1. 通过 查找后删除
    ```
        User.query.filter(User.id.__gt__(3)).delete()
        db.session.commit()   
    ```
    
2. 通过 session 删除对象

    ```
       user = User.query.get(1)
       db.session.delete(user)
       db.session.commit()
    ```

 > 本文代码示例 <a href="https://github.com/Laurel-rao/csdn_demo/tree/master/flask_db">Github</a>