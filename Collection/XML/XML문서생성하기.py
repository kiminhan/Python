from xml.etree.ElementTree import Element, ElementTree, SubElement, parse, dump

note = Element("note")
note.attrib["date"] = "20120104"
note.attrib["editor"] = "pycharm"
to = Element("to")
to.text = "Tove"
note.append(to)

SubElement(note, "to").text = "김인한"
SubElement(note, "to").text = "김기정"
SubElement(note,"from").text = "jani"
SubElement(note, "heading").text = "Reminder"
SubElement(note, "body").text = "Don't forget me this weekend!"

def indent(elem, level = 0):
    i = "\n" + level*" "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + " "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

indent(note)
dump(note)
ElementTree(note).write("note.xml")

# from_tag = note.find("from")
# print(from_tag)
# from_tags = note.findall("from")
# print(from_tags)
# from_text = note.findtext("from")
# print(from_text)

tree = parse("note.xml")
note = tree.getroot()

# print(note.get("date"))
# print(note.get("foo","default"))
# print(note.keys())
# print(note.items())
# to_tag = note.find("to")
# # print(to_tag.text)
# to_tags = note.findall("to")
#
# for to_element in to_tags:
#     print(to_element.text)

# print(from_tag)
# print(from_tags)
# print(from_text)

# childs = note.getiterator()
# childs = note.getchildren()
#
# note.getiterator("from")

# print("Search from Root")
# for parent in note.getiterator():
#     for child in parent:
#         print(child.text)
#
# print(" \nSearch from from")
# for child in note.getiterator("from"):
#     print(child.text)