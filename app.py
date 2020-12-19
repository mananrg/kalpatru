#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import readability_stats_ptm
import os
import zipfile
from flask import Flask, request, redirect, url_for, flash, render_template, send_file, session
from werkzeug.utils import secure_filename
import return_tokenized_results
import return_scores_from_text_only
import return_scores_from_text_only_with_novelty_comparision
import return_scores_from_text_only_for_script_writing
import urllib
from flask import jsonify
import random
#import urllib2
#import html2text
from bs4 import BeautifulSoup
from datetime import datetime
import nltk
import pdfkit
import time
UPLOAD_FOLDER = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER2 = '/var/www/html/'
ALLOWED_EXTENSIONS = set(['zip'])
dcounter=0
app = Flask(__name__)
app.config['UPLOAD_FOLDER2'] = UPLOAD_FOLDER2
from flask_mysqldb import MySQL
import MySQLdb

app = Flask(__name__)
app.secret_key = "12345678"

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'doc_matrix'

db = MySQL(app)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_text_from_url(url):
    html=urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html,'html.parser')
    # kill all script and style elements
    for script in soup(["script", "style"]):
       script.extract()    # rip it out
    # get text
    text2 = soup.get_text()
    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text2.splitlines())
                                                                                    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  ")) 
    text2 = '\n'.join(chunk for chunk in chunks if chunk)
    return(text2)


@app.route('/predict',methods=['GET'])
def handlemsg():
    msg=request.args.get('msg')
    return("""you typed msg"""+msg)


@app.route('/', methods=['POST', 'GET'])
def login():
	if request.method == 'POST':
		if 'username' in request.form and 'password' in request.form:
			username = request.form['username']
			password = request.form['password']
			cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
			cursor.execute("SELECT * from users where username=%s and password=%s", (username, password))
			loginResult  = cursor.fetchone()
			session['id'] = loginResult['id']
			if loginResult is not None:
				if loginResult['username'] == username and loginResult['password'] == password:
					session['is_login'] = True
					return redirect('text_editor_new/#-'+str(loginResult['app_key']))
				else:
					return "Unable to login"
			else:
				return "Unable to login"

	return render_template('login.html');

@app.route('/psychologist-input/',methods=['GET','POST'])
def psychologistOption():     
    if request.method=='POST':

        munchausenwordlist=str(request.form.get('munchausenwords'))
        print("munchausen words list received is")
        print(munchausenwordlist)
    return render_template('hello.html')
    #return render_template('css/styles.css')
    #return render_templates('images/')
#def process_dashboard() :
# return """<html> hye</html>"""


@app.route('/uploadajax', methods=['POST', 'GET'])
def uploadFileAjax():
	if request.method == 'POST':
		file = request.files['compare_file']
		name = "Compare_file_"
		filename = name+str(datetime.now())+secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER2'], filename))
		return jsonify({'file_path': os.path.join(app.config['UPLOAD_FOLDER2'], filename),'file_name': request.url_root+'download?file_name='+filename})
	return("Hello")

	
@app.route('/download', methods=['POST', 'GET'])
def download_file():
  file_name = request.args.get('file_name')
  #path = "html2pdf.pdf"
  #path = "info.xlsx"
  path = file_name
  #path = "sample.txt"
  return send_file(path, as_attachment=True)	

@app.route('/generatePdf', methods=['POST', 'GET'])
def generatePdf():
  file_name = request.args.get('result_url')
  filename = str(time.time())+str(random.randrange(1, 1000))+'.pdf'
  pdfkit.from_string(file_name,filename)
  return jsonify({'file_name': request.url_root+'download?file_name='+filename})
       
	


@app.route('/text-editor/',methods=['GET','POST'])

# def text_editor():
# 	if session['is_login']==True:
#     	return render_template('text_editor_comparison.html')
#     else:
#     	return redirect('/')

@app.route('/text_editor_new/', methods=['GET', 'POST'])
def text_editor_new():
	if session['is_login'] == True:
		return render_template('text_editor_comparison_new.html')
	else:
		return redirect('/')

@app.route('/update_counter', methods=['GET'])
def update_counter():
  cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
  cursor.execute("SELECT hit_count from users where id=%s", (session['id'],))
  mysqlResult  = cursor.fetchone()
  hit_count= mysqlResult['hit_count']+1;
  
  cursor.execute("UPDATE users SET hit_count=%s where id=%s", (hit_count,session['id']))
  db.connection.commit()

  data = [{'count': hit_count}]
  return jsonify(data)


import concurrent.futures

MAX_THREADS = 30

def download_url(url):
    print("the url to be fetched is")
    print(url)
    #resp = requests.get(url)
    #title = ''.join(x for x in url if x.isalpha()) + "html"
    html=urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html,'html.parser')

        # kill all script and style elements
    for script in soup(["script", "style"]):
                script.extract()    # rip it out

                # get text
    text2 = soup.get_text()

                # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text2.splitlines())
                # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
                # drop blank lines
    text2 = '\n'.join(chunk for chunk in chunks if chunk)


    print(text2)
    
    print("The response text IS")
    print(text2)
    with open("title.txt", "a") as fh:
        
        fh.write(text2)
        
    time.sleep(0.25)
        
def download_stories(story_urls):
    threads = min(MAX_THREADS, len(story_urls))
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        executor.map(download_url, story_urls)

#from google import google
import time
@app.route('/scores-for-firepad',methods=['GET'])
def handletext():
        text=request.args.get('text')
        print(text)
        compare_url=request.args.get('compare_url')
        print("compare_url url is")
        print(compare_url)
        compare_file=request.args.get('compare_file')
        google_n_count=request.args.get('google_n_count')
        try: 
          from googlesearch import search 
        except ImportError:  
          print("No module named 'google' found") 
  






        t0=time.time()
        if google_n_count:
           
                  
                  google_n_count=int(google_n_count)
                  print(type(google_n_count))
                  print(google_n_count)
                  if text :
                     t1=time.time()
                     search_results = search(text, num=google_n_count,stop=10,pause=2)
                     t2=time.time()
                     print("search Request took")
                     print({round(t2-t1, 2)})
                     print("seconds.")
                     text_cat=""
                     print(search_results)
                     t3 = time.time()
                     search_results2= list(search_results)
                     download_stories(search_results2[0:google_n_count])
                     t4 = time.time()
                    # print(f"{t1-t0} seconds to download {len(story_urls)} stories.")
                     #for eachelem in search_results :
                         #try :
                     #        print(eachelem)
                     #        print("----------------")
                             #print(eachelem.link)
                     #        print("----Description--")
                             #print(eachelem.description)
                     #        print("----Cached---")
                             #print(eachelem.cached)
                     #        print("----------------")
                             #if (eachelem.description) :

                     #        text_cat=text_cat+str(eachelem)
                         #except :
                         #    print("some error in fetching text and concatenating it:")
                     #print("text concatenated of descriptions is")
                     #print(text_cat)
                     print("WE ARE NOW GOING TO OPEN THE FILE TITLE.TXT")
                     file_title=open("title.txt","r")
                     print("file for this user opened")
                     
                     
                     text_cat=str(file_title.read())
                     if text_cat!="" :
                         print("we are just about to return scores fromfunction")
                         print("type of text is")
                         print(type(text))
                         print("type of text_cat is")
                         print(type(text_cat))
                         print("The text concatenated and to be evaluated is")
                         print(text_cat)
                         import re
                         text_cat2 = re.sub("[!@#$%^&*()[]{};:,./<>?\|`~-=_+]", " ", text_cat)
                         print("text_cat is now text_cat2 after re.sub on special charaters")
                         #text_cat= text_cat.translate ({ord(c): " " for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+"})
                         x_json=return_scores_from_text_only_with_novelty_comparision.ret_scores_res(text,str(text_cat2))
                         os.remove("title.txt")
                         return(x_json)


          #except :  
          #        print("No module named 'google' found")
        elif compare_url : 
          html=urllib.request.urlopen(compare_url).read()
          soup = BeautifulSoup(html,'html.parser')

        # kill all script and style elements
          for script in soup(["script", "style"]):
                script.extract()    # rip it out

                # get text
          text2 = soup.get_text()

                # break into lines and remove leading and trailing space on each
          lines = (line.strip() for line in text2.splitlines())
                # break multi-headlines into a line each
          chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
                # drop blank lines
          text2 = '\n'.join(chunk for chunk in chunks if chunk)

        
          print(text2)
          #raw=nltk.clean_html(html)
          #print(raw)
          n=return_tokenized_results.ret_len_res(text)
          x_json=return_scores_from_text_only_with_novelty_comparision.ret_scores_res(text,text2)
          return(x_json)
        elif 'no file' not in compare_file :
          import textract
          textam = textract.process(compare_file)
          textams=str(textam)
          textams=textams.encode('utf-8', errors='ignore')
          print("the text of attachment is")
          textamsd=textams.decode('UTF-8')
          print(textamsd)

          x_json=return_scores_from_text_only_with_novelty_comparision.ret_scores_res(text,textamsd)
          return(x_json)
        elif compare_file and compare_url :
          import textract
          textam = textract.process(compare_file)
          textams=str(textam)
          textams=textams.encode('utf-8', errors='ignore')
          print("the text of attachment is")
          textamsd=textams.decode('UTF-8')
          print(textamsd)
          html=urllib.request.urlopen(compare_url).read()
          soup = BeautifulSoup(html,'html.parser')

                             # kill all script and style elements
          for script in soup(["script", "style"]):
              script.extract()    # rip it out

          # get text
          text2 = soup.get_text()

                                                                                                     # break into lines and remove leading and trailing space on each
          lines = (line.strip() for line in text2.splitlines())
                                                                                          # break multi-headlines into a line each
          chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
          # drop blank lines
          text2 = '\n'.join(chunk for chunk in chunks if chunk)


          print(text2)
          x_json=return_scores_from_text_only_with_novelty_comparision.ret_scores_res(text,textamsd+text2)
          return(x_json)

        else: 
          x_json=return_scores_from_text_only_for_script_writing.ret_scores_res(text)
          return(x_json)

#@app.route('/scores-for-firepad-with-nr-comparision',methods=['GET'])
#def handletext2():
        #text=request.args.get('text')
        #text_to_compare=request.args.get('text_to_compare')
        #n=return_tokenized_results.ret_len_res(text)
        
        #x_json=return_scores_from_text_only_with_comparision(text,text_to_compare)
        #return(x_json)
@app.route('/get-edit-url-flag-and-textlist',methods=['GET'])
def handletext2():
        edit_url_flag=0
        textlist=[]
        text=request.args.get('text')
        textlist=text.split("|")
        if len(textlist)==1:
          print("no delimeter found")
          edit_url_flag=0
        elif len(textlist)>=2:
          edit_url_flag=1
        return(edit_url_flag,textlist)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
	session['is_login'] = False;
	return redirect('/')

          
        
        



if __name__ == "__main__":
    app.run(host='0.0.0.0', port='6011', debug='true')
