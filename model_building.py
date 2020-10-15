import pandas as pd
import numpy as np

df = pd.read_csv('zillow_clean.csv')

#convert zipcode to str to make it a categorical variable (optional)
#df.zipcode = df['zipcode'].apply(lambda x: str(x))

#convert data to dummy by replacing categorical variables with binary variables 
#for each value
df_dum = pd.get_dummies(df)

#train test spli
from sklearn.model_selection import train_test_split
X = df_dum.drop(['price'], axis=1)
y = df_dum.price.values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

### build multiple models and compare them ###

#multiple linear regression
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score

lr = LinearRegression()
lr.fit(X_train, y_train)

np.mean(cross_val_score(lr, X_train, y_train, scoring='neg_mean_absolute_error', cv=3))

#random forest
from sklearn.ensemble import RandomForestRegressor

rf = RandomForestRegressor()
rf.fit(X_train, y_train)

np.mean(cross_val_score(rf, X_train, y_train, scoring='neg_mean_absolute_error', cv=3))

#support vector regressor
from sklearn.svm import SVR

svr = SVR()
svr.fit(X_train, y_train)

np.mean(cross_val_score(svr, X_train, y_train, scoring='neg_mean_absolute_error', cv=3))

#tuning models to find the best parameters

#from sklearn.model_selection import GridSearchCV

#parameters = {'n_estimators':range(10, 300, 10), 'criterion':('mse', 'mae')
#              , 'max_features':('auto', 'sqrt', 'log2')}

#gs = GridSearchCV(rf, parameters, scoring='neg_mean_absolute_error', cv=3)
#gs.fit(X_train, y_train)

#gs.best_score_
#gs.best_estimator_

#testing the different models

lr_pred = lr.predict(X_test)
rf_pred = rf.predict(X_test)
svr_pred = svr.predict(X_test)

from sklearn.metrics import mean_absolute_error

mean_absolute_error(y_test, lr_pred)
mean_absolute_error(y_test, rf_pred)
mean_absolute_error(y_test, svr_pred)



