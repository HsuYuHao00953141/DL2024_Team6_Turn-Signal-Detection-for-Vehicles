import json
import os
 
def convert(img_size, box):
    # dw = 1. / (img_size[0])
    # dh = 1. / (img_size[1])
    # x = (box[0] + box[2]) / 2.0 - 1
    # y = (box[1] + box[3]) / 2.0 - 1
    # w = box[2] - box[0]
    # h = box[3] - box[1]
    # x = x * dw
    # w = w * dw
    # y = y * dh
    # h = h * dh
    x1 = box[0]
    y1 = box[1]
    x2 = box[2]
    y2 = box[3]
    return (x1, y1, x2, y2)
 
 
def decode_json(json_floder_path, json_name):
    txt_name = "D:\\datasets\\sea_urchin_datasets\\sea_urchin\label_txt\\" + json_name[0:-5] + '.txt' #生成txt文件你想存放的路径
    txt_file = open(txt_name, 'w')
 
    json_path = os.path.join(json_floder_path, json_name)
    data = json.load(open(json_path, 'r', encoding='utf-8'))
 
    img_w = data['imageWidth']
    img_h = data['imageHeight']
 
    for i in data['shapes']:
 
        if (i['shape_type'] == 'polygon' and i['label'] == 'sea_urchin'): #分类的标签
            x1 = float((i['points'][0][0]))/img_w
            y1 = float((i['points'][0][1]))/img_h
            x2 = float((i['points'][1][0]))/img_w
            y2 = float((i['points'][1][1]))/img_h
 
            bb = (x1, y1, x2, y2)
            bbox = convert((img_w, img_h), bb)
            txt_file.write( '0' + " " + " ".join([str(a) for a in bbox]) + '\n')
 
        if (i['shape_type'] == 'polygon' and i['label'] == 'water horse bucket'): #分类的标签
            x1 = float((i['points'][0][0]))/img_w
            y1 = float((i['points'][0][1]))/img_h
            x2 = float((i['points'][1][0]))/img_w
            y2 = float((i['points'][1][1]))/img_h
 
            bb = (x1, y1, x2, y2)
            bbox = convert((img_w, img_h), bb)
            txt_file.write( '1' + " " + " ".join([str(a) for a in bbox]) + '\n')
 
 
if __name__ == "__main__":
 
    json_floder_path = "D:\\datasets\\sea_urchin_datasets\\sea_urchin\\original_labeled"  #json文件的路径
    json_names = os.listdir(json_floder_path)
    for json_name in json_names:
        decode_json(json_floder_path, json_name)
