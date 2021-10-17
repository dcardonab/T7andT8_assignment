# Team Members

* David Cardona
* Robert Fischer
* Sanjeev Nandal

# Tutorial 7

## Part 1

Answer in the context of BlueZ Gatttool:

1. What is a handle and give an example of one of them

    * Handles can be used to communicate with a server for BLE services and characteristics.
    
    * Each handle corresponds to a different uuid.

2. What is a characteristic value and give an example of one of them

    * Characteristics organize attributes and uses them as data values etc.
    
    * A characteristic value is an identifier for specific features.
    
    * Characteristic value handle of environmnental data.
        * handle: 0x000e, uuid: 00140000-0001-11e1-ac36-0002a5d5c51b

5. Translate the data recorded in the final text file: test.txt to physical values. (you could write a python program to automate this, otherwise you can do it manually.)


# Tutorial 2

## Part 1

1. GATT is used exclusively after a connection has been established between the two devices. (True or False)

    * Answer: True

2. Complete the sentence below:

    We use SensorTile as the GATT ____________

    a. Server

    b. Client

    c. Peer

    d. Service

    * Answer: A

3. Complete the sentence below:

    We use BeagleBone Black Rev. C/Raspberry Pi3B+/Pi Zero W as the GATT ___________

    a. Server

    b. Client

    c. Peer

    d. Service

    * Answer: B

4. Complete the sentence below:

    We can discover, read, and write characteristics with gatttool.

    GATT stands for **Generic Attribute Profile** and defines a data structure for organizing characteristics and attributes


## Part 2

1. Take screenshots corresponding to Figures 8, 13 and 15

2. Save Requested Motion Data to Text File as in section 4 of the tutorial 8 and submit  text file: motion_data.txt


# Notes

* GATT stands for Generic Attributes, and it defines a hierarchical data structure that is exposed to connected BLE devices.

* GATT is built on top of the Attribute Protocol (ATT), which uses GATT data to define the way that two BLE devices send and receive standard messages.

* T7 uses the SensorTile as the GATT server to provide services, and the BeagleBone as the GATT client to send requests to the GATT server. This is done via the `gatttool`.

* `gatttool` is the BlueZ utility that handles BLE communication with GATT.

* In the command `gatttool -b C0:6E:48:32:48:36 -t random -I`, `-b` is the option to indicate the mac address. `-t` is the option to declare the Bluetooth MAC address type, which is set to type random in the BLE_Sample App firmware. `-I` is the option to use gatttool in interactive mode.

* The first 4 bits (hexadecimal) received by the client are time stamps. The next 8 bits are air pressure data. The last 4 bits are temperature data from temperature sensor 1.

* The data displayed by the server should be interpreted as having two digits after the decimal point for the pressure data (mbar), and one digit after the decimal point for the temperature (celsius).

* The environmental data should be read from right to left (little endian rule).

* The ST LED is composed of feature mask (F), which is 20000000, and command (C), which is 01 (1).

* Characteristic value handle of environmnental data.

    * handle: 0x000e, uuid: 00140000-0001-11e1-ac36-0002a5d5c51b

* Client characteristic configuration handle for environmetanl data transmission.

    * handle: 0x000f, uuid: 00002902-0000-1000-8000-00805f9b34fb

* SensorTile LED configuration handle.

    * handle: 0x001b, uuid: 00000002-000f-11e1-ac36-0002a5d5c51b
