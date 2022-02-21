# 선형 회귀

- 이상치 데이터(outlier)에 취약하다



### 추정치를 찾는 방법 (학습 방법)

1. 학습의 목표 : L = 전체 오차의 평균

   MSE (Mean Squared Error)

   - L (Loss function) : 목표 함수

   - 이 값을 최소화해야 한다

2. **MLE (Maximum Likelihood Estimation)** :star:

   MLE 최대화 = MSE 최소화

   ex) 숫자 1 ~ 500

   - unknown : `어떤 의도`를 가지고 숫자 몇개를 뽑는다

   - known : `16`, `64` (관측 사실)

   - 어떤 의도였을까?

     - 가능성이 가장 높은 가정을 찾는다. (maximize)

       L (우도함수) = 가능도 확률 (Likelihood probability)

       1. 짝수?
       2. < 100 ?
       3. 거듭제곱 ?



### 1. 단순 선형 회귀

- 하나의 feature와 연속적인 target 사이의 관계



### 2. 다중 선형 회귀

- 여러 개의 feature와 연속적인 target 사이의 관계



### 3. 성능 평가

1. 잔차 그래프 (residual plot)
2. `MSE` (평균 제곱 오차)
3. `R2` (결정 계수)



### 4. Regularization (규제) :star:

- Overfitting을 방지하기 위하여

  `Regularization term`

  - 제곱 : `Ridge` (L2)

  - 1차 : `LASSO` (L1)
  - `λ`(람다) : 규제의 강도
    - 람다 값이 커질수록 규제가 강해지고 모델 가중치 감소

  

  1. 릿지(Ridge) 회귀

     최소 제곱 비용 함수에 가중치의 제곱합을 추가

     `L2` : `MSE + Regularization term(Panalty)`

     - 특정 `w`가 과도하게 커지는 현상 방지

     - 특정 `w`가 과도하게 크면 ->  overfitting의 가능성

     - 그러나 `전체 MSE`가 약간 증가

  2. 라쏘(LASSO)

     `L1` 패널티는 모델 가중치의 절댓값의 합

  3. 엘라스틱 넷(Elastic Net)

     `Ridge`와 `LASSO`의 절충안

     `L1` 패널티, m > n 일 때에는 `L2` 패널티

