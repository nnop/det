from os import path
from easydict import EasyDict as edict

cfg = edict()
cfg.data_root = 'data/'
cfg.xml_dir = path.join(cfg.data_root, 'xml')
cfg.img_dir = path.join(cfg.data_root, 'image')
