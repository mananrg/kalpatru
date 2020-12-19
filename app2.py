#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import readability_stats_ptm
import os
import zipfile
from flask import Flask, request, redirect, url_for, flash, render_template
from werkzeug.utils import secure_filename
import return_tokenized_results
import return_scores_from_text_only

UPLOAD_FOLDER = os.path.dirname(os.path.realpath(__file__))
ALLOWED_EXTENSIONS = set(['zip'])
dcounter=0
app = Flask(__name__)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


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


@app.route('/text-editor/',methods=['GET','POST'])

def text_editor():
    return render_template('text_editor.html')

@app.route('/scores-for-firepad',methods=['GET'])
def handletext():
        text=request.args.get('text')
        n=return_tokenized_results.ret_len_res(text)
        x_json=return_scores_from_text_only.ret_scores_res(text)
        return(x_json)

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
    app.run(host='0.0.0.0')
