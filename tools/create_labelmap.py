#!/usr/bin/env python
# -*- coding: utf-8 -*-
from caffe.proto import caffe_pb2
from lib.utils import make_if_not_exist

labmap = caffe_pb2.LabelMap()
# bg
item = labmap.item.add()
item.name = 'null'
item.label = 0
item.display_name = 'null'

item = labmap.item.add()
item.label = 1
item.name = 'head'
item.display_name = 'head'

make_if_not_exist('helper')

with open('helper/labelmap.prototxt', 'w') as f:
    f.write(str(labmap))

print 'labelmap save to helper/labelmap.prototxt.'
