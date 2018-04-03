
# ########### Created by Rohan Arora #############
# Meta Keyword

from flask import Flask
from flask import request
from flask import render_template
from NLP import nlp
from pymongo import MongoClient
import webbrowser

count = count1 = 0
query = ["Web"]
#queryString = query[0]
stringCount = []
stringCount1 = []

Client = MongoClient()
db = Client["W33"]
linkData = db["linkData"]

i = 0
for res in linkData.find():
    # texts = res["Contents"]
    text1 = res["MetaKeywords"]
    text = res["MetaDesc"].split(" ")
    # print (texts)

    #print len(filter(lambda x: queryString in x, texts))

    match = [s for s in text if any(xs in s for xs in query)]
    match1 = [s for s in text1 if any(xs in s for xs in query)]

    # print(match)
    # print(match1)

    i += 1
    stringCount.append({
        'URL': res["URL"],
        'Count': len(match)
        })

    stringCount1.append({
        'URL': res["URL"],
        'Count': len(match1)
    })

# print(stringCount)
# print(stringCount1)

maxx = max([i['Count'] for i in stringCount])
maxx1 = max([i['Count'] for i in stringCount1])

for link in stringCount:
    if link['Count']==maxx and maxx != 0:
        print link['URL']
        print link['Count']
        count += 1

print("--------------------------------------------------")
print("--------------------------------------------------")
print("--------------------------------------------------")
print("--------------------------------------------------")

for link1 in stringCount1:
    if link1['Count']==maxx1 and maxx1 != 0:
        print link1['URL']
        print link1['Count']
        count1 += 1

x = "number of metaDescriptions found in links = %d" % count
y = "number of metaKeywords found in links = %d" % count1
print (x)
print (y)
    #webbrowser.open_new_tab(link['URL'])


