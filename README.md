# 我的图床

### 初始化脚本
```bash
pip install requirements.txt
```

### 使用说明
#### 使用SM.MS图床
该图床可无需注册使用，即随手上传图片，并获得一个外链。

```python
import myimage
img_path = r'xxxx'
img_path_online = myimage.upload_img(img_path)
```

#### 使用七牛云
需要配置您的键，支持两种方式。

##### 1. （推荐）配置settings文件启动
打开settings文件后，填写一下键信息：
```python
DOMAIN = xxx
BUCKET = xxx
AK = xxx
SK = xxx
```

接着就可以使用以下代码上传图片了：
```python
import myimage
q = myimage.IMG_Qiniuyun()

img_path = r'xxx'
img_path_online = q.upload_img(img_path)
```
##### 2. 直接通过参数输入启动
```python
import myimage
q = myimage.IMG_Qiniuyun()
q.init_from_params(domain='xx', bucket='xx', ak='xx', sk='xx')

img_path = r'xxx'
img_path_online = q.upload_img(img_path)
```

```


