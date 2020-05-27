import numpy as np
import matplotlib.pyplot as plt
import json


def depth_image(data):
    path_to_img = data['snap']['depthImage']['path']
    h, w = data['snap']['depthImage']['height'], data['snap']['depthImage']['width']
    with open(path_to_img, 'r') as raw:
        arr_as_string = raw.read()

    heat_array = arr_as_string.split(',')
    heat_array = np.array(heat_array[0:len(heat_array)-1], dtype=float).reshape(h, w)
    plt.imshow(heat_array, cmap='hot', interpolation='nearest')
    plt.savefig(path_to_img)

    return json.dumps({'userId': data['user']['userId'], 'datetime': data['snap']['datetime'], 'depthPath': path_to_img, 'height': h, 'weight': w})
