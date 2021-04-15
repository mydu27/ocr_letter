## 1 项目功能

    上传图片，自动识别出图片中的字母

## 2 接口说明
- 2.1 上传图片，返回识别结果
    #### 接口功能
    > 上传图片，返回识别结果
    #### URL
    > [{your_ip}:8020/api/v1/ocr/letters]
    #### 支持格式
    > JSON
    #### HTTP请求方式
    POST
    #### 入参
      > | 名称     | 必选 | 类型   | 说明   |
      > | :------- | :--- | :----- | ------ |
      > | image | True | File | 上传的图片文件（必须为PNG或JPG） |
    ## 出参 (格式: Json)
    200: OK
    
      > | 返回字段 | 字段类型 | 说明              |
      > | :------- | :------- | :---------------- |
      > | data    | dict   | 识别出的字母列表 |
      > | code    | int   | <br>200-成功<br>415-图片格式错误<br> |

## 3 安装说明

### 3.1 DOCKER制作

    ```
    镜像构建详情看Dockerfile文件
    容器部署详情看docker-compose.yml文件
    ```

### 3.2 DOCKER部署命令

    ```
    构建镜像前，先配置docker-compose文件
    在build项填写项目目录的绝对路径，Dockerfile要放在目录中     
    在mysqlIp项填写自己mysql的ip 
    在mysqlPort项填写自己mysql的端口 
    在dbName项填写自己数据库的名称（数据库需在mysql中提前建好） 
    在mysqlUser项填写自己mysql的用户名 
    在mysqlPwd项填写自己mysql的密码
    配置好通过docker-compose来启动项目
    sudo docker-compose up -d
    ```
