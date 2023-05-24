import pandas as pd
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv('water_potability.csv')

x = data.drop("Potability", axis=1)
y = data["Potability"]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

dt = DecisionTreeClassifier()
param_grid = {
    'max_depth': [3, 5, 15, 31, 71, 51, 101],
    'min_samples_split': [3, 5, 7, 13, 15, 26, 37 ,51, 101],
    'min_samples_leaf': [13, 23, 41, 67, 75, 79, 81, 83, 150]
}

grid_search = GridSearchCV(dt, param_grid, cv=5, error_score='raise')
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy='mean')

imputer.fit(x_train)

x_train_imputed = imputer.transform(x_train)
x_test_imputed = imputer.transform(x_test)
grid_search.fit(x_train_imputed, y_train)


best_dt = grid_search.best_estimator_

import pickle

pickle.dump(best_dt,open('dsm.pkl','wb'))