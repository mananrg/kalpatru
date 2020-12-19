import requests
import ast

def category_classifier(test_data):
    res=requests.get("https://api.uclassify.com/v1/frederick/commons_api/classify/?readKey=nwozo7alzWYKqGx2FkHr3BJk&text="+test_data)
    D2=ast.literal_eval(res.text)
    return D2


def intro_extro(test_data):
    res=requests.get("https://api.uclassify.com/v1/prfekt/myers-briggs-attitude/classify/?readKey=nwozo7alzWYKqGx2FkHr3BJk&text="+test_data)
    D2=ast.literal_eval(res.text)
    return D2

def judging_function(test_data):
    res=requests.get("https://api.uclassify.com/v1/prfekt/myers-briggs-judging-function/classify/?readKey=nwozo7alzWYKqGx2FkHr3BJk&text="+test_data)
    D2=ast.literal_eval(res.text)
    return D2

def lifestyle(test_data):
    res=requests.get("https://api.uclassify.com/v1/prfekt/myers-briggs-lifestyle/classify/?readKey=nwozo7alzWYKqGx2FkHr3BJk&text="+test_data)
    D2=ast.literal_eval(res.text)
    return D2


def perceiving_function(test_data):
    res=requests.get("https://api.uclassify.com/v1/prfekt/myers-briggs-perceiving-function/classify/?readKey=nwozo7alzWYKqGx2FkHr3BJk&text="+test_data)
    D2=ast.literal_eval(res.text)
    return D2

def type_indicator_analyzer(test_data):
    res=requests.get("https://api.uclassify.com/v1/g4mes543/myers-briggs-type-indicator-text-analyzer/classify/?readKey=nwozo7alzWYKqGx2FkHr3BJk&text="+test_data)
    D2=ast.literal_eval(res.text)
    return D2


