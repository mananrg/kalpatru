import numpy as np
import pandas as pd
df = pd.read_csv('./DepressionDataset.csv')
df.head()

from sklearn.model_selection import train_test_split

X = df['Text']  
y = df['Label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)


from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer()

X_train_counts = count_vect.fit_transform(X_train)

from sklearn.feature_extraction.text import TfidfTransformer
tfidf_transformer = TfidfTransformer()

X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
X_train_tfidf.shape

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer()

X_train_tfidf = vectorizer.fit_transform(X_train) # remember to use the original X_train set
X_train_tfidf.shape

from sklearn.svm import LinearSVC
clf = LinearSVC()
clf.fit(X_train_tfidf,y_train)

#Building Pipeline
from sklearn.pipeline import Pipeline
text_clf = Pipeline([('tfidf', TfidfVectorizer()),
                     ('clf', LinearSVC()),])

text_clf.fit(X_train, y_train)  

#saving and loading the model
from joblib import dump, load
dump(text_clf, 'depression_model.joblib') 
new_clf = load('depression_model.joblib') 

# Form a prediction set
predictions = new_clf.predict(X_test)
print(predictions)
# Report the confusion matrix
from sklearn import metrics
print(metrics.confusion_matrix(y_test,predictions))
# Print a classification report

print(metrics.classification_report(y_test,predictions))
# Print the overall accuracy
#print(metrics.accuracy_score(y_test,predictions))


review="I am hopeless"
print(new_clf.predict([review])[0])
review2= "Getting anxious"
print(new_clf.predict([review2]))
print(new_clf.predict(["this anxiety"]))

#df['prediction']=df['Text'].apply(new_clf.predict)


