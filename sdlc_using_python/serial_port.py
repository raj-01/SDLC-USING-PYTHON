import serial 


def serial_open():
		global pulse ; 
		pulse = serial.Serial("/dev/ttyACM0", 9600 , timeout = 10 ) ; 
		if  pulse.isOpen() : 
     			is_connection_estab = True ;
		else :
     			is_connection_estab = False ; 
		return is_connection_estab ; 


def serial_write( data ):
	pulse.write(data);


def serial_read() :
	return pulse.read() ; 


def serial_close() :
	shut_down = pulse.close() ;

	if shut_down < 0 : 
		is_connection_terminated = True ; 
	else : 
    		is_connection_terminated = False ; 


	return is_connection_terminated ; 









