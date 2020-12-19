import dash
import plotly
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
import plotly.offline as pyo
import personality
from flask import Flask
from getpostsfromjson import get_postscount_and_posts,flesch,novelty_score,novelty_ratio,smog_index,text_standard,kincaid,coleman_liau,readability_index,dae_chall,linsear_write,gunning_fog
from vikash.app import json_file_session
json_file_session='your_posts_1.json'

timestamp1 = "Nov 12 2019"
timestamp2 = "Jan 15 2020"
if json_file_session:
  print("JSON_FILE_SESSION IS")
  print(json_file_session)
  print("calling get postscount_and_posts")
  count,postconcat,checkdate_list,scores,dictp=get_postscount_and_posts(json_file_session,timestamp1,timestamp2)
"""
flesch(scores)
novelty_score(scores)
novelty_ratio(scores)
smog_index(scores)
text_standard(scores)
kincaid(scores)
coleman_liau(scores)
readability_index(scores)
dae_chall(scores)
linsear_write(scores)
gunning_fog(scores)
"""
server=Flask(__name__)
@server.route('/')
def fleschf():
    pass
app=dash.Dash(__name__,server=server,routes_pathname_prefix='/flesch/')
app.layout=html.Div([
dcc.Graph(
figure={
    'data':[go.Scatter(x=checkdate_list,y=flesch(scores))],
    'layout':{'title':'Flesch Score'}
    })
    ])

@server.route('/')
def novelty_scoref():
    pass
app=dash.Dash(__name__,server=server,routes_pathname_prefix='/noveltyscore/')
app.layout=html.Div([
dcc.Graph(
figure={
    'data':[go.Scatter(x=checkdate_list,y=novelty_score(scores))],
    'layout':{'title':'Novelty Score'}
    })
    ])

@server.route('/')
def noveltyratiof():
    pass
app=dash.Dash(__name__,server=server,routes_pathname_prefix='/noveltyratio/')
app.layout=html.Div([
dcc.Graph(
figure={
    'data':[go.Scatter(x=checkdate_list,y=novelty_ratio(scores))],
    'layout':{'title':'Novelty Ratio'}

    })
    ])


@server.route('/')
def smogindexf():
    pass
app=dash.Dash(__name__,server=server,routes_pathname_prefix='/smogindex/')
app.layout=html.Div([
dcc.Graph(
figure={
    'data':[go.Scatter(x=checkdate_list,y=smog_index(scores))],
    'layout':{'title':'Smog Index'}

    })
    ])

@server.route('/')
def kincaidf():
    pass
app=dash.Dash(__name__,server=server,routes_pathname_prefix='/kincaid/')
app.layout=html.Div([
dcc.Graph(
figure={
    'data':[go.Scatter(x=checkdate_list,y=kincaid(scores))],
    'layout':{'title':'Kincaid'}

    })
    ])


@server.route('/')
def coleman_liauf():
    pass
app=dash.Dash(__name__,server=server,routes_pathname_prefix='/colemanliau/')
app.layout=html.Div([
dcc.Graph(
figure={
    'data':[go.Scatter(x=checkdate_list,y=coleman_liau(scores))],
    'layout':{'title':'Coleman Liau'}

    })
    ])


@server.route('/')
def readability_indexf():
    pass
app=dash.Dash(__name__,server=server,routes_pathname_prefix='/readabilityindex/')
app.layout=html.Div([
dcc.Graph(
figure={
    'data':[go.Scatter(x=checkdate_list,y=readability_index(scores))],
    'layout':{'title':'Readability Index'}

    })
    ])


@server.route('/')
def dae_challf():
    pass
app=dash.Dash(__name__,server=server,routes_pathname_prefix='/daechall/')
app.layout=html.Div([
dcc.Graph(
figure={
    'data':[go.Scatter(x=checkdate_list,y=dae_chall(scores))],
    'layout':{'title':'Dae-Chall'}

    })
    ])


@server.route('/')
def linsear_writef():
    pass
app=dash.Dash(__name__,server=server,routes_pathname_prefix='/linsearwrite/')
app.layout=html.Div([
dcc.Graph(
figure={
    'data':[go.Scatter(x=checkdate_list,y=linsear_write(scores))],
    'layout':{'title':'Linsear-Write'}

    })
    ])


@server.route('/')
def gunning_fogf():
    pass
app=dash.Dash(__name__,server=server,routes_pathname_prefix='/gunningfog/')
app.layout=html.Div([
dcc.Graph(
figure={
    'data':[go.Scatter(x=checkdate_list,y=gunning_fog(scores))],
    'layout':{'title':'Gunning Fog'}

    })
    ])


if __name__ =='__main__':
   app.run_server(host='0.0.0.0',port=6030)
