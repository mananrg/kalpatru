import content_selection
from google.cloud import storage
from config import bucketName, localFolder, bucketFolder
from google.cloud import vision
from google.cloud.vision import types
import os,io,re
import bs4 as bs
import json
from bs4 import BeautifulSoup
import json,re,requests,wget
from google.protobuf.json_format import MessageToJson
from google.cloud import vision,storage
from google.cloud.vision import types
import re
import requests
from bs4 import BeautifulSoup
import wget,config
#from flask import Flask,render_template
from os import listdir
from os.path import isfile, join
from flask import Flask, request, redirect, url_for, flash, render_template
import socket
import urllib.request

#app=Flask(__name__)
dict1={}
outlabel=[]
outscore=[]
list1=[]
site2={}
dict2={}
dict3={}
dict5={}
site3={}
site4=()
dict6={}
site1=[]
list7=[]

v2={}
dictofWords={}
dict8={}
filter={}
#@app.route('/cloudvisionhere',methods=['GET'])
def start_processing():
 
 json_posts='/var/www/html/posts/your_posts_1.json'   
 x=content_selection.ret_html(json_posts)
 print('*********************')
 print(os.getcwd())
 os.environ['GOOGLE_APPLICATION_CREDENTIALS']=r'gcp_cloud_vision.json'
 storage_client = storage.Client()
 bucketFolder='do_images'
 bucketName="techhealthtools"
 localFolder='/var/www/html/down_images/'
 bucket = storage_client.get_bucket(bucketName)
 img_list_for_vision=[]
 os.mkdir('down_images')
 for site in x.items():
   #print("site")
   #print(site)
   site1=site[1]
  # print(site1)
   sno =site[0].split(":", 1)[0]
   website=site[0].split(":",1)[1]
   #timestamp=site[0].split(":",0)[1]
   # print(timestamp)
   v=site[1]
   #dict2={site1:website}
  # print(dict2)
  # print(dict3)
   #print(dict4)
   #print(v)
   #sno=k[0:2]
   #website=k[2:]
   #print("serial no")
   #print(sno)
   #print("website")
   #print(website)
   #print(k)
   #print("timestamp")
   #print(v)
   dict1['timestamp']=v
   suggestion=[]
   filter={'time1':site1}
   #print(filter)

   for k1,v1 in filter.items():
    list1=str(v1)
    #for p in list1:
     #print(p)
    if website:
     try:
       response = requests.get(website,timeout=3)
       soup = BeautifulSoup(response.text, 'html.parser')
       img_tags = soup.findAll('img',{"src":True})
       urls = []
       for img in img_tags:
           #print('************************')
           #print('inside img src')
           #dict3={site1:{website:img}}
           #print(dict3)
           urls.append(img)
       img_list=[i.get('src') for i in urls]
       img_list_for_vision.append(dict1)
       len_img_list_for_this_site=len(img_list)
       i=0
       for image_url in img_list:

         try:
              #print(img_list)
              #print('inside image url')
             
              dict3={list1:{image_url}}
              print(dict3)
              os.chdir(r'/var/www/html/down_images')
              local_image_filename=wget.download(image_url)
            #  print(local_image_filename)
              new_filename_to_append=str(sno)+str(":")+str(i)+":"+str(v)+":"
              #print(new_filename_to_append)
              os.system('mv'+' '+local_image_filename+' '+new_filename_to_append+local_image_filename)
              suggestion.append([sno,website,image_url,"successfully_downloaded",new_filename_to_append+local_image_filename])
             # print( new_filename_to_append+local_image_filename)

              #dict3={site1:{website:img}}
            #  print(suggestion)
         except Exception as e:
              #print("some error")
              suggestion.append([sno,website,image_url,e])
              #new_filename_to_append
         i=i+1
       suggestion.append([sno,website,"succesfully_response_received"])   
     except Exception as f:
       #print("error retreiving response from main url of x.items with 3 timeout seconds")
       suggestion.append([sno,website,f])
      # print(suggestion)
   dict1["suggestions"+"for_timestamp:"+str(v)]=suggestion 
   dict5[str(v)]=suggestion
   #print(dict5)
 os.chdir(r'/var/www/html/down_images')
 with open('json_posts-sno_uri_imglist_timestamp2.txt', 'a') as fp:
         fp.write(str(dict1))
 out_list=[]
 print('1111111111111111111111111111111')
 os.environ['GOOGLE_APPLICATION_CREDENTIALS']=r'/var/www/html/gcp_cloud_vision.json'
 client=vision.ImageAnnotatorClient()
 print('22222222222222222222222222222222')
 with os.scandir('/var/www/html/down_images/') as entries:

      for entry in entries:
        # print(entry)
         os.chdir('/var/www/html/down_images/')  
         file_name=entry.name
         #print(file_name)
         image_path=f'{file_name}'
         with io.open(image_path,'rb') as image_file:
            content=image_file.read()
            
         image=vision.types.Image(content=content)
         response=client.label_detection(image=image)
         labels = response.label_annotations
         #print(type(response))
         #print('-'*30)
         #list7=label 
         #print(labels)
         #print(response)
         #print('Labels (and confidence score):')
         #print('=' * 79)
         for label in response.label_annotations:

            for site in x.items():
                site4=site[1]
                site=str(site4)
               # for site3 in site2.items():
                # print(site3.time)
            #for site5 in site2.items():
             #print(site5)
            dict4={site:{label.description:label.score}}
            print('****************************************')
            print('INSIDE  DICT4 ')
            print(dict4)
            # for k2,v2 in dict4.items():
             #   list7=v2
                #dictOfWords = { i1 : list7 for i1 in range(0, len(list7) ) }
                #print(dictOfWords)
                #for j in list:
                    
                   # dict6={j}
                 #   print(j)
                 #  for k3,v3 in j.items():
                  #     for z in (k3,v3):
                   #        print(z)
                        #if (z=="description"):
                         #   v2=v1
                        #if (z=="score"):
                         #   filter={v2,v1}
                          #  print(filter)
           # list7=label 
            #print(dict4)
            #for site1, label in dict4_old()
           # dict4_new=dict(label, site1)

            #for i in dict4_new:
            #print(i, " :  ", new_dict[i]) 
            
            #print(dict4)
          #  print(dict4)
            score =int(label.score)
            #print(f'{label.description} ({label.score*100}%)')
            #out_description=label.description
            #print(out_description)
            #out_score=label.score
            #x=label.description
            #y=label.score
            #print(x)
            #print(y)
            
            #outlabel.append(x)
            #outscore.append(y)
            #return render_template('del.html',label_description=label.description,label_score=label.score) 
         #print('=' * 79)
         #print(' ')
         #print("for file_name")
         #print(file_name)
         #print("response is")
         #print(response)
        
         serialized = MessageToJson(response)
         x = eval(serialized)
        # x.update( {'fb_timestamp' : file_name.split(':',3)[2] })
         out_list.append(x)
         file_name_of_result=file_name+'_json_result'+'.txt'
         with open(file_name_of_result, 'w') as json_f:
            json.dump(x, json_f)
         os.chdir('/var/www/html/down_images/')
         
         
 #print("everything from down_images done")
 os.chdir('/var/www/html/')
 #print(label.description)
 #print(label.score)
 j=0
 """
 for i in out_list:
     try:  
         print("while")
       
         #print(i['labelAnnotations'][0]['description'])
         #print(i['labelAnnotations'][0]['score'])
         for j in i['labelAnnotations']:

            print(j['labelAnnotations'][0]['description'])

         j+=1 
     except:
         print("Missed")
"""
 #return render_template('try1.html',out_list=out_list)i
 dict2={v:website}

 #dict3={site1:{website:img}}
 #dict4={site1:{website:{img:label}}}
 return out_list,outlabel,outscore,dict2
#start_processing()
  #   return tm

# print(outlabel)
# print(outscor
#if __name__=="__main__":
#    app.run(debug=True,host='0.0.0.0', port=5010)
          
