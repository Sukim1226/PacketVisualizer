# 졸업 프로젝트

## 1. 졸업 프로젝트 개요

*IoT 기기를 제어할때 네트워크 통신 상의 무결성을 검증하자. 이를 위해 각 통신 방식 별로 패킷을 수집하고, 이를 시각화 할 수 있는 프로그램을 제작해 패킷을 분석 해보자.*

<br/>


#### - Packet 수집 방식

스마트폰의 Smart things app을 통해 스마트 LED를 제어하고, 그 과정에서 발생하는 패킷들을 수집합니다.

패킷들은 Ble, Wifi, Zigbee 스마트 LED를 제어하는 세가지 방식에 따라 각각 수집하였습니다.

Ble와 Zigbee 통신은 Nordic Sniffer를 이용하여 수집하였고

Wifi 통신 패킷은 라즈베리 파이에 Open Wrt 펌웨어를 올려 무선 AP를 구성하고, AP에 Smart things hub와 스마트 폰을 연결한 뒤 수집했습니다. 라즈베리 파이로 들어오는 패킷들을 Wireshark SSH remote packet capture를 이용해 패킷들을 확인했습니다.



자세한 패킷 수집 방법은 메뉴얼화 하여 아래 구글 독스 링크로 첨부하겠습니다.

https://docs.google.com/document/d/1SUztSTuu6S8oWnLE1XN9kYI41vMQ5j6C6ZSl63t9p3I/edit?usp=sharing


<br/>

#### - Packet Visualize 방식

<img width="1437" alt="스크린샷 2020-10-11 오후 4 24 52" src="https://user-images.githubusercontent.com/5088280/95672777-895ab300-0bde-11eb-9d28-0548efe18143.png">



Python의 plotly 라이브러리를 이용하여, 패킷을 시각화 하였습니다. 수집한 패킷 파일은 WireShark에서 csv와 json 파일로 export 후에 불러와서 csv 파일을 통해 packet info를 불러오고, json 파일을 통해 packet 내부 value 값들을 불러왔습니다.

패킷의 색깔을 통해 종류를 구분했고, 자세한 정보를 보고 싶은 packet은 마우스를 hover 시키면 나오는 박스를 통해 확인할 수 있습니다.



------
<br/>

## 2. Packet Visualize 프로그램

#### - File Description

+ src/FileIO.py
  - json 파일과 csv 파일을 load/store 한다.<br/><br/>
  
+ src/Protocol.py 
  - ```def filter(self, protocol)```: 불러온 파일의 데이터를 프로토콜에 따라 필터링 한다.
  - ```def pack(self)```: GUI class에 건낼 데이터 패키지를 생성한다.
  - 아래는 Protocol의 child class이다.
  >+ src/WIFI.py : **class WF**
  >   - Description: Frame No. / Time / Src / Dst / Sequence / Next Sequence / Info
  >   - Color_key: TCP flag 값으로 색상 분류
  >+ src/ZigBee.py : **class ZB**
  >   - Description: Frame No. / Time / Sequence / Info / (Color)
  >   - Color_key: zbee_zcl 값으로 색상 분류 
  >+ src/BLE.py : **class BLE**
  >   - Description: Frame No. / Time / (Value) / (Request in Frame) / Info
  >   - Color_key: btatt.opcode 값으로 색상 분류

<br/>

+ src/GUI.py
  - ```def add(self, protocol_instance)```: Protocol class의 instance를 받아 정보를 저장한다.
  - ```def match_color(self, color_keys)```: color_keys dictionary와 랜덤 RGB 값을 매칭한다.
  - ```def make_figure(self, datas, color_keys, title)```: 하나의 Gantt chart figure를 생성한다.
  - ```def make_subplot(self)```: 여러 Gantt chart를 담는 subplot을 생성한다.
  - ```def show(self, cmd)```: cmd는 'WiFi', 'ZigBee', 'BLE' 중 하나이며 해당 protocol의 Gantt chart가 새 탭에 출력된다.

<br/>

+ main.py
  - Wi-Fi, ZigBee, BLE 파일명을 받아 instance를 생성하고 Packet Timeline Chart를 출력한다.<br/>

#### - Usage

```python
python main.py [BLE packet 파일 이름] [ZIGBEE packet 파일 이름] [WIFI packet 파일 이름]
# ex) python main.py 0920_BLE_Yurim 0928_zigbee1 0928_WiFi3_filtered
```

위의 명령어를 실행하면 브라우저에 각각의 패킷이 시각화된 화면이 3개의 탭으로 나타남.



<img width="1434" alt="스크린샷 2020-10-11 오후 4 24 24" src="https://user-images.githubusercontent.com/5088280/95672779-8a8be000-0bde-11eb-92f9-daf51d5f6a9b.png">
