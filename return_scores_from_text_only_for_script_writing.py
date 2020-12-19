import textstat
import json
import uclassify
import requests
import ast
import personality
def ret_scores_res(text):
     test_data=text
     score_flesch_reading_ease=textstat.flesch_reading_ease(test_data)
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
     res=requests.get("https://api.uclassify.com/v1/uClassify/discourse/classify/?readKey=nwozo7alzWYKqGx2FkHr3BJk&text="+test_data)
     #print("response received from discourse classify uclassify api which is")
     #print(res.text)
     #data = {'texts': "the movie is really good."}
     #test_data=test_data.encode('utf-8')
     #test_data=test_data.encode("ascii", "ignore")
     #test_data=str(test_data)
     
     #decoded_string = test_data.encode().decode('unicode_escape')
     #res=requests.post('https://api.uclassify.com/v1/uclassify/discourse/classify', \
     #        data =  "{\"texts\": [\"  "+decoded_string+"\"]}", \
     #        headers = {'Authorization': 'Token ' + "nwozo7alzWYKqGx2FkHr3BJk"})
     print("response received is")
     print(res.text)
     D2=ast.literal_eval(res.text)
     D_intro_extro=personality.intro_extro(test_data)
     D_judging_function=personality.judging_function(test_data)
     D_lifestyle=personality.lifestyle(test_data)
     D_perceiving_function=personality.perceiving_function(test_data)
     
     res_wilber=requests.get("https://api.uclassify.com/v1/prfekt/voice-aqal-eng/classify/?readKey=nwozo7alzWYKqGx2FkHr3BJk&text="+test_data)
     #print(res_wilber.text)
     D3=ast.literal_eval(res_wilber.text)

     res_mbti_types=requests.get("https://api.uclassify.com/v1/g4mes543/myers-briggs-type-indicator-text-analyzer/classify/?readKey=nwozo7alzWYKqGx2FkHr3BJk&text="+test_data)
     D4=ast.literal_eval(res_mbti_types.text)
     #print(D4)
     #{"Personal UL":0.712463,"Philosophical LR":0.047937,"Practical UR":0.076761,"Social LL":0.162839}
     dict={}
     dict['Wilber AQAL model- Personal UL %']=D3['Personal UL']*100
     dict['Wilber AQAL model- Philosophical LR %']=D3['Philosophical LR']*100
     dict['Wilber AQAL model- Practical UR %']=D3['Practical UR']*100
     dict['Wilber AQAL model- Social LL %']=D3['Social LL']*100
     dict['Wilber AQAL model - Interpretation']="What parts of reality the author chooses to focus on. AQAL: quadrants. UL denotes Upper left quadrant. UR denotes Upper Right quadrant. LL denotes Lower left quadrant. LR denotes Lower Right quadrant.Wiki of theory of 4 quadrants- https://en.wikipedia.org/wiki/Integral_theory_(Ken_Wilber) . The class 'Personal UL' has been trained on 27202 features (words) whereof 7384 are unique. The class 'Philosophical LR' has been trained on 56561 features (words) whereof 13686 are unique. The class 'Practical UR' has been trained on 76606 features (words) whereof 16798 are unique. The class 'Social LL' has been trained on 53617 features (words) whereof 12721 are unique."
     dict['Myers Briggs model-Attitudes-percentages:Introvert(I) + Extrovert(E)']=""+str(D_intro_extro['Introversion']*100)+ "% + " + str(D_intro_extro['Extraversion']*100)+"%"



     dict['Myers Briggs model-Functions-percentages:Feeling(F) + Thinking(T)']=""+str(D_judging_function['Feeling']*100)+ "%  + " + str(D_judging_function['Thinking']*100)+"%"     
     dict['Myers Briggs model-Functions 2-percentages:Sensing(S) + iNtuition(N)']=""+str(D_perceiving_function['Sensing']*100)+ "% + " + str(D_perceiving_function['iNtuition']*100)+"%"


     dict['Myers Briggs model-Lifestyle Preferences-percentages:Judging(J) + Perceiving(P)']=""+str(D_lifestyle['Judging']*100)+ "% + " + str(D_lifestyle['Perceiving']*100)+"%"
    
     dict['Myers Briggs Interpretation']="Myers Briggs details of Attitudes, Functions, Lifestyle Preferences are located here : https://en.wikipedia.org/wiki/Myers%E2%80%93Briggs_Type_Indicator"
     #{'ENFJ': 0.0262952, 'ENFP': 0.0289212, 'ENTJ': 0.1472, 'ENTP': 0.0842695, 'ESFJ': 0.0282435, 'ESFP': 0.0261412, 'ESTJ': 0.0419099, 'ESTP': 0.079024, 'INFJ': 0.0693513, 'INFP': 0.0330037, 'INTJ': 0.12749, 'INTP': 0.0343322, 'ISFJ': 0.109142, 'ISFP': 0.0516871, 'ISTJ': 0.0828216, 'ISTP': 0.0301683}
     dict['MBTI - Keirsey temperaments - The Teacher or The Giver- ENFJ']=D4['ENFJ'] * 100
     dict['MBTI - Keirsey temperaments - The Champion - ENFP']=D4['ENFP'] * 100
     dict['MBTI - Keirsey temperaments - The FieldMarshal or The Commander - ENTJ']=D4['ENTJ'] * 100
     dict['MBTI - Keirsey temperaments - The Inventor - ENTP']=D4['ENTP'] * 100
     dict['MBTI - Keirsey temperaments - The Provider or The Caregiver - ESFJ']=D4['ESFJ'] * 100
     dict['MBTI - Keirsey temperaments - The Performer - ESFP']=D4['ESFP'] * 100
     dict['MBTI - Keirsey temperaments - The Supervisor or The Director - ESTJ']=D4['ESTJ'] * 100
     
     dict['MBTI - Keirsey temperaments - The Promoter or The Persuader- ESTP']=D4['ESTP'] * 100
     dict['MBTI - Keirsey temperaments - The Counsellor or The Advocate - INFJ']=D4['INFJ'] * 100
     dict['MBTI - Keirsey temperaments - The Healer or The Mediator- INFP']=D4['INFP'] * 100
     dict['MBTI - Keirsey temperaments - The Mastermind or The Architect - INTJ']=D4['INTJ'] * 100
     dict['MBTI - Keirsey temperaments - The Architect or The Thinker - INTP']=D4['INTP'] * 100
     dict['MBTI - Keirsey temperaments - The Protector - ISFJ']=D4['ISFJ'] * 100
     dict['MBTI - Keirsey temperaments - The Composer or The Artist - ISFP']=D4['ISFP'] * 100
     dict['MBTI - Keirsey temperaments - The Inspector - ISTJ']=D4['ISTJ'] * 100
     dict['MBTI - Keirsey temperaments - The Crafter - ISTP']=D4['ISTP'] * 100
     dict['MBTI - Keirsey temperaments - Interpretation']="Wiki : https://en.wikipedia.org/wiki/Myers%E2%80%93Briggs_Type_Indicator  or https://www.verywellmind.com/the-myers-briggs-type-indicator-2795583"
     


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
     return(x)
