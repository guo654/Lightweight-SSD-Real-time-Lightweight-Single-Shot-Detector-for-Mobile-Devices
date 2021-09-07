# Lightweight SSD: Real-time Lightweight Single Shot Detector for Mobile Devices
The paper link is 
scitepress.org/Papers/2021/101880/pdf/index.html

This paper proposes a Lightweight SSD for object detection. The code is based on the tensorflow official github https://github.com/tensorflow/models/tree/master/research/object_detection.

#### We have changed or added the following files：
###### 1.MBlitenet: samixconv_blocks.py , samixmobilenet_v2.py
###### 2.CFPN: feature_map_generators.py
###### 3.Biou：box_list, box_list_ops, losses
###### 4.Mosaic
###### 5.RGBMixGray: dataset_tools
#### NOTE: You can directly copy the these files, replace the original files in tensorflow official github.
