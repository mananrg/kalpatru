import json
from operator import itemgetter
#import matplotlib.pyplot as plt2
#import matplotlib.pyplot as plt3
from datetime import datetime
import textstat
print("achin")
import time
from time import mktime
from pytz import timezone
import pytz
utc = pytz.utc
print(utc.zone)
#file= open("posts/your_posts_1.json")
#datastore = json.load(file)
#import matplotlib
#matplotlib.axes.Axes.pie
#matplotlib.pyplot.pie
def getScoresFromTimeString(timestring,datastore) :
 i=0
 text_stats_string=""
 while(i<5) :

       try: 
        i+=1
        string_for_api_calls=datastore[i]["data"][0]["post"]
        print("post is")
        print(string_for_api_calls)
        time_stamp=datastore[i]["timestamp"]
       
        dt_object = datetime.fromtimestamp(time_stamp)
        #dt_object=dt_object.date()
        print("datetime format of parent post is")
        
        print(dt_object)
        #date_time_str_child=timestring
        print("timestring is")
        print(timestring)
        child_date2=datetime.strptime(timestring, "%Y-%m-%d")
        #date_child=time.strptime(date_time_str_child, "%Y-%m-%d")
        #print(type(date_child))
        print("child_date2 object is")
        print(child_date2)
        difference=child_date2-dt_object
        print("the difference between child date 2 and dt_object is")
        print(difference)
        
        
        print("type of child date2 object is")
        print(type(child_date2))
        datetime1=dt_object.date()
        datetime2=child_date2.date()
        
        
        
        if (dt_object > child_date2):
         print("parent's post is Greater than when child joined, considering only those posts here onwards which bothered child")
        
         text_stats_string=text_stats_string+string_for_api_calls + "."
         print("text_stats_string right now is")
         print(text_stats_string)
         print("time stamp of this post is")
         print(time_stamp)
    
         test_data=text_stats_string
         print("text of parent's posts on which scores will get calculated is")
         print("ACHIN ROCKS")
         print(test_data)
         score_flesch_reading_ease=textstat.flesch_reading_ease(test_data)
         score_smog_index=textstat.smog_index(test_data)
         score_kincaid_grade=textstat.flesch_kincaid_grade(test_data)
         scorecoleman_liau_index=textstat.coleman_liau_index(test_data)
         score_readability_index=textstat.automated_readability_index(test_data)
         score_dale_chall=textstat.dale_chall_readability_score(test_data)
         score_difficult_words=textstat.difficult_words(test_data)
         score_linsear_write=textstat.linsear_write_formula(test_data)
         score_gunning_fog=textstat.gunning_fog(test_data)
         score_text_standard=textstat.text_standard(test_data)
       except:
         print("this code got hit at i")
         print(i)
 return(score_flesch_reading_ease,score_smog_index,score_kincaid_grade,scorecoleman_liau_index,score_readability_index,score_dale_chall,score_difficult_words,score_linsear_write,score_gunning_fog,score_text_standard)

from flask import Flask, request, redirect, url_for, flash, render_template
app = Flask(__name__)

@app.route('/predict',methods=['GET'])
def handlemsg():
        file= open("posts/your_posts_1.json")
        datastore = json.load(file)
        msg=request.args.get('msg')
        print("""you sent timestring msg"""+msg)
        #print("datastore value is")
        #print(datastore)
        score_flesch_reading_ease,score_smog_index,score_kincaid_grade,scorecoleman_liau_index,score_readability_index,score_dale_chall,score_difficult_words,score_linsear_write,score_gunning_fog,score_text_standard=getScoresFromTimeString(msg,datastore)
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
        return(json.dumps(dict))


if __name__ == "__main__":
        app.run(host='0.0.0.0',port=7000,debug=True)
#print(getScoresFromTimeString("2019-08-10",datastore))
     
