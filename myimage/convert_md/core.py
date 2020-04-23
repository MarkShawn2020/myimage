# -*- coding: utf-8 -*-
# -----------------------------------
# @CreateTime   : 2020/4/23 21:57
# @Author       : Mark Shawn
# @Email        : shawninjuly@gmail.com
# ------------------------------------
import re
import myimage
q = myimage.IMG_Qiniuyun()


def get_online_img_path(local_img_path_matched):
	img_name = local_img_path_matched.group(1)
	abs_local_img_path = r"{}\{}.png".format(md_img_dir_path, img_name)
	abs_online_img_path = q.upload_img(abs_local_img_path)
	return "![{}]({})".format(img_name, abs_online_img_path)


def convert(md_path, md_img_dir_path):
	# md_path_to_save = r'C:\Users\mark\Desktop\华为财挑2020初赛之5G预测模型参考_converted.md'
	# md_img_dir_name_in_file = '华为财挑2020初赛之5G预测模型参考.assets'
	md_path_to_save = md_path.replace('.md', '_converted.md')
	md_img_dir_name_in_file = md_img_dir_path.split('\\')[-1]

	with open(md_path, 'r', encoding='utf-8') as f:
		s = f.read()

	s2 = re.sub('!\[(.*?)\]\({}/(.*?)\)'.format(md_img_dir_name_in_file), get_online_img_path, s)

	with open(md_path_to_save, 'w', encoding='utf-8') as f:
		f.write(s2)


if __name__ == '__main__':
	md_path = r'C:\Users\mark\Desktop\华为财挑2020初赛之5G预测模型参考.md'
	md_img_dir_path = r'C:\Users\mark\Desktop\华为财挑2020初赛之5G预测模型参考.assets'
	convert(md_path, md_img_dir_path)
