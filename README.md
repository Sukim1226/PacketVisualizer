# 졸업 프로젝트

### 1. 졸업 프로젝트 개요

*IoT 기기를 제어할때 네트워크 통신 상의 무결성을 검증하자. 이를 위해 각 통신 방식 별로 패킷을 수집하고, 이를 시각화 할 수 있는 프로그램을 제작해 패킷을 분석 해보자.*



##### - Packet 수집 방식

스마트폰의 Smart things app을 통해 스마트 LED를 제어하고, 그 과정에서 발생하는 패킷들을 수집합니다.

패킷들은 Ble, Wifi, Zigbee 스마트 LED를 제어하는 세가지 방식에 따라 각각 수집하였습니다.

Ble와 Zigbee 통신은 Nordic Sniffer를 이용하여 수집하였고

Wifi 통신 패킷은 라즈베리 파이에 Open Wrt 펌웨어를 올려 무선 AP를 구성하고, AP에 Smart things hub와 스마트 폰을 연결한 뒤 수집했습니다. 라즈베리 파이로 들어오는 패킷들을 Wireshark SSH remote packet capture를 이용해 패킷들을 확인했습니다.



자세한 패킷 수집 방법은 메뉴얼화 하여 아래 구글 독스 링크로 첨부하겠습니다.

https://docs.google.com/document/d/1SUztSTuu6S8oWnLE1XN9kYI41vMQ5j6C6ZSl63t9p3I/edit?usp=sharing



##### - Packet Visualize 방식

<img width="1424" alt="스크린샷 2020-10-11 오후 3 54 46" src="https://user-images.githubusercontent.com/5088280/95672433-b48fd300-0bdb-11eb-94d6-20b9be86864a.png">

Python의 plotly 라이브러리를 이용하여, 패킷을 시각화 하였습니다. 수집한 패킷 파일은 WireShark에서 csv와 json 파일로 export 후에 불러와서 csv 파일을 통해 packet info를 불러오고, json 파일을 통해 packet 내부 value 값들을 불러왔습니다.

패킷의 색깔을 통해 종류를 구분했고, 자세한 정보를 보고 싶은 packet은 마우스를 hover 시키면 나오는 박스를 통해 확인할 수 있습니다.



------

### 2. Packet Visualize 프로그램



- main.py
  - 
- src/WIFI.py
- src/BLE.py
- src/Zigbee.py
- src/FileIO.py
- src/Zigbee.py
- src/__init__.py
