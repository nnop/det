from xml.etree import ElementTree
from os import path

class VOCParser(object):
    def __init__(self, arg):
        if isinstance(arg, str):
            assert path.isfile(arg), '{} not exists.'.format(arg)
            self.tree = ElementTree.parse(arg)
        elif isinstance(arg, ElementTree.ElementTree):
            self.tree = arg
        else:
            raise ValueError('Wrong argument for VOCParser.')

    @property
    def objects(self):
        objs = []
        obj_nodes = self.tree.findall('object')
        for node in obj_nodes:
            o = {}
            o['name'] = node.find('name').text
            bndbox_node = node.find('bndbox')
            xmin = int(bndbox_node.find('xmin').text)
            xmax = int(bndbox_node.find('xmax').text)
            ymin = int(bndbox_node.find('ymin').text)
            ymax = int(bndbox_node.find('ymax').text)
            o['bbox'] = [xmin, ymin, xmax, ymax]
            objs.append(o)
        return objs
        
    @property
    def size(self):
        size_node = self.tree.find('size')
        wid = int(size_node.find('width').text)
        hei = int(size_node.find('height').text)
        depth = int(size_node.find('depth').text)
        return (hei, wid, depth)
