# flask-QnA
QnA sites flask and python 

## 실행 방법
### 1. download source

### 2. 기본 python & Flask 설치
```
> # install python 3.8.5
> python -V 
python 3.8.5
> pip install Flask
> python -m pip install --upgrade pip
```

### 3. Flask 실행(개발환경)
```
> set FLASK_APP=pybo
> set FLASK_ENV=development
> flask run
```
- http://127.0.0.1:5000 접속
- 운영 환경으로 배포 시, `set FLASK_ENV=production` 반영

## AWS 접속 
- http://15.164.54.80/
  - 2022/07/23 기준 사용 가능