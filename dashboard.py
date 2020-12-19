from cloud_vision_api import start_processing
from flask import Flask,render_template
app=Flask(__name__)
#@app.route('/dashboard')
individual_dict_description=[]
individual_dict_score=[]
@app.route('/dashboard')
def dashboard():
   
   output=start_processing()
   print("____________________________________OUTPUT___________________________________")
   print(output)
   #individual_dict_description=[]
   #individual_dict_score=[]

   for i in output:
       try:  
           #   print(i['labelAnnotations'])
            for individual_dict in i['labelAnnotations']:
                individual_dict_description.append(individual_dict['description'])
                #print(individual_dict_description)
                individual_dict_score.append(individual_dict['score'])
                #print(individual_dict_score)


       except:
        print("Empty")
   #print("111111111")
   #print(individual_dict_description)
   #print(individual_dict_score)

   return render_template('dashboard.html',description_score=zip(individual_dict_description, individual_dict_score))
    #print(individual_dict_score)
    #print("222222")
#x,y=dashboard()     

#print(individual_dict_description)
#print(individual_dict_score)
if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0', port=5004)
#for eachelem in x:
#    print(eachelem)
#for eachelem in y:
#    print(eachelem)
