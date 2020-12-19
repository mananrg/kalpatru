import textstat
import json
import numpy as np
import uclassify
import requests
import ast
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import return_scores_from_text_only_for_script_writing
  # X = input("Enter first string: ").lower()
    # Y = input("Enter second string: ").lower()
def cosined(x1,x2):
      X =x1.lower()
      Y =x2.lower()

      X_list = word_tokenize(X)
      Y_list = word_tokenize(Y)

                  # sw contains the list of stopwords
      sw = stopwords.words('english')
      l1 =[];l2 =[]

                              # remove stop words from string
      X_set = {w for w in X_list if not w in sw}
      Y_set = {w for w in Y_list if not w in sw}

                                            # form a set containing keywords of both strings
      rvector = X_set.union(Y_set)
      for w in rvector:
          if w in X_set: l1.append(1) # create a vector
          else: l1.append(0)
          if w in Y_set: l2.append(1)
          else: l2.append(0)
      c = 0
            # cosine formula
      for i in range(len(rvector)):
        c+= l1[i]*l2[i]
      cosine = c / float((sum(l1)*sum(l2))**0.5)
      return(1-cosine)

def jaccard_similarity(list1, list2):
        s1 = set(list1)
        s2 = set(list2)
        return len(s1.intersection(s2)) / len(s1.union(s2))
        
def f(mydict):
      return dict((k+"_Comparision",f(v) if hasattr(v,'keys') else v) for k,v in mydict.items())


def ret_scores_res(text,text_for_novelty_comparision_addition):
     test_data=text
     test_data2=text_for_novelty_comparision_addition
     score_flesch_reading_ease=textstat.flesch_reading_ease(test_data)
     y=return_scores_from_text_only_for_script_writing.ret_scores_res(test_data2)
     w=return_scores_from_text_only_for_script_writing.ret_scores_res(test_data)
     #score_flesch_reading_ease2=textstat.flesch_reading_ease(test_data2)
     score_smog_index=textstat.smog_index(test_data)
     score_kincaid_grade=textstat.flesch_kincaid_grade(test_data)
     scorecoleman_liau_index=textstat.coleman_liau_index(test_data)
     score_readability_index=textstat.automated_readability_index(test_data)
     score_dale_chall=textstat.dale_chall_readability_score(test_data)
     score_difficult_words=textstat.difficult_words(test_data)
     score_linsear_write=textstat.linsear_write_formula(test_data)
     score_gunning_fog=textstat.gunning_fog(test_data)
     score_text_standard=textstat.text_standard(test_data)
     novelty_score=len(set(test_data.split()))
     novelty_ratio=novelty_score/len(test_data.split())*100
     list1=list(set(test_data.split()))
     list2=text_for_novelty_comparision_addition.split()
     jc=jaccard_similarity(list1,list2)
     
     #nrwithcomparision=(1-jc)*100
     nrwithcomparision=cosined(test_data,text_for_novelty_comparision_addition)
     res=requests.get("https://api.uclassify.com/v1/uClassify/discourse/classify/?readKey=nwozo7alzWYKqGx2FkHr3BJk&text="+test_data)
     D2=ast.literal_eval(res.text)
     dict={}
     dict['flesch']=score_flesch_reading_ease
     if dict['flesch']>=90 and dict['flesch']<=100 :

       dict['flesch_interpretation']="Very Easy/5th grade/Easily understood by an average 11-year-old student."
     if dict['flesch']>=80 and dict['flesch']<=89 :
       dict['flesch_interpretation']="Easy/6th grade/ Conversational English for consumers" 

     if dict['flesch']>=70 and dict['flesch']<=79:
       dict['flesch_interpretation']="Fairly easy./7th grade"
     if dict['flesch']>=60 and dict['flesch']<=69:
       dict['flesch_interpretation']="8th & 9th grade./Standard/Plain English/ Easily understood by 13- to 15-year-old students"
     if dict['flesch']>=50 and dict['flesch']<=59:
       dict['flesch_interpretation']="Fairly Difficult/10th to 12th grade."
     if dict['flesch']>=30 and dict['flesch']<=49 :
       dict['flesch_interpretation']="Difficult to read / College."
     if dict['flesch']>=0 and dict['flesch']<=29 :
       dict['flesch_interpretation']="Very Confusing/Best understood by university graduates./College Graduate"
     if dict['flesch']<0 :
       dict['flesch_interpretation']="Negative.Not understandable easily by university graduates"
     if dict['flesch']>100 :
       dict['flesch_interpretation']="Greater than 100.Very very extremely easy for schools and universities both."
     #dict['novelty_score']=novelty_score
     dict['novelty_ratio']=novelty_ratio
     dict['novelty_ratio_interpretation']="Count(New words appearing / total words appearing)*100 Percent. This percentage has to be more and more if you want to claim copyright or be less repetetive in your written text. Example -> 'I am unique'. -> count of 'I'=1, count of 'am'=1, count of 'unique'=1 . Total words=3. Novelty ratio=1+1+1/3=100 percent"
     dict['novelty_score']=novelty_score

     dict['novelty_score_interpretation']="simply counts the number of new words appearing and takes it as the novelty score.Its called New Word Count Measure(by scientist Allan et al., discovered in 2003)" 
     dict['novelty_ratio_with_comparision']=nrwithcomparision
     #dict['novelty_ratio_with_comparision_interpretation']="In percentage.Novelty ratio of what you wrote in the editor * dissimilarity percentage of (what you wrote) and (reference content from google descriptiongs/your file/your url you provided.) To be a unique peace of writing comparable from internet or uploaded files or both, it has to be more and more but meaningful. "
     dict['novelty_ratio_with_comparision_interpretation']="Cosine distance between your written text and text from 3 inputs you gave. 1)google's descriptions of n pages or 2)url you provided or 3)file you uploaded or 4)all/any of the inputs. Cosine distance =1- cosine similarity. Cosine similarity is what you studied in dot product of a and b in school maths. If you are not satisfied with results, we can customize this formula based on your requirements and testing."
     dict['Discourse-Agreement_percentage']=D2['agreement']*100
     dict['Discourse-Announcement_percentage']=D2['announcement']*100
     dict['Discourse-Answer_percentage']=D2['answer']*100
     dict['Discourse-Appreciation_percentage']=D2['appreciation']*100
     dict['Discourse-Disagreement_percentage']=D2['disagreement']*100
     dict['Discourse-Elaboration_percentage']=D2['elaboration']*100
     dict['Discourse-Humor_percentage']=D2['humor']*100
     dict['Discourse-Negative_reaction']=D2['negative_reaction']*100
     dict['Discourse-Question_percentage']=D2['question']*100
     dict['Discourse_Other_percentage']=D2['other']*100
     dict['smog_index']=score_smog_index
     dict['smog_index_interpretation']="This is a grade formula in that a score of 9.3 means that a ninth grader would be able to read the document.Texts of fewer than 30 sentences are statistically invalid, because the SMOG formula was normed on 30-sentence samples. "
     dict['kincaid']=score_kincaid_grade
     dict['kincaid_interpretation']=" This is a grade formula in that a score of 9.3 means that a ninth grader would be able to read the document and so on."
     dict['coleman_liau']=scorecoleman_liau_index
     dict['coleman_liau_interpretation']="This is a grade formula in that a score of 9.3 means that a ninth grader would be able to read the document and so on."
     dict['readability_index']=score_readability_index
     dict['readability_index_interpretation']="Returns the ARI (Automated Readability Index) which outputs a number that approximates the grade level needed to comprehend the text.For example if the ARI is 6.5, then the grade level to comprehend the text is 6th to 7th grade."
     dict['dae_chall']=score_dale_chall

     if dict['dae_chall']<=4.9 :
        dict['dae_chall_interpretation']="Average 4th grade student or lower.This is Different from other tests, since it uses a lookup table of the most commonly used 3000 English words. Thus it returns the grade level using the New Dale-Chall Formula."
     if dict['dae_chall']>=5.0 and dict['dae_chall']<=5.9 :
        dict['dae_chall_interpretation']="average 5th or 6th-grade student.This is Different from other tests, since it uses a lookup table of the most commonly used 3000 English words. Thus it returns the grade level using the New Dale-Chall Formula."
     if dict['dae_chall']>=6.0 and dict['dae_chall']<=6.9 :
        dict['dae_chall_interpretation']="average 7th or 8th-grade students.This is Different from other tests, since it uses a lookup table of the most commonly used 3000 English words. Thus it returns the grade level using the New Dale-Chall Formula."
     if dict['dae_chall']>=7.0 and dict['dae_chall']<=7.9 :
        dict['dae_chall_interpretation']="average 9th or 10th-grade student..This is Different from other tests, since it uses a lookup table of the most commonly used 3000 English words. Thus it returns the grade level using the New Dale-Chall Formula."
     if dict['dae_chall']>=8.0 and dict['dae_chall']<=8.9 :
        dict['dae_chall_interpretation']="average 11th or 12th-grade student.This is Different from other tests, since it uses a lookup table of the most commonly used 3000 English words. Thus it returns the grade level using the New Dale-Chall Formula."
     if dict['dae_chall']>=9.0 and dict['dae_chall']<=9.9 :
        dict['dae_chall_interpretation']="average 13th to 15th-grade (college) student.This is Different from other tests, since it uses a lookup table of the most commonly used 3000 English words. Thus it returns the grade level using the New Dale-Chall Formula."

     dict['difficult_words']=score_difficult_words
     dict['difficult_words_interpretation']="This score is based on difficult words of language"
     dict['linsear_write']=score_linsear_write
     dict['linsear_write_interpretation']="This is a grade formula in that a score of 9.3 means that a ninth grader would be able to read the document.and so on"
     dict['gunning_fog']=score_gunning_fog 
     dict['gunning_fog_interpretation']="This is a grade formula in that a score of 9.3 means that a ninth grader would be able to read the document.and so on"
     dict['text_standard']=score_text_standard
     dict['text_standard_interpretation']="Based upon all the above tests, returns the estimated school grade level required to understand the text."
     
     x=json.dumps(dict)
     print("test 2 data's json response is")
     print(y)
     a=json.loads(w)
     b=json.loads(y)
     print("a is")

     print(a)
     print("b is")
     print(b)
     print("di is")
     #di={}
     #di['sex']='yes'
     di={}
     di=f(b)
     print(di)
     c={**a, **di }
     
     #c = {key: value for (key, value) in (a.items() + b.items())}
     #z=np.array([w,y])
     print("merged dictionary is")
     print(c)
     z=json.dumps(c)
     return(z)
