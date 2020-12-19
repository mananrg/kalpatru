import plotly
import dash
import plotly.offline as pyo
import plotly.graph_objs as go
import dash_core_components as dcc
import dash_html_components as html
from copy_cloud_vision_api import start_processing
from datetime import date
from datetime import datetime


x,listp,scores ,str=start_processing()
print("********************************************************")
print("Length")
print(len(listp))
print(str)
dt=[]
dt_object=[]
dt_object1=[]
dt_object2=[]
dt=[1579453013, 1579354953, 1579251972]
dt_object = datetime.fromtimestamp(dt[0])
dt_object1 = datetime.fromtimestamp(dt[1])
dt_object2 = datetime.fromtimestamp(dt[2])
print(dt_object)
print(dt_object1)
print(dt_object2)

listp.append('Army')
listp.append('Wing Chun')
listp.append('Krav Maga')
scores.append(0.734566)
scores.append(0.5)
scores.append(0.8)
print('-'*100)
print(listp)
print('-'*100)
print(scores)
print('-'*100)
print(len(listp))
print(len(scores))
print('-'*100)
pre_list=['Krav Maga','Wing Chun','Army','Soldier','Military','Military Uniform','Gun','Military Officer','Marines','Military Person','Infantry','Military Organization','Law Enforcement','Action-adventure','Game','Soldier','Shooter Game','Army','Military','Gun','Professional Boxer','Combat Sport','Contact Sport','Striking Combat Sports','Mixed Martial Arts','Shootfighting','Strike','Punch','Wrestler','Professional Boxing','Boxing','Combat','Combat Sport','Contact Sport','Professional Boxer','Striking Combat Sports','Mixed Martial Arts','Strike','Muay Thai','Kick','Punch','Kickboxing','Shootfighting','Pradal Serey','Sanshou','Combat','Pankration','Shoot Boxing','Martial Arts','Wrestler','Professional Boxing','Lethwei','Rebellion','Protest','Police','Rebellion','Protest','Gun','Firearm','Assault Rifle','Rifle','Pradal Serey','Sanshou','Army']

def post_list(pre_list):
    x=list(dict.fromkeys(pre_list))
    print("*"*100)
    print("*"*100)
    print(x)
    print("*"*100)
    print("*"*100)
    print()
    return x
post_list=post_list(pre_list)

def data(pre_list,scores,listp): 
    dictx={}
    #listp=['Krav Maga','Wing Chun','Army','Law Enforcement','red']
    #scores=[5,6,7,8,2]
    for i in range(0,len(listp)):
        dictx[listp[i]]=scores[i]
    #print(dictx)
    list_labels=[]
    list_scores=[]
    for k,v in dictx.items():
        if k in pre_list:
            list_labels.append(k)
            list_scores.append(v)
    print("*"*100)
    print("*"*100)
    print("LABELS")        
    print(list_labels)
    print("-"*100)
    print("SCORES")
    print(list_scores)
    print("*"*100)
    print("*"*100)

    return list_labels,list_scores
#list_labels,list_scores=data(post_list,scores,listp)
#listp=['Krav Maga','Wing Chun','Army','Law Enforcement','red']
#scores=[5,6,7,8,2]
list_labels,list_scores=data(post_list,scores,listp)


data=go.Bar(x=list_labels,y=(dt_object,dt_object1,dt_object2),width=.30)
app=dash.Dash()
app.layout=html.Div([
        dcc.Graph(
        figure={
    'data':[data],
    'layout':{'title':'Mean World Syndrome'}
        }
        )
    ])
if __name__=='__main__':
    app.run_server(host='0.0.0.0',port=6020)

