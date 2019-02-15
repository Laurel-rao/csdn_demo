
# 数据库

1. 创建代码后 ,运行 `flask init db`
    - 文件夹中无 app.py 或 wsgi.py 会报错
    ```
    Usage: flask db init [OPTIONS]

    Error: Failed to find Flask application or factory in module "app". Use "FLASK_APP=app:name to specify one.
    ```
    - 在文件目录中打开命令行，指定该文件
    ```
        set FLASK_APP=manage.py
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