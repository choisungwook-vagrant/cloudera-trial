# 개요
* 클라우데라 60일 평가판 설치를 위한 인프라 구성

<br>

# 준비
* virtualbox 설치
* vagrant 설치
* python 3.6이상 설치
* 충분한 CPU, 메모리, 디스크 용량
  * 권장 CPU: 4core 이상
  * 권장 메모리: 64GB 이상
  * 권장 디스크 용량: 200GB이상

<br>

# 설치방법
## 설정파일 생성
* config/Readme.md파일을 참고하여 설정파일 생성

## vagrant 플러그인 설치
```sh
vagrant plugin install vagrant-disksize
```

## vagrant 실행
```
vagrant up
```

## 웹 대시보드 설치
* putty같은 ssh client로 bootstrap 원격 접속
* sudo ./cloudera-manager-installer.bin
* 설치는 CUI로 진행
![](imgs/installing.png)

* 설치가 끝나면 웹 대시보드 접속(예: http://192.168.25.188:7180)
![](imgs/install_done.png)

* 라이센스가 없으므로 평가판 선택
![](imgs/license.png)
