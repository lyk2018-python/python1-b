from bs4 import BeautifulSoup
from pprint import pprint

with open("index.html", "r") as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

######### OBJECTS #########

# ATTRIBUTES
# pprint(soup.ul.li.div.attrs)
# pprint(soup.ul.li.div["class"])

# ELEMENT İÇERİĞİ
# pprint(soup.ul.li.div.string)

# ELEMENT ADI
# pprint(soup.ul.li.div.name)

######### GOING DOWN #########

# USE TAG NAME
# print(soup.head.style.string)
# print(soup.div.ul.li.div.string)

# CONTENTS
# print(soup.div.ul.children)
# for child in soup.div.ul.children:
#     print(child)

# for child in soup.div.ul.contents:
#     print(child)

# pprint(soup.div.ul.contents[1])

######### SIBLINGS #########
# print(soup.li.next_sibling.next_sibling.contents[1].attrs)
# print(soup.li.next_sibling.next_element.contents[1].string)

######### SEARCH #########

# FIND SINGLE ELEMENT
# pprint(soup.find("div", {"id" : "ikinci_satir"}))
# pprint(soup.find("div", {"sezer" : "serhat"}))
# pprint(soup.find(id = "ikinci_satir"))
# pprint(soup.find("div", class_="deneme"))

# FIND MULTIPLE ELEMENT
# pprint(soup.find_all("li")[1])
# pprint(soup.find_all("div", {"class" : "deneme"}))
# pprint(soup.find_all("div", { "style" : "color:red"}))
# pprint(soup.find_all("td")[3])