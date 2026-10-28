# Nissan Leaf 2011 ZE0 VCM ECU

These are UDS messages you can send to the VCM ECU to make queries and get responses.

These are the queries (0x797) and responses (0x79A) that can be made of the VCM.

There are 3 layers of protocols in use, as detailed in the root folder README.md.  In the linked documents for messages relating to ECUs the raw ISO 15765‐4 (CAN 11/500) is first shown with the parts relating to ISO 14229-1 (UDS) and ISO 15765-2 (ISO-TP) indented.

With UDS messages there are:

* SI: The Service identifier.
* DID: The Data Identifier. A DID basically identifies a piece of ECU data.

While the message may have 8 bytes of data ISO-TP indicates the length of the data actually used, the reset can be ignored and are no shown in the indented data information

The messages are named using the UDS DID field followed by a descriptive name when the message usage is known.  Where matches are found names used are the same as in the existing `Leaf2018-CAN.pdf` document.

## UDS Session control

This message must be sent before requesting DID information.  It set the ECU session to a Nissan specific type.

*	Type: UDS protocol
*	Description: Needed before other messages are sent to the VCM
*	Query: 0x797 02 10 C0 00 00 00 00 00
	* ISO-TP PCI Field: 02 = Single Frame with 2 bytes
	* UDS PCI Field: 10 C0 = Diagnostic Session Control service request vehicle manufacturer specific with suppressPosRspMsgIndication bit set 
*	Answer: 0x79A 02 50 C0 00 00 00 00 00 
	* ISO-TP PCI Field: 02 = Single Frame with 2 bytes
	* UDS PCI Field: 50 C0 = Diagnostic Session Control service confirmation reply

## 0x1304 - Power Software

*	Type: Boolean
*	Description: Power SW is True if the Leaf’s power switch is ON otherwise it is False. The fifth reply byte value is 0x80 if the car is powered on.
*	Query: 0x797 03 22 13 04 00 00 00 00
	* ISO-TP PCI Field: 03 = Single Frame with 3 bytes
	* UDS PCI Field: 22 13 04 = Read Data By Identifier request for DID 0x1304
*	Answer: 0x79A 05 62 13 04 **00** BA 00 00
	* ISO-TP PCI Field: 05 = Single Frame with 5 bytes
	* UDS PCI Field: 62 13 04 = Read Data By Identifier reply for DID 0x1304
	* Data: **00** BA
*	Formula: Power SW = (data[4] & 128 == 128)

## 0x1156 - Gear

*	Type: Integer
*	Description: Gear position (1=Park, 2=Reverse, 3=Neutral, 4=Drive, 7=Eco). The fifth reply byte value is the gear value.
*	Query: 0x797 03 22 11 56 00 00 00 00
	* ISO-TP PCI Field: 03 = Single Frame with 3 bytes
	* UDS PCI Field: 22 11 56 = Read Data By Identifier request for DID 0x1156
*	Answer: 0x79A 07 62 11 56 **01** 00 01 01
	* ISO-TP PCI Field: 07 = Single Frame with 7 bytes
	* UDS PCI Field: 62 11 56 = Read Data By Identifier reply for DID 0x1156
	* Data: **01** 00 01 01
*	Formula: Gear = data[4]

NB: Byte 4 matches 2018 data but should check against data captured during actual drive.  Also there are three extra bytes returned, 00 01 01, that have an unknown meaning.

## 0x132A

*	Type:
*	Description:
*	Query: 0x797 03 22 13 2A 00 00 00 00
	* ISO-TP PCI Field: 03 = Single Frame with 3 bytes
	* UDS PCI Field: 22 13 2A = Read Data By Identifier request for DID 0x132A
*	Answer: 0x79A 05 62 13 2A 00 60 00 00
	* ISO-TP PCI Field: 05 = Single Frame with 5 bytes
	* UDS PCI Field: 62 13 2A = Read Data By Identifier reply for DID 0x132A
	* Data: 00 60
*	Formula:

NB: Answer data 00 changes to 10 when power on.

## 0x1103 - Bat 12V Voltage (V)

*	Type:Integer
*	Description: The voltage of the 12 volt battery as read by the Leaf’s Vehicle Control Module ECU. The Bat 12V Voltage is the fifth reply byte value times 0.08.
*	Query: 0x797 03 22 11 03 00 00 00 00
	* ISO-TP PCI Field: 03 = Single Frame with 3 bytes
	* UDS PCI Field: 22 11 03 = Read Data By Identifier request for DID 0x1103
*	Answer: 0x79A 07 62 11 03 **A3** 03 00 00
	* ISO-TP PCI Field: 07 = Single Frame with 7 bytes
	* UDS PCI Field: 62 11 03 = Read Data By Identifier reply for DID 0x1103
	* Data: **A3** 03 00 00 
*	Formula: Bat 12V Voltage = ( data[4] * 0.08 )

NB: Byte 4 matches 2018 data and LeafSpy screen.  Also there are three extra bytes returned, 03 00 00, that have an unknown meaning.

## 0x1203 - Quick Charge

*	Type: Integer
*	Description: Number of quick charges (QC). Each time a quick charge occurs this number increments by 1, even not fully.
*	Query: 0x797 03 22 12 03 00 00 00 00
	* ISO-TP PCI Field: 03 = Single Frame with 3 bytes
	* UDS PCI Field: 22 12 03 = Read Data By Identifier request for DID 0x1203
*	Answer: 0x79A 07 62 12 03 **01 1C** FF FF
	* ISO-TP PCI Field: 07 = Single Frame with 7 bytes
	* UDS PCI Field: 62 12 03 = Read Data By Identifier reply for DID 0x1203
	* Data: **01 1C** FF FF
*	Formula: Quick Charge = (data[4] << 8) | data[5]

NB: Bytes 4 and 5 matches 2018 data and LeafSpy screen.  Also there are two extra bytes returned, FF FF, that have an unknown meaning.

## 0x1205 - L1 L2 Charge

*	Type: Integer
*	Description: Number of L1/L2 connections and charges, even not fully.
*	Query: 0x797 03 22 12 05 00 00 00 00
	* ISO-TP PCI Field: 03 = Single Frame with 3 bytes
	* UDS PCI Field: 22 12 05 = Read Data By Identifier request for DID 0x1205
*	Answer: 0x79A 07 62 12 05 **08 12** FF FF
	* ISO-TP PCI Field: 07 = Single Frame with 7 bytes
	* UDS PCI Field: 62 12 05 = Read Data By Identifier reply for DID 0x1205
	* Data: **08 12** FF FF 
*	Formula: L1 L2 Count = (data[4] << 8) | data[5]

NB: Bytes 4 and 5 matches 2018 data and LeafSpy screen.  Also there are two extra bytes returned, FF FF, that have an unknown meaning.

## 0x0081 - Chassis

NB: The SI of 0x21 is not defined in ISO 14229-1 (UDS).  If anyone knows it's meaning please let me know.

*	Type: String
*	Description: Chassis number 'ZE0-001093'
*	Query: 0x797 02 21 81 00 00 00 00 00
	* ISO-TP PCI Field: 02 = Single Frame with 2 bytes
	* UDS PCI Field: 21 81 = Unknown UDS SI, assuming request for DID 0x0081
*	Answer: 0x79A 10 15 61 81 **20 20 20 20**
	* ISO-TP PCI Field: First frame with 21 bytes total
	* UDS PCI Field: 21 81 = Unknown UDS SI, assuming reply for DID 0x0081
	* Data: **20 20 20 20**
*	Query: 0x797 30 00 0A 00 00 00 00 00
	* ISO-TP PCI Field: Flow Control Frame, Clear To Send, No more flow control frames, 10mS separation
*	Answer: 0x79A 21 **20 20 20 5A 45 30 2D** 
	* ISO-TP PCI Field: Consecutive Frame Sequence Number 1
	* Data: **'   ZE0-'**
*	Answer: 0x79A 22 **30 30 31 30 39 33 00**
	* ISO-TP PCI Field: Consecutive Frame Sequence Number 2
	* Data: **'001093'** 00
*	Answer: 0x79A 23 00 00 00 00 00 00 00
	* ISO-TP PCI Field: Consecutive Frame Sequence Number 3
	* Data: 00 00 00 00 00 00 00 
*	Formula: '    ' + '   ZE0-' + '001093'

NB: This different from the 2018 data where it returns a VIN string with no time separation.

## 0x124E

*	Type:
*	Description:
*	Query: 0x797 03 22 12 4E 00 00 00 00
	* ISO-TP PCI Field: 03 = Single Frame with 3 bytes
	* UDS PCI Field: 22 12 4E = Read Data By Identifier request for DID 0x124E
*	Answer: 0x79A 07 62 12 4E 00 72 00 98
	* ISO-TP PCI Field: 07 = Single Frame with 7 bytes
	* UDS PCI Field: 62 12 4E = Read Data By Identifier reply for DID 0x124E
	* Data: 00 72 00 98
*	Formula:

## 0x115D - Ambient C Temp (°C)?

*	Type:
*	Description: Probably ambient temperature
*	Query: 0x797 03 22 11 5D 00 00 00 00
	* ISO-TP PCI Field: 03 = Single Frame with 3 bytes
	* UDS PCI Field: 22 11 5D = Read Data By Identifier request for DID 0x115D
*	Answer: 0x79A 07 62 11 5D FF 38 FF 00
	* ISO-TP PCI Field: 07 = Single Frame with 7 bytes
	* UDS PCI Field: 62 11 5D = Read Data By Identifier reply for DID 0x115D
	* Data: FF 38 FF 00
*	Formula:

Does not look to be calculated the same was as in the 2018.  Ambient temperature was likely 15C to 20C range.

## 0x1261 - EstPwr AC 50W (W)?

*	Type:
*	Description: Probably Estimated Air Conditioning system power (COOL)
*	Query: 0x797 03 22 12 61 00 00 00 00 
	* ISO-TP PCI Field: 03 = Single Frame with 3 bytes
	* UDS PCI Field: 22 12 61 = Read Data By Identifier request for DID 0x1261
*	Answer: 0x79A 07 62 12 61 00 02 02 03
	* ISO-TP PCI Field: 07 = Single Frame with 7 bytes
	* UDS PCI Field: 62 12 61 = Read Data By Identifier reply for DID 0x1261
	* Data: 00 02 02 03
*	Formula:

## 0x1262 - EstPwr Htr 250W (W)?

*	Type:
*	Description: Probably Estimated Cabin PTC heater power (HEAT)
*	Query: 0x797 03 22 12 62 00 00 00 00
	* ISO-TP PCI Field: 03 = Single Frame with 3 bytes
	* UDS PCI Field: 22 12 62 = Read Data By Identifier request for DID 0x1262
*	Answer: 0x79A 07 62 12 62 00 02 00 00
	* ISO-TP PCI Field: 07 = Single Frame with 7 bytes
	* UDS PCI Field: 62 12 62 = Read Data By Identifier reply for DID 0x1262
	* Data: 00 02 00 00
*	Formula:

## 0x1152 - Aux Pwr 100W (W)?

*	Type:
*	Description: Probably Power used by the auxiliary equipment (Lights, Radio, Navigation system, rear defroster...)
*	Query: 0x797 03 22 11 52 00 00 00 00
	* ISO-TP PCI Field: 03 = Single Frame with 3 bytes
	* UDS PCI Field: 22 11 52 = Read Data By Identifier request for DID 0x1152
*	Answer: 0x79A 07 62 11 52 01 28 00 02
	* ISO-TP PCI Field: 07 = Single Frame with 7 bytes
	* UDS PCI Field: 62 11 52 = Read Data By Identifier reply for DID 0x1152
	* Data: 01 28 00 02
*	Formula:

## 0x1151 - AC Pwr 250W (W)?

*	Type:
*	Description: Probably A/C system Power (250W): Power used by the Air Conditioning System power. This includes the power used by the cabin PTC Heater.
*	Query: 0x797 03 22 11 51 00 00 00 00
	* ISO-TP PCI Field: 03 = Single Frame with 3 bytes
	* UDS PCI Field: 22 11 51 = Read Data By Identifier request for DID 0x1151
*	Answer: 0x79A 07 62 11 51 00 00 00 50
	* ISO-TP PCI Field: 07 = Single Frame with 7 bytes
	* UDS PCI Field: 62 11 51 = Read Data By Identifier reply for DID 0x1151
	* Data: 00 00 00 50
*	Formula:

## 0x1234 - PlugState

*	Type: Integer
*	Description: Plug state of J1772 (L1/L2) charge port ( 0=Not plugged, 1=Partial Plugged, 2=Plugged )
*	Query: 0x797 03 22 12 34 00 00 00 00
	* ISO-TP PCI Field: 03 = Single Frame with 3 bytes
	* UDS PCI Field: 22 12 34 = Read Data By Identifier request for DID 0x1234
*	Answer: 0x79A 07 62 12 34 **02** 00 0A 0A
	* ISO-TP PCI Field: 07 = Single Frame with 7 bytes
	* UDS PCI Field: 62 12 34 = Read Data By Identifier reply for DID 0x1234
	* Data: **02** 00 0A 0A
*	Formula: PlugState = data[4]

NB: Byte 4 matches 2018 data.  Also there are three extra bytes returned, 00 0A 0A, that have an unknown meaning.

## 0x114E - Charge Mode

*	Type: Integer
*	Description: Charging mode. ( 0=Not charging, 1=Level 1 charging [100-120 volts], 2=Level 2 charging [200-240 volts)], 3=Level 3 Quick Charging )
*	Query: 0x797 03 22 11 4E 00 00 00 00 
	* ISO-TP PCI Field: 03 = Single Frame with 3 bytes
	* UDS PCI Field: 22 11 4E = Read Data By Identifier request for DID 0x114E
*	Answer: 0x79A 07 62 11 4E **02** 01 1F 07
	* ISO-TP PCI Field: 07 = Single Frame with 7 bytes
	* UDS PCI Field: 62 11 4E = Read Data By Identifier reply for DID 0x114E
	* Data: **02** 01 1F 07
*	Formula: Charge mode = data[4]

NB: Byte 4 matches 2018 data.  Also there are three extra bytes returned, 01 1F 07, that have an unknown meaning.

## 0x1236 - OBC Out Pwr (W)

*	Type: Integer
*	Description: Charging power coming into the Leaf from the on-board charger, when the car is charging.
*	Query: 0x797 03 22 12 36 00 00 00 00
	* ISO-TP PCI Field: 03 = Single Frame with 3 bytes
	* UDS PCI Field: 22 12 36 = Read Data By Identifier request for DID 0x1236
	* Data: 22 12 36
*	Answer: 0x79A 07 62 12 36 **00 21** 00 1F
	* ISO-TP PCI Field: 07 = Single Frame with 7 bytes
	* UDS PCI Field: 62 12 36 = Read Data By Identifier reply for DID 0x1236
	* Data: **00 21** 00 1F
*	Formula: OBC Out Pwr = (( data[4] << 8 ) | data[5])*100

NB: Bytes 4 and 5 matches 2018 data and in line with LeafSpy.  Also there are three extra bytes returned, 00 1F, that have an unknown meaning.

## 0x1183 - Bat 12V Current (A)

*	Type: Integer
*	Description: Signed current in 1/256 A units
*	Query: 0x797 03 22 11 83 00 00 00 00
	* ISO-TP PCI Field: 03 = Single Frame with 3 bytes
	* UDS PCI Field: 22 11 83 = Read Data By Identifier request for DID 0x1183
*	Answer: 0x79A 07 62 11 83 **81 DA** 00 0E
	* ISO-TP PCI Field: 07 = Single Frame with 7 bytes
	* UDS PCI Field: 62 11 83 = Read Data By Identifier reply for DID 0x1183
	* Data: **81 DA** 00 0E
*	Formula: Value is (((data[4] << 8) | data[5]) - 0x8000) / 256.  Positive when charging 12V battery and negative when discharging.

NB: Bytes 4 and 5 matches LeafSpy screen.  Also there are two extra bytes returned, 00 0E, that have an unknown meaning.  Note also negative numbers maybe calculated differently from 2018 data.

This was the only message not sent during the initial sequence when LeafSpy started.  Probably because current calculation method is model dependant.

## Other possibilities

The following messages are those mentioned in the 2018 data but not seen while LeafSpy was used in a stationary car.

## 0x1255

Need to check drive capture to see if this is present for RPM (r/min) data.

## 0x1146

Need to check drive capture to see if this is present for Motor Pwr (W) data.

## 0x121A

Need to check drive capture to see if this is present for Speed data.

## 0x1106

Need to check all captures to see if this is present for AC data.

## 0x110F

Need to check all captures to see if this is present for RearHeater data.

