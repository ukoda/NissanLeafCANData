# Nissan Leaf CAN Data

This is a collection of CAN data and DBC files for the Nissan Leaf.

The intention is to get all the CAN data for different models of Nissan Leafs in one place as a resource for working with tools that use this data.

I was driven by my need for sample data for the 2011 ZE0 and being unable to find a DBC file that could decode the messages I was wanting to use.

Basically there is plenty of information on CAN messages for the Nissan Leaf but it is often for a different model from the one you need and the message formats have changed from model to model.

This repo will first focus on the ZEO as that is what I have so what I can capture messages from.  Hopefully others may see this as a place to add information they have found for their model, but does risk just being another site with the same good intent, much like the XKCD situation with standards:

![](standards.png)

The structure of this repo is a utilities folder and one folder for each model of Leaf.  In that folder at minimum we want:

* A README.md file detailing each of the other files in the folder
	* The README.md should list supporting links and credits where the work of others has helped source the information.
	* For DBC files it should indicate what busses it relates to and what messages or group of messages it decodes.  Comments of completeness or limitations are often helpful.
	* For captured data it should indicate which bus the data was captured from and what state the vehicle was in.
	* For images it should indicate which data capture(s) it relates to.
	* For PDF the original source should be provided.
* Supporting DBC files.
* Captured data used to create and test DBC files.  At this time I am using excellent and free SavvyCAN that saves captured data in simple CSV files.

We can optionally have supporting files such as:

* PDF documents that detail message formats.
* Images that show what the vehicle state is at the time of a capture, such as a photo of the vehicle dash or LeafSpy screen captures.

## SavvyCAN

For collecting and analysing CAN message I use the open source cross platorm [SavvyCAN](https://savvycan.com/) software.

TODO: Added a link to SavvyCAN user guide if good on exists.

While the classic ELM327 type ODB2 adaptor is popular for accessing a desired subset of the CAN messages it needs to filter messages as it has serious performance limitation.  The main Leaf bus can have over 1000 CAN messages being sent every second when the car is ready to drive.  The ELM327 can only handle a fraction of that number of messages in a second.  Therefore I use a [Peak System CAN to USB adaptor](https://www.aliexpress.com/item/1005011625782729.html) which is cheap and can keep up with the full message rate of the Leaf CAN bus. NB: SavvyCAN recommend the CANDue board, which is about 10 times the price of the one I used.

There was a few issues with getting SavvyCAN and the Peak CAN USB set up and working on my Linux system.  The key steps on my Linux Mint system where:

1. [Downloaded SavvyCAN](https://github.com/collin80/SavvyCAN/releases) as a Linux AppImage to a location on path, changed to a+x and created softlink as savvycan.  If you only wish to view CAN captures you SavvyCAN should now work.  The rest of the steps are perform captures.
2. `sudo apt install libsocketcan2*`
3. Plug in the Peak CAN USB.  Check `dmesg` that is was detected as `can0`.
4. `sudo ip link set can0 up type can bitrate 500000`
5. Start SavvyCAN.
6. Open connection page from "Connection" menu.
7. Click "Add New Device Connection"
8. Select "Connection Type" as "QT SerialBus Devices(SocketCAN, PeakCAN, etc)
9. Select "SerialBus Device Type:" as "socketcan"
10. Select "Port:" as "can0". If `can0` is not a drop down option you have done something wrong.  Check step 3 again.
11. Click on "Create New Connection".

Packets should now start being captured. The Left two LEDs on the Peak CAN will be on and the right on will flash with packets. 

## CAN busses

Leaf has three CAN busses, as detailed [here](https://leaf-obd.readthedocs.io/en/latest/diagnostic-connector.html), on the ODB2 port.

They are:

1. Pins 6 and 14. The Car CAN bus which has messages related to general vehicle operation including EV related messages.  It is the standard CAN bus for ODB2 adaptors and is the default to focus on unless you have a specific reason to focus on one of the other two.
2. Pins 13 and 12. The EV CAN bus which has messages related to the battery and drive system.
3. Pins 11 and 3.  The AV CAN bus which has messages related to the infotainment system.

For the Peak USB CAN adaptor it does not have an ODB2 type connector, just three screw terminals.  I used the connector and case from a cheap ELM327 adaptor that was unreliable and removed the PCBA from it.  I fitted a three way switch to select the bus I want to capture from the OSB2 connector and from the switch a cable to the Peak USB CAN.