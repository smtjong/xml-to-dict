import xml.dom.minidom as minidom

def parse_xml(root, xml_string):
    dom = minidom.parse(xml_string)
    dictionary = {}
    try:
        for node in dom.getElementsByTagName(root)[0].childNodes:
            name = node.nodeName
            data = node.firstChild.nodeValue
            dictionary[str(name)] = str(data)
    except AttributeError:
        name = dom.getElementsByTagName(root)[0].nodeName
        data = dom.getElementsByTagName(root)[0].firstChild.nodeValue
        dictionary[str(name)] = str(data)
    print # blank line
    return dictionary
        
def main():
    try:
        xml_file = raw_input("Enter the name of the XML file to parse: ")
        xml_root = raw_input("Enter the name of the root tag: ")
        print parse_xml(xml_root, xml_file)
    except IOError:
        print "Error: Please make sure you have input the correct file and try again."
        print 
        main()
    except IndexError:
        print "Error: Please make sure you have input the correct root and try again."
        print 
        main()

main()
    

