import xml.etree.ElementTree as ET
# read xml file
# parsed XML file into a variable tree
tree=ET.parse("/DataFormats/employee.xml")
root = tree.getroot() # get the root element
print(root.tag)

# get the first child node / tag
print(root[0].tag)

# get the attributes of the child node
print(root[0].attrib)

# fetch all the attribute in the child node
for employee in root.findall("employee"):
    emp_id = employee.get("id")
    print(emp_id)


for emp in root.findall("employee"):
    name = emp.find("name").text
    role = emp.find("role").text
    exp = emp.find("experience").text
    print(name, role, exp)

# root ---> child nodes ---> attributes of the child nodes ----> text of the attributes
# write the date to xml file

# create the root element
 root = ET.Element("employees")

 # create the child elements

emp1 = ET.SubElement(root , "employee" , id = "101")
ET.SubElement(emp1 , "name").text="harsha"
ET.SubElement(emp1, "role").text="tester"
ET.SubElement(emp1, "experience").text="5"

# create the child node 2

emp2 = ET.SubElement(root,"employee", id = "102")
ET.SubElement(emp2,"name").text="amit"
ET.SubElement(emp2,"role").text= "developer"
ET.SubElement(emp2,"experience").text="3"

# write to the file
tree = ET.ElementTree(root)
tree.writer


# updating the xml

tree = ET.parse()
root = tree.getroot()

for emp in root.findall("employee"):
    if emp.get("id") =="101"
        emp.find("experience").text = "16"


tree.write()

