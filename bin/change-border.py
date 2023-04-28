#!/usr/bin/env python3

import sys
import xml.etree.ElementTree as ET

def main():
    if len(sys.argv) != 3:
        raise Error('usage: {} INPUT_SVG_FILE OUTPUT_FILE'.format(sys.argv[0]))
    tree = ET.parse(sys.argv[1])
    ET.register_namespace('', 'http://www.w3.org/2000/svg')
    root = tree.getroot()
    bg = root.find('{http://www.w3.org/2000/svg}rect')

    bg.attrib["stroke"] = "white"
    bg.attrib["stroke-width"] = "2"
    bg.attrib["rx"] = "5"
    bg.attrib["ry"] = "5"

    tree.write(sys.argv[2], encoding='UTF-8')

if __name__ == '__main__':
    main()
