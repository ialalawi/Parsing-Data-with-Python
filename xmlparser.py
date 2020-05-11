# XMLParser - A program that can parse XML files retrieved from the Web and sum up certain element values
# Developer: Ismaeel Alalawi, All Rights Reserved 2020
# May, 2020

from urllib.request import urlopen
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Retrieve XML URL and create tree from decoded string
url = input('Enter - ')
xmltext = urlopen(url, context=ctx).read().decode()
tree = ET.fromstring(xmltext)

# Initialize the Count
total = 0

# Create list of XML simple elements contained in the comment node
counts = tree.findall('./comments/comment')

# Lopp through each count element and extract text information
for item in counts:
	txt = item.find('count').text
	total += int(txt)

# Print the sum of the counts in the XML file
print(total)

