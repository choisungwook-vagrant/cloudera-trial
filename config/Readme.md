# 개요
vagrant를 실행하기 위한 설정파일(config.yml)을 생성하는 파이썬 스크립트

<br>

# 준비
* 파이썬 3.6 이상
* 파이썬 가상환경
* 파이썬 패키지 설치
```sh
(venv)$ pip install -r requirements.txt
```

<br>

# 설정파일 생성
* bootstrapIP: ansible-server IP
  * IP 1개만 입력
* controlPlaneIPS: 쿠버네티스 control-plane IP
  * IP 1개만 입력
* workerIPS: 쿠버네티스 worker IPS
  * IP 1개 이상 IP입력
```sh
python generate_config.py --bootstrapIP="192.168.25.170" --serverIPS="192.168.25.171,192.168.25.172,192.168.25.173"
```

* cloudera cpu, memory, disk size를 변경하고 싶은 경우
  * 메모리는 1024*xGB 형식으로 입력
```sh
python generate_config.py --bootstrapIP="192.168.25.170" --serverIPS="192.168.25.171,192.168.25.172,192.168.25.173" --serverCPU="2" --serverMemory="4096" --serverDisk="30GB"
```