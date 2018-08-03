"""
Web Siteleri
------------
https://docs.python.org/3/howto/regex.html
https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285
https://github.com/serhattsnmz/dotnet-core-ile-web-programlama/blob/master/14%20-%20Routing.md
https://regex101.com/
"""

import re
import requests
from pprint import pprint

# Patern
image_pattern = "\w+\.[jpgpne]{3,4}"
mail_pattern  = "[a-zA-Z0-9_.-]+@[a-zA-Z0-9_.-]+\.[a-zA-Z0-9.]+"

# Patern nesnesi
image_reg = re.compile(image_pattern)
mail_reg  = re.compile(mail_pattern)

# Site request
req = requests.get("https://sezerbozkir.com")

# Gelen sitenin içinden mail adreslerini bulma
mail_listesi = mail_reg.findall(req.text)
if mail_listesi is not None:
    pprint(mail_listesi)

# Gelen sitenin içinden resimleri bulma
resim_listesi = image_reg.findall(req.text)
if resim_listesi is not None:
    pprint(resim_listesi)
