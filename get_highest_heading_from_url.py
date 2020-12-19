from  urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import re
import json
dict_of_heading_and_text={}
def get_headings(link_for_api_calls):
        try:
           reqs = requests.get(link_for_api_calls, timeout=10)
           soup = BeautifulSoup(reqs.text, 'lxml')
           #print("List of all the h1, h2, h3 :")
           i=0
           j=0
           for heading in soup.find_all(["h1", "h2", "h3"]):
                   #print(heading.name + ' ' + heading.text.strip())
                   heading_tag=heading.name
                   if "h1" in heading_tag :
                       i=i+1
                       dict_of_heading_and_text['h1_'+str(i)]=heading.text.strip()
                   if "h2" in heading_tag :
                       j=j+1
                       dict_of_heading_and_text['h2_'+str(j)]=heading.text.strip()
           #return(json.dumps(dict_of_heading_and_text))
        except:
           dict_of_heading_and_text['timeout']="link_timed_out_more_than_10_seconds"
           
        return(json.dumps(dict_of_heading_and_text))

                                
           #f = urlopen(link_for_api_calls)
           #htmlfile = str(f.read())
           #print(htmlfile)
           #print("----------------DOING THE PATTERN=RE.COMPILE BELOW THIS--------------OkOkOkOkOkOk------##########$$$$$$$$$$$$$$%%%%%%%%%%%%^^^^^-----------")
           #pattern=re.compile(r"'|<(h[^>]+)>(.*)</h[^>]+>|iU'")
           #list_of_tags_and_headings=pattern.findall(htmlfile)
           #for eachelement in list_of_tags_and_headings :
           #    if "h1" in eachelement[0]:
           #        print(eachelement[1])

               #if "h1" in eachelement[0]:
               #    print(eachelement[1])


#link_for_api_calls="https://www.republicworld.com/world-news/pakistan-news/pakistan-broadcast-corporation-snubbed-by-facebook-for-spreading-fake.html"

#print(get_headings(link_for_api_calls))
