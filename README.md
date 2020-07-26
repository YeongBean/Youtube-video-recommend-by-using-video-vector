# 비디오 벡터를 이용한 내용 기반 유튜브 영상 추천 시스템

## Intro
- 본 프로젝트의 내용을 다룬 논문은 2020KCC 학회지에 등재되어있습니다 (p1495).
- 본 프로젝트는 동영상에 어울리는 유튜브 태그와 관련 유튜브 영상을 추천해 주는 웹 서비스입니다.
- 유저가 영상을 업로드하면 기존 유튜브 영상들과의 유사성을 파악하여 가장 어울리는 태그와 연관된 유튜브 영상을 추천해 줍니다.
- 본 프로젝트는 박광훈 교수님의 **유튜브 동영상 분류를 위한 자동 태깅 방법에 대한 연구**에 기반하고 있습니다.
- 본 프로젝트에 사용된 데이터셋은 1/10 scaled yt8m 입니다.

## Research field
* Video Classification
* NLP
* Word Vectorization

## Tech Stack
* [Tensorflow](https://www.tensorflow.org/)
* [Gensim](https://radimrehurek.com/gensim/)
* [Django](https://www.djangoproject.com/)
* [Vue.js](https://kr.vuejs.org/v2/guide/index.html)

## Members
![profit_hunter](/img/profit_hunter.png)
* 팀명 **Profit Hunter**
* 윤영빈(컴퓨터공학과, 2015104192)
* 윤준현(컴퓨터공학과, 2015104193)
* 이현규(컴퓨터공학과, 2015104209)
* 이태현(컴퓨터공학과, 2015104208)

## Links
* [Youtube-8M Challenge](https://research.google.com/youtube8m/)
* [Mediapipe](https://github.com/google/mediapipe)

## Test
![test image1](/img/test1.png)
1. 슬라이드바를 이용해 출력 영상 링크의 갯수를 설정할 수 있습니다.
2. 드래그 앤 드롭으로 영상을 입력할 수 있습니다.

![test image2](/img/test2.png)
3. 출력은 입력 영상의 추천 태그들과 추천 영상들의 링크입니다.
4. 출력된 링크를 통해 유튜브 영상을 확인할 수 있습니다.
5. 예시는 금붕어가 있는 수족관 영상을 입력으로 사용한 

## How to run.
### 필요한 라이브러리 설치
1. git pull ssh://git@khuhub.khu.ac.kr:12959/2020-1-capstone-design1/PKH_Project1.git
2. python 3.5 ~ 3.7, node.js 12.16
3. google mediapipe 설치 https://google.github.io/mediapipe/getting_started/install
4. YouTube-8M feature extraction graph 설치 https://github.com/google/mediapipe/tree/master/mediapipe/examples/desktop/youtube8m (요구 사양 RAM 32GB 이상)
5. PKH_Project1/web/backend에서 requirements.txt 설치 (venv 사용 권장) -> pip install -r requirements.txt
6. PKH_Project1/web/frontend에서 package.json 설치 -> npm install

### 모델 학습
1. Train 
  - python train.py --frame_features --model=FrameLevelLogisticModel --feature_names='rgb,audio' --feature_sizes='1024,128' --train_data_pattern=/Train_데이터셋_저장경로/train*.tfrecord --train_dir PKH_Project1/web/backend/yt8m/esot3ria/model --start_new_model --segment_labels
2. Evaluation
  - python eval.py --eval_data_pattern=/Eval_데이터셋_저장경로/val*.tfrecord --train_dir PKH_Project1/web/backend/yt8m/esot3ria/model --run_once --segment_labels


### 웹서버 가동
#### 1~6의 절차가 반드시 완료되어 있어야 합니다.
- PKH_Project1/web/backend 디렉토리에서 
  - . env/bin/activate (가상환경 사용 시)
  - python manage.py makemigrations
  - python manage.py migrate
  - python manage.py runserver

#### front UI 수정하고 싶을 시, Vue의 사용법을 알아야합니다!

#### backend를 수정하고 싶을 시 django의 사용법을 알아야합니다!
