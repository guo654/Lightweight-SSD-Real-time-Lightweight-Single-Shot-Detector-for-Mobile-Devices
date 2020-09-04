#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import sys
import tensorflow as tf
 
# 用法：python trackTFRecord.py True file1 file2 
# trackTFRecord.py 就是当前这个py文件
# True 表示是否输出具体的数据
# file1 file2 表示的是需要查看的TFRecord文件的绝对路径
# 输出说明：tf.float32对应TFRecord的FloatList，tf.int64对应Int64List，tf.string对应BytesList
def main():
    print('TFRecord文件个数为{0}个'.format(len(sys.argv)-2))
    for i in range(2, len(sys.argv)):
        filepath = sys.argv[i]
        with tf.Session() as sess:
            filenames = [filepath]
            # 加载TFRecord数据
            ds = tf.data.TFRecordDataset(filenames)
            ds = ds.batch(10)
            ds = ds.prefetch(buffer_size=tf.contrib.data.AUTOTUNE)
            iterator = ds.make_one_shot_iterator()
            # 为了加快速度，仅仅简单拿一组数据看下结构
            batch_data = iterator.get_next()
            res = sess.run(batch_data)
            serialized_example = res[0]
            example_proto = tf.train.Example.FromString(serialized_example)
            features = example_proto.features
            print('{0} 信息如下：'.format(filepath))
            for key in features.feature:
                feature = features.feature[key]
                ftype = None
                fvalue = None
                if len(feature.bytes_list.value) > 0:
                    ftype = 'bytes_list'
                    fvalue = feature.bytes_list.value
                    
                if len(feature.float_list.value) > 0:
                    ftype = 'float_list'
                    fvalue = feature.float_list.value
                    
                if len(feature.int64_list.value) > 0:
                    ftype = 'int64_list'
                    fvalue = feature.int64_list.value
                
                result = '{0} : {1}'.format(key, ftype)
                if 'True' == sys.argv[1]:
                    result = '{0} : {1}'.format(result, fvalue)
                print(result) 
 
if __name__ == "__main__":
    main()
