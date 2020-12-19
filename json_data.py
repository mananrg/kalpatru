import pandas as pd
import json
from flask import Flask,jsonify
file_name='data_score/google_search_historyAchin.csv'

app=Flask(__name__)

@app.route('/')
def file():
    df=pd.read_csv('data_score/google_search_historyAchin.csv')
    adf = pd.DataFrame({'Date':df['Date'],'government_politics':df['government_politics']})
    adf.reset_index(drop=True, inplace=True)
    print(adf)
    print(type(adf))
    adf = adf.to_json()
    return json.dumps(adf)
if __name__ == '__main__':
   app.run(host='0.0.0.0',debug=True)
