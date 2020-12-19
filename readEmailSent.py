

from flask import Flask, request, render_template, jsonify

app = Flask(__name__)


@app.route('/getcsvfromemail', methods=['GET'])
def index():
    username = request.args.get('username')
    timestamp1 = request.args.get('timestamp1')
    timestamp2 = request.args.get('timestamp2')
    print(username, timestamp1, timestamp2)
    from googleapiclient.discovery import build
    from httplib2 import Http
    from oauth2client import file, client, tools
    import pandas as pd
    import json
    import personality
    import return_scores_from_text_only
    import personalitygetpostsfromjson
# https://codehandbook.org/how-to-read-email-from-gmail-api-using-python/
    SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'
    import datetime
    from getpostsfromjson import type_indicator_analyze_func, intro_extro_func, judging_func, lifestyle_func, perceiving_func, category_classifier_func, discourse
    from getpostsfromjson import flesch, novelty_score, novelty_ratio, smog_index, text_standard, kincaid, coleman_liau, readability_index, dae_chall, linsear_write, gunning_fog
    # print("11111111111111111111111111111111")
    dict_data = {}
    text_li = []
    timestamp_li = []
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('gmail', 'v1', http=creds.authorize(Http()))

    # Call the Gmail API to fetch INBOX
    results = service.users().messages().list(
        userId='me', labelIds=['SENT']).execute()
    messages = results.get('messages', [])
    # print(messages)

    if not messages:
        print("No messages found.")
    else:
        print("Message snippets:")

        for message in messages:
            # print("2222222222222222")
            msg = service.users().messages().get(
                userId='me', id=message['id']).execute()
            # print(msg['snippet'])
            # print(msg['internalDate'])
            # print(type(msg['internalDate']))
            text = msg['snippet']
            timestamp = msg['internalDate']
            your_dt = datetime.datetime.fromtimestamp(
                int(timestamp)/1000)  # using the local timezone
            # print(your_dt)
            # print(text)
            # print("*********************************************")
            # print(type(your_dt))
            your_dt = your_dt.strftime("%b %d %Y")
            # print(type(your_dt))
            # print("33333333333333")
            # print(your_dt)
            # print("***************************")
            # print(type(timestamp1))
            #print("type of your dt is",type(your_dt))
            #print("type of timestamp1 is",type(timestamp1))
            #print("timestamp 1 is ",timestamp1)
            #print("type of your timestamp2 is",type(timestamp2))
            #print("timestamp 2 is ",timestamp2)
            if (timestamp1 >= your_dt and timestamp2 <= your_dt):
                # print("444444444444")
                print(your_dt)
                print(text)
                print("*************************************************")
                text_li.append(text)
                timestamp_li.append(your_dt)
    # final_data={'Timestamp':timestamp_li,'title':text_li}
    # print(final_data)
    #print("length of timestamp li ",len(timestamp_li))
    #print("length of text li ",len(text_li))
    # return timestamp_li,text_li

    timestamp_list = timestamp_li
    text_list = text_li
    print(timestamp_list)
    print(text_list)
    i = 0
    checkdate_list = []
    judging_function = []
    lifestyle = []
    perceiving_function = []
    type_indicator_analyzer = []
    count_of_posts = 0
    str_to_return = []
    scores = []
    intro_extro = []
    category_classifier = []
    while(i < len(timestamp_list)):
        try:
            # print("1111111")
            string_for_api_calls = text_list[i]
            checkdate = timestamp_list[i]
            checkdate_list.append(checkdate)
            str_to_return.append(string_for_api_calls)
            #print("string is ",string_for_api_calls)
            # print("2222222222")
            scores.append(json.loads(
                return_scores_from_text_only.ret_scores_res(string_for_api_calls)))
            intro_extro.append((personality.intro_extro(string_for_api_calls)))
            judging_function.append(
                (personality.judging_function(string_for_api_calls)))
            lifestyle.append((personality.lifestyle(string_for_api_calls)))
            perceiving_function.append(
                (personality.perceiving_function(string_for_api_calls)))
            type_indicator_analyzer.append(
                (personality.type_indicator_analyzer(string_for_api_calls)))
            category_classifier.append(
                (personality.category_classifier(string_for_api_calls)))
            # print("333333")
        except:
            checkdate_list.remove(checkdate)
            str_to_return.remove(string_for_api_calls)
            print("Checkdate removed", checkdate)
            pass
        i += 1
    # print(str_to_return)
    print("type of date is ", type(checkdate_list))
    print("type of str is ", type(str_to_return))
    print("type of into extro is ", type(intro_extro_func(intro_extro)[0]))
    print('social_affairs is ', type(
        category_classifier_func(category_classifier)[13]))
    print(checkdate_list)
    # print(intro_extro_func(intro_extro)[0])
    # reverese_intro_extro=intro_extro_func(intro_extro)[0][::1]
    # print(reverese_intro_extro)
    scores_dict = {'Date': checkdate_list,
                   'Discourse-Agreement_percentage': discourse(scores)[0],
                   # "Agreement Percentage Difference":diff,
                   'Discourse-Announcement_percentage': discourse(scores)[1],
                   'Discourse-Answer_percentage': discourse(scores)[2],
                   'Discourse-Appreciation_percentage': discourse(scores)[3],
                   'Discourse-Disagreement_percentage': discourse(scores)[4],
                   'Discourse-Elaboration_percentage': discourse(scores)[5],
                   'Discourse-Humor_percentage': discourse(scores)[6],
                   'Discourse-Negative_reaction': discourse(scores)[7],
                   'Discourse-Question_percentage': discourse(scores)[8],
                   'Discourse_Other_percentage': discourse(scores)[9], 'Content': str_to_return, 'Introvert(I)': intro_extro_func(intro_extro)[0], 'Extrovert(E)': intro_extro_func(intro_extro)[1],
                   'Judging(J)': judging_func(judging_function)[0], 'Perceiving(P)': judging_func(judging_function)[1],
                   'Feeling(F)': lifestyle_func(lifestyle)[0], 'Thinking(T)': lifestyle_func(lifestyle)[1],
                   'Sensing(S)': perceiving_func(perceiving_function)[0], 'Intuition(I)': perceiving_func(perceiving_function)[1],
                   'Flesch': flesch(scores), 'Novelty Score': novelty_score(scores), 'Novelty Ratio': novelty_ratio(scores),
                   'Smog': smog_index(scores), 'Kincaid': kincaid(scores), 'Coleman': coleman_liau(scores), 'Readability': readability_index(scores),
                   'Dae Chall': dae_chall(scores), 'Linsear Write': linsear_write(scores), 'Gunning Fog': gunning_fog(scores),
                   'ENFJ - The Giver': type_indicator_analyze_func(type_indicator_analyzer)[0],
                   'ENFP - The Champion': type_indicator_analyze_func(type_indicator_analyzer)[1],
                   'ENTJ - The Commander': type_indicator_analyze_func(type_indicator_analyzer)[2],
                   'ENTP - The Debater': type_indicator_analyze_func(type_indicator_analyzer)[3],
                   'ESFJ - The Caregiver': type_indicator_analyze_func(type_indicator_analyzer)[4],
                   'ESFP - The Performer': type_indicator_analyze_func(type_indicator_analyzer)[5],
                   'ESTJ - The Director': type_indicator_analyze_func(type_indicator_analyzer)[6],
                   'ESTP - The Persuader': type_indicator_analyze_func(type_indicator_analyzer)[7],
                   'INFJ - The Advocate': type_indicator_analyze_func(type_indicator_analyzer)[8],
                   'INFP - The Mediator': type_indicator_analyze_func(type_indicator_analyzer)[9],
                   'INTJ - The Architect': type_indicator_analyze_func(type_indicator_analyzer)[10],
                   'INTP - The Thinker': type_indicator_analyze_func(type_indicator_analyzer)[11],
                   'ISFJ - The Protector': type_indicator_analyze_func(type_indicator_analyzer)[12],
                   'ISFP - The Artist': type_indicator_analyze_func(type_indicator_analyzer)[13],
                   'ISTJ - The Inspector': type_indicator_analyze_func(type_indicator_analyzer)[14],
                   'ISTP - The Crafter': type_indicator_analyze_func(type_indicator_analyzer)[15],
                   # 'Politics':category_classifier_func(category_classifier)
                   'agriculture_environment': category_classifier_func(category_classifier)[0],
                   'arts_culture': category_classifier_func(category_classifier)[1],
                   'business_industry': category_classifier_func(category_classifier)[2],
                   'economics_finance': category_classifier_func(category_classifier)[3],
                   'education_language': category_classifier_func(category_classifier)[4],
                   'employment_labour': category_classifier_func(category_classifier)[5],
                   'government_politics': category_classifier_func(category_classifier)[6],
                   'health_safety': category_classifier_func(category_classifier)[7],
                   'indigenous_affairs': category_classifier_func(category_classifier)[8],
                   'information_communications': category_classifier_func(category_classifier)[9],
                   'international_affairs': category_classifier_func(category_classifier)[10],
                   'law_justice': category_classifier_func(category_classifier)[11],
                   'science_technology': category_classifier_func(category_classifier)[12],
                   'social_affairs': category_classifier_func(category_classifier)[13]
                   }

    #print("intro extro",intro_extro_func(intro_extro)[0])
    #print("socail affairs",category_classifier_func(category_classifier)[13])

    print('\nConverting into dataframe......\n')
    df = pd.DataFrame(scores_dict)
    print("************************************************************************************************************** \n")
    print(df)
    print("\n**************************************************************************************************************")
    from joblib import dump, load
    new_clf = load('depression_model.joblib')
    pred = new_clf.predict_proba(df["Content"])

    df2 = pd.DataFrame(new_clf.predict_proba(
        df["Content"]), columns=new_clf.classes_)
    print("Converted into dataframe")
    frames = [df, df2]
    result = pd.concat(frames, axis=1)
    print('Converting into csv.......')

    filename = result.to_csv('/var/www/html/data_score/gmail_sent_' +
                             username + '_'+timestamp1+'_'+timestamp2+'.csv', index=False)
    print('You can now download the data at /var/www/html/data_score/gmail_sent_' +
          username + '_'+timestamp1+'_'+timestamp2+'.csv')

    filename_new = '/var/www/html/data_score/gmail_sent_' + \
        username + '_'+timestamp1+'_'+timestamp2+'.csv'

    print(filename_new)
    return jsonify(file_name=filename_new)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port="6101")
