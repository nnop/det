#!/usr/bin/env python
# -*- coding: utf-8 -*-
from glob import glob
from os import path
import sys

from lib.voc_parser import VOCParser
from lib.config import cfg

# get all xml files
xml_files = glob(path.join(cfg.xml_dir, '*.xml'))

# find all names
names = set()
for fn in xml_files:
    voc = VOCParser(fn)
    names |= set([o['name'] for o in voc.objects])
    sys.stdout.write('.')
    sys.stdout.flush()
sys.stdout.write('\n')
print 'all names:', names
