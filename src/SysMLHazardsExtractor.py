from lxml import etree


def extract_hazards_from_sysml():
    file_name = '../project.xml'
    parser = etree.XMLParser(remove_blank_text=True)
    tree = etree.parse(file_name, parser)
    root = tree.getroot()
    for element in root.iter(tag='Stereotype'):
        if element.attrib['Name'] == 'Hazard':
            # print(element.attrib)
            desired_parent = element.xpath('../..')
            print(desired_parent[0].attrib['Name'])
            desired_parent = element.xpath('../../../..')
            print(desired_parent[0].attrib['Name'])


def extract_hazards_from_sysml_2():
    file_name = '../project (2).xml'
    parser = etree.XMLParser(remove_blank_text=True)
    tree = etree.parse(file_name, parser)
    root = tree.getroot()
    for element in root.iter(tag='Stereotype'):
        if element.attrib['Name'] == 'Hazard':
            # print(element.attrib)
            desired_parent = element.xpath('../..')
            print(desired_parent[0].attrib['Name'])
            desired_parent2 = element.xpath('../../../..')
            if desired_parent2:
                print(desired_parent2[0].attrib['Name'])
            desired_parent = element.xpath(
                '../../TaggedValues/TaggedValueContainer'+
                '/ModelChildren')
            for elem in desired_parent[0].iter():
                if elem.attrib:
                    print(elem.attrib['Name'])
                    if 'Value' in elem.attrib.values():
                        print(elem.attrib['Value'])
                    else:
                        print('No Attrib Value')



def extract_hazards_from_sysml_3():
    file_name = '../project (2).xml'
    parser = etree.XMLParser(remove_blank_text=True)
    tree = etree.parse(file_name, parser)
    root = tree.getroot()
    for element in root.iter(tag='Stereotype'):
        if element.attrib['Name'] == 'Hazard':
            print(element.attrib)


if __name__ == '__main__':
    extract_hazards_from_sysml_3()