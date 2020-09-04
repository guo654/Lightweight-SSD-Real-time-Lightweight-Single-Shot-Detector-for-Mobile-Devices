# -*- coding: utf-8 -*-
"""
本模块负责检索json文件内容，解决notepad++检索内容卡顿问题

"""
import json

with open("/home/jari/guoshi/workspace/mobilenetssd/models-master/research/object_detection/ssd_mixmodel_fpn_coco/COCO/annotations/instances_val2017.json", 'r', encoding='utf-8') as f:
    write_data = json.load(f)
    print(write_data['annotations'])


###write data###
#with open(r'test.json', 'w') as dump_f:
    #json.dump(write_data, dump_f)



