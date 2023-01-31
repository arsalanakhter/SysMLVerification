import xml.etree.ElementTree as ET


def modify_attribute(tag, attrib, val):
    file_name = 'kheperaiv_5_tiled.argos'
    tree = ET.parse(file_name)
    root = tree.getroot()
    for element in root.iter(tag=tag):
        print(element.attrib)
        element.set(attrib, val)
        print(element.attrib)
        with open('modified_'+file_name, 'wb') as f:
            tree.write(f)
        break


tag = 'entity'
attrib = 'quantity'
val = '3'

modify_attribute(tag, attrib, val)