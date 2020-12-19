import pandas as pd
import os
from getpostsfromjson import get_postscount_and_posts,flesch,novelty_score,novelty_ratio,smog_index,text_standard,kincaid,coleman_liau,readability_index,dae_chall,linsear_write,gunning_fog
json_file_session='your_posts_1.json'

timestamp1 = "Dec 12 2019"
timestamp2 = "Jan 15 2020"
count,postconcat,checkdate_list,scores,dictp=get_postscount_and_posts(json_file_session,timestamp1,timestamp2)
flesch=flesch(scores)
novelty_score=novelty_score(scores)
novelty_ratio=novelty_ratio(scores)
smog_index=smog_index(scores)
text_standard=text_standard(scores)
kincaid=kincaid(scores)
coleman_liau=coleman_liau(scores)
readability_index=readability_index(scores)
dae_chall=dae_chall(scores)
linsear_write=linsear_write(scores)
gunning_fog=gunning_fog(scores)
df = pd.DataFrame({'date':checkdate_list, 'flesch':flesch,'novelty_score':novelty_score,'novelty_ratio':novelty_ratio,'smog_index':smog_index,'text_standard':text_standard,'kincaid':kincaid,'coleman_liau':coleman_liau,'readability_index':readability_index,'dae_chall':dae_chall,'linsear_write':linsear_write,'gunning_fog':gunning_fog})
#os.chdir('dash-tutorial-master/data')
df.to_csv("dash-tutorial/data/population_il_cities.csv",index=False)
