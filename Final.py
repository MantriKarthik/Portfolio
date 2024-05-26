
# F1 Scores: Logistic Regression = 0.76, Random Forest = 0.76

import pandas as pd
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('car.csv')

labelencode = LabelEncoder()
df = df.apply(labelencode.fit_transform)

X = df[['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety']]
y = df['class']

X_train, X_test = X[:1000], X[1000:]
y_train, y_test = y[:1000], y[1000:]

model = LogisticRegression()

model.fit(X_train, y_train)

y_pred_model = model.predict(X_test)

f1_lr = f1_score(y_test, y_pred_model, average='weighted')

print('F1 Score (Logistic Regression):', f1_lr)

randomforest = RandomForestClassifier(n_estimators=250, criterion='gini')

param_grid = {'max_features': ['sqrt', 'log2', int(0.4*X_train.shape[1])]}

grid_search = GridSearchCV(randomforest, param_grid, cv=5)

grid_search.fit(X_train, y_train)

y_pred_randomforest = grid_search.predict(X_test)

f1_randomforest = f1_score(y_test, y_pred_randomforest, average='weighted')

print('F1 Score (Random Forest):', f1_randomforest)
