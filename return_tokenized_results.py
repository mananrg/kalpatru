import nltk
from nltk.tokenize import sent_tokenize

def ret_res(text):
  sent_tokenize_list = sent_tokenize(text)
  return (sent_tokenize_list)

def ret_len_res(text):
  sent_tokenize_list=sent_tokenize(text)
  y=len(sent_tokenize_list)
  return (y)
#x=ret_res("whats up. My name is chin. i am expecting this to be 3rd sentence. But you know what, i am confused.ok now tere was no space between full stop and next character.")

#print (x)
