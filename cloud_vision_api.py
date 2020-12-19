import content_selection
from google.cloud import storage
from config import bucketName, localFolder, bucketFolder
from google.cloud import vision
from google.cloud.vision import types
import os,io,re
import bs4 as bs
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
app=Flask(__name__)
#x=[]
dict1={}
#json_posts='/var/www/html/posts/your_posts_1.json'
#@app.route('/cloudvisionhere',methods=['GET'])
def start_processing():
    
 #y=str(request.args.get('json_posts'))
 json_posts='/var/www/html/posts/your_posts_1.json'   
 x=content_selection.ret_html(json_posts)
 #print(x)
 #x=json_posts
 os.environ['GOOGLE_APPLICATION_CREDENTIALS']=r'gcp_cloud_vision.json'
 storage_client = storage.Client()
 #print("bucketname imported from config is")
 #print(bucketName)

 bucketFolder='do_images'
 bucketName="techhealthtools"
 localFolder='/var/www/html/down_images/'
 bucket = storage_client.get_bucket(bucketName)
 img_list_for_vision=[]
 os.mkdir('down_images')
 #dict1={}
 for site in x.items():
   #site=site.split(":")
   print("site")
   print(site)
   sno =site[0].split(":", 1)[0]
   website=site[0].split(":",1)[1]
   v=site[1]
   #sno=k[0:2]
   #website=k[2:]
   print("serial no")
   print(sno)
   print("website")
   print(website)
   #print(k)
   print("timestamp")
   print(timestamp)
   #print(v)

   #dict1['sno']=sno
   #dict1['site']=website
   #       dict1['img_list']=img_list
   dict1['timestamp']=v
   suggestion=[]
   print(suggestion)
   #dict1['suggestions']=suggestion
   
   

  #with open('json_posts-sno_uri_imglist_timestamp.json', 'w') as fp:
  #  json.dump(dict, fp)
   #print("dictionary without image list is")
   #print(dict1)
   if website:
     #print("i reached inside loop without site in x error")
     try:
       response = requests.get(website,timeout=3)
       #print("i reached after response without site in x error")
       soup = BeautifulSoup(response.text, 'html.parser')
       img_tags = soup.findAll('img',{"src":True})

      
       urls = []
       for img in img_tags:
         urls.append(img)
       img_list=[i.get('src') for i in urls]
       #print("img_list for this site is")
       #print(img_list)
       #len_img_list=len(img_list)
       
       #dict1['img_list']=img_list
       
       img_list_for_vision.append(dict1)
       #with open('json_posts-sno_uri_imglist_timestamp.json', 'w') as fp:
       #             json.dump(dict, fp)

       

       #socket.setdefaulttimeout(19)
       len_img_list_for_this_site=len(img_list)
       i=0
       for image_url in img_list:
         try:
              #suggestion.append([sno,website,image_url])
              os.chdir(r'/var/www/html/down_images')
              #urllib.request.urlretrieve (image_url, image_url)
              #local_image_filename=""
              local_image_filename=wget.download(image_url)
              new_filename_to_append=str(sno)+str(":")+str(i)+":"+str(v)+":"
              #str(local_image_filename)
              os.system('mv'+' '+local_image_filename+' '+new_filename_to_append+local_image_filename)
              #local_image_filename=str(sno)+str(i)+str(v)+local_image_filename
              
              
              suggestion.append([sno,website,image_url,"successfully_downloaded",new_filename_to_append+local_image_filename])

         except Exception as e:
              print("some error")
              suggestion.append([sno,website,image_url,e])
         i=i+1

       #for image_url in img_list:
         #try:
         #  os.chdir(r'/var/www/html/down_images')  
         #  local_image_filename= wget.download(image_url)  
        
         #except:
           #print('Issue Downloading')  
           
           #pass
       suggestion.append([sno,website,"succesfully_response_received"])
        dict1["suggestions"+"for_timestamp:"+str(v)]=suggestioni
        for key,value in dict1.items() :
            print(values)

     except Exception as f:
       #dict1['url_status']="error retreiving url"
       print("error retreiving response from main url of x.items with 3 timeout seconds")
       
       suggestion.append([sno,website,f])
   #else:
      #dict1['img_list']="na" 
   #dict1['timestamp']=v
   dict1["suggestions"+"for_timestamp:"+str(v)]=suggestion 



 os.chdir(r'/var/www/html')
 with open('json_posts-sno_uri_imglist_timestamp2.txt', 'a') as fp:
         #json.dump(dict1, fp)
         fp.write(str(dict1))
         #fp.write(dict1)
 #def upload_files(bucketName):
 #    """Upload files to GCP bucket."""
 #    print('Entered the upload function')
 #    files = [f for f in listdir(localFolder) if isfile(join(localFolder, f))]
 #    for file in files:
 #        print('file name')
 #        print(file)
 #        localFile = localFolder + file
 #        blob = bucket.blob(bucketFolder + file)
 #        blob.upload_from_filename(localFile)
 #upload_files(bucketName)
 out_list=[]
 os.environ['GOOGLE_APPLICATION_CREDENTIALS']=r'gcp_cloud_vision.json'
 client=vision.ImageAnnotatorClient()
 #os.system('sudo mkdir results/')
 #print('ResultDirctory') 
 with os.scandir('/var/www/html/down_images/') as entries:
     for entry in entries:
      #print(os.getcwd()
      #try:
         os.chdir('/var/www/html/down_images/')  
         #print("At start current working directory is")
         #print(os.getcwd())
         file_name=entry.name
         #print("Image:")
         #print(file_name)
         image_path=f'{file_name}'
         with io.open(image_path,'rb') as image_file:
            content=image_file.read()
         image=vision.types.Image(content=content)
         response=client.label_detection(image=image)
         labels = response.label_annotations
         #print(type(response))
         #print('-'*30)
         #print('labels')
         #print(response)
         #print('Labels (and confidence score):')
         #print('=' * 79)
         out_description=[]
         out_score=[]

         for label in response.label_annotations:
            score =int(label.score)
            #print(f'{label.description} ({label.score*100}%)')
            #out_description=label.description
            #print(out_description)
            #out_score=label.score
            #return render_template('del.html',label_description=label.description,label_score=label.score) 
         #print('=' * 79)
         #print(' ')
         #print("for file_name")
         #print(file_name)
         #print("response is")
         #print(response)
        
         serialized = MessageToJson(response)
         x = eval(serialized)
         #print(x.values['description']) #p
         #print('x')
         #print(type(x))
         #print(x)
         x.update( {'fb_timestamp' : file_name.split(':',3)[2] })
         #y[entry.split(':',1)
         out_list.append(x)
         
         file_name_of_result=file_name+'_json_result'+'.txt'
         #print('file name of results')
         #print(file_name_of_result)
         #print("Before open")
         #print(os.getcwd())
         with open(file_name_of_result, 'w') as json_f:
             #print('Entered With')
             #print('After with cwd')
             #print(os.getcwd())
             json.dump(x, json_f)
         os.chdir('/var/www/html/down_images/')
         #return out_list
         
         
 print("everything from down_images done")
 os.chdir('/var/www/html/')
 #print(label.description)
 #print(label.score)
 #print(out_description)
 #print(out_score)
 #print('11111111111')
 #print(x['labelAnnotations'])
 #print('222222222222')
 #print(out_list)

 j=0
 for i in out_list:
     try:  
         print("while")
       
         print(i['labelAnnotations'][0]['description'])
         print(i['labelAnnotations'][0]['score'])
         #print(i['labelAnnotations'][0]['fb_timestamp']
         for j in i['labelAnnotations']:

            print(j)    
         j+=1 
     except:
         print("Missed")

 #return render_template('try.html',out_list=out_list)
 return out_list
#start_processing(json_posts)
#if __name__=="__main__":
#    app.run(debug=True,host='0.0.0.0', port=5002)
 
