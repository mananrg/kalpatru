import pandas as pd

import re

def googlesearch2df(username,html_file):
    with open(html_file, 'r') as f:
            file_content = f.read()
            #print(file_content)
    pattern=re.compile(r'<div class="content-cell mdl-cell mdl-cell--6-col mdl-typography--body-1">Searched for......ef="https://www.google.com/search\?q\=[\w\+\.\?\!\@\#\$\%\^\&\*\(\)\:\;\'\"\[\]\{\}\,\-\_\+\=\|\<\s]+>([\w\+\.\?\!\@\#\$\%\^\&\*\(\)\:\;\"\'\[\]\{\}\,\-\_\+\=\|\s]+)</a><br>(...\s+\d+,\s+\d+)')
    results=pattern.findall(file_content)
    print(results)
    print("*************************************************************")
    df = pd.DataFrame(results,columns=['Title','Timestamp'])
    print(df)
    print("*************************************************************")
    f.close()
    df.to_json(username+'_google_search_history.json',orient='records')
    print("Converting data into json")
    
#googlesearch2df("harleen","download.html")     

def googlevisited2df(username,html_file):
    with open(html_file, 'r') as f:
            file_content = f.read()
    pattern=re.compile(r'div class="content-cell mdl-cell mdl-cell--6-col mdl-typography--body-1">Visited.......f\=\"https\:\/\/www.google.com\/url\?q\=[\w\+\.\?\!\@\#\$\%\^\&\*\(\)\:\;\"\'\[\]\{\}\,\-\_\=\|\<\s\d\/]+>([\w\+\.\?\!\@\#\$\%\^\&\*\(\)\:\;"\'\[\]\{\}\,\-\_\+\=\|\<\s\d\â€“\.â€]+)</a><br>(...\s+\d+,\s+\d+)')
    results=pattern.findall(file_content)
    print("*************************************************************")
    print(results)
    df = pd.DataFrame(results,columns=['Title','Timestamp'])
    print(df)
    print("*************************************************************")
    f.close()
    df.to_json(username+'_google_visited_history.json',orient='records')
    print("Converting data into json")


#username="Harleen"
#file="my_activity.html"
#file="My ActivityAchin.html"
#googlevisited2df(username,file)
#googlesearch2df(username,file)
