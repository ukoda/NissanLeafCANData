# 2011 ZE0 Nissan Leaf

The captures here are from a Japanese domestic market 2011 ZE0 imported to New Zealand and it has had an UK infotainment system installed.

Probably the most useful capture here is the `car_leafspy.csv` file detailed in the Car CAN captures section.

Generally filenames start with the CAN bus name so filenames starting with `car_` relate to data that normal ODB2 adaptor can see.  The other files are more useful for custom hardware that will be added to the related bus.

At this time there are no DBC files present.  These will be the next focus of activity here.

## Car CAN captures

These are messages captured from the main Car CAN bus which is only bus a traditional ODB2 adaptor can access.

### car_leafspy.csv

A splitter was used so that messages could be capture while LeafSpy was connected to a LELink.  This has the advantage over other captures that LeafSpy will send messages and get replies from message type not seen normally.  This capture should have all the messages needed for the information that LeafSpy shows.

The capture started before LeafSpy was started so the initialisation sequence used by LeafSpy can be see.  The car was parked and charging during this capture.

There are four screen capture files, `LeafSpy1.png` to `LeadfSpy4.png` that show the data LeafSpy saw.

### car_drive.csv

The car started as off, was then driven, parked, plugged in and charging enabled.  There is a delay between when the car was plugged and the EVSE was told it was allowed to charge the car.  After a short time charging was stopped.

## EV CAN captures

These are messages captured from the EV CAN bus.

### ev_charging.csv

This is with the car plugged in to an AC EVSE configured to deliver 8 to 20 Amps from about 250V (long story why so high).  The vehicle was actively charging and was probably in the 65% to 90% SoC range at the time of capture.

### ev_drive.csv

This was a short drive starting with the car off, then driven down the road with bursts of relatively hard acceleration, parked and turned off.

### ev_idle.csv

This was with the car parked and off.  The car was taken to the accessory state then turned off again.  It was not charging.

## AV CAN captures

These are messages captured from the AV CAN bus.

### av.csv

For this capture was started with the vehicle off.  The vehicle was turned on and the infotainment system was allowed to boot and connect to a Bluetooth phone playing music from Spotiy.  The buttons on the steering wheel where then used to, in order:

1. Volume turned up.
2. Volume turned down.
3. Seek forward to next track.
4. Seek backwards to start of current track.

The vehicle was then turned off and capture stopped after when CAN messages stopped being sent on this bus.