from lxml import etree



def xmlParser(xml):
    with open(xml) as parsedXml:
        xml = parsedXml.read()
        root = etree.fromstring(xml)
        print(root.getchildren())


if __name__ == "__main__":
    xmlParser('test.xml')
        

