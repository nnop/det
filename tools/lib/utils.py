import os
from os import path
from config import cfg

def check_data(name):
    """
    check both image and annotation exists for name.
    """
    img_path = path.join(cfg.img_dir, name+'.jpg')
    assert path.isfile(img_path), '{} not exists.'.format(img_path)
    xml_path = path.join(cfg.xml_dir, name+'.xml')
    assert path.isfile(xml_path), '{} not exists.'.format(xml_path)

def main_name(p):
    return path.splitext(path.split(p)[1])[0]

def make_if_not_exist(path):
    if not os.path.exists(path):
        os.makedirs(path)
