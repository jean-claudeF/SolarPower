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
L tlc2652:TLC2652 U2
U 1 1 63B71693
P 2550 4675
F 0 "U2" H 2550 4950 50  0000 L CNN
F 1 "TLC2652" H 2550 4875 50  0000 L CNN
F 2 "" H 2600 4725 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/lm741.pdf" H 2700 4825 50  0001 C CNN
	1    2550 4675
	1    0    0    -1  
$EndComp
Text GLabel 2500 4275 2    50   Input ~ 0
+5V
Wire Wire Line
	2450 4375 2450 4275
Wire Wire Line
	2450 4275 2500 4275
$Comp
L Device:C C3
U 1 1 63B71E36
P 2550 5175
F 0 "C3" H 2600 4950 50  0000 L CNN
F 1 "100n" H 2325 4950 50  0000 L CNN
F 2 "" H 2588 5025 50  0001 C CNN
F 3 "~" H 2550 5175 50  0001 C CNN
	1    2550 5175
	1    0    0    -1  
$EndComp
$Comp
L Device:C C4
U 1 1 63B72396
P 2775 5175
F 0 "C4" H 2825 4950 50  0000 L CNN
F 1 "100n" H 2775 4875 50  0000 L CNN
F 2 "" H 2813 5025 50  0001 C CNN
F 3 "~" H 2775 5175 50  0001 C CNN
	1    2775 5175
	1    0    0    -1  
$EndComp
Wire Wire Line
	2650 5025 2775 5025
Wire Wire Line
	2550 5325 2775 5325
Wire Wire Line
	2775 5325 3050 5325
Wire Wire Line
	3050 5325 3050 4875
Wire Wire Line
	3050 4875 2750 4875
Connection ~ 2775 5325
Wire Wire Line
	2450 4975 2450 5025
Wire Wire Line
	2450 5025 2375 5025
Wire Wire Line
	2375 5025 2375 5325
Wire Wire Line
	2375 5325 2550 5325
Connection ~ 2550 5325
$Comp
L power:GNDD #PWR05
U 1 1 63B73253
P 2550 5400
F 0 "#PWR05" H 2550 5150 50  0001 C CNN
F 1 "GNDD" H 2554 5245 50  0001 C CNN
F 2 "" H 2550 5400 50  0001 C CNN
F 3 "" H 2550 5400 50  0001 C CNN
	1    2550 5400
	1    0    0    -1  
$EndComp
Wire Wire Line
	2550 5400 2550 5325
$Comp
L Device:R R7
U 1 1 63B73990
P 2075 5125
F 0 "R7" H 2145 5171 50  0000 L CNN
F 1 "1k" H 2145 5080 50  0000 L CNN
F 2 "" V 2005 5125 50  0001 C CNN
F 3 "~" H 2075 5125 50  0001 C CNN
	1    2075 5125
	1    0    0    -1  
$EndComp
$Comp
L Device:R R10
U 1 1 63B73FA1
P 2550 4050
F 0 "R10" V 2650 4075 50  0000 C CNN
F 1 "18k" V 2625 4300 50  0000 C CNN
F 2 "" V 2480 4050 50  0001 C CNN
F 3 "~" H 2550 4050 50  0001 C CNN
	1    2550 4050
	0    1    1    0   
$EndComp
$Comp
L Device:R R9
U 1 1 63B74819
P 2550 3925
F 0 "R9" V 2450 3925 50  0000 C CNN
F 1 "18k" V 2575 4175 50  0000 C CNN
F 2 "" V 2480 3925 50  0001 C CNN
F 3 "~" H 2550 3925 50  0001 C CNN
	1    2550 3925
	0    1    1    0   
$EndComp
Wire Wire Line
	2400 3925 2400 4050
Wire Wire Line
	2700 3925 2700 4050
Wire Wire Line
	2400 4050 2075 4050
Wire Wire Line
	2075 4050 2075 4775
Connection ~ 2400 4050
Wire Wire Line
	2250 4775 2075 4775
Connection ~ 2075 4775
Wire Wire Line
	2075 4775 2075 4975
Wire Wire Line
	2700 4050 3075 4050
Wire Wire Line
	3075 4675 2950 4675
Wire Wire Line
	3075 4050 3075 4675
Connection ~ 2700 4050
Text GLabel 3225 4675 2    50   Input ~ 0
+OUT
Wire Wire Line
	3075 4675 3225 4675
Connection ~ 3075 4675
Wire Wire Line
	2075 5275 2075 5325
Wire Wire Line
	2075 5325 2375 5325
Connection ~ 2375 5325
$Comp
L Device:R R6
U 1 1 63B774C3
P 1825 5125
F 0 "R6" H 1895 5171 50  0000 L CNN
F 1 "1M" H 1895 5080 50  0000 L CNN
F 2 "" V 1755 5125 50  0001 C CNN
F 3 "~" H 1825 5125 50  0001 C CNN
	1    1825 5125
	1    0    0    -1  
$EndComp
Wire Wire Line
	2250 4575 1825 4575
Wire Wire Line
	1825 4575 1825 4975
Wire Wire Line
	1825 5275 1825 5325
Wire Wire Line
	1825 5325 2075 5325
Connection ~ 2075 5325
Text GLabel 1700 4575 0    50   Input ~ 0
+IN
Wire Wire Line
	1700 4575 1825 4575
Connection ~ 1825 4575
$Comp
L tlc2652:TLC2652 U1
U 1 1 63B7878D
P 2525 6475
F 0 "U1" H 2525 6750 50  0000 L CNN
F 1 "TLC2652" H 2525 6675 50  0000 L CNN
F 2 "" H 2575 6525 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/lm741.pdf" H 2675 6625 50  0001 C CNN
	1    2525 6475
	1    0    0    -1  
$EndComp
$Comp
L Device:R R8
U 1 1 63B790A8
P 2525 5875
F 0 "R8" V 2400 5875 50  0000 C CNN
F 1 "100k" V 2625 5775 50  0000 C CNN
F 2 "" V 2455 5875 50  0001 C CNN
F 3 "~" H 2525 5875 50  0001 C CNN
	1    2525 5875
	0    1    1    0   
$EndComp
Text GLabel 2525 6075 2    50   Input ~ 0
+5V
Wire Wire Line
	2525 6075 2425 6075
Wire Wire Line
	2425 6075 2425 6175
$Comp
L Device:C C2
U 1 1 63B7B70F
P 2525 6975
F 0 "C2" H 2300 6625 50  0000 L CNN
F 1 "100n" H 2325 6725 50  0000 L CNN
F 2 "" H 2563 6825 50  0001 C CNN
F 3 "~" H 2525 6975 50  0001 C CNN
	1    2525 6975
	1    0    0    -1  
$EndComp
$Comp
L Device:C C5
U 1 1 63B7BD5C
P 2775 6975
F 0 "C5" H 2700 6650 50  0000 L CNN
F 1 "100n" H 2600 6750 50  0000 L CNN
F 2 "" H 2813 6825 50  0001 C CNN
F 3 "~" H 2775 6975 50  0001 C CNN
	1    2775 6975
	1    0    0    -1  
$EndComp
Wire Wire Line
	2425 6775 2350 6775
Wire Wire Line
	2350 6775 2350 7125
Wire Wire Line
	2350 7125 2525 7125
Wire Wire Line
	2525 7125 2775 7125
Connection ~ 2525 7125
Wire Wire Line
	2775 7125 3025 7125
Wire Wire Line
	3025 7125 3025 6675
Wire Wire Line
	3025 6675 2725 6675
Connection ~ 2775 7125
Wire Wire Line
	2625 6825 2775 6825
$Comp
L power:GNDD #PWR04
U 1 1 63B7DDEA
P 2525 7250
F 0 "#PWR04" H 2525 7000 50  0001 C CNN
F 1 "GNDD" H 2529 7095 50  0001 C CNN
F 2 "" H 2525 7250 50  0001 C CNN
F 3 "" H 2525 7250 50  0001 C CNN
	1    2525 7250
	1    0    0    -1  
$EndComp
Wire Wire Line
	2525 7125 2525 7250
Wire Wire Line
	2375 5875 1975 5875
Wire Wire Line
	1975 5875 1975 6575
Wire Wire Line
	1975 6575 2225 6575
Wire Wire Line
	2225 6375 2175 6375
Wire Wire Line
	2175 6375 2175 7125
Wire Wire Line
	2175 7125 2350 7125
Connection ~ 2350 7125
Wire Wire Line
	2675 5875 3025 5875
Wire Wire Line
	3025 5875 3025 6475
Wire Wire Line
	3025 6475 2925 6475
Text GLabel 3175 6475 2    50   Input ~ 0
-OUT
Wire Wire Line
	3025 6475 3175 6475
Connection ~ 3025 6475
$Comp
L Device:R R5
U 1 1 63B81904
P 1750 6575
F 0 "R5" V 1625 6550 50  0000 C CNN
F 1 "10k" V 1850 6575 50  0000 C CNN
F 2 "" V 1680 6575 50  0001 C CNN
F 3 "~" H 1750 6575 50  0001 C CNN
	1    1750 6575
	0    1    1    0   
$EndComp
Wire Wire Line
	1900 6575 1975 6575
Connection ~ 1975 6575
Text GLabel 1500 6575 0    50   Input ~ 0
-IN
Wire Wire Line
	1500 6575 1600 6575
$Comp
L Device:R R1
U 1 1 63B8AD6D
P 2425 2950
F 0 "R1" V 2300 2925 50  0000 C CNN
F 1 "Rs1" V 2525 2950 50  0000 C CNN
F 2 "" V 2355 2950 50  0001 C CNN
F 3 "~" H 2425 2950 50  0001 C CNN
	1    2425 2950
	0    1    1    0   
$EndComp
$Comp
L Device:R R2
U 1 1 63B8B328
P 3025 2950
F 0 "R2" V 2900 2925 50  0000 C CNN
F 1 "Rs2" V 3125 2950 50  0000 C CNN
F 2 "" V 2955 2950 50  0001 C CNN
F 3 "~" H 3025 2950 50  0001 C CNN
	1    3025 2950
	0    1    1    0   
$EndComp
Text GLabel 3650 3175 2    50   Input ~ 0
+IN
Text GLabel 1925 3150 0    50   Input ~ 0
-IN
$Comp
L Device:R R3
U 1 1 63B98413
P 5200 1025
F 0 "R3" V 5075 1025 50  0000 C CNN
F 1 "47k" V 5300 1000 50  0000 C CNN
F 2 "" V 5130 1025 50  0001 C CNN
F 3 "~" H 5200 1025 50  0001 C CNN
	1    5200 1025
	0    1    1    0   
$EndComp
$Comp
L Device:R R4
U 1 1 63B9883B
P 5425 1375
F 0 "R4" H 5250 1425 50  0000 L CNN
F 1 "2k7" H 5200 1350 50  0000 L CNN
F 2 "" V 5355 1375 50  0001 C CNN
F 3 "~" H 5425 1375 50  0001 C CNN
	1    5425 1375
	1    0    0    -1  
$EndComp
$Comp
L Device:C C1
U 1 1 63B98B29
P 5750 1375
F 0 "C1" H 5550 1425 50  0000 L CNN
F 1 "4u7" H 5550 1275 50  0000 L CNN
F 2 "" H 5788 1225 50  0001 C CNN
F 3 "~" H 5750 1375 50  0001 C CNN
	1    5750 1375
	1    0    0    -1  
$EndComp
$Comp
L power:GNDD #PWR02
U 1 1 63B98D4A
P 5425 1700
F 0 "#PWR02" H 5425 1450 50  0001 C CNN
F 1 "GNDD" H 5429 1545 50  0001 C CNN
F 2 "" H 5425 1700 50  0001 C CNN
F 3 "" H 5425 1700 50  0001 C CNN
	1    5425 1700
	1    0    0    -1  
$EndComp
Wire Wire Line
	5350 1025 5425 1025
Wire Wire Line
	5750 1025 5425 1025
Connection ~ 5425 1025
$Comp
L power:GNDD #PWR03
U 1 1 63BA09DB
P 5750 1700
F 0 "#PWR03" H 5750 1450 50  0001 C CNN
F 1 "GNDD" H 5754 1545 50  0001 C CNN
F 2 "" H 5750 1700 50  0001 C CNN
F 3 "" H 5750 1700 50  0001 C CNN
	1    5750 1700
	1    0    0    -1  
$EndComp
Text GLabel 5975 1025 2    50   Input ~ 0
Voltage
Wire Wire Line
	5750 1025 5975 1025
Connection ~ 5750 1025
Wire Wire Line
	5425 1025 5425 1225
Wire Wire Line
	5425 1525 5425 1700
Wire Wire Line
	5750 1025 5750 1225
Wire Wire Line
	5750 1525 5750 1700
Text Notes 2900 3450 0    50   ~ 0
Discharge\ncurrent \nshunt\n 
Text Notes 2325 3450 0    50   ~ 0
Charge\ncurrent \nshunt\n 
Text Notes 6000 1200 0    50   ~ 0
Voltage signal\n
Text Notes 3225 4950 0    50   ~ 0
Load current\nsignal\n
Text Notes 3200 6725 0    50   ~ 0
Charge current\nsignal\n
$Comp
L Device:Q_PMOS_GDS Q1
U 1 1 63BDD8D9
P 2325 1800
F 0 "Q1" V 2667 1800 50  0000 C CNN
F 1 "SUP90P06-09L" V 2576 1800 50  0000 C CNN
F 2 "" H 2525 1900 50  0001 C CNN
F 3 "~" H 2325 1800 50  0001 C CNN
	1    2325 1800
	0    1    -1   0   
$EndComp
Wire Wire Line
	2125 1700 2075 1700
$Comp
L Device:R R11
U 1 1 63BDD8E0
P 2075 1850
F 0 "R11" H 1875 1875 50  0000 L CNN
F 1 "10k" H 1875 1775 50  0000 L CNN
F 2 "" V 2005 1850 50  0001 C CNN
F 3 "~" H 2075 1850 50  0001 C CNN
	1    2075 1850
	1    0    0    -1  
$EndComp
Connection ~ 2075 1700
Wire Wire Line
	2075 2000 2325 2000
Wire Wire Line
	2725 1325 2725 1700
Wire Wire Line
	2725 1700 2525 1700
$Comp
L Connector:Screw_Terminal_01x02 J2
U 1 1 63BDD8EA
P 2925 2525
F 0 "J2" H 3005 2517 50  0000 L CNN
F 1 "Battery" H 3005 2426 50  0000 L CNN
F 2 "" H 2925 2525 50  0001 C CNN
F 3 "~" H 2925 2525 50  0001 C CNN
	1    2925 2525
	1    0    0    -1  
$EndComp
Wire Wire Line
	2725 2525 2725 1700
$Comp
L power:GNDD #PWR01
U 1 1 63BDD8F1
P 2725 3450
F 0 "#PWR01" H 2725 3200 50  0001 C CNN
F 1 "GNDD" H 2729 3295 50  0001 C CNN
F 2 "" H 2725 3450 50  0001 C CNN
F 3 "" H 2725 3450 50  0001 C CNN
	1    2725 3450
	1    0    0    -1  
$EndComp
Wire Wire Line
	1500 1700 1800 1700
Wire Wire Line
	1700 1325 2725 1325
Text GLabel 2075 2450 2    50   Input ~ 0
GATE_CHARGE
$Comp
L Diode:BZD27Cxx D1
U 1 1 63BDD8FB
P 1800 1850
F 0 "D1" V 1750 1675 50  0000 L CNN
F 1 "ZD18" V 1850 1625 50  0000 L CNN
F 2 "Diode_SMD:D_SMF" H 1800 1675 50  0001 C CNN
F 3 "https://www.vishay.com/docs/85153/bzd27series.pdf" H 1800 1850 50  0001 C CNN
	1    1800 1850
	0    1    1    0   
$EndComp
Connection ~ 1800 1700
Wire Wire Line
	1800 1700 2075 1700
Connection ~ 2075 2000
$Comp
L Device:R R12
U 1 1 63BDD904
P 2075 2225
F 0 "R12" H 1875 2250 50  0000 L CNN
F 1 "10k" H 1850 2150 50  0000 L CNN
F 2 "" V 2005 2225 50  0001 C CNN
F 3 "~" H 2075 2225 50  0001 C CNN
	1    2075 2225
	1    0    0    -1  
$EndComp
Wire Wire Line
	2075 2000 2075 2075
Wire Wire Line
	1800 2000 2075 2000
Connection ~ 2725 1700
$Comp
L Device:Q_PMOS_GDS Q2
U 1 1 63BDD90D
P 3875 1800
F 0 "Q2" V 4217 1800 50  0000 C CNN
F 1 "SUP90P06-09L" V 4126 1800 50  0000 C CNN
F 2 "" H 4075 1900 50  0001 C CNN
F 3 "~" H 3875 1800 50  0001 C CNN
	1    3875 1800
	0    1    -1   0   
$EndComp
Wire Wire Line
	3675 1700 3625 1700
$Comp
L Device:R R13
U 1 1 63BDD914
P 3625 1850
F 0 "R13" H 3425 1875 50  0000 L CNN
F 1 "10k" H 3425 1775 50  0000 L CNN
F 2 "" V 3555 1850 50  0001 C CNN
F 3 "~" H 3625 1850 50  0001 C CNN
	1    3625 1850
	1    0    0    -1  
$EndComp
Connection ~ 3625 1700
Wire Wire Line
	3625 2000 3875 2000
$Comp
L Diode:BZD27Cxx D2
U 1 1 63BDD91C
P 3350 1850
F 0 "D2" V 3300 1675 50  0000 L CNN
F 1 "ZD18" V 3400 1625 50  0000 L CNN
F 2 "Diode_SMD:D_SMF" H 3350 1675 50  0001 C CNN
F 3 "https://www.vishay.com/docs/85153/bzd27series.pdf" H 3350 1850 50  0001 C CNN
	1    3350 1850
	0    1    1    0   
$EndComp
Connection ~ 3350 1700
Wire Wire Line
	3350 1700 3625 1700
Connection ~ 3625 2000
$Comp
L Device:R R14
U 1 1 63BDD925
P 3625 2225
F 0 "R14" H 3425 2250 50  0000 L CNN
F 1 "10k" H 3400 2150 50  0000 L CNN
F 2 "" V 3555 2225 50  0001 C CNN
F 3 "~" H 3625 2225 50  0001 C CNN
	1    3625 2225
	1    0    0    -1  
$EndComp
Wire Wire Line
	3625 2000 3625 2075
Wire Wire Line
	3350 2000 3625 2000
Wire Wire Line
	2725 1700 3350 1700
$Comp
L Connector:Screw_Terminal_01x02 J3
U 1 1 63BDD92E
P 4575 2525
F 0 "J3" H 4655 2517 50  0000 L CNN
F 1 "Load" H 4655 2426 50  0000 L CNN
F 2 "" H 4575 2525 50  0001 C CNN
F 3 "~" H 4575 2525 50  0001 C CNN
	1    4575 2525
	1    0    0    -1  
$EndComp
Wire Wire Line
	4375 2525 4375 1700
Wire Wire Line
	4375 1700 4075 1700
Wire Wire Line
	4375 2625 4375 2950
$Comp
L Connector:Screw_Terminal_01x02 J1
U 1 1 63BDD93A
P 1300 2525
F 0 "J1" H 1218 2742 50  0000 C CNN
F 1 "Charging power" H 1375 2200 50  0000 C CNN
F 2 "" H 1300 2525 50  0001 C CNN
F 3 "~" H 1300 2525 50  0001 C CNN
	1    1300 2525
	-1   0    0    -1  
$EndComp
Wire Wire Line
	1500 2625 1625 2625
Wire Wire Line
	1625 2625 1625 2950
Text GLabel 3625 2450 2    50   Input ~ 0
GATE_DISCHARGE
Text GLabel 1700 1325 0    50   Input ~ 0
+BATTERY
Wire Wire Line
	1500 2525 1500 1700
Text GLabel 1400 1700 0    50   Input ~ 0
+CHARGE
Wire Wire Line
	1400 1700 1500 1700
Connection ~ 1500 1700
Wire Wire Line
	2725 2625 2725 2950
Wire Wire Line
	2075 2375 2075 2450
Wire Wire Line
	3625 2375 3625 2450
Wire Wire Line
	1625 2950 2075 2950
Wire Wire Line
	2575 2950 2725 2950
Connection ~ 2725 2950
Wire Wire Line
	2725 2950 2725 3450
Wire Wire Line
	2725 2950 2875 2950
Wire Wire Line
	3175 2950 3425 2950
Wire Wire Line
	2725 1025 2725 1325
Wire Wire Line
	2725 1025 5050 1025
Connection ~ 2725 1325
Wire Wire Line
	1925 3150 2075 3150
Wire Wire Line
	2075 3150 2075 2950
Connection ~ 2075 2950
Wire Wire Line
	2075 2950 2275 2950
Wire Wire Line
	3650 3175 3425 3175
Wire Wire Line
	3425 3175 3425 2950
Connection ~ 3425 2950
Wire Wire Line
	3425 2950 4375 2950
$Comp
L Analog_ADC:ADS1115IDGS U4
U 1 1 63C38A28
P 5525 5325
F 0 "U4" H 5525 6006 50  0000 C CNN
F 1 "ADS1115IDGS" H 4925 5625 50  0000 C CNN
F 2 "Package_SO:TSSOP-10_3x3mm_P0.5mm" H 5525 4825 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/ads1113.pdf" H 5475 4425 50  0001 C CNN
	1    5525 5325
	1    0    0    -1  
$EndComp
$Comp
L oled:SH1106 U3
U 1 1 63C38A2E
P 5525 3925
F 0 "U3" H 5195 4021 50  0000 R CNN
F 1 "SH1106" H 5195 3930 50  0000 R CNN
F 2 "" H 5525 3425 50  0001 C CNN
F 3 "" H 5475 3025 50  0001 C CNN
	1    5525 3925
	1    0    0    -1  
$EndComp
$Comp
L Device:R R15
U 1 1 63C38A34
P 6025 3575
F 0 "R15" H 5825 3725 50  0000 L CNN
F 1 "10K" H 5900 3925 50  0000 L CNN
F 2 "" V 5955 3575 50  0001 C CNN
F 3 "~" H 6025 3575 50  0001 C CNN
	1    6025 3575
	1    0    0    -1  
$EndComp
Wire Wire Line
	5925 3925 6025 3925
Wire Wire Line
	5925 4025 6225 4025
$Comp
L Device:R R16
U 1 1 63C38A3C
P 6225 3575
F 0 "R16" H 6295 3621 50  0000 L CNN
F 1 "10K" H 6150 3950 50  0000 L CNN
F 2 "" V 6155 3575 50  0001 C CNN
F 3 "~" H 6225 3575 50  0001 C CNN
	1    6225 3575
	1    0    0    -1  
$EndComp
Wire Wire Line
	6025 3725 6025 3925
Wire Wire Line
	6225 3725 6225 4025
Wire Wire Line
	6225 3425 6225 3325
Wire Wire Line
	6225 3325 6025 3325
Wire Wire Line
	5525 3325 5525 3425
Wire Wire Line
	6025 3425 6025 3325
Connection ~ 6025 3325
Wire Wire Line
	6025 3325 5525 3325
Wire Wire Line
	5525 4325 5525 4375
Wire Wire Line
	5525 5725 5525 5775
Wire Wire Line
	5925 5525 6025 5525
Wire Wire Line
	6025 5525 6025 5775
Wire Wire Line
	6025 5775 5525 5775
Text Notes 4825 5775 0    50   ~ 0
ADDR = 0x48
Text Notes 4725 4375 0    50   ~ 0
ADDR = 0x3C
Wire Wire Line
	6025 5325 5925 5325
Connection ~ 6025 3925
Wire Wire Line
	6225 5425 5925 5425
Connection ~ 6225 4025
Wire Wire Line
	5525 4825 4625 4825
Wire Wire Line
	4625 4825 4625 3325
Wire Wire Line
	4625 3325 5525 3325
Connection ~ 5525 3325
Text GLabel 4950 5225 0    50   Input ~ 0
Voltage
Text GLabel 4950 5325 0    50   Input ~ 0
+OUT
Text GLabel 4950 5425 0    50   Input ~ 0
-OUT
Wire Wire Line
	5125 5425 4950 5425
Wire Wire Line
	5125 5325 4950 5325
Wire Wire Line
	5125 5225 4950 5225
$Comp
L power:GNDD #PWR06
U 1 1 63C4BEF5
P 5525 4375
F 0 "#PWR06" H 5525 4125 50  0001 C CNN
F 1 "GNDD" H 5529 4220 50  0001 C CNN
F 2 "" H 5525 4375 50  0001 C CNN
F 3 "" H 5525 4375 50  0001 C CNN
	1    5525 4375
	1    0    0    -1  
$EndComp
$Comp
L power:GNDD #PWR07
U 1 1 63C4C478
P 5525 5775
F 0 "#PWR07" H 5525 5525 50  0001 C CNN
F 1 "GNDD" H 5529 5620 50  0001 C CNN
F 2 "" H 5525 5775 50  0001 C CNN
F 3 "" H 5525 5775 50  0001 C CNN
	1    5525 5775
	1    0    0    -1  
$EndComp
Connection ~ 5525 5775
Wire Wire Line
	6225 4025 6225 4400
Wire Wire Line
	6025 3925 6025 4500
$Comp
L power:GNDD #PWR08
U 1 1 6414F2EB
P 6900 4925
F 0 "#PWR08" H 6900 4675 50  0001 C CNN
F 1 "GNDD" H 6904 4770 50  0001 C CNN
F 2 "" H 6900 4925 50  0001 C CNN
F 3 "" H 6900 4925 50  0001 C CNN
	1    6900 4925
	1    0    0    -1  
$EndComp
Wire Wire Line
	6900 4925 6900 4100
Text GLabel 7575 4200 0    50   Input ~ 0
INT_LED
Text Notes 9675 3950 0    50   ~ 0
D5, D6,D7 INPUT\nwith pullup\n
Wire Wire Line
	9600 4200 9525 4200
Wire Wire Line
	9600 4300 9525 4300
Text GLabel 9600 4200 2    50   Input ~ 0
GATE_DISCHARGE
Text GLabel 9600 4300 2    50   Input ~ 0
GATE_CHARGE
Wire Wire Line
	8675 4200 9225 4200
$Comp
L Device:D D3
U 1 1 6414F2FA
P 9375 4200
F 0 "D3" H 9400 4400 50  0000 C CNN
F 1 "D" H 9425 4325 50  0000 C CNN
F 2 "" H 9375 4200 50  0001 C CNN
F 3 "~" H 9375 4200 50  0001 C CNN
	1    9375 4200
	-1   0    0    1   
$EndComp
$Comp
L Device:D D4
U 1 1 6414F300
P 9375 4300
F 0 "D4" H 9375 4084 50  0000 C CNN
F 1 "D" H 9375 4175 50  0000 C CNN
F 2 "" H 9375 4300 50  0001 C CNN
F 3 "~" H 9375 4300 50  0001 C CNN
	1    9375 4300
	-1   0    0    1   
$EndComp
Wire Wire Line
	8675 4000 8925 4000
Text GLabel 8925 4000 2    50   Input ~ 0
+3V3
$Comp
L smartyreader-cache:smartyreader-rescue_WEMOS_D1_mini W1
U 1 1 6414F308
P 8125 4350
F 0 "W1" H 8267 5137 60  0000 C CNN
F 1 "D1mini" H 8267 5031 60  0000 C CNN
F 2 "" H 8125 4350 60  0001 C CNN
F 3 "" H 8125 4350 60  0001 C CNN
	1    8125 4350
	1    0    0    -1  
$EndComp
Wire Wire Line
	6900 4100 7575 4100
$Comp
L Switch:SW_DIP_x01 SW1
U 1 1 6414F311
P 9000 5025
F 0 "SW1" V 8954 5155 50  0000 L CNN
F 1 "SW1" V 9045 5155 50  0000 L CNN
F 2 "" H 9000 5025 50  0001 C CNN
F 3 "~" H 9000 5025 50  0001 C CNN
	1    9000 5025
	0    1    1    0   
$EndComp
$Comp
L power:GNDD #PWR09
U 1 1 6414F317
P 9000 5325
F 0 "#PWR09" H 9000 5075 50  0001 C CNN
F 1 "GNDD" H 9004 5170 50  0001 C CNN
F 2 "" H 9000 5325 50  0001 C CNN
F 3 "" H 9000 5325 50  0001 C CNN
	1    9000 5325
	1    0    0    -1  
$EndComp
Wire Wire Line
	6225 4400 7575 4400
Connection ~ 6225 4400
Wire Wire Line
	6225 4400 6225 5425
Wire Wire Line
	6025 4500 7575 4500
Connection ~ 6025 4500
Wire Wire Line
	6025 4500 6025 5325
Wire Wire Line
	8675 4400 9000 4400
Wire Wire Line
	9000 4400 9000 4725
Wire Wire Line
	8675 4300 9225 4300
Text Notes 9000 5750 0    50   ~ 0
(Don't use D8 as input with pullup!)\n
$EndSCHEMATC
