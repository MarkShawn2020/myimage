# 我的图床

### 初始化脚本
```bash
pip install requirements.txt
```

### 使用说明
#### 七牛云使用
```python
DOMAIN = xxx
BUCKET = xxx
AK = xxx
SK = xxx

from myimage import Qiniuyun
q = Qiniuyun(DOMAIN, BUCKET, AK, SK)

img_path = r'C:\Users\mark\Pictures\mark_wechat_pocket_qr.png'
img_path_online = q.upload(img_path)
```

