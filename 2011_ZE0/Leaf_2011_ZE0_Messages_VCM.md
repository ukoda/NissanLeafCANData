# Nissan Leaf 2011 ZE0 VCM ECU

These are messages you can send to the VCM ECU to make queries and get responses.

These are the queries (0x797) and responses (0x79A) that can be made of the VCM.

NB: The first of these are from the start of LeafSpy so are probably generic to all Leafs so LeafSpy can determine what type of vehicle it is before sending vehicle specific messages.  These messages have been listed in the order they are seen after LeafSpy starts.  It is currently unclear at which point in the list the messages go from common to all Leafs to specific to the ZE0.

Where matches are found names used are the same as in the existing `Leaf2018-CAN.pdf` document.

The indented information is for the ISO-TP summary, see the README.md in the repo root folder.  While the message may have 8 bytes of data ISO-TP indicates the length of the data actually used, the reset can be ignored and are no shown in the indented data information

## Access Request

*	Type: Undocumented protocol
*	Description: Needed before other messages are sent to the VCM
*	Query: 0x797 02 10 C0 00 00 00 00 00 
	* PCI Field: Single Frame with 2 bytes
	* Data: 10 C0
*	Answer: 0x79A 02 50 C0 00 00 00 00 00 
	* PCI Field: Single Frame with 2 bytes
	* Data: 50 C0
*	Formula:

## 1304 - Power Software

*	Type: Boolean
*	Description: Power SW is True if the Leaf’s power switch is ON otherwise it is False. The fifth reply byte value is 0x80 if the car is powered on.
*	Query: 0x797 03 22 13 04 00 00 00 00
	* PCI Field: Single Frame with 3 bytes
	* Data: 22 13 04
*	Answer: 0x79A 05 62 13 04 **00** BA 00 00
	* PCI Field: Single Frame with 5 bytes
	* Data: 62 13 04 **00** BA
*	Formula: Power SW = (data[4] & 128 == 128)

## 1156 - Gear

*	Type: Integer
*	Description: Gear position (1=Park, 2=Reverse, 3=Neutral, 4=Drive, 7=Eco). The fifth reply byte value is the gear value.
*	Query: 0x797 03 22 11 56 00 00 00 00
	* PCI Field: Single Frame with 3 bytes
	* Data: 22 11 56
*	Answer: 0x79A 07 62 11 56 **01** 00 01 01
	* PCI Field: Single Frame with 7 bytes
	* Data 62 11 56 **01** 00 01 01
*	Formula: Gear = data[4]

NB: Byte 4 matches 2018 data but should check against data captured during actual drive.  Also there are three extra bytes returned, 00 01 01, that have an unknown meaning.

## 132A

*	Type:
*	Description:
*	Query: 0x797 03 22 13 2A 00 00 00 00
	* PCI Field: Single Frame with 3 bytes
	* Data: 22 13 2A
*	Answer: 0x79A 05 62 13 2A 00 60 00 00
	* PCI Field: Single Frame with 5 bytes
	* Data: 62 13 2A 00 60
*	Formula:

NB: Answer data 00 changes to 10 when power on.

## 1103 - Bat 12V Voltage (V)

*	Type:Integer
*	Description: The voltage of the 12 volt battery as read by the Leaf’s Vehicle Control Module ECU. The Bat 12V Voltage is the fifth reply byte value times 0.08.
*	Query: 0x797 03 22 11 03 00 00 00 00
	* PCI Field: Single Frame with 3 bytes
	* Data: 22 11 03
*	Answer: 0x79A 07 62 11 03 **A3** 03 00 00
	* PCI Field: Single Frame with 7 bytes
	* Data: 62 11 03 **A3** 03 00 00 
*	Formula: Bat 12V Voltage = ( data[4] * 0.08 )

NB: Byte 4 matches 2018 data and LeafSpy screen.  Also there are three extra bytes returned, 03 00 00, that have an unknown meaning.

## 1203 - Quick Charge

*	Type: Integer
*	Description: Number of quick charges (QC). Each time a quick charge occurs this number increments by 1, even not fully.
*	Query: 0x797 03 22 12 03 00 00 00 00
	* PCI Field: Single Frame with 3 bytes
	* Data: 22 12 03
*	Answer: 0x79A 07 62 12 03 **01 1C** FF FF
	* PCI Field: Single Frame with 7 bytes
	* Data: 62 12 03 **01 1C** FF FF
*	Formula: Quick Charge = (data[4] << 8) | data[5]

NB: Bytes 4 and 5 matches 2018 data and LeafSpy screen.  Also there are two extra bytes returned, FF FF, that have an unknown meaning.

## 1205 - L1 L2 Charge

*	Type: Integer
*	Description: Number of L1/L2 connections and charges, even not fully.
*	Query: 0x797 03 22 12 05 00 00 00 00
	* PCI Field: Single Frame with 3 bytes
	* Data: 22 12 05
*	Answer: 0x79A 07 62 12 05 **08 12** FF FF
	* PCI Field: Single Frame with 7 bytes
	* Data: 62 12 05 **08 12** FF FF 
*	Formula: L1 L2 Count = (data[4] << 8) | data[5]

NB: Bytes 4 and 5 matches 2018 data and LeafSpy screen.  Also there are two extra bytes returned, FF FF, that have an unknown meaning.

## 0081 - Chassis

*	Type: String
*	Description: Chassis number 'ZE0-001093'
*	Query: 0x797 02 21 81 00 00 00 00 00
	* PCI Field: Single Frame with 2 bytes
	* Data: 21 81
*	Answer: 0x79A 10 15 61 81 **20 20 20 20**
	* PCI Field: First frame with 21 bytes total
	* Data: 61 81 **20 20 20 20**
*	Query: 0x797 30 00 0A 00 00 00 00 00
	* PCI Field: Flow Control Frame, Clear To Send, No more flow control frames, 10mS separation
*	Answer: 0x79A 21 **20 20 20 5A 45 30 2D** 
	* PCI Field: Consecutive Frame Sequence Number 1
	* Data: **'   ZE0-'**
*	Answer: 0x79A 22 **30 30 31 30 39 33 00**
	* PCI Field: Consecutive Frame Sequence Number 2
	* Data: **'001093'** 00
*	Answer: 0x79A 23 00 00 00 00 00 00 00
	* PCI Field: Consecutive Frame Sequence Number 3
	* Data: 00 00 00 00 00 00 00 
*	Formula: '   ZE0-' + '001093'

NB: This different from the 2018 data where it returns a VIN string with no time separation.

## 124E

*	Type:
*	Description:
*	Query: 0x797 03 22 12 4E 00 00 00 00
	* PCI Field: Single Frame with 3 bytes
	* Data: 22 12 4E
*	Answer: 0x79A 07 62 12 4E 00 72 00 98
	* PCI Field: Single Frame with 7 bytes
	* Data: 62 12 4E 00 72 00 98
*	Formula:

## 115D - Ambient C Temp (°C)?

*	Type:
*	Description: Probably ambient temperature
*	Query: 0x797 03 22 11 5D 00 00 00 00
	* PCI Field: Single Frame with 3 bytes
	* Data: 22 11 5D
*	Answer: 0x79A 07 62 11 5D FF 38 FF 00
	* PCI Field: Single Frame with 7 bytes
	* Data: 62 11 5D FF 38 FF 00
*	Formula:

Does not look to be calculated the same was as in the 2018.

## 1261 - EstPwr AC 50W (W)?

*	Type:
*	Description: Probably Estimated Air Conditioning system power (COOL)
*	Query: 0x797 03 22 12 61 00 00 00 00 
	* PCI Field: Single Frame with 3 bytes
	* Data: 22 12 61
*	Answer: 0x79A 07 62 12 61 00 02 02 03
	* PCI Field: Single Frame with 7 bytes
	* Data: 62 12 61 00 02 02 03
*	Formula:

## 1262 - EstPwr Htr 250W (W)?

*	Type:
*	Description: Probably Estimated Cabin PTC heater power (HEAT)
*	Query: 0x797 03 22 12 62 00 00 00 00
	* PCI Field: Single Frame with 3 bytes
	* Data: 22 12 62
*	Answer: 0x79A 07 62 12 62 00 02 00 00
	* PCI Field: Single Frame with 7 bytes
	* Data: 62 12 62 00 02 00 00
*	Formula:

## 1152 - Aux Pwr 100W (W)?

*	Type:
*	Description: Probably Power used by the auxiliary equipment (Lights, Radio, Navigation system, rear defroster...)
*	Query: 0x797 03 22 11 52 00 00 00 00
	* PCI Field: Single Frame with 3 bytes
	* Data: 22 11 52
*	Answer: 0x79A 07 62 11 52 01 28 00 02
	* PCI Field: Single Frame with 7 bytes
	* Data: 62 11 52 01 28 00 02
*	Formula:

## 1151 - AC Pwr 250W (W)?

*	Type:
*	Description: Probably A/C system Power (250W): Power used by the Air Conditioning System power. This includes the power used by the cabin PTC Heater.
*	Query: 0x797 03 22 11 51 00 00 00 00
	* PCI Field: Single Frame with 3 bytes
	* Data: 22 11 51
*	Answer: 0x79A 07 62 11 51 00 00 00 50
	* PCI Field: Single Frame with 7 bytes
	* Data: 62 11 51 00 00 00 50
*	Formula:

## 1234 - PlugState

*	Type: Integer
*	Description: Plug state of J1772 (L1/L2) charge port ( 0=Not plugged, 1=Partial Plugged, 2=Plugged )
*	Query: 0x797 03 22 12 34 00 00 00 00
	* PCI Field: Single Frame with 3 bytes
	* Data: 22 12 34
*	Answer: 0x79A 07 62 12 34 **02** 00 0A 0A
	* PCI Field: Single Frame with 7 bytes
	* Data: 62 12 34 **02** 00 0A 0A
*	Formula: PlugState = data[4]

NB: Byte 4 matches 2018 data.  Also there are three extra bytes returned, 00 0A 0A, that have an unknown meaning.

## 114E - Charge Mode

*	Type: Integer
*	Description: Charging mode. ( 0=Not charging, 1=Level 1 charging [100-120 volts], 2=Level 2 charging [200-240 volts)], 3=Level 3 Quick Charging )
*	Query: 0x797 03 22 11 4E 00 00 00 00 
	* PCI Field: Single Frame with 3 bytes
	* Data: 22 11 4E
*	Answer: 0x79A 07 62 11 4E **02** 01 1F 07
	* PCI Field: Single Frame with 7 bytes
	* Data: 62 11 4E **02** 01 1F 07
*	Formula: Charge mode = data[4]

NB: Byte 4 matches 2018 data.  Also there are three extra bytes returned, 01 1F 07, that have an unknown meaning.

## 1236 - OBC Out Pwr (W)

*	Type: Integer
*	Description: Charging power coming into the Leaf from the on-board charger, when the car is charging.
*	Query: 0x797 03 22 12 36 00 00 00 00
	* PCI Field: Single Frame with 3 bytes
	* Data: 22 12 36
*	Answer: 0x79A 07 62 12 36 **00 21** 00 1F
	* PCI Field: Single Frame with 7 bytes
	* Data: 62 12 36 **00 21** 00 1F
*	Formula: OBC Out Pwr = (( data[4] << 8 ) | data[5])*100

NB: Bytes 4 and 5 matches 2018 data and in line with LeafSpy.  Also there are three extra bytes returned, 00 1F, that have an unknown meaning.

## 1183 - Bat 12V Current (A)

*	Type: Integer
*	Description: Signed current in 1/256 A units
*	Query: 0x797 03 22 11 83 00 00 00 00
	* PCI Field: Single Frame with 7 bytes
	* Data: 22 11 83
*	Answer: 0x79A 07 62 11 83 **81 DA** 00 0E
	* PCI Field: Single Frame with 7 bytes
	* Data: 62 11 83 **81 DA** 00 0E
*	Formula: Value is (((data[4] << 8) | data[5]) - 0x8000) / 256.  Positive when charging 12V battery and negative when discharging.

NB: Bytes 4 and 5 matches LeafSpy screen.  Also there are two extra bytes returned, 00 0E, that have an unknown meaning.  Note also negative numbers maybe calculated differently from 2018 data.

This was the only message not sent during the initial sequence when LeafSpy started.  Probably because current calculation method is model dependant.

## Other possibilities

The following messages are those mentioned in the 2018 data but not seen while LeafSpy was used in a stationary car.

## 1255

Need to check drive capture to see if this is present for RPM (r/min) data.

## 1146

Need to check drive capture to see if this is present for Motor Pwr (W) data.

## 121A

Need to check drive capture to see if this is present for Speed data.

## 1106

Need to check all captures to see if this is present for AC data.

## 110F

Need to check all captures to see if this is present for RearHeater data.

