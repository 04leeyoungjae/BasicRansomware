# 서버파일

## 모방 범죄 예방 차원에서 의도적인 취약점이 포함되어 있습니다.

### Apache2를 이용합니다.
### 사용 서버OS는 Raspberry Pi OS입니다.
### 사용법
/var/www/html 폴더에 파일을 저장합니다

### 파일설명
1. chat : 해커와 채팅할 수 있는 채팅사이트를 구성합니다.
2. chat.php : 채팅을 전송하는 기능을 구현합니다. id 정보가 특정한 hash값과 같다면 강조하는 기능을 포함합니다.
3. download.php : 바이러스를 다운로드 하는 기능을 구현합니다.
4. index.html : apache2의 기본 웹페이지입니다.
5. refresh.php : 채팅을 읽어오는 기능을 구현합니다.
6. write.php : 랜섬웨어에 사용한 키를 전송하는 기능을 구현합니다. 채팅과는 별도로 동작합니다.
