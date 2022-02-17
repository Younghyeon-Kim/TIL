# ML Modeling

### 머신 러닝 모델의 정석

| train            | evaluation       | test                                                   |
| ---------------- | ---------------- | ------------------------------------------------------ |
| 학습에 직접 관여 | 학습에 간접 관여 | 최종 평가 (**:star:전혀 사용되지 않은 데이터여야 함**) |

- optimal_depth를 찾을 때

​		`score(evaluation)`

- 최종 모델의 성능을 확인할 때

​		`score(test)`

- Cross Validation Test : Train과 Test를 교차 검증해봐야 함



### 조정 변수 (Hyper Parameter Tuning)

- KNN : K(최적 이웃)

- DT : depth

  의 결정을 위하여 evaluation을 사용한다.

  결과에 따라 최종 test로 모델의 성능을 평가한다.