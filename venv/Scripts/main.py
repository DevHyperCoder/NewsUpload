from __future__ import print_function
import webbrowser
from functools import partial
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import google_docs_client
import dropbox_client
import tkinter
import tkhyperlinkManager
from os.path import join as pjoin
from bs4 import BeautifulSoup
import html5lib
import requests
import urllib3
import re
import lxml
from flask import Flask , render_template , request
import parse
from pprint import pprint
import datetime

# If you are modifying these scopes, delete the file token.pickle.
app = Flask(__name__)


#Read the contents of the files
# C:\Users\user\Documents\News Aggregator
path_to_file = pjoin("C:\\", "Users", "user", "Documents", "News Aggregator", "document.txt")
f = open(path_to_file, "r")
texts_in_file = f.readlines()
f.close()

text_in_file = [""]
text_in_file_revised = [""]
DEBUG = False
GUI = False
array_of_doc_id = [""]
#Try to remover in the next build
array_of_doc_title = [""]
array_of_https_doc= [""]

for line in texts_in_file:
    text_in_file.append(line)


if DEBUG:
    for text in text_in_file:
        print(text)



def upload_to_google_docs(contents,title):

    if not contents:
        contents = " "
    if not title:
        title = " "

    if DEBUG:
        print(text)
        print(contents)
        print("////////////////////////////////////")

    # upload to google docs for editing
    doc_id = google_docs_client.upload_to_google_docs(title, contents)
    array_of_doc_title.append(title)
    array_of_doc_id.append(doc_id)
    array_of_https_doc.append('https://docs.google.com/document/d/' + doc_id)
    # # asdfasdf
    # google_docs_client.retrieve(doc_id)



array_of_url=[""]
array_of_title=[""]
for text in text_in_file:
    if not text == "":
       array_of_url.append(text)

       array_of_title.append(parse.parse_title(text))




def on_click_doc_id(docId):
    link = 'https://docs.google.com/document/d/'+docId
    if DEBUG:
        print(link)
    webbrowser.open(link)

def on_click_save_to_dropbox(docId):
    text = google_docs_client.retrieve_contents(docId)
    title = google_docs_client.retrieve_title(docId)

    print(text)
    print(title)
    dropbox_client.upload_to_dropbox(title,text)


if GUI:
    m = tkinter.Tk()

    m.attributes("-fullscreen", True)

    m.bind("<Escape>", lambda e: m.quit())
    t = tkinter.Text(m)
    t.insert(tkinter.END, "Please wait: \n")

    m.mainloop()
    t.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=tkinter.YES)
    text_for_tkinter = [""]
    hyperlink = tkhyperlinkManager.HyperlinkManager(t)

    for (docId,title) in zip(array_of_doc_id,array_of_doc_title):
      # Add the hyper link
      t.insert(tkinter.INSERT, title,
               hyperlink.add(partial(on_click_doc_id, docId)))
      t.insert(tkinter.END, "\n")
      t.insert(tkinter.INSERT, docId,
               hyperlink.add(partial(on_click_save_to_dropbox, docId)))
      t.insert(tkinter.END, "\n")

    t.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=tkinter.YES)
    m.mainloop()


i=0
for doc_title in array_of_doc_title:
  array_of_doc_title[i]='Go to Google Docs --'+doc_title
  i+=1


print("array_of_doc_id")
pprint(array_of_doc_id)
print("array_of_https_doc")
pprint(array_of_https_doc)



@app.route("/")
def returner():
    return render_template("mainhtml.html",ar_title = array_of_title)
@app.route("/uploadgd/<doc_title>/", methods=['GET', 'POST'])
def index(doc_title):
    i = array_of_title.index(doc_title)
    url = array_of_url [i]
    content = parse.parse(url)
    upload_to_google_docs(content,doc_title)


    return render_template("mainhtml.html",ar_title = array_of_title)

@app.route("/index/")
def indexer():
    return render_template("index.html",my_list=zip(array_of_https_doc,array_of_doc_id,array_of_doc_title))
@app.route('/updropbox/' , methods = ["POST","GET"])
def upload_dropbox():
    return render_template("form.html")

@app.route('/dropbox/' , methods = ["POST","GET"])
def handle():
    doc_id = request.form['text']

    print(doc_id)
    text = google_docs_client.retrieve_contents(doc_id)
    title = google_docs_client.retrieve_title(doc_id)

    print(text)
    print(title)
    dropbox_client.upload_to_dropbox(title, text)
    return render_template("index.html", my_list=zip(array_of_https_doc, array_of_doc_id, array_of_doc_title))

@app.route('/upload/<doc_link>/' , methods = ["POST","GET"])
def a(doc_link):
    print("hai")
    print (doc_link)
    text = google_docs_client.retrieve_contents(doc_link)
    title = google_docs_client.retrieve_title(doc_link)

    print(text)
    print(title)

    dropbox_client.upload_to_dropbox(title, text)
    return render_template("index.html", my_list=zip(array_of_https_doc,array_of_doc_id, array_of_doc_title))

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0',port = '5001')
