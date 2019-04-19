# HaruHueyApis
HaruHueyApis Test Back-end @ Submit

### 개발 환경 및 기술 스택

Python 3.6 - Django 2.1<br/>
urllib3 / urllib5 / requests / beautifulsoup4 / psycopg2<br/>
Virtualenv<br/>
PostgreSQL 9.6<br/>
Visual Studio Code | PyCharm 2018.01<br/>

### 배포 환경

Google Cloud Platform ( GCP )<br/>
Compute Engine vCPU 1 / 0.6 GB Mem / HDD / Tokyo(asia-northeast1-b)<br/>
SQL PostgreSQL 9.6 / vCPU 1 / 0.6 GB Mem / HDD / Tokyo(asia-northeast1-a)<br/>
Debian 9 (stretch) Python 3.6 | NGINX · Gunicorn · Crontab(Django-Crontab) <br/>
https://apis.haruhuey.kr --> Cloudflare SSL · DNS<br/>

### Apis 기타 사항

기존 스마트채팅 API 코드를 기반으로 새로 진행 중인 프로젝트 입니다.<br/>
스마트채팅 API 기반 Back-end 서버에서 사용하던 코드들을 조금씩 수정하여<br/>
Django ORM과 Django-crontab을 연동하였고 현재 서버에 배포 된 버전이 아닌<br/>
수정을 위해 삭제 된 부분이 있는 코드입니다.<br/>
<br/>
교내 데이터 연동 모듈은 학교 상벌점 데이터 시트(구글 스프레드시트) 문제로 시험기간이<br/>
끝난 후 수정 후 모듈을 다시 제작하여 연동 할 계획입니다.<br/>
<br/>
commit 시간 기준 DB 데이터<br/>
급식 - 25<br/>
대기품질 - 884개<br/>
날씨 - 5804개<br/>
테스트 기간(현재) 로그 데이터 - 198개(KAKAO I) / 60개(구글 어시스턴트)
