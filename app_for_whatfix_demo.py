#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import readability_stats_ptm
import os
import zipfile
from flask import Flask, request, redirect, url_for, flash, render_template, send_file
from werkzeug.utils import secure_filename
import return_tokenized_results
import return_scores_from_text_only
import return_scores_from_text_only_with_novelty_comparision
import return_scores_from_text_only_for_script_writing
import return_scores_from_text_only_for_whatfix
import urllib
from flask import jsonify
#import urllib2
#import html2text
from bs4 import BeautifulSoup
from datetime import datetime
import nltk
UPLOAD_FOLDER = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER2 = '/var/www/html/'
ALLOWED_EXTENSIONS = set(['zip'])
dcounter=0
app = Flask(__name__)
app.config['UPLOAD_FOLDER2'] = UPLOAD_FOLDER2

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

@app.route('/', methods=['GET', 'POST'])

def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        timestring=str(request.form.get('bday'))
        print("timestring received is")
        print(timestring)
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            zip_ref = zipfile.ZipFile(os.path.join(UPLOAD_FOLDER, filename), 'r')
            zip_ref.extractall(UPLOAD_FOLDER)
            zip_ref.close()
            print("the file is uploaded")
            #os.chdir("/var/www/html/posts")
            
            
            #datastore=open("/var/www/html/posts/your_posts_1.json")
            
            with open('/var/www/html/posts/your_posts_1.json') as f:
                  datastore = json.load(f)
                  print("reading datastore of the current user in queue")
                  print(datastore)
                  print("the results are as below")
                  score_flesch_reading_ease,score_smog_index,score_kincaid_grade,scorecoleman_liau_index,score_readability_index,score_dale_chall,score_difficult_words,score_linsear_write,score_gunning_fog,score_text_standard=readability_stats_ptm.getScoresFromTimeString(timestring,datastore)
                  dict={}
                  dict['flesh']=score_flesch_reading_ease
                  dict['smog']=score_smog_index
                  dict['kincaid']=score_kincaid_grade
                  dict['coleman_liau']=scorecoleman_liau_index
                  dict['readability_index']=score_readability_index
                  dict['dae_chall']=score_dale_chall
                  dict['difficult_words']=score_difficult_words
                  dict['linsear_write']=score_linsear_write
                  dict['gunning_fog']=score_gunning_fog 
                  dict['text_standard']=score_text_standard    
                  return """<html>"""+json.dumps(dict) + """These are the scores of difference between your posts and your kid's thoughts/behaviour on readability understanding of your posts. The poorer the scores, the more lonely or tech addicted your kid is at home"""+"""</html>"""
            return redirect(url_for('upload_file',
                                    filename=filename))
    return render_template('index.html')

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
       
       
	


@app.route('/text-editor/',methods=['GET','POST'])

def text_editor():
    return render_template('text_editor_comparison.html')

@app.route('/scores-for-firepad',methods=['GET'])
def handletext():
        text=request.args.get('text')
        print(text)
        compare_url=request.args.get('compare_url')
        print("compare_url url is")
        print(compare_url)
        compare_file=request.args.get('compare_file')
        google_n_count=request.args.get('google_n_count')
        if google_n_count:
           
                  from google import google
                  if text :
                     search_results = google.search(text, int(google_n_count))
                     text_cat=""
                     for eachelem in search_results :
                         #try :
                             print("----------------")
                             print(eachelem.link)
                             print("----Description--")
                             print(eachelem.description)
                             print("----Cached---")
                             print(eachelem.cached)
                             print("----------------")
                             if (eachelem.description) :
                                text_cat=text_cat+str(eachelem.description)
                         #except :
                         #    print("some error in fetching text and concatenating it")
                     print("text concatenated of descriptions is")
                     print(text_cat)
                     if text_cat!="" :
                         x_json=return_scores_from_text_only_with_novelty_comparision.ret_scores_res(text,text_cat)
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
          x_json=return_scores_from_text_only_for_whatfix.ret_scores_res(text)
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

          
        
        



if __name__ == "__main__":
    app.run(host='0.0.0.0', port='6012', debug='true')
