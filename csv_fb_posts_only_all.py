import return_scores_from_text_only
import pandas as pd
from datetime import datetime
import json
import personality
from copy_get_highest_heading_from_url import h1,h2
import numpy as np
from datetime import datetime
import pprint
import json
from datetime import datetime
import csv
def get_postscount_and_posts(json_file):
    with open(json_file) as f:
        datastore = json.load(f)
    i=0
    content_list=[]
    checkdate_list=[]
    while(i<len(datastore)) :
        try:
            if datastore[i]["data"][0]["post"]:
                post=datastore[i]["data"][0]["post"]
                time_stamp=datastore[i]["timestamp"]
                check = datetime.fromtimestamp(time_stamp)
                #print(check)
                #print("Check is",check)
                checkdate=check.date()
                #print("11111111111111111111111111111111111111111")
                s1 = checkdate.strftime("%d/%m/%Y") 
                print("")
                print(i)
                print("*"*120)
                print("Post date is: ",s1)
                print("Post is",post)
                checkdate_list.append(s1)
                print("*"*120)
                print("")
                content_list.append(str(post))
                    
        except:
            print("In exception")
            pass
        i+=1
    
    checkdate_list.reverse()
    print("Checkdate reversed...")
    #print(checkdate_list)
    
    content_list.reverse()
    print("Content reversed...")
    return checkdate_list,content_list



def all_scores(total_strings,timestamp): 
    scores=[]
    fi_timestamp=[]
    intro_extro=[]
    judging_function=[]
    lifestyle=[]
    perceiving_function=[]
    type_indicator_analyzer=[]
    category_classifier=[]
    all_str=[]
    i=0
    while i<len(total_strings):
        try:
            print("i is ",i)
            all_str.append(total_strings[i])
            scores.append(json.loads(return_scores_from_text_only.ret_scores_res(total_strings[i])))
            intro_extro.append((personality.intro_extro(total_strings[i])))
            judging_function.append((personality.judging_function(total_strings[i])))
            lifestyle.append((personality.lifestyle(total_strings[i])))
            perceiving_function.append((personality.perceiving_function(total_strings[i])))
            type_indicator_analyzer.append((personality.type_indicator_analyzer(total_strings[i])))
            category_classifier.append((personality.category_classifier(total_strings[i])))
            fi_timestamp.append(timestamp[i])
        except:
            all_str.remove(total_strings[i])
            #scores.remove(json.loads(return_scores_from_text_only.ret_scores_res(total_strings[i])))
            #intro_extro.remove((personality.intro_extro(total_strings[i])))
            #judging_function.remove((personality.judging_function(total_strings[i])))
            #lifestyle.remove((personality.lifestyle(total_strings[i])))
            #perceiving_function.remove((personality.perceiving_function(total_strings[i])))
            #type_indicator_analyzer.remove((personality.type_indicator_analyzer(total_strings[i])))
            #category_classifier.remove((personality.category_classifier(total_strings[i])))
            print("Removing Timestamp",timestamp[i])
            #fi_timestamp.remove(timestamp[i])
        i+=1
    #print("1111111111111111111111111111111111111111111111111111111111111111111111111111")
    #pprint.pprint(scores)
    
    #print("2222222222222222222222222222222222222222222222222222222222222222222222222222")
    return scores,fi_timestamp,all_str,intro_extro,judging_function,lifestyle,perceiving_function,type_indicator_analyzer,category_classifier
#all_scores(content)



def category_classifier_func(scores):
    x=['agriculture_environment', 'arts_culture', 'business_industry', 'economics_finance', 'education_language', 'employment_labour', 'government_politics', 'health_safety', 'indigenous_affairs', 'information_communications', 'international_affairs', 'law_justice','science_technology','social_affairs']
    df=pd.DataFrame(scores)
    #print('**************************************************************')
    #print(df)
    #print('**************************************************************')
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

def discourse(scores):
    Discourse_Agreement_percentage=[]
    Discourse_Announcement_percentage=[]
    Discourse_Answer_percentage=[]
    Discourse_Appreciation_percentage=[]
    Discourse_Disagreement_percentage=[]
    Discourse_Elaboration_percentage=[]
    Discourse_Humor_percentage=[]
    Discourse_Negative_reaction=[]
    Discourse_Question_percentage=[]
    Discourse_Other_percentage=[]
    for i in scores:
        Discourse_Agreement=(i['Discourse-Agreement_percentage'])
        Discourse_Agreement_percentage.append(Discourse_Agreement)
        Discourse_Announcement=(i['Discourse-Announcement_percentage'])
        Discourse_Announcement_percentage.append(Discourse_Announcement)
        Discourse_Answer=(i['Discourse-Answer_percentage'])
        Discourse_Answer_percentage.append(Discourse_Answer)
        Discourse_Appreciation=(i['Discourse-Appreciation_percentage'])
        Discourse_Appreciation_percentage.append(Discourse_Appreciation)
        Discourse_Disagreement=(i['Discourse-Disagreement_percentage'])
        Discourse_Disagreement_percentage.append(Discourse_Disagreement)
        Discourse_Elaboration=(i['Discourse-Elaboration_percentage'])
        Discourse_Elaboration_percentage.append(Discourse_Elaboration)
        Discourse_Humor=(i['Discourse-Humor_percentage'])
        Discourse_Humor_percentage.append(Discourse_Humor)
        Discourse_Negative=(i['Discourse-Negative_reaction'])
        Discourse_Negative_reaction.append(Discourse_Negative)
        Discourse_Question=(i['Discourse-Question_percentage'])
        Discourse_Question_percentage.append(Discourse_Question)
        Discourse_Other=(i['Discourse_Other_percentage'])
        Discourse_Other_percentage.append(Discourse_Other)
        
    return  Discourse_Agreement_percentage,Discourse_Announcement_percentage,Discourse_Answer_percentage,Discourse_Appreciation_percentage,Discourse_Disagreement_percentage,Discourse_Elaboration_percentage,Discourse_Humor_percentage,Discourse_Negative_reaction,Discourse_Question_percentage,Discourse_Other_percentage
def intro_extro_func(scores):
    intro=[]
    extro=[]
    for i in scores:
        x=(i['Extraversion'])
        extro.append(x)
        y=(i['Introversion'])
        intro.append(y)
    #print("INTRO")
    #print(intro)
    #print(len(intro))
    #print("EXTRO")
    #print(extro)
    #print(len(extro))
    return intro,extro


def judging_func(scores):
    feeling=[]
    thinking=[]
    for i in scores:
        x=(i['Feeling'])
        feeling.append(x)
        y=(i['Thinking'])
        thinking.append(y)
    #print("Feeling")
    #print(feeling)
    #print(len(feeling))
    #print("Thinking")
    #print(thinking)
    #print(len(thinking))
    return feeling,thinking

def lifestyle_func(scores):
    judging=[]
    perceiving=[]
    for i in scores:
        x=(i['Judging'])
        judging.append(x)
        y=(i['Perceiving'])
        perceiving.append(y)
    #print("judging")
    #print(judging)
    #print(len(judging))
    #print("perceiving")
    #print(perceiving)
    #print(len(perceiving))
    return judging,perceiving

def perceiving_func(scores):
    sensing=[]
    intuition=[]
    for i in scores:
        x=(i['Sensing'])
        sensing.append(x)
        y=(i['iNtuition'])
        intuition.append(y)
    #print("sensing")
    #print(sensing)
    #print(len(sensing))
    #print("intuition")
    #print(intuition)
    #print(len(intuition))
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
    #print("*****************************************************")
    #print(ESFP)
    #print("*****************************************************")
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

    #print("Novelty Score")
    #print(li)
    #print(len(li))
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
    #print("Text Standard Score")        
    #print(li)
    #print(len(li))
    return li

def novelty_ratio(scores):
    old_li=[]
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
    #print("Novelty Ratio Score")
    #print(old_li)
    #print(len(old_li))
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
    #print("Readability Index")
    #print(li)
    #print(len(li))
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
    #print("Flesch Score")
    #print(li)
    #print(len(li))
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
    #print("Smog Index")
    #print(li)
    #print(len(li))
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
    #print("Kincaid")
    #print(li)
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
    #print("Coleman Liau")
    #print(li)
    #print(len(li))
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
    #print("Dae Chall")
    #print(li)
    #print(len(li))
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
    #print("Linsear Write")
    #print(li)
    #print(len(li))
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
    #print("Gunning Fog")
    #print(li)
    #print(len(li))
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
        #print(len(count))
        #print(len(post_count))
    return final_date_list,post_count


file="harleen.m.physio@gmail.com/your_posts_1.json"

timestamp,content=get_postscount_and_posts(file)
#print("**************************************************************************************************")
#print(len(timestamp))
#print(len(content))
#print("**************************************************************************************************")

print("into scores")
scores,final_timestamp,all_str,intro_extro,judging_function,lifestyle,perceiving_function,type_indicator_analyzer,category_classifier=all_scores(content,timestamp)
print("got scores")

x=final_timestamp
y=discourse(scores)[0]
dic={}
for i in range(len(x)):
    dic[timestamp[i]]=y[i]
li=[x for x in dic.keys()]

def method(y):
    final_dict=[]
    for i in li:
        old_dict={}
        for val in y.items():
            value=val[1]-y[i]
            #print(value)
            if value>=0:
                old_dict[val[0]]=value
        final_dict.append(old_dict)
    return final_dict

diff=method(dic)

#[{t1}{t2}{t3........{t10}]
#print("*"*120)
#print("Diffence score \n")
#for id,data in enumerate(diff):
#    print(id,data)

#print("*"*120)
#print("")

maxlen_diff2=[len(x) for x in diff]
maxpos = maxlen_diff2.index(max(maxlen_diff2))  
#print("Max Position is ",maxpos)
#print("Max length",maxlen_diff2)
dates=diff[maxpos]
print(dates)
print(len(dates))
df2 = pd.DataFrame(dates,index=[0])
#f2=pd.DataFrame.from_dict(dates, orient='columns',index=[0])
print(df2)
df2.to_csv('/var/www/html/data_score/'+'fb_posts_only_bias.csv')
#final_dates=[x for x in dates]
#final_dates_list=[]
'''
for i in final_dates:
    d=datetime.strptime(i, "%d/%m/%Y")
    date_time = d.strftime("%d-%m-%Y")
    print(date_time)
    print(type(date_time))
    final_dates_list.append(date_time)
print(final_dates_list)
'''
##x=[ '21-05-2020', '11-06-2020', '03-07-2020', '09-07-2020', '24-07-2020', '31-07-2020', '02-08-2020', '12-08-2020', '13-08-2020']
#final=[]
#for i in final_dates:
#    d=datetime.strptime(i, "%d/%m/%Y")
#    date_time = d.strftime("%d/%m/%Y")
#    final.append(date_time)
#print(final)
scores_dict = {'Date':final_timestamp,'Content':all_str,
        'Discourse-Agreement_percentage':discourse(scores)[0],
        #"Agreement Percentage Difference":diff,
        'Discourse-Announcement_percentage':discourse(scores)[1],
        'Discourse-Answer_percentage':discourse(scores)[2],
        'Discourse-Appreciation_percentage':discourse(scores)[3],
        'Discourse-Disagreement_percentage':discourse(scores)[4],
        'Discourse-Elaboration_percentage':discourse(scores)[5],
        'Discourse-Humor_percentage':discourse(scores)[6],
        'Discourse-Negative_reaction':discourse(scores)[7],
        'Discourse-Question_percentage':discourse(scores)[8],
        'Discourse_Other_percentage':discourse(scores)[9],
        'Introvert(I)': intro_extro_func(intro_extro)[0] , 'Extrovert(E)':intro_extro_func(intro_extro)[1],
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
        }


print('\nConverting into dataframe......\n')
df = pd.DataFrame(scores_dict)
from joblib import dump, load
new_clf = load('depression_model.joblib') 
pred = new_clf.predict_proba(df["Content"])

df2=pd.DataFrame(new_clf.predict_proba(df["Content"]),columns=new_clf.classes_)
print(len(df))
print(len(df2))
print("Converted into dataframe")
frames=[df,df2]
result=pd.concat(frames,axis=1)
print("Converted into dataframe")

#print("************************************************************************************************************** \n")
#print(df)
username="Harleen"
'''
a_file = open(username+".json", "w")
json.dump(diff, a_file)
a_file.close()

a_file = open(username+".json", "r")
output = a_file.read()
print(output)
a_file.close()
'''

print('Converting into csv.......')
#os.chdir('data_score/')
result.to_csv('/var/www/html/data_score/'+'fb_posts_only_all_'+username + '.csv',index=False)
print('You can now download the data at /var/www/html/data_score/'+'fb_posts_only_all_'+ username+'.csv')
#print("\n\n")
'''
def display_avatar_top_elements(x):
        column_names=['Discourse-Agreement_percentage', 'Discourse-Announcement_percentage', 'Discourse-Answer_percentage', 'Discourse-Appreciation_percentage', 'Discourse-Disagreement_percentage', 'Discourse-Elaboration_percentage', 'Discourse-Humor_percentage', 'Discourse-Negative_reaction', 'Discourse-Question_percentage', 'Discourse_Other_percentage', 'Introvert(I)', 'Extrovert(E)', 'Judging(J)', 'Perceiving(P)', 'Feeling(F)', 'Thinking(T)', 'Sensing(S)', 'Intuition(I)', 'Flesch', 'Novelty Score', 'Novelty Ratio', 'Smog', 'Kincaid', 'Coleman', 'Readability', 'Dae Chall', 'Linsear Write', 'Gunning Fog', 'ENFJ - The Giver', 'ENFP - The Champion', 'ENTJ - The Commander', 'ENTP - The Debater', 'ESFJ - The Caregiver', 'ESFP - The Performer', 'ESTJ - The Director', 'ESTP - The Persuader', 'INFJ - The Advocate', 'INFP - The Mediator', 'INTJ - The Architect', 'INTP - The Thinker', 'ISFJ - The Protector', 'ISFP - The Artist', 'ISTJ - The Inspector', 'ISTP - The Crafter', 'agriculture_environment', 'arts_culture', 
        'business_industry', 'economics_finance', 'education_language', 'employment_labour', 'government_politics', 'health_safety', 'indigenous_affairs', 'information_communications', 'international_affairs', 'law_justice', 'science_technology', 'social_affairs']
        with open("/var/www/html/data_score/fb_posts_only_Harleen.csv",encoding="utf8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                date,content, *scores= row.values()
                if date in x:
                    print(date)
                    int_scores = [int(float(score)) for score in scores]
                    maxim=int_scores.index(max(int_scores))
                    maxim_val=max(int_scores)
                    print("Column is "+str(column_names[maxim])+" and score is "+str(maxim_val))

 
display_avatar_top_elements(final)

'''




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
