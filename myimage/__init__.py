# -*- coding: utf-8 -*-
# -----------------------------------
# @CreateTime   : 2020/3/10 1:46
# @Author       : Mark Shawn
# @Email        : shawninjuly@gmai.com
# ------------------------------------
from myimage.upload import qiniuyun, sm_ms
from myimage.convert_md.core import convert

upload_img = sm_ms.SMMS().upload_img

IMG_SMMS = sm_ms.SMMS
IMG_Qiniuyun = qiniuyun.Qiniuyun

convert_md = convert

