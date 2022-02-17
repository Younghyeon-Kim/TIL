# SVM (Support Vector Machine)



## 기본 개념

`Classification & Regression 가능`

- KNN Decision Boundary : 많은 test data로 확인
- D.T Boundary : 분기 지정 

- **SVM Decision Boundary**

  **마진** : 결정 경계선과 가장 가까운 훈련 샘플 데이터(**Support Vector**) 사이의 거리

  최대 마진 (마진이 가장 큰) 을 갖는 경계선으로 나눈다

  - case
    - 직선으로 완전히 분리가 가능한 경우
    - 직선으로 분리하지만 일부 오류를 허용하는 경우
    - 직선으로는 분리 불가, 곡선으로 분리하는 경우
    - 직선으로는 분리 불가, 곡선으로 분리하지만 일부 오류를 허용하는 경우 (**가장 많음**)



- SVM의 Hyper Parameter

  - gamma

    감마 값을 너무 키우면 Over fitting의 우려가 있다 (정규분포의 폭이 좁아짐)

  - C

  



- SVM은 **이진 분류 (Binary Classification)**용이다. 

  label or class가 [0, 1] 두 개인 경우

  - class 가 여러 개인 경우

    Classification을 여러 번

    ex ) [0, 1, 2]

    1. [0, others]

    2. [1, 2]



- 슬랙 변수 : 오류를 허용하는 직선

  오류를 허용하는 마진 : **소프트 마진 분류**



- :star:**C 값을 줄이면** 편향이 늘고 모델 분산이 줄어든다

  - 편향 : Bias
  - 분산 : Var

- kernel 함수

  - linear : 직선

  - rbf : 곡선

    (polynomial도 되나 rbf를 가장 많이 사용)