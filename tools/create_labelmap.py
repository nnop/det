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
item.name = 'listen'
item.display_name = 'listen'

item = labmap.item.add()
item.label = 2
item.name = 'read'
item.display_name = 'read'

item = labmap.item.add()
item.label = 3
item.name = 'write'
item.display_name = 'write'

item = labmap.item.add()
item.label = 4
item.name = 'handup'
item.display_name = 'handup'

item = labmap.item.add()
item.label = 5
item.name = 'twist'
item.display_name = 'twist'

item = labmap.item.add()
item.label = 6
item.name = 'play'
item.display_name = 'play'

make_if_not_exist('helper')

with open('helper/labelmap.prototxt', 'w') as f:
    f.write(str(labmap))

print 'labelmap save to "helper/labelmap.prototxt".'
