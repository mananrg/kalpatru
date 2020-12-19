from test_findall import googlesearch2df
import json
import return_scores_from_text_only
import pandas as pd
from datetime import datetime
import json
import personality
from datetime import datetime
def get_postscount_and_posts_search_history(username,timestamp1,timestamp2):
    i=0
    #timestamp1 = "Mar 1 2019"
    #timestamp2 = "Mar 10 2019"
    #date="
    checkdate_list=[]
    judging_function=[]
    lifestyle=[]
    perceiving_function=[]
    type_indicator_analyzer=[]
    count_of_posts=0
    str_to_return=[]
    scores=[]
    intro_extro=[]
    category_classifier=[]
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
            count_of_posts=count_of_posts+1
            if checkdate > t1date:
                if t2date > checkdate:
                    if string_for_api_calls:
                       print("####################################################################")
                       print("Strings is: ",string_for_api_calls)
                       checkdate_list.append(checkdate)
                       str_to_return.append(string_for_api_calls)
                       scores.append(json.loads(return_scores_from_text_only.ret_scores_res(string_for_api_calls)))
                       intro_extro.append((personality.intro_extro(string_for_api_calls)))
                       judging_function.append((personality.judging_function(string_for_api_calls)))
                       lifestyle.append((personality.lifestyle(string_for_api_calls)))
                       perceiving_function.append((personality.perceiving_function(string_for_api_calls)))
                       type_indicator_analyzer.append((personality.type_indicator_analyzer(string_for_api_calls)))
                       category_classifier.append((personality.category_classifier(string_for_api_calls)))

        except:
            checkdate_list.remove(checkdate)
            str_to_return.remove(string_for_api_calls)
            print("Checkdate removed",checkdate)
            pass
        i+=1
    #print("*************************************************************************************************")
    #print(checkdate_list)
    #print("*************************************************************************************************")
    return count_of_posts,str_to_return,checkdate_list,scores,intro_extro,judging_function,lifestyle,perceiving_function,type_indicator_analyzer,category_classifier


def get_postscount_and_posts_visited_history(username,timestamp1,timestamp2):
    i=0
    #timestamp1 = "Mar 1 2019"
    #timestamp2 = "Mar 10 2019"
    checkdate_list=[]
    judging_function=[]
    lifestyle=[]
    perceiving_function=[]
    type_indicator_analyzer=[]
    count_of_posts=0
    str_to_return=[]
    scores=[]
    intro_extro=[]
    category_classifier=[]
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
            
            count_of_posts=count_of_posts+1
            if checkdate > t1date:
                if t2date > checkdate:
                    if string_for_api_calls:
                       print("####################################################################")
                       print("Strings is: ",string_for_api_calls)
                       checkdate_list.append(checkdate)
                       str_to_return.append(string_for_api_calls)
                       scores.append(json.loads(return_scores_from_text_only.ret_scores_res(string_for_api_calls)))
                       intro_extro.append((personality.intro_extro(string_for_api_calls)))
                       judging_function.append((personality.judging_function(string_for_api_calls)))
                       lifestyle.append((personality.lifestyle(string_for_api_calls)))
                       perceiving_function.append((personality.perceiving_function(string_for_api_calls)))
                       type_indicator_analyzer.append((personality.type_indicator_analyzer(string_for_api_calls)))
                       category_classifier.append((personality.category_classifier(string_for_api_calls)))

        except:
            checkdate_list.remove(checkdate)
            str_to_return.remove(string_for_api_calls)
            print("Checkdate removed",checkdate)
            pass
        i+=1
    return count_of_posts,str_to_return,checkdate_list,scores,intro_extro,judging_function,lifestyle,perceiving_function,type_indicator_analyzer,category_classifier

