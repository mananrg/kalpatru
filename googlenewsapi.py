import requests
import dateutil.parser
from datetime import datetime
from flask import Flask
import pandas as pd


# app=Flask(__name__)

# @app.route('/')
def news():
#https://newsapi.org/docs/get-started
    url = ('http://newsapi.org/v2/top-headlines?'
       'language=en&'
       'apiKey=2a614474c05d4207961e16378b1d9253')

    response = requests.get(url).json()['articles']


    data_dict={}
    for i in response:
        date=dateutil.parser.parse(i['publishedAt']).strftime("%d-%m-%Y")
        data_dict[i['title']] = date
    
    # df = pd.DataFrame.from_dict(data_dict, orient='index',
    #                    columns=['Text', 'Date'])
    date=[x for x in data_dict.values()]
    title=[x for x in data_dict.keys()]
    # print(date)
    # print(title)
    return data_dict

# if __name__ == "__main__":
#     app.run(debug=True,host='0.0.0.0',port=2000)

#title , date
#title
#trolled  ,abused,employable ,education,health,travel,leisure,gender,racism, none