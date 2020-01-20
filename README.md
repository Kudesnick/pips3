# pips3
connect bluetooth gamepad PS3 to raspberry pi zero w

## Preamble
��������

## Step 1 fist start
����� ��������� ������ �� ������ �������� � config.txt ������
~~~
# Enable UART console
enable_uart=1
~~~
��� �������� ���������� ������ ������� � ������� � ���������� UART. ������� ������ �� ����� ����� � ������� ������ ����������� USB/UART � ��������� ��������� - ��������, PuTTY.
��� ����������� USB/UART ����������� ������������ ��� ���� ������� GPIO: 8 - TX; 10 - RX; 9 - GND. �������� ��������� ������� ��������� �� �������� �������� 115200 ����/�, 8 ��� ��� ��������, 1 ���� ���.
������ �������� ����� ����������� �����, ��������� �����. ��� ������� � �������� ��������� 'init=/usr/lib/raspi-config/init_resize.sh' � ����� ���������� ��������� ������ 'cmdline.txt'. ������ �������� ��������� ������, ������� ��������� ���������������� ������ sd-����� �� ��� ��������� �������. ���� �� �� ������ ����� ������, ������ �������� ������� ������� �� ����� 'cmdline.txt' �� ������� ������� ����������.
��� ����������� ������� ������� ����� �������� ����� 6-7 ������.
����� �������� �������� ������� �� �������� ����������� ����� ������ � ������. �� ��������� - ��� ���� login: pi, password: raspberry. ������� ������ ����� �������� ��������
~~~
# passwd pi
~~~
���������� ������� � ������� ����������������� ��������� ������ ����������� �� ����������� ����� ������. � �� ��������� ��������� ������ �� ssh �� ����� ����� �������� ������� ������, �������� �� ����������. ������� ��� �� �������, ���� ����������� ������������ ��� ������� � ���������� ����������, �������� �� UART ).

## Step 2 connect gamepad
����� ��������� ��������� ����. ����� ����� ������������ � WiFi, �������� ����������������� ������� paspi-config. 
��������� ����������� ��������� ��������� �������������� � ��� ���, ��� � ���� ������ ������ ������� �� ����������� ���������. [����� ������ ������](http://www.pabr.org/sixlinux/sixlinux.en.html) ������������� ������ ����������� ������� ��� ����������� mac-������ ��������. ������, ��������� ������ ����� [Bluez](http://www.bluez.org/) ������������ ����� "��������������" ������ �����������. ��� ���������� �������� ����������� ����, ��� � ����� [�����](https://pimylifeup.com/raspberry-pi-playstation-controllers/) � [�����](https://raspberrypi.stackexchange.com/questions/75000/connecting-pi3-modelb-with-a-sony-ps3-dualshock-controller). �� ���� �� ���� �������� ���������� �� ���������� ���� �� ����, ���.
����, ��� ������, ������������� � ����������� ������ ������ � ������������� ����������.
~~~
# apt-get install bluetooth libbluetooth3
# systemctl enable bluetooth.service
# usermod -G bluetooth -a pi
# reboot
~~~
������ � ���������� ������������ bluetooth � ��������� ������������ �����:
~~~
# bluetoothctl
agent on
default-agent
scan on
~~~
����� ������ ���� �����:
~~~
# bluetoothctl
Agent registered
[bluetooth]# agent on
Agent is already registered
[bluetooth]# default-agent
Default agent request successful
[bluetooth]# scan on
Discovery started
[CHG] Controller B8:27:EB:F2:88:85 Discovering: yes
~~~
����� ����, ��� ���������� ������ ����������� ���� � �������� ���-�� �����:
~~~
[NEW] Device CE:5A:24:7B:A8:33 Mi Band 3
[NEW] Device E4:68:14:74:F4:77 Mi Band 3
[NEW] Device C8:F0:10:D0:13:4B Gear S3 (09A5) LE
[CHG] Device CE:5A:24:7B:A8:33 UUIDs: 0000fee0-0000-1000-8000-00805f9b34fb
[CHG] Device C8:F0:10:D0:13:4B RSSI: -99
~~~
���������� �������� ����� USB-OTG ������ � ���������� (������ �� ����� �� �� ��� �� ������ ������� �� USB ����). ���������� ����� ����� ���������:
~~~
[NEW] Device 18:33:C7:BB:52:2B Sony PLAYSTATION(R)3 Controller Authorize service
[agent] Authorize service 00001124-0000-1000-8000-00805f9b34fb (yes/no):
~~~
��������
~~~
yes
~~~
�����:
~~~
[CHG] Device 18:33:C7:BB:52:2B Trusted: yes
[CHG] Device 18:33:C7:BB:52:2B UUIDs: 00001124-0000-1000-8000-00805f9b34fb
[CHG] Device 18:33:C7:BB:52:2B Class: 0x00001f00
~~~
����������� USB ������. ���������, ��� �������� ���������� � �����������:
~~~
[CHG] Device 18:33:C7:BB:52:2B Connected: yes
[CHG] Device 18:33:C7:BB:52:2B Icon is nil
[Sony PLAYSTATION(R)3 Controller]#
~~~
���������� �� ��������� ������ ��������� ������, ��������� 1 ���������� ������, ������������ � ���, ��� ���������� ������ � ������. ������� �� bluetoothctl, ������ 'quit'.
��������, ��� �������� ������������ �������������. ��� ����� �������� ���������� � ��������, ���� ��� ���������� �� ��������� ��������. ����� ����� ������������� ���������� � �������� ��������, ����� ������ 'PS3'. ���������� ��������� ����� ���������, � ����� ��������� ��������� ����� 1. �������� �������
~~~
$ ls /dev/input
~~~
� ��������, ��� � ������� ������� ���������� js0 - ��� � ���� ��� �������.

## Step 3 gamepad testing
��� �������� ��������� �������� �������:
~~~
# apt install joystick
$ jstest /dev/input/js0
~~~
������ ��������� �����:
~~~
Driver version is 2.1.0.
Joystick (Sony PLAYSTATION(R)3 Controller) has 6 axes (X, Y, Z, Rx, Ry, Rz)
and 17 buttons (BtnA, BtnB, BtnX, BtnY, BtnTL, BtnTR, BtnTL2, BtnTR2, BtnSelect, BtnStart, BtnMode, BtnThumbL, BtnThumbR, (null), (null), (null), (null)).
Testing ... (interrupt to exit)
Axes:  0:     0  1:     0  2:-32767  3:     0  4:     0  5:-32767 Buttons:  0:off  1:off  2:off  3:off  4:off  5:off  6:off  7:off  8:off  9:off 10:off 11:off 12:off 13:off 14:off 15:off 16:off
~~~
�������� � ��������� ������ ����� ����������� ���������� ��� ������� �� ��������������� ������ ���������. ��� ������ �� ����� �������������� ����������� ����������� ctl+C.

## Step 4 bye USB/UART bridge!
������, ����� �������� �� ������� ����������� �� USB ����� ���������� ������� �� USB ����, ��������������� ��� ��� ����������� COM-����. ��� ����� � ����� 'config.txt' ������� ������:
~~~
# Enable USB UART console
dtoverlay=dwc2
~~~
� � 'cmdline.txt' ����� ��������� 'rootwait' ������� 'modules-load=dwc2,g_serial'. �� ������������� ����. ���� �� ������������ ���������� � ��������� ��� � �� ����� USB ������, �� ������, ��� COM ���� ��������, �� � ���� ������ �� ������������ � �� �����������, �� ������ �� ��, ��� �� ��������� ���� ���������: �������� �������� 115200 ����/�, 8 ��� ��� ��������, 1 ���� ���. �� ����� ��������� ��������, ������� �� �������, ������������� ����� USB/UART ����������, ����� ������� �������� �������:
~~~
sudo systemctl enable getty@ttyGS0.service
~~~
����� � ���������� USB/UART ���������� ����� ��������� � ������������� ����������. ����� �� ������� � �� ������ ����� �������. � ��� �������� - ��� ������� - �����!
