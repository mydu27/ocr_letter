from starlette.config import Config  # 获取环境变量

config = Config(".env")

# url前缀
URL_FIX = '/api/v1'

# -------mysql-------
mysqlIp = config("mysqlIp", default='127.0.0.1')
mysqlPort = config("mysqlPort", cast=int, default=3306)
dbName = config("dbName", default='test')
mysqlUser = config("mysqlUser", default='root')
mysqlPwd = config("mysqlPwd", default='123456')
savePath = config("savePath", default='./images/')

# mysql 数据库
SQLALCHEMY_DATABASE_URI = f'mysql://{mysqlUser}:{mysqlPwd}@{mysqlIp}:{mysqlPort}/{dbName}?charset=utf8mb4'
