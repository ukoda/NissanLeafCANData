# 2011 ZE0 Nissan Leaf

The files here are the 2011 ZE0.

## DBC files

The DBC files present are:

### 2011_ze0_ev_dala_0x11a_to_0x68c.dbc

The original file name was `EV-can_ZE0.dbc` and comes [Dala's repo](https://github.com/dalathegreat/leaf_can_bus_messages).  It covers 28 message type from 0x11a to 0x68c captured on the EV bus, not the main car bus, with the focus on working directly with battery pack.  However where theses messages are present on the car bus the format is likely to be the same.

## Message description

These are human readable markdown format descriptions of messages.

### Leaf_2011_ZE0_Messages.md

This is an overview of the messages which includes the list of ECUs.

### Leaf_2011_ZE0_Messages_VCM.md

The details of messages exchanged with the Vehicle Control Module (VCM).

## Other information sources

*	SafetyUggs [ZE0_3NA0D_cyclic_CAN_frames.md](https://github.com/SafetyUggs/Leaf-BMS-Reverse-Engineering/blob/main/ZE0(3NA0D)/ZE0_3NA0D_cyclic_CAN_frames.md) Nissan Leaf ZE0 battery controller (LBC): cyclic CAN frames.  Details the structure of several battery related messages.  All of the messages detailed appear in `2011_ze0_ev_dala_0x11a_to_0x68c.dbc`.
*	SafetyUggs [ZE0_3NA0D_diagnostic_services.md](https://github.com/SafetyUggs/Leaf-BMS-Reverse-Engineering/blob/main/ZE0(3NA0D)/ZE0_3NA0D_diagnostic_services.md) Nissan Leaf ZE0 battery controller (LBC): diagnostic services.
*	SafetyUggs [ze0_bms_soh.md](https://github.com/SafetyUggs/Leaf-BMS-Reverse-Engineering/blob/main/ZE0(3NA0D)/ze0_bms_soh.md) How the Leaf ZE0 BMS works out SOH.