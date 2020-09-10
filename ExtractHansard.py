import requests
import pandas as pd

year_2020 = requests.get('https://api.parliament.nsw.gov.au/api/hansard/search/year/2020')
#get pdf doc id
year_2020.json()[1]['Events'][0]['PdfDocId']
#get date
year_2020.json()[1]['date']

#extract all dates this year
date = []
doc_id = []
p = 0
while p < len(year_2020.json()):
    date.append(year_2020.json()[p]['date'])
    doc_id.append(year_2020.json()[p]['Events'][0]['PdfDocId'])
    p += 1
#find None responses in doc_id list, remove from both lists
l = [i for i, v in enumerate(doc_id) if v == None]
for x in l:
    del date[x]
    del doc_id[x]
#download hansards
x = 0
while x < len(doc_id):
    doc = requests.get(f"https://api.parliament.nsw.gov.au/api/hansard/search/daily/pdf/{doc_id[x]}")
    with open(fr"C:\Users\Jarrod\Downloads\Hansards\NSW_HANSARD_{date[x]}.pdf", 'wb') as f:
        f.write(doc.content)
    x += 1

