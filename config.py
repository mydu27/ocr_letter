from starlette.config import Config  # 获取环境变量

config = Config(".env")

# url前缀
URL_FIX = '/api/v1'

# -------mysql-------
mysqlIp = config("mysqlIp", default='172.16.10.183')
mysqlPort = config("mysqlPort", cast=int, default=5306)
dbName = config("dbName", default='test')
mysqlUser = config("mysqlUser", default='root')
mysqlPwd = config("mysqlPwd", default='pujian123')
savePath = config("savePath", default='./images/')

# mysql 数据库
SQLALCHEMY_DATABASE_URI = f'mysql://{mysqlUser}:{mysqlPwd}@{mysqlIp}:{mysqlPort}/{dbName}?charset=utf8mb4'
