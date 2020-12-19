import spacy
import json
from flask import Flask

nlp = spacy.load("en_core_web_sm")



app = Flask(__name__)

@app.route('/')
def index():
    pos_dic={}
    sent="Apple is looking at buying U.K. startup for $1 billion" 
    doc=nlp(sent)
    for token in doc:
        pos_dic[token.text]=token.pos_
    print(pos_dic)
    return json.dumps(pos_dic)

if __name__ =='__main__':
    app.run(host='0.0.0.0',port=5007)
