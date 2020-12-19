import content_selection
json_posts='/var/www/html/posts/your_posts_1.json'
x,y=content_selection.ret_html(json_posts)
import json
i=0
dict_1={}


print(x)
print(y)

res={}
l=len(x)
i=0
for key in x: 
        for value in y: 
            
            if i<l :
              res[str(i)+':'+str(key)] = value 
            i=i+1
            y.remove(value) 
            break 

print(res)

import json
with open('json_posts-index_uri_ts.json', 'w') as fp:
        json.dump(res, fp)



#dict(list(enumerate(y)))
#dict_1(zip(x,y))
#print(dict_1)

#while(i<len(x)):
    
#    if x[i]:
      #  dict['main_jsons_uri']=x[i]
      #  dict['timestamp_status']=y[i]
#    else:

      #  y[i]="no_uri_found"
      #  dict['main_jsons_uri']="not_found"
      #  dict['timestamp_status']="ts_not_applicable"
    
    #i=i+1
#print(dict)
#z=json.dumps(dict)

#print(z)
