# -*- coding: utf-8 -*-
"""AnalisisyPrediccionConMachineLearning.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1MZjmV1JqEN8NaLf4ilLPfFEX9YLhu8PO
"""

# Commented out IPython magic to ensure Python compatibility.
# importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

df = pd.read_csv('data.csv')

df.head()

df.shape

df.info()

df.columns

df.isnull().sum()

df.drop("Unnamed: 32", axis=1, inplace=True)

df.drop('id',axis=1, inplace=True)

df.describe()

plt.figure(figsize = (8,7))
sns.countplot(x="diagnosis", data=df, palette='magma')

plt.figure(figsize=(20,18))
#sns.heatmap(df.corr(), annot=True,linewidths=.5, cmap="Purples")

df.columns

# Getting Mean Columns with diagnosis
m_col = ['diagnosis','radius_mean', 'texture_mean', 'perimeter_mean',
       'area_mean', 'smoothness_mean', 'compactness_mean', 'concavity_mean',
       'concave points_mean', 'symmetry_mean', 'fractal_dimension_mean']

# Getting Se Columns with diagnosis
s_col = ['diagnosis','radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se',
       'compactness_se', 'concavity_se', 'concave points_se', 'symmetry_se',
       'fractal_dimension_se']

# Getting Worst column with diagnosis
w_col = ['diagnosis','radius_worst', 'texture_worst',
       'perimeter_worst', 'area_worst', 'smoothness_worst',
       'compactness_worst', 'concavity_worst', 'concave points_worst',
       'symmetry_worst', 'fractal_dimension_worst']

sns.pairplot(df[m_col],hue = 'diagnosis', palette='Blues')

# pairplot for se columns
sns.pairplot(df[s_col],hue = 'diagnosis', palette='Greens')

sns.pairplot(df[w_col],hue = 'diagnosis', palette='Oranges')

df['diagnosis'].value_counts()

df['diagnosis']=df['diagnosis'].map({'B':0,'M':1})

df['diagnosis'].value_counts()

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
                df.drop('diagnosis', axis=1),
                df['diagnosis'],
                test_size=0.2,
                random_state=42)

print("Shape of training set:", X_train.shape)
print("Shape of test set:", X_test.shape)

from sklearn.preprocessing import StandardScaler

ss = StandardScaler()
X_train = ss.fit_transform(X_train)
X_test = ss.fit_transform(X_test)

from sklearn.linear_model import LogisticRegression

logreg = LogisticRegression()
logreg.fit(X_train, y_train)
predictions1 = logreg.predict(X_test)

from sklearn.metrics import confusion_matrix, classification_report

print("Confusion Matrix: \n", confusion_matrix(y_test, predictions1))
print('\n')
print(classification_report(y_test, predictions1))

from sklearn.metrics import accuracy_score

logreg_acc = accuracy_score(y_test, predictions1)
print("Accuracy of the Logistic Regression Model is: ", logreg_acc)

from sklearn.neighbors import KNeighborsClassifier

error_rate = []

for i in range(1,42):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train, y_train)
    pred_i = knn.predict(X_test)
    error_rate.append(np.mean(pred_i != y_test))

plt.figure(figsize=(12,6))
plt.plot(range(1,42), error_rate, color='purple', linestyle="--",
         marker='o', markersize=10, markerfacecolor='b')
plt.title('Error_Rate vs K-value')
plt.show()

knn = KNeighborsClassifier(n_neighbors=9)
knn.fit(X_train, y_train)
predictions2 = knn.predict(X_test)

print(confusion_matrix(y_test, predictions2))
print("\n")
print(classification_report(y_test, predictions2))

knn_model_acc = accuracy_score(y_test, predictions2)
print("Accuracy of K Neighbors Classifier Model is: ", knn_model_acc)

from sklearn.ensemble import RandomForestClassifier

rfc = RandomForestClassifier(n_estimators=300)
rfc.fit(X_train, y_train)
predictions4 = rfc.predict(X_test)

print("Confusion Matrix: \n", confusion_matrix(y_test, predictions4))
print("\n")
print(classification_report(y_test, predictions4))

rfc_acc = accuracy_score(y_test, predictions4)
print("Accuracy of Random Forests Model is: ", rfc_acc)

from sklearn.svm import SVC

svc_model = SVC(kernel="rbf")
svc_model.fit(X_train, y_train)
predictions5 = svc_model.predict(X_test)

print("Confusion Matrix: \n", confusion_matrix(y_test, predictions5))
print("\n")
print(classification_report(y_test, predictions5))

svm_acc = accuracy_score(y_test, predictions5)
print("Accuracy of SVM model is: ", svm_acc)

print(logreg_acc)
print(knn_model_acc)
print(rfc_acc)
print(svm_acc)

plt.figure(figsize=(12,6))
model_acc = [logreg_acc, knn_model_acc, rfc_acc, svm_acc]
model_name = ['LogisticRegression', 'KNN', 'RandomForests', 'SVM']
sns.barplot(x= model_acc, y=model_name, palette='magma')

features = ['radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean', 'smoothness_mean',
            'compactness_mean', 'concavity_mean', 'concave points_mean', 'symmetry_mean', 'fractal_dimension_mean',
            'radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se',
            'compactness_se', 'concavity_se', 'concave points_se', 'symmetry_se', 'fractal_dimension_se',
            'radius_worst', 'texture_worst', 'perimeter_worst', 'area_worst', 'smoothness_worst',
            'compactness_worst', 'concavity_worst', 'concave points_worst', 'symmetry_worst', 'fractal_dimension_worst']

# Solicitar valores de entrada al usuario
user_input = []
for feature in features:
    value = float(input(f"Por favor, ingresa el valor de {feature}: "))
    user_input.append(value)

# Convertir la entrada del usuario en un array de NumPy para procesamiento
user_input = np.array([user_input])

user_input_scaled = ss.transform(user_input)

prediction = logreg.predict(user_input_scaled)

# Imprimir la clase predicha
print("La predicción para los datos ingresados es:", "Maligno" if prediction[0] == 1 else "Benigno")

import pickle

# Guardar el modelo de regresión logística
with open('logreg_model.pkl', 'wb') as file:
    pickle.dump(logreg, file)

# Guardar el modelo KNN
with open('knn_model.pkl', 'wb') as file:
    pickle.dump(knn, file)

# Guardar el modelo de Random Forest
with open('rfc_model.pkl', 'wb') as file:
    pickle.dump(rfc, file)

# Guardar el modelo SVM
with open('svm_model.pkl', 'wb') as file:
    pickle.dump(svc_model, file)

# También es importante guardar el StandardScaler
with open('scaler.pkl', 'wb') as file:
    pickle.dump(ss, file)