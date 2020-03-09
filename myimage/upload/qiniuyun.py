# -*- coding: utf-8 -*-
# -----------------------------------
# @CreateTime   : 2020/3/10 1:47
# @Author       : Mark Shawn
# @Email        : shawninjuly@gmai.com
# ------------------------------------
import qiniu

from myimage.common import *
from myimage import settings as st


class Qiniuyun:

	def __init__(self):
		self._must_keys = [
			"QINIU_DOMAIN",
			"QINIU_BUCKET",
			"QINIU_AK",
			"QINIU_SK"
		]
		try:
			self.init_from_settings()
		except NotImplementedError:
			logging.warning("建议通过settings文件配置七牛云，否则必须通过`self.init_from_params`初始化！")


	def init_from_settings(self):
		for key in self._must_keys:
			if not hasattr(st, key):
				raise NotImplementedError("从`upload/settings.py`文件初始化七牛云，必须要有以下键：{}".format(self._must_keys))
			else:
				setattr(self, key, getattr(st, key))
		self.q = qiniu.Auth(self.__ak, self.__sk)

	def init_from_params(self, domain, bucket, ak, sk):
		"""
		七牛云图床配置的几个参数
		具体可以查看https://portal.qiniu.com/kodo/bucket

		:param domain:
		:param bucket:
		:param ak:
		:param sk:
		"""
		self._domain = domain
		self._bucket = bucket
		self.__ak    = ak
		self.__sk    = sk
		self.q = qiniu.Auth(self.__ak, self.__sk)

	@check_local_exist
	def upload_img(self, img_path: str, check_exist=True):
		"""
		上传文件到七牛云与个人站点

		:param img_path: 要上传的本地文件地址
		:param check_exist: 是否检查目标服务器已存在对应文件，如果有，则不上传
		:return: 目标图像的外链
		"""
		key = os.path.basename(img_path)
		img_path_online =  "{}/{}".format(self._domain, key)
		if check_exist and check_target_exist(img_path_online):
			logging.info("Using cached: {}".format(img_path_online))
		else:
			token = self.q.upload_token(self._bucket, key, 3600)
			ret, info = qiniu.put_file(token , key, img_path)
			assert ret["key"] == key
			logging.info("Uploaded: {}".format(img_path_online))
		return img_path_online


if __name__ == '__main__':
	q = Qiniuyun()
	q.init_from_settings()
