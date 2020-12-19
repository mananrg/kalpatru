import json
print('hello')
data_scratched=""
#listtoret=[]
def ret_html(json_of_posts):    
    data = json.loads(open(json_of_posts).read())
    #print(data)
    i=0
    timestamp=[]
    listtoret=[]
    while(i<30):
        data_scratched=""
        try:
        
      #      print(i)a
            data_timestamp=data[i]["timestamp"]
            data_scratched=data[i]["attachments"][0]["data"][0]["external_context"]["url"]
            #print(data_scratched)
            print(data_timestamp)
            
           
        except:
            
        
            
            print( 'passing and moving on to next')
        i+=1
        timestamp.append(data_timestamp)
        #listtoret.append(data_timestamp)
        listtoret.append(data_scratched)
    tm =timestamp
    print(tm)
     
    #print(listtoret)
    
    res={}
    l=len(listtoret)
    i=0
    for key in listtoret:
                for value in timestamp:

                                if i<l :
                                  res[str(i)+':'+str(key)] = value
                                  i=i+1
                                  timestamp.remove(value)
                                  break

                                 
    print(res)

    
    with open('json_posts-index_uri_ts.json', 'w') as fp:
        json.dump(res, fp)





    return res
    return tm 
        #i+=1
    #    return data_scratched


#x,y=ret_html('/var/www/html/posts/your_posts_1.json')
#print(len(x))
#print(len(y))
#print(x)
#print(y)

#print(ret_html('/var/www/html/posts/your_posts_1.json'))

