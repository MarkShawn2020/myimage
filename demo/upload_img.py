# -*- coding: utf-8 -*-
# -----------------------------------
# @CreateTime   : 2020/4/23 22:59
# @Author       : Mark Shawn
# @Email        : shawninjuly@gmail.com
# ------------------------------------

import myimage
q = myimage.IMG_Qiniuyun()

IMG_PATH = 'XXX'
online_img_path = q.upload_img(IMG_PATH)
print(online_img_path)