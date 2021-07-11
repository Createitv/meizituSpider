## About <a name = "about"></a>

[妹子图](https://www.mzitu.com/)全站图片爬虫

![举例](https://typora-1300715298.cos.ap-shanghai.myqcloud.com/uPic/image-20210711104354843.png)

#### ![其中一页](https://typora-1300715298.cos.ap-shanghai.myqcloud.com/uPic/image-20210711104317155.png)

## Getting Started <a name = "getting_started"></a>

### 本机环境

`python3.9`+`vscode`

```
Scrapy==2.5.0
itemadapter==0.2.0
```

### Installing


```
pip3 install -r requirements.txt
```

### Command

```
scrapy crawl meizi
```

### settings.py

```
CONCURRENT_REQUESTS = 10 # 默认10并发
DOWNLOAD_DELAY = 0.4 # 请求延迟0.4*(0.5-1.5之间的随机数)
IMAGES_STORE = 'images' # 替换images改成自己想保存的文件夹
```
