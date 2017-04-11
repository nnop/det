#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
create name size file for test split
"""
from os import path
from lib.config import cfg
from lib.voc_parser import VOCParser
from lib.utils import make_if_not_exist

def gen_name_size(split_path, out_path):
    # open test splits
    with open(split_path) as f:
        lines = f.readlines()
        lines = [l.strip() for l in lines]

    # get all sizes
    out_lines = []
    for l in lines:
        img_p, xml_p = l.split()
        xml_p = path.join(cfg.data_root, xml_p)
        voc_xml = VOCParser(xml_p)
        hei, wid, ch = voc_xml.size
        fn = path.split(xml_p)[1]
        name = path.splitext(fn)[0]
        out_lines.append('{} {} {}\n'.format(name, hei, wid))

    make_if_not_exist('helper')
    with open(out_path, 'w') as f:
        f.writelines(out_lines)

if __name__ == "__main__":
    gen_name_size('splits/train.txt', 'helper/train_name_size.txt')
    gen_name_size('splits/test.txt', 'helper/test_name_size.txt')
    gen_name_size('splits/test1.txt', 'helper/test1_name_size.txt')
    gen_name_size('splits/test2.txt', 'helper/test2_name_size.txt')
    print 'done.'

