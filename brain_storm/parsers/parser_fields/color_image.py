import json
import PIL
import numpy as np
import logging



def color_image(data):
    path_to_img = data['snap']['colorImage']['path']
    with open(path_to_img, 'rb') as raw:
        img_bytes = raw.read()

    h, w = data['snap']['colorImage']['height'], data['snap']['colorImage']['width']
    img_from_bytes = PIL.Image.frombytes('RGB', (w, h), img_bytes)
    img_from_bytes.save(path_to_img)
    #logging.warning(data)
    #return json.dumps({'userId': data['user']['userId'],  'datetime': data['snap']['datetime'], 'colorPath': path_to_img})
    return json.dumps({'userId': data['user']['userId'],  'datetime': data['snap']['datetime'], 'colorPath': path_to_img, 'height': h, 'width': w})

