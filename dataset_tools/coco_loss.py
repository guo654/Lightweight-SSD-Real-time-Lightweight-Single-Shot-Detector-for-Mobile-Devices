import os
import tensorflow as tf

file_list = tf.gfile.Glob(os.path.join('/home/jari/guoshi/workspace/mobilenetssd/models-master/research/object_detection/ssd_mixmodel_fpn_coco/data', 'coco_train.record-?????-of-?????'))
i = 0
count = 0
for file in file_list:
    for string_record in tf.python_io.tf_record_iterator(file):
        example = tf.train.Example()
        example.ParseFromString(string_record)

        i += 1
        image_id = example.features.feature['image/source_id'].bytes_list.value
        xmax = example.features.feature['image/object/bbox/xmax'].float_list.value
        # xmin = example.features.feature['image/object/bbox/xmin'].float_list.value
        # ymax = example.features.feature['image/object/bbox/ymax'].float_list.value
        # ymin = example.features.feature['image/object/bbox/ymin'].float_list.value

        if xmax == []:
            print(image_id)
            count += 1
    #print(file, 'has been checked.')

print(i, 'images have been checked.')
print(count, 'annotations without bbox.')

