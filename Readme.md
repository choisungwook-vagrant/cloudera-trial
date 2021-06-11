# 개요
* 클라우데라 60일 평가판 설치를 위한 인프라 구성

<br>

# 준비
* virtualbox 설치
* vagrant 설치
* 충분한 CPU, 메모리, 디스크 용량
  * 권장 CPU: 4core 이상
  * 권장 메모리: 64GB 이상
  * 권장 디스크 용량: 200GB이상

<br>

# 설치방법
## 설정
* config/Readme.md파일을 참고하여 설정파일 생성

## 실행
```
vagrant up
vagrant ssh cloudrea1.network.com
```

## cloudrea설치
* 수동으로 평가판 버전 설치바이너리 실행
```
sudo su
sudo ./cloudera-manager-installer.bin
```

* 설치는 CUI로 진행
![](imgs/installing.png)

* 설치가 끝나면 접속페이지 제공
![](imgs/install_done.png)

예: http://192.168.25.188:7180/

## 라이센스 입력
* 라이센스가 없으므로 평가판 선택

![](imgs/license.png)

<br>

# vagrant가 설치하는 내용
> 참고자료: https://docs.cloudera.com/documentation/enterprise/latest/topics/installation_reqts.html#pre-install

* vagrant가 자동 설치 진행. 아래 목록은 설정 내용
  * 방화벽 비활성화
  * chrony 또는 ntp 설치
  * selinux 비활성화

<br>