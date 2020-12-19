import return_scores_from_text_only
import pandas as pd
from datetime import datetime
import json
import personality
from copy_get_highest_heading_from_url import h1,h2
import numpy as np


timestamp1 = "Mar 1 2020"
timestamp2 = "Apr 15 2020"
datastore=""
def get_postscount_and_posts(json_file,timestamp1,timestamp2):
    with open(json_file) as f:
        datastore = json.load(f)
    data_link={}
    i=0
    while(i<len(datastore)) :
        try:
            time_stamp=datastore[i]["timestamp"]
            data_link[time_stamp]={}
#            if datastore[i]["data"][0]["post"]:
#                string_for_api_calls=datastore[i]["data"][0]["post"]
#                time_stamp=datastore[i]["timestamp"]


            
            if datastore[i]["attachments"][0]["data"][0]["external_context"["url"] and datastore[i]["data"][0]["post"] :
                    string_for_api_calls=datastore[i]["data"][0]["post"]
                    #if datastore[i]["attachments"][0]["data"][0]["external_context"]["url"] :
                    link=datastore[i]["attachments"][0]["data"][0]["external_context"]["url"]
                    data_link[time_stamp]['content']=string_for_api_calls
                    print(data_link)
                    print(string_for_api_calls)
                    data_link[time_stamp]['link']=link
            elif datastore[i]["attachments"][0]["data"][0]["external_context"]["url"] and !datastore[i]["data"][0]["post"]:
                
                    link=datastore[i]["attachments"][0]["data"][0]["external_context"]["url"]
                    #data_link[time_stamp]['content']=string_for_api_calls
                    #print(data_link)
                    #print(string_for_api_calls)
                    data_link[time_stamp]['content']="..."

                    data_link[time_stamp]['link']=link

            elif !datastore[i]["attachments"][0]["data"][0]["external_context"]["url"] and datastore[i]["data"][0]["post"]:
                    data_link[time_stamp]['content']=datastore[i]["data"][0]["post"]
                    data_link[time_stamp]['link']="..."

            else:
                #data_link[time_stamp]['content']=''
                data_link[time_stamp]['link']="..."
                data_link[time_stamp]['content']=datastore[i]["data"][0]["post"]
                
        except:
            pass
        i+=1
    #for i in enumerate(data_link.items()):
    #    print(i)
    df=pd.DataFrame.from_dict(data_link, orient='index')
    print("tital entries of ttttttimestamp in my json fillllle are")
    print(len(df))
    print(df)
    #df.dropna(axis=0,inplace=True)
    df=df.head()
    df['h1']=df['link'].apply(h1)
    df['h2']=df['link'].apply(h2)
    df['heading'] = df['h1'].str.cat(df['h2'],sep=" ")
    timestamp = df.index.tolist()
    content = df['content'].tolist()
    link = df['link'].tolist()
    heading=df['heading'].tolist()
    df.drop(columns=['h1', 'h2'],inplace=True)
    df = df.replace(np.nan, '.',regex=True,inplace=True)
    print(df)
    print(len(timestamp))
    print(len(content))
    print(len(link))
    
    return timestamp,content,link,heading,df
#timestamp,content,link,df=get_postscount_and_posts("your_posts_1.json",timestamp1,timestamp2)


def all_scores(total_strings): 
    scores=[]
    intro_extro=[]
    judging_function=[]
    lifestyle=[]
    perceiving_function=[]
    type_indicator_analyzer=[]
    category_classifier=[]
    for str_to_return in total_strings:
        print(str_to_return)
        scores.append(json.loads(return_scores_from_text_only.ret_scores_res(str_to_return)))
        intro_extro.append((personality.intro_extro(str_to_return)))
        judging_function.append((personality.judging_function(str_to_return)))
        lifestyle.append((personality.lifestyle(str_to_return)))
        perceiving_function.append((personality.perceiving_function(str_to_return)))
        type_indicator_analyzer.append((personality.type_indicator_analyzer(str_to_return)))
        category_classifier.append((personality.category_classifier(str_to_return)))
    print(lifestyle)
    return scores,intro_extro,judging_function,lifestyle,perceiving_function,type_indicator_analyzer,category_classifier
#all_scores(content)



def category_classifier_func(scores):
    x=['agriculture_environment', 'arts_culture', 'business_industry', 'economics_finance', 'education_language', 'employment_labour', 'government_politics', 'health_safety', 'indigenous_affairs', 'information_communications', 'international_affairs', 'law_justice','science_technology','social_affairs']
    df=pd.DataFrame(scores)
    print('**************************************************************')
    print(df)
    print('**************************************************************')
    compile_list=[df[i].tolist() for i in x]
    agriculture_environment=compile_list[0]
    arts_culture=compile_list[1]
    business_industry=compile_list[2]
    economics_finance=compile_list[3]
    education_language=compile_list[4]
    employment_labour=compile_list[5]
    government_politics=compile_list[6]
    health_safety=compile_list[7]
    indigenous_affairs=compile_list[8]
    information_communications=compile_list[9]
    international_affairs=compile_list[10]
    law_justice=compile_list[11]
    science_technology=compile_list[12]
    social_affairs=compile_list[13]
    #print("******************************************")
    #print(agriculture_environment)
    return agriculture_environment,arts_culture,business_industry,economics_finance,education_language,employment_labour,government_politics,health_safety,indigenous_affairs,information_communications,international_affairs,law_justice,science_technology,social_affairs

def intro_extro_func(scores):
    intro=[]
    extro=[]
    for i in scores:
        x=(i['Extraversion'])
        extro.append(x)
        y=(i['Introversion'])
        intro.append(y)
    print("INTRO")
    print(intro)
    print(len(intro))
    print("EXTRO")
    print(extro)
    print(len(extro))
    return intro,extro


def judging_func(scores):
    feeling=[]
    thinking=[]
    for i in scores:
        x=(i['Feeling'])
        feeling.append(x)
        y=(i['Thinking'])
        thinking.append(y)
    print("Feeling")
    print(feeling)
    print(len(feeling))
    print("Thinking")
    print(thinking)
    print(len(thinking))
    return feeling,thinking

def lifestyle_func(scores):
    judging=[]
    perceiving=[]
    for i in scores:
        x=(i['Judging'])
        judging.append(x)
        y=(i['Perceiving'])
        perceiving.append(y)
    print("judging")
    print(judging)
    print(len(judging))
    print("perceiving")
    print(perceiving)
    print(len(perceiving))
    return judging,perceiving

def perceiving_func(scores):
    sensing=[]
    intuition=[]
    for i in scores:
        x=(i['Sensing'])
        sensing.append(x)
        y=(i['iNtuition'])
        intuition.append(y)
    print("sensing")
    print(sensing)
    print(len(sensing))
    print("intuition")
    print(intuition)
    print(len(intuition))
    return sensing,intuition


def type_indicator_analyze_func(scores):
    x=['ENFJ','ENFP','ENTJ','ENTP','ESFJ','ESFP','ESTJ','ESTP','INFJ','INFP','INTJ','INTP','ISFJ','ISFP','ISTJ','ISTP']
    #ENFJ,ENFP,ENTJ,ENTP,ESFJ,ESFP,ESTJ,ESTP,INFJ,INFP,INTJ,INTP,ISFJ,ISFP,ISTJ,ISTP=([] for i in range(16))
    df=pd.DataFrame(scores)
    #print('**************************************************************')
    #print(df)
    #print('**************************************************************')
    compile_list=[df[i].tolist() for i in x]
    ENFJ=compile_list[0]
    ENFP=compile_list[1]
    ENTJ=compile_list[2]
    ENTP=compile_list[3]
    ESFJ=compile_list[4]
    ESFP=compile_list[5]
    ESTJ=compile_list[6]
    ESTP=compile_list[7]
    INFJ=compile_list[8]
    INFP=compile_list[9]
    INTJ=compile_list[10]
    INTP=compile_list[11]
    ISFJ=compile_list[12]
    ISFP=compile_list[13]
    ISTJ=compile_list[14]
    ISTP=compile_list[15]
    print("*****************************************************")
    print(ESFP)
    print("*****************************************************")
    return ENFJ,ENFP,ENTJ,ENTP,ESFJ,ESFP,ESTJ,ESTP,INFJ,INFP,INTJ,INTP,ISFJ,ISFP,ISTJ,ISTP
    
        

def novelty_score(scores):
    li=[]
    #print(scores)
    for i in scores:
        #prinat(i)
        try:
            #print("scores list is")
            x=(i['novelty_score'])
            #print('*'*60)
            li.append(x)       
        except:
            print("Exception")

    print("Novelty Score")
    print(li)
    print(len(li))
    return li

def text_standard(scores):
    li=[]
    #print(scores)
    for i in scores:
        #prinat(i)
        try:
            #print("scores list is")
            x=(i['text_standard'])
            #print('*'*60)
            li.append(x)
        except:
            print("Exception")
    print("Text Standard Score")        
    print(li)
    pritn(len(li))
    return li

def novelty_ratio(scores):
    old_li=[]
    li=[]
    #print(scores)
    for i in scores:
        #prinat(i)
        try:
            #print("scores list is")
            x=(i['novelty_ratio'])
            #print('*'*60)
            old_li.append(x)
        except:
            print("Exception")
    print("Novelty Ratio Score")
    print(old_li)
    print(len(old_li))
    return old_li

def readability_index(scores):
    li=[]
    #print(scores)
    for i in scores:
        #prinat(i)
        try:
            #print("scores list is")
            x=(i['readability_index'])
            #print('*'*60)
            li.append(x)
        except:
            print("Exception")
    print("Readability Index")
    print(li)
    print(len(li))
    return li

def flesch(scores):
    li=[]
    #print(scores)
    for i in scores:
        #prinat(i)
        try:
            #print("scores list is")
            x=(i['flesch'])
            #print('*'*60)
            li.append(x)
        except:
            print("Exception")
    print("Flesch Score")
    print(li)
    print(len(li))
    return li

def smog_index(scores):
    li=[]
    #print(scores)
    for i in scores:
        #prinat(i)
        try:
            #print("scores list is")
            x=(i['smog_index'])
            #print('*'*60)
            li.append(x)
        except:
            print("Exception")
    print("Smog Index")
    print(li)
    print(len(li))
    return li

def kincaid(scores):
    li=[]
    #print(scores)
    for i in scores:
        #prinat(i)
        try:
            #print("scores list is")
            x=(i['kincaid'])
            #print('*'*60)
            li.append(x)
        except:
            print("Exception")
    print("Kincaid")
    print(li)
    return li

def coleman_liau(scores):
    li=[]
    #print(scores)
    for i in scores:
        #prinat(i)
        try:
            #print("scores list is")
            x=(i['coleman_liau'])
            #print('*'*60)
            li.append(x)
        except:
            print("Exception")
    print("Coleman Liau")
    print(li)
    print(len(li))
    return li

def readability_index(scores):
    li=[]
    #print(scores)
    for i in scores:
        #prinat(i)
        try:
            #print("scores list is")
            x=(i['readability_index'])
            #print('*'*60)
            li.append(x)
        except:
            print("Exception")
    print("Readability Index")
    print(li)
    print(len(li))
    return li

def dae_chall(scores):
    li=[]
    #print(scores)
    for i in scores:
        #prinat(i)
        try:
            #print("scores list is")
            x=(i['dae_chall'])
            #print('*'*60)
            li.append(x)
        except:
            print("Exception")
    print("Dae Chall")
    print(li)
    print(len(li))
    return li

def linsear_write(scores):
    li=[]
    #print(scores)
    for i in scores:
        #prinat(i)
        try:
            #print("scores list is")
            x=(i['linsear_write'])
            #print('*'*60)
            li.append(x)
        except:
            print("Exception")
    print("Linsear Write")
    print(li)
    print(len(li))
    return li

def gunning_fog(scores):
    li=[]
    #print(scores)
    for i in scores:
        #prinat(i)
        try:
            #print("scores list is")
            x=(i['gunning_fog'])
            #print('*'*60)
            li.append(x)
        except:
            print("Exception")
    print("Gunning Fog")
    print(li)
    print(len(li))
    return li

def post_count(date):
    """
    Input=Date list
    Output=PostCount and vivid dates from the date list
    """
    date_copy=date
    final_date_list = list(dict.fromkeys(date_copy))
    post_count=[]
    for i in final_date_list:
        count=date.count(i)
        post_count.append(count)
        print(len(count))
        print(len(post_count))
    return final_date_list,post_count



timestamp,content,link,heading,df=get_postscount_and_posts("your_posts_1.json",timestamp1,timestamp2)
final_heading=[]
#for i in heading:
#    print(i)
#    i=str(i)
#    print(type(i))
#    final_heading.append(i)
print("----~!!@##$%^&*((%$$#@---Heading is")
print(heading)
scores,intro_extro,judging_function,lifestyle,perceiving_function,type_indicator_analyzer,category_classifier=all_scores(str(content))

hscores,hintro_extro,hjudging_function,hlifestyle,hperceiving_function,htype_indicator_analyzer,hcategory_classifier=all_scores(str(heading))



scores_dict = {'Date':timestamp,'Content':content,'Link':link,'Introvert(I)': intro_extro_func(intro_extro)[0] , 'Extrovert(E)':intro_extro_func(intro_extro)[1],
        'Judging(J)': judging_func(judging_function)[0],'Perceiving(P)':judging_func(judging_function)[1],
        'Feeling(F)':lifestyle_func(lifestyle)[0],'Thinking(T)':lifestyle_func(lifestyle)[1],
        'Sensing(S)':perceiving_func(perceiving_function)[0],'Intuition(I)':perceiving_func(perceiving_function)[1],
        'Flesch':flesch(scores),'Novelty Score':novelty_score(scores),'Novelty Ratio':novelty_ratio(scores),
        'Smog':smog_index(scores),'Kincaid':kincaid(scores),'Coleman':coleman_liau(scores),'Readability':readability_index(scores),
        'Dae Chall':dae_chall(scores),'Linsear Write':linsear_write(scores),'Gunning Fog':gunning_fog(scores),
        'ENFJ - The Giver':type_indicator_analyze_func(type_indicator_analyzer)[0],
        'ENFP - The Champion':type_indicator_analyze_func(type_indicator_analyzer)[1],
        'ENTJ - The Commander':type_indicator_analyze_func(type_indicator_analyzer)[2],
        'ENTP - The Debater':type_indicator_analyze_func(type_indicator_analyzer)[3],
        'ESFJ - The Caregiver':type_indicator_analyze_func(type_indicator_analyzer)[4],
        'ESFP - The Performer':type_indicator_analyze_func(type_indicator_analyzer)[5],
        'ESTJ - The Director':type_indicator_analyze_func(type_indicator_analyzer)[6],
        'ESTP - The Persuader':type_indicator_analyze_func(type_indicator_analyzer)[7],
        'INFJ - The Advocate':type_indicator_analyze_func(type_indicator_analyzer)[8],
        'INFP - The Mediator':type_indicator_analyze_func(type_indicator_analyzer)[9],
        'INTJ - The Architect':type_indicator_analyze_func(type_indicator_analyzer)[10],
        'INTP - The Thinker':type_indicator_analyze_func(type_indicator_analyzer)[11],
        'ISFJ - The Protector':type_indicator_analyze_func(type_indicator_analyzer)[12],
        'ISFP - The Artist':type_indicator_analyze_func(type_indicator_analyzer)[13],
        'ISTJ - The Inspector':type_indicator_analyze_func(type_indicator_analyzer)[14],
        'ISTP - The Crafter':type_indicator_analyze_func(type_indicator_analyzer)[15],
        #'Politics':category_classifier_func(category_classifier)
        'agriculture_environment':category_classifier_func(category_classifier)[0],
        'arts_culture':category_classifier_func(category_classifier)[1],
        'business_industry':category_classifier_func(category_classifier)[2],
'economics_finance':category_classifier_func(category_classifier)[3],
        'education_language':category_classifier_func(category_classifier)[4],
        'employment_labour':category_classifier_func(category_classifier)[5],
        'government_politics':category_classifier_func(category_classifier)[6],
        'health_safety':category_classifier_func(category_classifier)[7],
        'indigenous_affairs':category_classifier_func(category_classifier)[8],
        'information_communications':category_classifier_func(category_classifier)[9],
        'international_affairs':category_classifier_func(category_classifier)[10],
        'law_justice':category_classifier_func(category_classifier)[11],
        'science_technology':category_classifier_func(category_classifier)[12],
        'social_affairs':category_classifier_func(category_classifier)[13],        
        'Heading': heading,
        'HIntrovert(I)': intro_extro_func(hintro_extro)[0] , 'HExtrovert(E)':intro_extro_func(hintro_extro)[1],
        'HJudging(J)': judging_func(hjudging_function)[0],'HPerceiving(P)':judging_func(hjudging_function)[1],
        'HFeeling(F)':lifestyle_func(hlifestyle)[0],'HThinking(T)':lifestyle_func(hlifestyle)[1],
        'HSensing(S)':perceiving_func(hperceiving_function)[0],'HIntuition(I)':perceiving_func(hperceiving_function)[1],
        'HFlesch':flesch(hscores),'HNovelty Score':novelty_score(hscores),'HNovelty Ratio':novelty_ratio(hscores),
        'HSmog':smog_index(hscores),'HKincaid':kincaid(hscores),'HColeman':coleman_liau(hscores),'HReadability':readability_index(hscores),
        'HDae Chall':dae_chall(hscores),'HLinsear Write':linsear_write(hscores),'HGunning Fog':gunning_fog(hscores),
        'HENFJ - The Giver':type_indicator_analyze_func(htype_indicator_analyzer)[0],
        'HENFP - The Champion':type_indicator_analyze_func(htype_indicator_analyzer)[1],
        'HENTJ - The Commander':type_indicator_analyze_func(htype_indicator_analyzer)[2],
        'HENTP - The Debater':type_indicator_analyze_func(htype_indicator_analyzer)[3],
        'HESFJ - The Caregiver':type_indicator_analyze_func(htype_indicator_analyzer)[4],
        'HESFP - The Performer':type_indicator_analyze_func(htype_indicator_analyzer)[5],
        'HESTJ - The Director':type_indicator_analyze_func(htype_indicator_analyzer)[6],
        'HESTP - The Persuader':type_indicator_analyze_func(htype_indicator_analyzer)[7],
        'HINFJ - The Advocate':type_indicator_analyze_func(htype_indicator_analyzer)[8],
        'HINFP - The Mediator':type_indicator_analyze_func(htype_indicator_analyzer)[9],
        'HINTJ - The Architect':type_indicator_analyze_func(htype_indicator_analyzer)[10],
        'HINTP - The Thinker':type_indicator_analyze_func(htype_indicator_analyzer)[11],
        'HISFJ - The Protector':type_indicator_analyze_func(htype_indicator_analyzer)[12],
        'HISFP - The Artist':type_indicator_analyze_func(htype_indicator_analyzer)[13],
        'HISTJ - The Inspector':type_indicator_analyze_func(htype_indicator_analyzer)[14],
        'HISTP - The Crafter':type_indicator_analyze_func(htype_indicator_analyzer)[15],
        #'Politics':category_classifier_func(category_classifier)
        'Hagriculture_environment':category_classifier_func(hcategory_classifier)[0],
        'Harts_culture':category_classifier_func(hcategory_classifier)[1],
        'Hbusiness_industry':category_classifier_func(hcategory_classifier)[2],
        'Heconomics_finance':category_classifier_func(hcategory_classifier)[3],
        'Heducation_language':category_classifier_func(hcategory_classifier)[4],
        'Hemployment_labour':category_classifier_func(hcategory_classifier)[5],
        'Hgovernment_politics':category_classifier_func(hcategory_classifier)[6],
        'Hhealth_safety':category_classifier_func(hcategory_classifier)[7],
        'Hindigenous_affairs':category_classifier_func(hcategory_classifier)[8],
        'Hinformation_communications':category_classifier_func(hcategory_classifier)[9],
        'Hinternational_affairs':category_classifier_func(hcategory_classifier)[10],
        'Hlaw_justice':category_classifier_func(hcategory_classifier)[11],
        'Hscience_technology':category_classifier_func(hcategory_classifier)[12],
        'Hsocial_affairs':category_classifier_func(hcategory_classifier)[13]

        }


print('\nConverting into dataframe......\n')
df = pd.DataFrame(scores_dict)
from joblib import dump, load
pred = new_clf.predict_proba(df["Content"])
df2=pd.DataFrame(new_clf.predict_proba(X_test),columns=new_clf.classes_)
print(len(df))
print(len(df2))
print("************************************************************************************************************** \n")
print(df)
frames=[df,df2]
result=pd.concat(frames,axis=1)
username="FinalAchin"
print('Converting into csv.......')
#os.chdir('data_score/')
result.to_csv('/var/www/html/data_score/'+username + '.csv',index=False)
print('You can now download the data at /var/www/html/data_score/'+ username)








'''
print(scores)
print(intro_extro)
print(judging_function)
print(lifestyle)
print(perceiving_function)
print(type_indicator_analyzer)
print(category_classifier)
print("********************************************************************")

print(hscores)
print(hintro_extro)
print(hjudging_function)
print(hlifestyle)
print(hperceiving_function)
print(htype_indicator_analyzer)
print(hcategory_classifier)
'''
