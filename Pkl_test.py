import pickle
import pandas as pd
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

model=pickle.load(open('dsm.pkl','rb'))
data = pd.read_csv('water_potability.csv')

x = data.drop("Potability", axis=1)
y = data["Potability"]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy='mean')

imputer.fit(x_train)

x_train_imputed = imputer.transform(x_train)
x_test_imputed = imputer.transform(x_test)
y_pred = model.predict(x_test_imputed)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
print(x_test_imputed)