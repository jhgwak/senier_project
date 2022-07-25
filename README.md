# 졸업작품 프로젝트 입니다 

AI 학습을 이용하 인공지능 스마트팜

이 프로젝트는 실내 스마트팜이 아닌 노지스마트팜을 실용화 시킬 방법은 없을까 에서 온 프로젝트 입니다
노지 작물에서 충해로 인한 병해를막기위한 방법은 피해를 가장 많이 주는 벌래르 쫒아내는 것이라고 생각을 기반으로 시작하였습니다. 

노지작물에 피해르 많이 주느 나방종류를 중점으로 탐지와 트래킹을 하여 발견시 사용자에게 알림 서비스 제공 

이미지는 AI 허브에서 담배거세미 나방 이미지르 약 1000장을 사용
정확도가 조금 떨어지더라도 최대하 빠른 알고리즘이 필요하였다  

후보 : YOLO VS Haar Cascade VS HOG discriptor 알고리즘을 비교하여 선택 

YOLO : 정확도느 가장 높으나 속도가 가장 느림 
HOG discriptor : YOLO 보다 가벼우나 정확도가 가장 떨어짐 
Haar Cascade : 정확도가 HOG discriptor 보다 좋고 속도는 가장 빠름 --> 선택 
Haar Cascade 는 논문상으로는 200개의 특징만으로 90%의 정확도를 제공

1. Haar Feature Selection 
  Haar 특징을 계산 Haar Feature 은 4개의 사각형으로 구성된 하르특징은 대각선에 위치하 영역가 차이르 구함
2. Integral Images
  특징의 합을 구하느 과정 
3. Adaboost Traing
  특징추출중 대부분은 의미없는 특징이 추출된다 --> 최적의 특징을 찾기위해 모든 이미지에 특징으 적용후 임계값 설정후 계속반복
4. Cascade Classifier 
  특징 검출
  
 결과 
 
 <img width="630" alt="스크린샷 2021-11-04 오후 7 45 36" src="https://user-images.githubusercontent.com/88297412/180801380-da247b23-fc61-4c6b-af5b-512ebcfc7819.png">

<img width="543" alt="스크린샷 2021-11-04 오후 7 11 43" src="https://user-images.githubusercontent.com/88297412/180801418-078edf01-4a7b-4392-8e83-8ad92c7a6ed9.png">

