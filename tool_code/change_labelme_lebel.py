# -*- encoding: utf-8 -*-
import os
import json
 
 
def Edit_label(json_dir,new_label = 'Diadematidae'):
 
    json_files = os.listdir(json_dir)
    json_dict = {}
    for json_file in json_files:
 
        #  只获取json文件
        if json_file[-4:] != 'json':
            continue
        jsonfile = json_dir + '/' + json_file
        with open(jsonfile, 'r', encoding='utf-8') as jf:
            info = json.load(jf)
 
            # 找到位置进行修改
            for i, label in enumerate(info['shapes']):
                info['shapes'][i]['label'] = new_label
 
            # 使用新字典替换修改后的字典
            json_dict = info
 
        # 将替换后的内容写入原文件
        with open(jsonfile, 'w') as fw:
            json.dump(json_dict, fw)
 
 
 
if __name__ == '__main__':
    #  文件夹目录
    json_dir = r"D:\\datasets\\UDD datasets\\label"
    new_label = 'Diadematidae'
    Edit_label(json_dir,new_label)
    print('OK!')
