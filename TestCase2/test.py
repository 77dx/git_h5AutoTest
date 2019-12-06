# -*- coding:utf-8 -*-
import os,sys
#将项目根路径添加到path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

#将boss_Page加入路径
page_path = os.path.join(BASE_DIR,'TestCase2')
sys.path.append(page_path)



print BASE_DIR
print page_path