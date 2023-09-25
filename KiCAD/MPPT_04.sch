EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Amplifier_Current:INA168 U3
U 1 1 64913EAB
P 8925 1875
F 0 "U3" H 9050 2150 50  0000 L CNN
F 1 "INA169" H 8950 2075 50  0000 L CNN
F 2 "Package_TO_SOT_SMD:SOT-23-5" H 8925 1875 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/ina138.pdf" H 8925 1880 50  0001 C CNN
	1    8925 1875
	0    -1   1    0   
$EndComp
$Comp
L Device:R R8
U 1 1 64913EB5
P 8925 1250
F 0 "R8" V 8825 1225 50  0000 L CNN
F 1 "Rshunt" V 9050 1125 50  0000 L CNN
F 2 "" V 8855 1250 50  0001 C CNN
F 3 "~" H 8925 1250 50  0001 C CNN
	1    8925 1250
	0    -1   1    0   
$EndComp
$Comp
L Device:R R9
U 1 1 64913EBF
P 8925 2525
F 0 "R9" H 8995 2571 50  0000 L CNN
F 1 "Rout" H 8995 2480 50  0000 L CNN
F 2 "" V 8855 2525 50  0001 C CNN
F 3 "~" H 8925 2525 50  0001 C CNN
	1    8925 2525
	-1   0    0    -1  
$EndComp
$Comp
L power:GNDD #PWR06
U 1 1 64913EC9
P 9225 1925
F 0 "#PWR06" H 9225 1675 50  0001 C CNN
F 1 "GNDD" H 9229 1770 50  0001 C CNN
F 2 "" H 9225 1925 50  0001 C CNN
F 3 "" H 9225 1925 50  0001 C CNN
	1    9225 1925
	-1   0    0    -1  
$EndComp
$Comp
L power:GNDD #PWR05
U 1 1 64913ED3
P 8925 3075
F 0 "#PWR05" H 8925 2825 50  0001 C CNN
F 1 "GNDD" H 8929 2920 50  0001 C CNN
F 2 "" H 8925 3075 50  0001 C CNN
F 3 "" H 8925 3075 50  0001 C CNN
	1    8925 3075
	-1   0    0    -1  
$EndComp
Wire Wire Line
	8925 2175 8925 2250
Wire Wire Line
	8775 1250 8775 1575
Wire Wire Line
	8775 1575 8825 1575
Wire Wire Line
	9075 1250 9075 1575
Wire Wire Line
	9075 1575 9025 1575
Wire Wire Line
	9225 1775 9225 1925
Text GLabel 8550 1775 0    50   Input ~ 0
+5V
Wire Wire Line
	8550 1775 8625 1775
Connection ~ 8775 1250
$Comp
L Connector:Conn_01x01_Female J8
U 1 1 64913EF1
P 9475 1250
F 0 "J8" H 9367 1025 50  0001 C CNN
F 1 " " H 9367 1116 50  0001 C CNN
F 2 "" H 9475 1250 50  0001 C CNN
F 3 "~" H 9475 1250 50  0001 C CNN
	1    9475 1250
	1    0    0    -1  
$EndComp
Wire Wire Line
	9275 1250 9075 1250
Connection ~ 9075 1250
Text GLabel 9100 2250 2    50   Input ~ 0
VI2
Wire Wire Line
	9100 2250 8925 2250
Connection ~ 8925 2250
Wire Wire Line
	8925 2250 8925 2375
$Comp
L Device:R R6
U 1 1 64913F0B
P 8025 1850
F 0 "R6" H 8095 1896 50  0000 L CNN
F 1 "20k" H 8095 1805 50  0000 L CNN
F 2 "" V 7955 1850 50  0001 C CNN
F 3 "~" H 8025 1850 50  0001 C CNN
	1    8025 1850
	1    0    0    -1  
$EndComp
$Comp
L Device:R R7
U 1 1 64913F15
P 8025 2400
F 0 "R7" H 8095 2446 50  0000 L CNN
F 1 "1k" H 8095 2355 50  0000 L CNN
F 2 "" V 7955 2400 50  0001 C CNN
F 3 "~" H 8025 2400 50  0001 C CNN
	1    8025 2400
	1    0    0    -1  
$EndComp
Wire Wire Line
	8025 1700 8025 1250
Connection ~ 8025 1250
Wire Wire Line
	8025 1250 8775 1250
Wire Wire Line
	8025 2000 8025 2125
Wire Wire Line
	8025 2550 8025 3000
$Comp
L Connector:Conn_01x01_Female J7
U 1 1 64929EAD
P 9450 3000
F 0 "J7" H 9342 2775 50  0001 C CNN
F 1 " " H 9342 2866 50  0001 C CNN
F 2 "" H 9450 3000 50  0001 C CNN
F 3 "~" H 9450 3000 50  0001 C CNN
	1    9450 3000
	1    0    0    -1  
$EndComp
Wire Wire Line
	9250 3000 8925 3000
Connection ~ 8025 3000
Text GLabel 8125 2125 2    50   Input ~ 0
VU2
Wire Wire Line
	8125 2125 8025 2125
Connection ~ 8025 2125
Wire Wire Line
	8025 2125 8025 2250
$Comp
L Raspi_Pico:Pico U7
U 1 1 6495EACA
P 6125 4725
F 0 "U7" H 6125 5940 50  0000 C CNN
F 1 "Pico" H 6125 5849 50  0000 C CNN
F 2 "RPi_Pico:RPi_Pico_SMD_TH" V 6125 4725 50  0001 C CNN
F 3 "" H 6125 4725 50  0001 C CNN
	1    6125 4725
	1    0    0    -1  
$EndComp
$Comp
L oled:SH1106 U6
U 1 1 6495EAD0
P 4050 4875
F 0 "U6" H 3720 4971 50  0000 R CNN
F 1 "SH1106" H 3720 4880 50  0000 R CNN
F 2 "" H 4050 4375 50  0001 C CNN
F 3 "" H 4000 3975 50  0001 C CNN
	1    4050 4875
	1    0    0    -1  
$EndComp
Text Notes 4975 4875 0    50   ~ 0
I2C SCL
Text Notes 4975 4775 0    50   ~ 0
I2C SDA
Wire Wire Line
	4450 4975 4650 4975
Wire Wire Line
	4050 5275 4050 5325
Text GLabel 3950 4325 0    50   Input ~ 0
+3V3
Wire Wire Line
	3950 4325 4050 4325
Wire Wire Line
	4050 4325 4050 4375
Text Notes 2775 5300 0    50   ~ 0
I2C pullups on breakout boards
$Comp
L power:GNDD #PWR08
U 1 1 649AC3D3
P 4050 5325
F 0 "#PWR08" H 4050 5075 50  0001 C CNN
F 1 "GNDD" H 4054 5170 50  0001 C CNN
F 2 "" H 4050 5325 50  0001 C CNN
F 3 "" H 4050 5325 50  0001 C CNN
	1    4050 5325
	1    0    0    -1  
$EndComp
Text Notes 8125 1000 0    50   ~ 0
Rshunt = 10mOhm\nRout = 10k  (is already on breakout board)\nfor 30A range
Text Notes 7425 7500 0    50   ~ 0
Solar stepup converter
Wire Wire Line
	5175 3175 5175 4175
Wire Wire Line
	5175 4175 5425 4175
$Comp
L power:GNDD #PWR01
U 1 1 64B5627C
P 6125 5875
F 0 "#PWR01" H 6125 5625 50  0001 C CNN
F 1 "GNDD" H 6129 5720 50  0001 C CNN
F 2 "" H 6125 5875 50  0001 C CNN
F 3 "" H 6125 5875 50  0001 C CNN
	1    6125 5875
	1    0    0    -1  
$EndComp
Text GLabel 8175 4175 2    50   Input ~ 0
+3V3
$Comp
L Device:C C2
U 1 1 64DABA53
P 8525 2525
F 0 "C2" H 8300 2550 50  0000 L CNN
F 1 "100nF" H 8275 2375 50  0000 L CNN
F 2 "" H 8563 2375 50  0001 C CNN
F 3 "~" H 8525 2525 50  0001 C CNN
	1    8525 2525
	1    0    0    -1  
$EndComp
Wire Wire Line
	8925 2675 8925 3000
Connection ~ 8925 3000
Wire Wire Line
	8925 3000 8525 3000
Wire Wire Line
	8925 3000 8925 3075
Wire Wire Line
	8525 2675 8525 3000
Connection ~ 8525 3000
Wire Wire Line
	8525 3000 8025 3000
Wire Wire Line
	8525 2375 8525 2250
Wire Wire Line
	8525 2250 8925 2250
Text GLabel 7075 4675 2    50   Input ~ 0
VI2
Text GLabel 7075 4575 2    50   Input ~ 0
VU2
Wire Wire Line
	6825 4575 7075 4575
Wire Wire Line
	6825 4675 7075 4675
Wire Wire Line
	4450 4875 5425 4875
Wire Wire Line
	5425 4775 4650 4775
Wire Wire Line
	4650 4775 4650 4975
Text Notes 9725 2175 0    50   ~ 0
OUTPUT\n\nTo battery\novercharge \nprotection\ncircuit\n
$Comp
L Device:C C1
U 1 1 64DC1466
P 7700 2450
F 0 "C1" H 7475 2475 50  0000 L CNN
F 1 "100nF" H 7450 2300 50  0000 L CNN
F 2 "" H 7738 2300 50  0001 C CNN
F 3 "~" H 7700 2450 50  0001 C CNN
	1    7700 2450
	1    0    0    -1  
$EndComp
Wire Wire Line
	8025 2125 7700 2125
Wire Wire Line
	7700 2125 7700 2300
Wire Wire Line
	7700 2600 7700 3000
Wire Wire Line
	7700 3000 8025 3000
$Comp
L Jumper:Jumper_2_Open JP1
U 1 1 64F61310
P 3725 6075
F 0 "JP1" V 3679 6173 50  0000 L CNN
F 1 "Auto / Manual PWM" V 3770 6173 50  0000 L CNN
F 2 "" H 3725 6075 50  0001 C CNN
F 3 "~" H 3725 6075 50  0001 C CNN
	1    3725 6075
	0    1    1    0   
$EndComp
$Comp
L power:GNDD #PWR02
U 1 1 64F61D7B
P 3725 6275
F 0 "#PWR02" H 3725 6025 50  0001 C CNN
F 1 "GNDD" H 3729 6120 50  0001 C CNN
F 2 "" H 3725 6275 50  0001 C CNN
F 3 "" H 3725 6275 50  0001 C CNN
	1    3725 6275
	1    0    0    -1  
$EndComp
$Comp
L Device:R_POT RV1
U 1 1 64F63403
P 7800 4375
F 0 "RV1" H 7730 4329 50  0000 R CNN
F 1 "10k" H 7730 4420 50  0000 R CNN
F 2 "" H 7800 4375 50  0001 C CNN
F 3 "~" H 7800 4375 50  0001 C CNN
	1    7800 4375
	-1   0    0    1   
$EndComp
Wire Wire Line
	6825 4375 7650 4375
$Comp
L power:GNDD #PWR03
U 1 1 64F64E5B
P 7800 4525
F 0 "#PWR03" H 7800 4275 50  0001 C CNN
F 1 "GNDD" H 7804 4370 50  0001 C CNN
F 2 "" H 7800 4525 50  0001 C CNN
F 3 "" H 7800 4525 50  0001 C CNN
	1    7800 4525
	1    0    0    -1  
$EndComp
Wire Wire Line
	7800 4175 7800 4225
Wire Wire Line
	6825 4175 7800 4175
Wire Wire Line
	8175 4175 7800 4175
Connection ~ 7800 4175
Text Notes 8025 4725 0    50   ~ 0
Manual PWM\n(only when JP1 is set)\nRV1 can be omitted when JP1 is not set.\n
Text Notes 3900 6425 0    50   ~ 0
JP1 set: Manual PWM over Rv1\nJP1 open: Automatic MPP tracking\n
$Comp
L Device:D_Schottky D3
U 1 1 65087936
P 7100 3875
F 0 "D3" H 7100 4091 50  0000 C CNN
F 1 "D_Schottky" H 7100 4000 50  0000 C CNN
F 2 "" H 7100 3875 50  0001 C CNN
F 3 "~" H 7100 3875 50  0001 C CNN
	1    7100 3875
	1    0    0    -1  
$EndComp
Wire Wire Line
	6825 3875 6950 3875
Text GLabel 8150 3875 2    50   Input ~ 0
+5V_IN
Wire Wire Line
	7250 3875 8150 3875
$Comp
L Driver_FET:IR2101 U1
U 1 1 650C2BB4
P 3625 1575
F 0 "U1" H 3950 1575 50  0000 C CNN
F 1 "IR2101" H 4050 1675 50  0000 C CNN
F 2 "" H 3625 1575 50  0001 C CIN
F 3 "https://www.infineon.com/dgdl/ir2101.pdf?fileId=5546d462533600a4015355c7a755166c" H 3625 1575 50  0001 C CNN
	1    3625 1575
	1    0    0    -1  
$EndComp
$Comp
L power:GNDD #PWR011
U 1 1 650C2BBA
P 3625 2200
F 0 "#PWR011" H 3625 1950 50  0001 C CNN
F 1 "GNDD" H 3629 2045 50  0001 C CNN
F 2 "" H 3625 2200 50  0001 C CNN
F 3 "" H 3625 2200 50  0001 C CNN
	1    3625 2200
	1    0    0    -1  
$EndComp
$Comp
L Device:CP C3
U 1 1 650C2BC1
P 3100 1250
F 0 "C3" H 3218 1296 50  0000 L CNN
F 1 "47uF" H 3218 1205 50  0000 L CNN
F 2 "" H 3138 1100 50  0001 C CNN
F 3 "~" H 3100 1250 50  0001 C CNN
	1    3100 1250
	1    0    0    -1  
$EndComp
Wire Wire Line
	3625 1075 3100 1075
Wire Wire Line
	3100 1075 3100 1100
$Comp
L power:GNDD #PWR09
U 1 1 650C2BC9
P 3100 1400
F 0 "#PWR09" H 3100 1150 50  0001 C CNN
F 1 "GNDD" H 3104 1245 50  0001 C CNN
F 2 "" H 3100 1400 50  0001 C CNN
F 3 "" H 3100 1400 50  0001 C CNN
	1    3100 1400
	1    0    0    -1  
$EndComp
$Comp
L Device:R R4
U 1 1 650C2BCF
P 4175 1875
F 0 "R4" V 3968 1875 50  0000 C CNN
F 1 "12" V 4059 1875 50  0000 C CNN
F 2 "" V 4105 1875 50  0001 C CNN
F 3 "~" H 4175 1875 50  0001 C CNN
	1    4175 1875
	0    1    1    0   
$EndComp
Wire Wire Line
	3925 1875 4025 1875
$Comp
L Device:Q_NMOS_GDS Q2
U 1 1 650C2BD6
P 4725 1875
F 0 "Q2" H 4930 1921 50  0000 L CNN
F 1 "IRFP4368" H 4930 1830 50  0000 L CNN
F 2 "" H 4925 1975 50  0001 C CNN
F 3 "~" H 4725 1875 50  0001 C CNN
	1    4725 1875
	1    0    0    -1  
$EndComp
$Comp
L Device:R R5
U 1 1 650C2BDC
P 4825 2275
F 0 "R5" H 4755 2229 50  0000 R CNN
F 1 "10m" H 4755 2320 50  0000 R CNN
F 2 "" V 4755 2275 50  0001 C CNN
F 3 "~" H 4825 2275 50  0001 C CNN
	1    4825 2275
	-1   0    0    1   
$EndComp
$Comp
L power:GNDD #PWR013
U 1 1 650C2BE2
P 4825 2475
F 0 "#PWR013" H 4825 2225 50  0001 C CNN
F 1 "GNDD" H 4829 2320 50  0001 C CNN
F 2 "" H 4825 2475 50  0001 C CNN
F 3 "" H 4825 2475 50  0001 C CNN
	1    4825 2475
	1    0    0    -1  
$EndComp
Wire Wire Line
	4825 2425 4825 2475
Wire Wire Line
	4825 2075 4825 2125
Wire Wire Line
	4325 1875 4525 1875
Text GLabel 1350 825  0    50   Input ~ 0
POWER_IN
Wire Wire Line
	4825 1625 4825 1650
Text GLabel 3700 950  2    50   Input ~ 0
VCC_DRIVER
Wire Wire Line
	3700 950  3625 950 
Wire Wire Line
	3625 950  3625 1075
Connection ~ 3625 1075
$Comp
L Device:L L1
U 1 1 650C2BF1
P 4825 1475
F 0 "L1" H 4878 1521 50  0000 L CNN
F 1 "150uH" H 4878 1430 50  0000 L CNN
F 2 "" H 4825 1475 50  0001 C CNN
F 3 "~" H 4825 1475 50  0001 C CNN
	1    4825 1475
	1    0    0    -1  
$EndComp
$Comp
L Device:CP C4
U 1 1 650C2BF7
P 4550 1250
F 0 "C4" H 4668 1296 50  0000 L CNN
F 1 "200uF" H 4300 1125 50  0000 L CNN
F 2 "" H 4588 1100 50  0001 C CNN
F 3 "~" H 4550 1250 50  0001 C CNN
	1    4550 1250
	1    0    0    -1  
$EndComp
$Comp
L power:GNDD #PWR012
U 1 1 650C2BFD
P 4550 1400
F 0 "#PWR012" H 4550 1150 50  0001 C CNN
F 1 "GNDD" H 4554 1245 50  0001 C CNN
F 2 "" H 4550 1400 50  0001 C CNN
F 3 "" H 4550 1400 50  0001 C CNN
	1    4550 1400
	1    0    0    -1  
$EndComp
$Comp
L Device:CP C5
U 1 1 650C2C03
P 6425 2075
F 0 "C5" H 6543 2121 50  0000 L CNN
F 1 "200uF" H 6543 2030 50  0000 L CNN
F 2 "" H 6463 1925 50  0001 C CNN
F 3 "~" H 6425 2075 50  0001 C CNN
	1    6425 2075
	1    0    0    -1  
$EndComp
$Comp
L power:GNDD #PWR014
U 1 1 650C2C09
P 6425 2475
F 0 "#PWR014" H 6425 2225 50  0001 C CNN
F 1 "GNDD" H 6429 2320 50  0001 C CNN
F 2 "" H 6425 2475 50  0001 C CNN
F 3 "" H 6425 2475 50  0001 C CNN
	1    6425 2475
	1    0    0    -1  
$EndComp
Connection ~ 4825 1650
Wire Wire Line
	4825 1650 4825 1675
Wire Wire Line
	4550 1100 4825 1100
Wire Wire Line
	4825 1100 4825 1325
Connection ~ 4825 1100
Wire Wire Line
	6425 1925 6425 1650
Wire Wire Line
	6425 2225 6425 2475
$Comp
L Device:Q_NMOS_GDS Q3
U 1 1 650C2C1B
P 5550 1550
F 0 "Q3" V 5799 1550 50  0000 C CNN
F 1 "IRFP4368" V 5890 1550 50  0000 C CNN
F 2 "" H 5750 1650 50  0001 C CNN
F 3 "~" H 5550 1550 50  0001 C CNN
	1    5550 1550
	0    1    1    0   
$EndComp
Wire Wire Line
	4825 1650 5225 1650
Wire Wire Line
	5550 1350 5225 1350
Wire Wire Line
	5225 1350 5225 1650
Connection ~ 5225 1650
Wire Wire Line
	5225 1650 5350 1650
$Comp
L power:GNDD #PWR010
U 1 1 650C2C26
P 3250 2200
F 0 "#PWR010" H 3250 1950 50  0001 C CNN
F 1 "GNDD" H 3254 2045 50  0001 C CNN
F 2 "" H 3250 2200 50  0001 C CNN
F 3 "" H 3250 2200 50  0001 C CNN
	1    3250 2200
	1    0    0    -1  
$EndComp
Wire Wire Line
	3325 1575 3250 1575
Wire Wire Line
	5750 1650 6025 1650
$Comp
L Device:R R1
U 1 1 650C2C2E
P 2525 1675
F 0 "R1" V 2318 1675 50  0000 C CNN
F 1 "1k" V 2409 1675 50  0000 C CNN
F 2 "" V 2455 1675 50  0001 C CNN
F 3 "~" H 2525 1675 50  0001 C CNN
	1    2525 1675
	0    1    1    0   
$EndComp
Wire Wire Line
	2675 1675 2900 1675
$Comp
L Device:Q_NPN_CBE Q1
U 1 1 650C2C36
P 2800 1900
F 0 "Q1" H 2991 1946 50  0000 L CNN
F 1 "BC547" H 2991 1855 50  0000 L CNN
F 2 "" H 3000 2000 50  0001 C CNN
F 3 "~" H 2800 1900 50  0001 C CNN
	1    2800 1900
	1    0    0    -1  
$EndComp
$Comp
L power:GNDD #PWR07
U 1 1 650C2C3C
P 2900 2200
F 0 "#PWR07" H 2900 1950 50  0001 C CNN
F 1 "GNDD" H 2904 2045 50  0001 C CNN
F 2 "" H 2900 2200 50  0001 C CNN
F 3 "" H 2900 2200 50  0001 C CNN
	1    2900 2200
	1    0    0    -1  
$EndComp
$Comp
L Device:R R3
U 1 1 650C2C42
P 2800 2775
F 0 "R3" V 2593 2775 50  0000 C CNN
F 1 "10k" V 2684 2775 50  0000 C CNN
F 2 "" V 2730 2775 50  0001 C CNN
F 3 "~" H 2800 2775 50  0001 C CNN
	1    2800 2775
	0    1    1    0   
$EndComp
$Comp
L Device:R R2
U 1 1 650C2C48
P 2600 2050
F 0 "R2" H 2775 2050 50  0000 R CNN
F 1 "4k7" H 2530 2095 50  0000 R CNN
F 2 "" V 2530 2050 50  0001 C CNN
F 3 "~" H 2600 2050 50  0001 C CNN
	1    2600 2050
	-1   0    0    1   
$EndComp
$Comp
L power:GNDD #PWR04
U 1 1 650C2C4E
P 2600 2200
F 0 "#PWR04" H 2600 1950 50  0001 C CNN
F 1 "GNDD" H 2604 2045 50  0001 C CNN
F 2 "" H 2600 2200 50  0001 C CNN
F 3 "" H 2600 2200 50  0001 C CNN
	1    2600 2200
	1    0    0    -1  
$EndComp
Wire Wire Line
	3625 2075 3625 2200
Wire Wire Line
	3250 1575 3250 2200
Wire Wire Line
	2900 2100 2900 2200
Wire Wire Line
	2600 1900 2375 1900
Wire Wire Line
	2375 2775 2650 2775
Connection ~ 2600 1900
$Comp
L Diode:BZD27Cxx D1
U 1 1 650C2C5A
P 3150 2775
F 0 "D1" H 3150 2559 50  0000 C CNN
F 1 "ZD27" H 3150 2650 50  0000 C CNN
F 2 "Diode_SMD:D_SMF" H 3150 2600 50  0001 C CNN
F 3 "https://www.vishay.com/docs/85153/bzd27series.pdf" H 3150 2775 50  0001 C CNN
	1    3150 2775
	-1   0    0    1   
$EndComp
$Comp
L Diode:BZD27Cxx D2
U 1 1 650C2C60
P 3525 2775
F 0 "D2" H 3525 2559 50  0000 C CNN
F 1 "ZD27" H 3525 2650 50  0000 C CNN
F 2 "Diode_SMD:D_SMF" H 3525 2600 50  0001 C CNN
F 3 "https://www.vishay.com/docs/85153/bzd27series.pdf" H 3525 2775 50  0001 C CNN
	1    3525 2775
	-1   0    0    1   
$EndComp
Wire Wire Line
	2950 2775 3000 2775
Wire Wire Line
	3300 2775 3375 2775
Wire Wire Line
	3675 2775 6025 2775
Wire Wire Line
	6025 2775 6025 1650
Connection ~ 6025 1650
Wire Wire Line
	6025 1650 6425 1650
Wire Wire Line
	2375 1900 2375 2775
Wire Wire Line
	2900 1700 2900 1675
Connection ~ 2900 1675
Wire Wire Line
	2900 1675 3325 1675
Wire Wire Line
	6425 1250 6425 1650
Wire Wire Line
	6425 1250 8025 1250
Connection ~ 6425 1650
Wire Wire Line
	5175 3175 1975 3175
Text Notes 1750 1775 0    50   ~ 0
PWM\n
Text Notes 2575 2475 0    50   ~ 0
Idle state protection\n
Wire Wire Line
	1350 825  4825 825 
Wire Wire Line
	4825 825  4825 1100
Text Notes 950  1125 0    50   ~ 0
From solar panels +\n10-40V
Text GLabel 10025 1025 2    50   Input ~ 0
VBAT
Wire Wire Line
	10025 1025 9075 1025
Wire Wire Line
	9075 1025 9075 1250
Text Notes 8175 3750 0    50   ~ 0
+5V from Battery power \nover DC-DC converter\n
Wire Wire Line
	1975 3175 1975 1675
Wire Wire Line
	1975 1675 2375 1675
Wire Wire Line
	3725 5575 3725 5875
Wire Wire Line
	3725 5575 5425 5575
$Comp
L Sensor_Temperature:DS18B20 U2
U 1 1 65125C77
P 2725 7075
F 0 "U2" H 2495 7121 50  0000 R CNN
F 1 "DS18B20" H 2495 7030 50  0000 R CNN
F 2 "Package_TO_SOT_THT:TO-92_Inline" H 1725 6825 50  0001 C CNN
F 3 "http://datasheets.maximintegrated.com/en/ds/DS18B20.pdf" H 2575 7325 50  0001 C CNN
	1    2725 7075
	1    0    0    -1  
$EndComp
$Comp
L Sensor_Temperature:DS18B20 U4
U 1 1 65127087
P 3425 7075
F 0 "U4" H 3195 7121 50  0000 R CNN
F 1 "DS18B20" H 3195 7030 50  0000 R CNN
F 2 "Package_TO_SOT_THT:TO-92_Inline" H 2425 6825 50  0001 C CNN
F 3 "http://datasheets.maximintegrated.com/en/ds/DS18B20.pdf" H 3275 7325 50  0001 C CNN
	1    3425 7075
	1    0    0    -1  
$EndComp
$Comp
L Sensor_Temperature:DS18B20 U5
U 1 1 651279B1
P 4225 7075
F 0 "U5" H 3995 7121 50  0000 R CNN
F 1 "DS18B20" H 3995 7030 50  0000 R CNN
F 2 "Package_TO_SOT_THT:TO-92_Inline" H 3225 6825 50  0001 C CNN
F 3 "http://datasheets.maximintegrated.com/en/ds/DS18B20.pdf" H 4075 7325 50  0001 C CNN
	1    4225 7075
	1    0    0    -1  
$EndComp
Wire Wire Line
	2725 7375 3425 7375
Wire Wire Line
	3425 7375 4225 7375
Connection ~ 3425 7375
$Comp
L power:GNDD #PWR015
U 1 1 6512DD93
P 3425 7475
F 0 "#PWR015" H 3425 7225 50  0001 C CNN
F 1 "GNDD" H 3429 7320 50  0001 C CNN
F 2 "" H 3425 7475 50  0001 C CNN
F 3 "" H 3425 7475 50  0001 C CNN
	1    3425 7475
	1    0    0    -1  
$EndComp
Wire Wire Line
	3425 7375 3425 7475
Wire Wire Line
	2725 6775 3425 6775
Wire Wire Line
	3425 6775 4225 6775
Connection ~ 3425 6775
Wire Wire Line
	3725 7075 3725 6675
Wire Wire Line
	3025 6675 3725 6675
Connection ~ 3725 6675
$Comp
L Device:R R10
U 1 1 65141E1A
P 4600 6925
F 0 "R10" H 4670 6971 50  0000 L CNN
F 1 "4K7" H 4670 6880 50  0000 L CNN
F 2 "" V 4530 6925 50  0001 C CNN
F 3 "~" H 4600 6925 50  0001 C CNN
	1    4600 6925
	1    0    0    -1  
$EndComp
Text GLabel 4750 6775 2    50   Input ~ 0
+3V3
Wire Wire Line
	3025 6675 3025 7075
Wire Wire Line
	4225 6775 4600 6775
Connection ~ 4225 6775
Wire Wire Line
	4525 7075 4600 7075
Wire Wire Line
	4600 6775 4750 6775
Connection ~ 4600 6775
Wire Wire Line
	4600 7075 5300 7075
Wire Wire Line
	5300 7075 5300 6675
Connection ~ 4600 7075
Wire Wire Line
	3725 6675 5300 6675
Wire Wire Line
	5425 5675 5300 5675
Wire Wire Line
	5300 5675 5300 6675
Connection ~ 5300 6675
$EndSCHEMATC