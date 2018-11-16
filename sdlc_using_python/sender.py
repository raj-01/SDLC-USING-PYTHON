import data_input 
import serial_port 
import time 
import nrzi 
import bit_stuffing
import crc
def send_data() :
			
		crc_remainder = crc.crc_remainder(data_input.input_a_c_i) ;
 		crc_codded_data = data_input.input_a_c_i + crc_remainder ; 
		zero_inserted_data = bit_stuffing.zero_bit_insertion( crc_codded_data ) ;
		

		# start flag
		start_flag =  "01111110";
		#end flag 
		end_flag = "01111110" ;

		sdlc_format_data  = start_flag + zero_inserted_data + end_flag ;     
	
		# adding syncronisation bits  0000000000000000
		sdlc_format_data = '0000000000000000' + sdlc_format_data ; 
		print(sdlc_format_data);
		nrzi_encoded_sdlc_data = nrzi.nrzi_encode( sdlc_format_data ) ; 	

	  	print( nrzi_encoded_sdlc_data ) ; 
				
		if serial_port.serial_open() == False :
			print("error :serial connection for sending data is not established") ;
		else  :	

			
			for itr in  nrzi_encoded_sdlc_data :
				time.sleep(0.000115) ; 
				serial_port.serial_write( itr ) ;


		#time.sleep(0.000115) ;		
		#serial_port.serial_write( 'e' ) ;
		#print( serial_port.serial_read() ) ; 	
		#while( serial_port.serial_read() != 'c' ):
				#serial_port.serial_write( 'e' ) ;
				#print('b') ;
				#time.sleep(0.000115) ; 
				

		#if serial_port.serial_close() == False : 
		#	print("serial connection for sending data is still alive") ; 

		#time.sleep(0.5) ; 
		return True ; 


