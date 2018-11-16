***** To run the programme in terminal ---> python master.py 

**** master.py automaticaly first run the sender.py and if sending part is done succesfully then it will run receiver.py  

****usb port and baud rate required has to be manualy updated in serial_port.py. 

**** nrzi decoding function will take two arguments in receiver.py 

**** utf8 decoding is not used for now but have to use if data received in pc is of fully using usb 8 bit protocol . currenty one bit comunication is happening so no chance of utf8 encoding in usb protocol . Not if using fully 8 bit of usb protocol then nrzi decode function has to be modified for that number of bits  .
