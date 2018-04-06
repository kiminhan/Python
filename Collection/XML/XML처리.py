from xml.etree.ElementTree import Element, ElementTree, SubElement, parse, dump

blog = Element("blog")
blog.attrib["date"] = "20151231"
blog.attrib["editor"] = "pycharm"
subject = Element("subject")
subject.text = "Why python?"
author = Element("author")
author.text = "Eric\n  "
Agenda = Element("Agenda")
Agenda.text = ""

blog.append(subject)
blog.append(author)
blog.append(Agenda)


SubElement(author, "age").text = "58"
SubElement(author, "nation").text = "USA"
SubElement(Agenda, "a.").text = "Data Type"
SubElement(Agenda, "b.").text = "Controll Flow"
SubElement(Agenda, "c.").text = "Function"
SubElement(blog,"content").text = "Life is too short, You need Python!"

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

indent(blog)
dump(blog)
ElementTree(blog).write("blog.xml")
from_tag = blog.find("subject")
print(from_tag.text)
from_tags = blog.findall("author")
for i in from_tags:
    for from_tags_list in i:
        print(from_tags_list.text)

tree = parse("blog.xml")
Agenda = tree.getroot()

for j in Agenda:
    for child in j:
        print(child.text)

print(blog.keys())
print(blog.items())