#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
create splits (train, test)
format:
    image_path xml_path
"""
from glob import glob
from os import path
from lib import cfg
from lib.utils import *

tr_lines = []
te_lines = []
te1_lines = []
te2_lines = []

all_xml = glob(path.join(cfg.xml_dir, '*.xml'))
for p in all_xml:
    name = main_name(p)
    check_data(name)
    img_p = path.join('image/'+name+'.jpg')
    xml_p = path.join('xml/'+name+'.xml')
    if name.startswith('tr'):
        tr_lines.append('{} {}\n'.format(img_p, xml_p))
    elif name.startswith('te1'):
        te1_lines.append('{} {}\n'.format(img_p, xml_p))
    elif name.startswith('te2'):
        te2_lines.append('{} {}\n'.format(img_p, xml_p))
    else:
        raise ValueError('wrong name: {}'.format(name))
te_lines = te1_lines + te2_lines

make_if_not_exist('splits')

with open('splits/train.txt', 'w') as f:
    f.writelines(tr_lines)
print '{} save to "splits/train.txt".'.format(len(tr_lines))

with open('splits/test.txt', 'w') as f:
    f.writelines(te_lines)
print '{} save to "splits/test.txt".'.format(len(te_lines))

with open('splits/test1.txt', 'w') as f:
    f.writelines(te1_lines)
print '{} save to "splits/test1.txt".'.format(len(te1_lines))

with open('splits/test2.txt', 'w') as f:
    f.writelines(te2_lines)
print '{} save to "splits/test2.txt".'.format(len(te2_lines))
