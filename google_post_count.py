from test_findall import googlesearch2df
import json
import return_scores_from_text_only
import pandas as pd
from datetime import datetime
import json
import personality
from datetime import datetime
def get_postscount_searched(username,timestamp1,timestamp2):
    i=0
    #timestamp1 = "Mar 1 2019"
    #timestamp2 = "Mar 10 2019"
    count_of_posts=0
    json_file=username+"_google_search_history.json"
    with open(json_file) as f:
        datastore = json.load(f)
    while(i<len(datastore)) :
        try:
            string_for_api_calls=datastore[i]['Title']
            date=datastore[i]["Timestamp"]
            check=datetime.strptime(date,"%d %b %Y")
            checkdate=check.date()
            t1 = datetime.strptime(timestamp1, "%b %d %Y")
            t2 = datetime.strptime(timestamp2, "%b %d %Y")
            t1date=t1.date()
            t2date=t2.date()  
            if checkdate > t1date:
                if t2date > checkdate:
                    if string_for_api_calls:
                        count_of_posts=count_of_posts+1
                       
        except:
            pass
        i+=1
    #print("*************************************************************************************************")
    print("Pages Searched : ",count_of_posts)
    #print("*************************************************************************************************")
    return count_of_posts

def get_postscount_visited(username,timestamp1,timestamp2):
    i=0
    #timestamp1 = "Mar 1 2019"
    #timestamp2 = "Mar 10 2019"
    count_of_posts=0
    json_file=username+"_google_visited_history.json"
    with open(json_file) as f:
        datastore = json.load(f)
        #print(datastore)
    while(i<len(datastore)) :
        try:
            string_for_api_calls=datastore[i]['Title']
            date=datastore[i]["Timestamp"]
            check=datetime.strptime(date,"%d %b %Y")
            checkdate=check.date()
            t1 = datetime.strptime(timestamp1, "%b %d %Y")
            t2 = datetime.strptime(timestamp2, "%b %d %Y")
            t1date=t1.date()
            t2date=t2.date()
            if checkdate > t1date:
                if t2date > checkdate:
                    if string_for_api_calls:
                       count_of_posts=count_of_posts+1
        except:
            pass
        i+=1
    print("Pages visited : ",count_of_posts)
    return count_of_posts

from test_findall import googlesearch2df,googlevisited2df
username="Achin"
#file="My Activity.html"
#googlesearch2df(username,file)
#googlevisited2df(username,file)

timestamp1 = "Mar 1 2019"
timestamp2 = "Mar 10 2019"
get_postscount_visited(username,timestamp1,timestamp2)
get_postscount_searched(username,timestamp1,timestamp2)
