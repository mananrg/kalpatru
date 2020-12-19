import return_scores_from_text_only
import pandas as pd
from datetime import datetime
import json
import personality

datastore = ""


def get_postscount_and_posts(json_file, timestamp1, timestamp2):
    with open(json_file) as f:
        datastore = json.load(f)
# print(datastore)
    i = 0
    category_classifier = []
    checkdate_list = []
    judging_function = []
    lifestyle = []
    perceiving_function = []
    type_indicator_analyzer = []
    count_of_posts = 0
    str_to_return = ""
    scores = []
    intro_extro = []
    len_datastore = len(datastore)
    while(i < len(datastore)):
        try:
            string_for_api_calls = datastore[i]["data"][0]["post"]
            #print("post is")
            # print(string_for_api_calls)
            time_stamp = datastore[i]["timestamp"]
            # print(time_stamp)
            #timestamp1 = "Dec 12 2019"
            #timestamp2 = "Jan 15 2020"
            check = datetime.fromtimestamp(time_stamp)
            print(check)
            t1 = datetime.strptime(timestamp1, "%b %d %Y")
            t2 = datetime.strptime(timestamp2, "%b %d %Y")
            t1date = t1.date()
            t2date = t2.date()
            checkdate = check.date()
            if checkdate > t1date:
                if checkdate < t2date:
                    s1 = checkdate.strftime("%m/%d/%Y")
                    checkdate_list.append(s1)
                    # print(checkdate_list)
                    count_of_posts = count_of_posts+1
                    # print("count",count_of_posts)
                    # str_to_return=str_to_return+"."+string_for_api_calls
                    str_to_return = string_for_api_calls
                    scores.append(json.loads(
                        return_scores_from_text_only.ret_scores_res(str_to_return)))
                    intro_extro.append(
                        (personality.intro_extro(str_to_return)))
                    judging_function.append(
                        (personality.judging_function(str_to_return)))
                    lifestyle.append((personality.lifestyle(str_to_return)))
                    perceiving_function.append(
                        (personality.perceiving_function(str_to_return)))
                    type_indicator_analyzer.append(
                        (personality.type_indicator_analyzer(str_to_return)))
                    category_classifier.append(
                        (personality.category_classifier(str_to_return)))

        except:
            #print("inside exception")
            pass
        i += 1
    dictp = {}
    for eachelem in checkdate_list:
        post_c = 0
        if checkdate_list.count(eachelem) > 1:
            dictp['post_c_associated_with' +
                  eachelem] = checkdate_list.count(eachelem)

    #print("dictionary associated with post count is")
    # print(dictp)
    # print(scores)
    # print("**"*64)
    # print("Into-Extro")
    # print(intro_extro)
    # print("--"*64)
    #print("judging function")
    # print(judging_function)
    # print("--"*64)
    # print("lifestyle")
    # print(lifestyle)
    # print("--"*64)
    #print("perceiving function")
    # print(perceiving_function)
    # print("--"*64)
    # print("type_indicator_analyzer")
    # print(type_indicator_analyzer)
    # print("**"*64)
    # print(len(str_to_return))
    # print(count_of_posts)

    return count_of_posts, str_to_return, checkdate_list, scores, dictp, intro_extro, judging_function, lifestyle, perceiving_function, type_indicator_analyzer, category_classifier


def discourse(scores):
    Discourse_Agreement_percentage = []
    Discourse_Announcement_percentage = []
    Discourse_Answer_percentage = []
    Discourse_Appreciation_percentage = []
    Discourse_Disagreement_percentage = []
    Discourse_Elaboration_percentage = []
    Discourse_Humor_percentage = []
    Discourse_Negative_reaction = []
    Discourse_Question_percentage = []
    Discourse_Other_percentage = []
    for i in scores:
        Discourse_Agreement = (i['Discourse-Agreement_percentage'])
        Discourse_Agreement_percentage.append(Discourse_Agreement)
        Discourse_Announcement = (i['Discourse-Announcement_percentage'])
        Discourse_Announcement_percentage.append(Discourse_Announcement)
        Discourse_Answer = (i['Discourse-Answer_percentage'])
        Discourse_Answer_percentage.append(Discourse_Answer)
        Discourse_Appreciation = (i['Discourse-Appreciation_percentage'])
        Discourse_Appreciation_percentage.append(Discourse_Appreciation)
        Discourse_Disagreement = (i['Discourse-Disagreement_percentage'])
        Discourse_Disagreement_percentage.append(Discourse_Disagreement)
        Discourse_Elaboration = (i['Discourse-Elaboration_percentage'])
        Discourse_Elaboration_percentage.append(Discourse_Elaboration)
        Discourse_Humor = (i['Discourse-Humor_percentage'])
        Discourse_Humor_percentage.append(Discourse_Humor)
        Discourse_Negative = (i['Discourse-Negative_reaction'])
        Discourse_Negative_reaction.append(Discourse_Negative)
        Discourse_Question = (i['Discourse-Question_percentage'])
        Discourse_Question_percentage.append(Discourse_Question)
        Discourse_Other = (i['Discourse_Other_percentage'])
        Discourse_Other_percentage.append(Discourse_Other)

    return Discourse_Agreement_percentage, Discourse_Announcement_percentage, Discourse_Answer_percentage, Discourse_Appreciation_percentage, Discourse_Disagreement_percentage, Discourse_Elaboration_percentage, Discourse_Humor_percentage, Discourse_Negative_reaction, Discourse_Question_percentage, Discourse_Other_percentage


def category_classifier_func(scores):
    x = ['agriculture_environment', 'arts_culture', 'business_industry', 'economics_finance', 'education_language', 'employment_labour', 'government_politics',
         'health_safety', 'indigenous_affairs', 'information_communications', 'international_affairs', 'law_justice', 'science_technology', 'social_affairs']
    df = pd.DataFrame(scores)
    # print('**************************************************************')
    # print(df)
    # print('**************************************************************')
    compile_list = [df[i].tolist() for i in x]
    agriculture_environment = compile_list[0]
    arts_culture = compile_list[1]
    business_industry = compile_list[2]
    economics_finance = compile_list[3]
    education_language = compile_list[4]
    employment_labour = compile_list[5]
    government_politics = compile_list[6]
    health_safety = compile_list[7]
    indigenous_affairs = compile_list[8]
    information_communications = compile_list[9]
    international_affairs = compile_list[10]
    law_justice = compile_list[11]
    science_technology = compile_list[12]
    social_affairs = compile_list[13]
    # print("******************************************")
    # print(agriculture_environment)
    return agriculture_environment, arts_culture, business_industry, economics_finance, education_language, employment_labour, government_politics, health_safety, indigenous_affairs, information_communications, international_affairs, law_justice, science_technology, social_affairs


def intro_extro_func(scores):
    intro = []
    extro = []
    for i in scores:
        x = (i['Extraversion'])
        extro.append(x)
        y = (i['Introversion'])
        intro.append(y)
    # print("INTRO")
    # print(intro)
    #print("Length of intro  : ",len(intro))
    # print("EXTRO")
    # print(extro)
    # print(len(extro))
    return intro, extro


def judging_func(scores):
    feeling = []
    thinking = []
    for i in scores:
        x = (i['Feeling'])
        feeling.append(x)
        y = (i['Thinking'])
        thinking.append(y)
    # print("Feeling")
    # print(feeling)
    # print(len(feeling))
    # print("Thinking")
    # print(thinking)
    # print(len(thinking))
    return feeling, thinking


def lifestyle_func(scores):
    judging = []
    perceiving = []
    for i in scores:
        x = (i['Judging'])
        judging.append(x)
        y = (i['Perceiving'])
        perceiving.append(y)
    # print("judging")
    # print(judging)
    # print(len(judging))
    # print("perceiving")
    # print(perceiving)
    # print(len(perceiving))
    return judging, perceiving


def perceiving_func(scores):
    sensing = []
    intuition = []
    for i in scores:
        x = (i['Sensing'])
        sensing.append(x)
        y = (i['iNtuition'])
        intuition.append(y)
    # print("sensing")
    # print(sensing)
    # print(len(sensing))
    # print("intuition")
    # print(intuition)
    # print(len(intuition))
    return sensing, intuition


def type_indicator_analyze_func(scores):
    x = ['ENFJ', 'ENFP', 'ENTJ', 'ENTP', 'ESFJ', 'ESFP', 'ESTJ', 'ESTP',
         'INFJ', 'INFP', 'INTJ', 'INTP', 'ISFJ', 'ISFP', 'ISTJ', 'ISTP']
    #ENFJ,ENFP,ENTJ,ENTP,ESFJ,ESFP,ESTJ,ESTP,INFJ,INFP,INTJ,INTP,ISFJ,ISFP,ISTJ,ISTP=([] for i in range(16))
    df = pd.DataFrame(scores)
    # print('**************************************************************')
    # print(df)
    # print('**************************************************************')
    compile_list = [df[i].tolist() for i in x]
    # for i in x:

    #     i=df[i].tolist()
    #     compile_list.append(i)

    #     return compile_list
    ENFJ = compile_list[0]
    ENFP = compile_list[1]
    ENTJ = compile_list[2]
    ENTP = compile_list[3]
    ESFJ = compile_list[4]
    ESFP = compile_list[5]
    ESTJ = compile_list[6]
    ESTP = compile_list[7]
    INFJ = compile_list[8]
    INFP = compile_list[9]
    INTJ = compile_list[10]
    INTP = compile_list[11]
    ISFJ = compile_list[12]
    ISFP = compile_list[13]
    ISTJ = compile_list[14]
    ISTP = compile_list[15]
    # print("*****************************************************")
    # print(ESFP)
    # print("*****************************************************")
    return ENFJ, ENFP, ENTJ, ENTP, ESFJ, ESFP, ESTJ, ESTP, INFJ, INFP, INTJ, INTP, ISFJ, ISFP, ISTJ, ISTP


def novelty_score(scores):
    li = []
    # print(scores)
    for i in scores:
        # prinat(i)
        try:
            #print("scores list is")
            x = (i['novelty_score'])
            # print('*'*60)
            li.append(x)
        except:
            print("Exception")

    #print("Novelty Score")
    # print(li)
    # print(len(li))
    return li


def text_standard(scores):
    li = []
    # print(scores)
    for i in scores:
        # prinat(i)
        try:
            #print("scores list is")
            x = (i['text_standard'])
            # print('*'*60)
            li.append(x)
        except:
            print("Exception")
    #print("Text Standard Score")
    # print(li)
    # print(len(li))
    return li


def novelty_ratio(scores):
    old_li = []
    li = []
    # print(scores)
    for i in scores:
        # prinat(i)
        try:
            #print("scores list is")
            x = (i['novelty_ratio'])
            # print('*'*60)
            old_li.append(x)
        except:
            print("Exception")
    #print("Novelty Ratio Score")
    # print(old_li)
    # print(len(old_li))
    return old_li


def readability_index(scores):
    li = []
    # print(scores)
    for i in scores:
        # prinat(i)
        try:
            #print("scores list is")
            x = (i['readability_index'])
            # print('*'*60)
            li.append(x)
        except:
            print("Exception")
    #print("Readability Index")
    # print(li)
    # print(len(li))
    return li


def flesch(scores):
    li = []
    # print(scores)
    for i in scores:
        # prinat(i)
        try:
            #print("scores list is")
            x = (i['flesch'])
            # print('*'*60)
            li.append(x)
        except:
            print("Exception")
    #print("Flesch Score")
    # print(li)
    # print(len(li))
    return li


def smog_index(scores):
    li = []
    # print(scores)
    for i in scores:
        # prinat(i)
        try:
            #print("scores list is")
            x = (i['smog_index'])
            # print('*'*60)
            li.append(x)
        except:
            print("Exception")
    #print("Smog Index")
    # print(li)
    # print(len(li))
    return li


def kincaid(scores):
    li = []
    # print(scores)
    for i in scores:
        # prinat(i)
        try:
            #print("scores list is")
            x = (i['kincaid'])
            # print('*'*60)
            li.append(x)
        except:
            print("Exception")
    # print("Kincaid")
    # print(li)
    return li


def coleman_liau(scores):
    li = []
    # print(scores)
    for i in scores:
        # prinat(i)
        try:
            #print("scores list is")
            x = (i['coleman_liau'])
            # print('*'*60)
            li.append(x)
        except:
            print("Exception")
    #print("Coleman Liau")
    # print(li)
    # print(len(li))
    return li


def readability_index(scores):
    li = []
    # print(scores)
    for i in scores:
        # prinat(i)
        try:
            #print("scores list is")
            x = (i['readability_index'])
            # print('*'*60)
            li.append(x)
        except:
            print("Exception")
    #print("Readability Index")
    # print(li)
    # print(len(li))
    return li


def dae_chall(scores):
    li = []
    # print(scores)
    for i in scores:
        # prinat(i)
        try:
            #print("scores list is")
            x = (i['dae_chall'])
            # print('*'*60)
            li.append(x)
        except:
            print("Exception")
    #print("Dae Chall")
    # print(li)
    # print(len(li))
    return li


def linsear_write(scores):
    li = []
    # print(scores)
    for i in scores:
        # prinat(i)
        try:
            #print("scores list is")
            x = (i['linsear_write'])
            # print('*'*60)
            li.append(x)
        except:
            print("Exception")
    #print("Linsear Write")
    # print(li)
    # print(len(li))
    return li


def gunning_fog(scores):
    li = []
    # print(scores)
    for i in scores:
        # prinat(i)
        try:
            #print("scores list is")
            x = (i['gunning_fog'])
            # print('*'*60)
            li.append(x)
        except:
            print("Exception")
    #print("Gunning Fog")
    # print(li)
    # print(len(li))
    return li


def post_count(date):
    """
    Input=Date list
    Output=PostCount and vivid dates from the date list
    """
    date_copy = date
    final_date_list = list(dict.fromkeys(date_copy))
    post_count = []
    for i in final_date_list:
        count = date.count(i)
        post_count.append(count)
        # print(len(count))
        # print(len(post_count))
    return final_date_list, post_count
# flesch(scores)
# novelty_score(scores)
# novelty_ratio(scores)
# smog_index(scores)
# text_standard(scores)
# kincaid(scores)
# coleman_liau(scores)
# readability_index(scores)
# dae_chall(scores)
# linsear_write(scores)
# gunning_fog(scores)
