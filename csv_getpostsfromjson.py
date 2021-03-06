import pandas as pd
from getpostsfromjson import get_postscount_and_posts,flesch,novelty_score,novelty_ratio,smog_index,text_standard,kincaid,coleman_liau,readability_index,dae_chall,linsear_write,gunning_fog
from getpostsfromjson import type_indicator_analyze_func,intro_extro_func,judging_func,lifestyle_func,perceiving_func,category_classifier_func
from vikash.app import json_file_session

username="Achin"
json_file_session='your_posts_1.json'
timestamp1 = "Nov 12 2019"
timestamp2 = "Jan 15 2020"

print("\nCalling get postcount and posts.............\n")

if json_file_session:
    count,postconcat,checkdate_list,scores,dictp,intro_extro,judging_function,lifestyle,perceiving_function,type_indicator_analyzer,category_classifier=get_postscount_and_posts(json_file_session,timestamp1,timestamp2)


print('\nProcessing the data.......\n')
type_indicator_analyze_func(type_indicator_analyzer)


scores_dict = {'Date':checkdate_list,'Introvert(I)': intro_extro_func(intro_extro)[0] , 'Extrovert(E)':intro_extro_func(intro_extro)[1],
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
        'social_affairs':category_classifier_func(category_classifier)[13]

        }


print('\nConverting into dataframe......\n')
df = pd.DataFrame(scores_dict)


print("************************************************************************************************************** \n")
print(df)
print("\n**************************************************************************************************************")


print('Converting into csv.......')
#os.chdir('data_score/')
df.to_csv('/var/www/html/data_score/'+username + '.csv',index=False)
print('You can now download the data at /var/www/html/data_score/'+ username)

