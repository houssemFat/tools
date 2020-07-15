import requests
import re

html = requests.get("http://jbauman.com/UWL.html")
# print(html.text)
these_regex = "<p.*?>(.+?)<P>"
pattern = re.compile(these_regex)
text = html.text.replace('\n', ' ')
text = text.replace('\r', ' ')
text = text.replace(' </BODY>', '<P>')

elements = re.findall(pattern, text)
words = []
for e in elements:
    words = words + e.split(' ')
words = list(filter(lambda x: x != '', words))
print ('\n'.join(words))
"""
data = {
    "q": ' '.join(words),
    "source": "en",
    "target": "ar",
    "format": "text"
}
res = requests.post("https://translation.googleapis.com/language/translate/v2", data, json=True)
print (res.text)
"""
