from lxml import etree


def extract_hazards_from_sysml():
    file_name = '../project.xml'
    parser = etree.XMLParser(remove_blank_text=True)
    tree = etree.parse(file_name, parser)
    root = tree.getroot()
    for element in root.iter(tag='Stereotype'):
        if element.attrib['Name'] == 'Hazards':
            # print(element.attrib)
            desired_parent = element.xpath('../..')
            print(desired_parent[0].attrib['Name'])


if __name__ == '__main__':
    extract_hazards_from_sysml()