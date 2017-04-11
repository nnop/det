#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from glob import glob
from os import path

from lib.config import cfg
from lib.utils import make_if_not_exist

def dump_list(anno_list, out_fn):
    all_list = []
    for anno in anno_list:
        anno_fn = path.split(anno)[1]
        anno_path = path.join('Annotations', anno_fn)
        name, _  = path.splitext(anno_fn)
        image_path = path.join('JPEGImages', name+'.jpeg')
        assert path.exists(path.join(cfg.data_root, image_path)), \
                '{} not exists.'.format(image_path)
        all_list.append('{} {}\n'.format(image_path, anno_path))
    with open(out_fn, 'w') as f:
        f.writelines(all_list)
    print 'dump {} to {}.'.format(len(anno_list), out_fn)

anno_list = glob(path.join(cfg.xml_dir, '*.xml'))
random.shuffle(anno_list)
n = len(anno_list)
make_if_not_exist('splits')
dump_list(anno_list[:int(n*0.9)], 'splits/train.txt')
dump_list(anno_list[int(n*0.9):], 'splits/test.txt')

