# -*- coding: utf-8 -*-
# -----------------------------------
# @CreateTime   : 2020/3/10 3:41
# @Author       : Mark Shawn
# @Email        : shawninjuly@gmai.com
# ------------------------------------
from myimage.common import *


class SMMS:

	def __init__(self):
		self._host = 'https://sm.ms/api/v2'
		self._upload_api = self._host + '/upload'

	@check_local_exist
	def upload_img(self, img_path):
		result = requests.post(self._upload_api, files={"smfile": open(img_path, "rb")}).json()
		if result["code"] == "success":
			logging.info("Uploaded {}".format(result["data"]["url"]))
			return result['data']["url"]

		elif result["code"] == "image_repeated":
			logging.info("Repeated {}".format(result["images"]))
			return result["images"]

		else:
			raise result


if __name__ == '__main__':
	SMMS().upload_img(r'C:\Users\mark\Documents\微信截图_20190806164931.png')