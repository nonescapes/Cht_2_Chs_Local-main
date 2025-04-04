# Author: catwbu
# Date: 2023-1-04

# Date: 2024-06-23
# Version:1.1.0

from opencc import OpenCC as cc
import pyperclip
import keyboard
import time

import os
import configparser
import ast

#觸發按鍵設定
#key_='f4','f3'
'''
#自定義修復詞
fix_text=[['捷径','快捷方式'],
['fps','帧数'],
['教学','教程'],
['文档夹','文件夹'],
['程序崩溃','程序闪退'],
['影片','视频'],['仿真器','模拟器'],['模块','模组'],['存盘','存档']]
'''
# 获取当前工作目录
current_directory = os.getcwd()
print(f"當前目錄為: {current_directory}")

# 构建配置文件的完整路径
config_file_path = os.path.join(current_directory, 't2c_settings.ini')
# 创建配置解析器对象
config = configparser.ConfigParser()
# 读取配置文件时指定编码为 utf-8
with open(config_file_path, 'r', encoding='utf-8') as file:
    config.read_file(file)
# 获取 fix_text 的内容
fix_text_str = config['DEFAULT']['fix_text']
key_=config['DEFAULT']['key']

# 使用 ast.literal_eval 将字符串转换为 Python 对象
fix_text = ast.literal_eval(fix_text_str)

# 打印结果
print(fix_text)
print(key_)

while True:
    #esc 關閉功能
#    if keyboard.read_key() == "esc": break
    if keyboard.read_key() == key_:
        time.sleep(0.05)
        keyboard.press_and_release("ctrl+c")
        time.sleep(0.05)
        ttext = cc('tw2sp').convert(pyperclip.paste())
        #自定義詞彙套用
        for i in fix_text:
            if i[0] in ttext:
                ttext=ttext.replace(i[0],i[1])
        pyperclip.copy(ttext)
        print(ttext)
        keyboard.press_and_release("ctrl+v")
        time.sleep(1.5)
        continue
