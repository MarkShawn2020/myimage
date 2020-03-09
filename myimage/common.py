# -*- coding: utf-8 -*-
# -----------------------------------
# @CreateTime   : 2020/3/10 1:48
# @Author       : Mark Shawn
# @Email        : shawninjuly@gmai.com
# ------------------------------------
import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")


import requests


def check_target_exist(target_path: str):
	return requests.head(target_path).status_code == 200