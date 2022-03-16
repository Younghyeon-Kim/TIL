# 텍스트 분류

## 1. 영어 텍스트 분류

|             |                                                              |
| ----------- | ------------------------------------------------------------ |
| 데이터 이름 | Bag of Words Meets Bags of Popcorn                           |
| 데이터 용도 | 텍스트 분류 학습을 목적으로 사용한다                         |
| 데이터 권한 | MIT 권한을 가지고 있으나 Kaggle에 가입한 후 사용하길 권장한다. |
| 데이터 출처 | [워드 팝콘](https://www.kaggle.com/c/word2vec-nlp-tutorial/data) |



### 1. 데이터 분석

- `EDA` : 탐색적 자료 분석

  1. 데이터 크기

  2. 데이터의 개수

  3. 각 리뷰의 문자 길이 분포

  4. 많이 사용된 단어

  5. 긍정, 부정 데이터의 분포

  6. 각 리뷰의 단어 개수 분포

  7. 특수문자 및 대문자, 소문자 비율

     

### 2. 데이터 전처리

- 데이터 정제
  1. HTML 및 문장 부호 제거
  2. 불용어 제거
  3. 단어 최대 길이 설정
  4. 단어 패딩
  5. 벡터 표상화



- 저장할 것

  1. 정제된 텍스트 데이터

  2. 벡터화한 데이터

  3. 정답 라벨

  4. 데이터 정보 (단어 사전, 전체 단어 개수)

     

### 3. 모델링
