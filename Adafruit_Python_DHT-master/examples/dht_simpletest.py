{\rtf1\ansi\ansicpg1252\cocoartf2513
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Monaco;}
{\colortbl;\red255\green255\blue255;\red132\green134\blue132;\red255\green255\blue255;\red38\green38\blue38;
\red148\green6\blue75;\red14\green114\blue164;\red19\green36\blue126;}
{\*\expandedcolortbl;;\cssrgb\c58824\c59608\c58824;\cssrgb\c100000\c100000\c100000;\cssrgb\c20000\c20000\c20000;
\cssrgb\c65490\c11373\c36471;\cssrgb\c0\c52549\c70196;\cssrgb\c9412\c21176\c56863;}
{\*\listtable{\list\listtemplateid1\listhybrid{\listlevel\levelnfc0\levelnfcn0\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{decimal\}.}{\leveltext\leveltemplateid1\'02\'00.;}{\levelnumbers\'01;}\fi-360\li720\lin720 }{\listname ;}\listid1}}
{\*\listoverridetable{\listoverride\listid1\listoverridecount0\ls1}}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls1\ilvl0
\f0\fs26 \cf2 \cb3 {\listtext	1.	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 # SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries\cf4 \strokec4 \
\ls1\ilvl0\cf2 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	2.	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 # SPDX-License-Identifier: MIT\cf4 \strokec4 \
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls1\ilvl0\cf4 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	3.	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec4 \'a0\
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls1\ilvl0\cf5 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	4.	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec5 import\cf4 \strokec4  time\
\ls1\ilvl0\cf5 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	5.	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec5 import\cf4 \strokec4  board\
\ls1\ilvl0\cf5 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	6.	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec5 import\cf4 \strokec4  adafruit_dht\
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls1\ilvl0\cf4 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	7.	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec4 \'a0\
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls1\ilvl0\cf2 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	8.	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 # Initial the dht device, with data pin connected to:\cf4 \strokec4 \
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls1\ilvl0\cf4 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	9.	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec4 dhtDevice = adafruit_dht.DHT11(board.D4)\
\ls1\ilvl0\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	10.	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec4 \'a0\
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls1\ilvl0\cf2 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	11.	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 # you can pass DHT22 use_pulseio=False if you wouldn't like to use pulseio.\cf4 \strokec4 \
\ls1\ilvl0\cf2 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	12.	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 # This may be necessary on a Linux single board computer like the Raspberry Pi,\cf4 \strokec4 \
\ls1\ilvl0\cf2 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	13.	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 # but it will not work in CircuitPython.\cf4 \strokec4 \
\ls1\ilvl0\cf2 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	14.	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 # dhtDevice = adafruit_dht.DHT22(board.D18, use_pulseio=False)\cf4 \strokec4 \
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls1\ilvl0\cf4 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	15.	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec4 \'a0\
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls1\ilvl0\cf5 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	16.	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec5 while\cf4 \strokec4  \cf5 \strokec5 True\cf4 \strokec4 :\
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls1\ilvl0\cf4 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	17.	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec4     \cf5 \strokec5 try\cf4 \strokec4 :\
\ls1\ilvl0\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	18.	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec4         \cf2 \strokec2 # Print the values to the serial port\cf4 \strokec4 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	19.	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec4         temperature_c = dhtDevice.temperature\
\ls1\ilvl0\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	20.	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec4         temperature_f = temperature_c * (\cf6 \strokec6 9\cf4 \strokec4  / \cf6 \strokec6 5\cf4 \strokec4 ) + \cf6 \strokec6 32\cf4 \strokec4 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	21.	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec4         humidity = dhtDevice.humidity\
\ls1\ilvl0\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	22.	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec4         \cf5 \strokec5 print\cf4 \strokec4 (\
\ls1\ilvl0\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	23.	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec4             \cf7 \strokec7 "Temp: \{:.1f\} F / \{:.1f\} C    Humidity: \{\}% "\cf4 \strokec4 .format(\
\ls1\ilvl0\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	24.	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec4                 temperature_f, temperature_c, humidity\
\ls1\ilvl0\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	25.	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec4             )\
\ls1\ilvl0\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	26.	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec4         )\
\ls1\ilvl0\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	27.	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec4 \'a0\
\ls1\ilvl0\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	28.	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec4     \cf5 \strokec5 except\cf4 \strokec4  \cf6 \strokec6 RuntimeError\cf4 \strokec4  \cf5 \strokec5 as\cf4 \strokec4  error:\
\ls1\ilvl0\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	29.	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec4         \cf2 \strokec2 # Errors happen fairly often, DHT's are hard to read, just keep going\cf4 \strokec4 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	30.	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec4         \cf5 \strokec5 print\cf4 \strokec4 (error.args[\cf6 \strokec6 0\cf4 \strokec4 ])\
\ls1\ilvl0\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	31.	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec4         time.sleep(\cf6 \strokec6 2.0\cf4 \strokec4 )\
\ls1\ilvl0\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	32.	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec4         \cf5 \strokec5 continue\cf4 \strokec4 \
\ls1\ilvl0\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	33.	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec4     \cf5 \strokec5 except\cf4 \strokec4  \cf6 \strokec6 Exception\cf4 \strokec4  \cf5 \strokec5 as\cf4 \strokec4  error:\
\ls1\ilvl0\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	34.	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec4         dhtDevice.\cf5 \strokec5 exit\cf4 \strokec4 ()\
\ls1\ilvl0\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	35.	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec4         \cf5 \strokec5 raise\cf4 \strokec4  error\
\ls1\ilvl0\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	36.	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec4 \'a0\
\ls1\ilvl0\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	37.	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec4     time.sleep(\cf6 \strokec6 2.0\cf4 \strokec4 )\
}