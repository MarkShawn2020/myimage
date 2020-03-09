# -*- coding: utf-8 -*-
# -----------------------------------
# @CreateTime   : 2020/3/10 1:48
# @Author       : Mark Shawn
# @Email        : shawninjuly@gmai.com
# ------------------------------------
import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")

import os
import requests


def check_local_exist(func):
	def wrapper(self, img_path, *args, **kwargs):
		assert os.path.exists(img_path), "本地不存在该图片！请核实: {}".format(img_path)
		return func(self, img_path, *args, **kwargs)
	return wrapper


def check_target_exist(target_path: str):
	return requests.head(target_path).status_code == 200