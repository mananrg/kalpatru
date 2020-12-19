import pandas as pd
import re

def google2df(username,html_file):
    with open(html_file, 'r') as f:
            file_content = f.read()
    #print(str_buff)
    #str_buff="Searched for  How to download google7 Oct 2002"
    pattern=re.compile(r'<div class="content-cell mdl-cell mdl-cell--6-col mdl-typography--body-1">Visited.......f\=\"https\:\/\/www.google.com\/url\?q\=[\w\+\.\?\!\@\#\$\%\^\&\*\(\)\:\;\"\'\[\]\{\}\,\-\_\=\|\<\s\d\/]+>([\w\+\.\?\!\@\#\$\%\^\&\*\(\)\:\;"\'\[\]\{\}\,\-\_\+\=\|\<\s\d\â€“\.â€]+)</a><br>(\d+\s...\s\d+)')
    #<a href\=\"https\:\/\/www.google.com\/url\?q\=[\w\+\.\?\!\@\#\$\%\^\&\*\(\)\:\;\"\'\[\]\{\}\,\-\_\=\|\<\s\d\/]+>
    #([\w\+\.\?\!\@\#\$\%\^\&\*\(\)\:\;"\'\[\]\{\}\,\-\_\+\=\|\<\s\d\â€“\.â€]+)</a><br>(\d+\s...\s\d+)
    #\<a href="https://www.google.com/search\?q\=[\w\+\.\?\!\@\#\$\%\^\&\*\(\)\:\;\'\"\[\]\{\}\,\-\_\+\=\|\<\s]+>([\w\+\.\?\!\@\#\$\%\^\&\*\(\)\:\;\"\'\[\]\{\}\,\-\_\+\=\|\<\s]+)</a><br>(\d+\s...\s\d+)
    #print(pattern)
        #phone=re.search(r'\d\s\w\w\w\s\d\d\d\d',x)
    #print(type(file_content))
    #x=str(str_buff)
    results=pattern.findall(file_content)
    print("*************************************************************")
    #dict_results=dict(results)
    #print(dict_results)
    #print(type(dict_results))
    print(results)
    df = pd.DataFrame(results,columns=['Title','Timestamp'])
    #df.set_index('Timestamp',inplace=True)
    print(df)
    #for index,row in df.iterrows():
     #   print(type(row['Title']))
    print("*************************************************************")
    f.close()
    df.to_json(username+'_google_search.json',orient='records')
    print("Converting data into json")


username="Achin"
file="My Activity.html"
google2df(username,file)

        
