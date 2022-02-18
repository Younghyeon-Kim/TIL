# Colab

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

# feature 결정 과정

# data load 및 대략적인 data 확인
df = pd.read_csv('train.csv')
df.head()

df.info()

# 총 생존률
df['Survived'].sum() / 891

#Pclass 에 따른 생존률 비교 - 1 > 2 > 3
df[['Pclass', 'Survived']].groupby(['Pclass']).mean()

#Sex 에 따른 생존률 비교 - female > male
df[['Sex', 'Survived']].groupby(['Sex']).mean()

# SibSp 에 따른 생존률 비교 - 1, 2 : 동행이 적은 편이 살아남을 확률이 높다
df[['SibSp', 'Survived']].groupby(['SibSp']).mean().sort_values(by='Survived', ascending=False)

# Parch 에 따른 생존률 비교 - 3, 1, 2, 0 : 동행이 적을 수록 살아남을 확률이 높다
df[['Parch', 'Survived']].groupby(['Parch']).mean().sort_values(by='Survived', ascending=False)

#Embarked 에 따른 생존률 비교 - C에서 탑승한 승객의 생존률이 높음
df[['Embarked', 'Survived']].groupby(['Embarked']).mean()

#Age 에 따른 생존률 비교 - 유아의 생존율이 높고 
#범주화
ages = df['Age']
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
labels = ['유아', '10대', '20대', '30대', '40대', '50대', '60대', '70대', '80대']
cuts1 = pd.cut(ages, bins, right=False, labels=labels)
cuts1 = pd.DataFrame(cuts1)

conc1 = pd.concat([cuts1, df.loc[:, 'Survived':'Survived']], axis = 1)
conc1.groupby(['Age']).mean()

# Fare에 따른 생존률 비교 - 100달러 이상부터 생존률이 높아짐
fares = df['Fare']
# max(fares)

bins = [0, 100, 200, 300, 400, 500, 600]
labels = ['소액', '100달러 이상', '200달러 이상', '300달러 이상', '400달러 이상', '500달러 이상']
cuts2 = pd.cut(fares, bins, right=False, labels=labels)
cuts2 = pd.DataFrame(cuts2)

conc2 = pd.concat([cuts2, df.loc[:, 'Survived':'Survived']], axis = 1)
conc2.groupby(['Fare']).mean()

df.head()

# target과 관계성이 떨어지는 데이터들 drop
df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1, inplace=True)
df.head()

# obj인 dtype들 숫자로 변환
df['Sex'].replace(['female', 'male'], [0, 1], inplace=True)
df['Embarked'].replace(['C', 'Q', 'S'], [0 ,1, 2], inplace=True)

df.head()

# 결측값 확인 (179개)
df.isnull().sum()

# NaN 데이터 처리
# 1. 제거
# 2. 값 대체
# 제거하면 891 -> 712로 데이터가 너무 적어짐
# 값 대체로 진행

print(df['Age'].mean())     # 평균값
print(df['Age'].mode())     # 최빈값 둘이 비슷

# 평균값으로 대체
df['Embarked'].fillna(df['Embarked'].mean(), inplace=True)
df['Age'].fillna(df['Age'].mean(), inplace=True)

# 다시 결측값 유무 확인
df.isnull().sum()