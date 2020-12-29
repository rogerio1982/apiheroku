import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
#from sklearn import neighbors
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import accuracy_score
import pickle



#df = pd.read_csv('iris.csv')
dataset = pd.read_csv('iris.csv')
#input faetures
#X = df[['sepal_length','sepal_width','petal_length','petal_width']]

#output target
#y = df[['species']]

y = dataset.species #target coluna alvo
X = dataset.drop('species', axis=1) #todas ascolunas menos target

#train-test-split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=.5)

#model
model = LogisticRegression()

#model=neighbors.KNeighborsClassifier()
model.fit(X_train, y_train)

# Save the model as a pickle in a file
#joblib.dump(model, 'iris_trained_model.pkl')
# Saving model to disk
pickle.dump(model, open('iris_trained_model2.pkl','wb'))


# #load model
# with open('iris_trained_model.pkl', 'rb') as f:
#        model = joblib.load(f)

#prediction
#predictions=model.predict(X_test)
#print(predictions)
#print(accuracy_score(y_test,predictions)*100)
