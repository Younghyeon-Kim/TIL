# Desicion Tree (의사결정 나무)

##  종류

- Quinlan : ID3, C4.5

  잘 쓰지 않는다

- Beiman 등 : :star:`CART` (Classification And Regression Tree) :star:

  앞으로 배우게 될 내용

  `이진 트리 (Binary Tree)`라고 함

- Tree 가지 : ID3, C4.5 = 3개, CART = 2개

  

## :star:분기를 결정하기 위해서

1. `Entropy (평균 정보량)`
2. `Gini Index (지니 계수)`
3. `IG (정보 이득)`

**:star: Entropy (평균 정보량) :  `시그마(for문) P.log2(P)`**

​	`최소값 : 0, 최대값 : 1(class 2개)` >> `class >= 3, 최대값 > 1`

**:star: Gini Index (지니 계수)**

​	**`I = 1 - P`**

​	**`평균 I = 시그마 P(1 - P)`, `시그마 P - 시그마 P 제곱`, `1 - 시그마 P 제곱`**

---

순도 높다 : 무질서도 낮다, 엔트로피 낮다

순도 낮다 : 무질서도 높다, 엔트로피 높다

---



x의 분기 조건 판단하기

| x    | class |
| ---- | ----- |
| 1.0  | 0     |
| 1.2  | 1     |
| 3.5  | 2     |
| 2.8  | 0     |
| 2.2  | 1     |
| 1.2  | 2     |

​	x 의 중복을 제거 후 sort : [1.0  1.2  2.2  2.8  3.5]

​	중간의 평균 값 (분기 후보) : [1.1  1.7  2.5  3.15]

---

## 추가적으로

1. 실수 값의 경우 모든 후보(Brute force)들에 대해 계산

   계산량이 너무 많다 (오래 걸림)

- 계산량을 줄이려면

  - random(50%)
  - 통계 분포 등을 이용해 후보를 줄임

  그러나 근사적일 수 밖에 없고 권장되는 부분은 아님

2. Overfitting (과잉 적합)

   `'모델이 훈련데이터에 너무 잘 맞지만 일반성이 떨어진다'`는 의미

   훈련 데이터에 대해 높은 성능을 보여줌 >> 테스트 데이터에서도 높은 성능 보일 확률 적음

   훈련 데이터에 너무 맞추어졌기 때문에 훈련 데이터 이외의 다양한 변수에는 대응하기 힘듬

   모델의 복잡도가 필요 이상으로 높다.

   KNN : K가 너무 작을 경우

   D.T : Depth가 너무 크면

   

   Overfitting 해결 방법

   1. depth 제한 : optimal depth를 찾음
   2. 가지치기(Prune) 방법 : Pruning 알고리즘
      1. 사전 가지치기 : Pre-Pruning
         - 미리 depth의 수를 제한한다
      2. 사후 가지치기 : Post-Pruning
         - Tree를 최대한 깊게 만든다
         - Pruning - Bottom up 방식으로 필요 없는 부분은 병합 (Tree를 단순하게)
      3. Beiman's pruning : Cost Complexity Pruning (CCP)
         - `Cost = MSE + panalty|leaf node 수|`



3. :star:Importance of features (D.T의 장점)

   ex) 각 feature의 target 값에 대한 기여도를 IG, SDR = Importance

   `x1` = 3.8

   `x2` = 2.5

   `x3` = 1.8

   -> `x1`의 중요도가 가장 높다
