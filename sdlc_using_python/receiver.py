import serial_port 
import time 
import nrzi 
import bit_stuffing
import crc  
import binascii
import utf8_to_decimal
import int_lookup  
import hex_lookup 

def data_received(time_for_receiving_data):

		#if serial_port.serial_open() == False :
		#	print("error :serial connection for reading data is not established") ;
			#is_receiver_ready = False ;
			#exit(1) ; 
		#else  :
			#is_receiver_ready = True ; 			

		
	
		#if  is_receiver_ready == True :
			detect_start_flag = '';
			detect_end_flag = '' ; 
			is_start_flag_detected = False ;
			is_end_flag_detected = False ; 
			store_data = '' ;  
			
			time_out1 = (time.time())*1000 + time_for_receiving_data*1000 ;    # setting timer of milli sec resolution 
			
			temp = '1' ;
			f = open('rx_file.txt' , 'r+') ;
			#read_data  = f.read() ;  
			#print( read_data ) ;
			count = 0 ; 
			while ( time_out1 > (time.time())*1000 ) :	
			#for itr in read_data :	
				#alpha = itr ;  
				alpha = serial_port.serial_read();
								
				count = count + 1 ; 
				#alpha = binascii.a2b_qp(alpha);
				#print(alpha) 
				#alpha = int_lookup.utf8_int_lookup( alpha ) ;
				#alpha = hex_lookup.hex_int(alpha)
				#if len(str(alpha)) == 0 :
					#int_alpha = alpha ;  	 
					#alpha = utf8_to_decimal.decode_utf8( alpha );			
				
				 
				if alpha != None :
					 
					alpha = bin(int(alpha ))[2:] ; 
					f.write( alpha ) ;
					#f.write('e') ; 
				 	#temp = str(alpha) ;
  					#f.write( temp ) ;
					#print( temp ) ;  
					temp = nrzi.nrzi_decode(int(temp) , int(alpha) ) ;
					#f.write( temp ) ; 
					 
					if is_end_flag_detected == False and is_start_flag_detected == True :
						detect_end_flag = detect_end_flag + temp
						#print( detect_end_flag ) ; 
						if detect_end_flag == '01111110' :
							is_end_flag_detected = True ;
							store_data = store_data[0:-7] ;    # removing residul end flag from store data 
							      								
							break ; 
						if len( detect_end_flag ) == 8 :
							detect_end_flag = detect_end_flag[1:] ; 


 					if is_start_flag_detected == True and is_end_flag_detected == False :
						store_data = store_data + temp ;


					if is_start_flag_detected == False :
						detect_start_flag = detect_start_flag + temp ;
						#print(detect_start_flag) ; 
			 			if detect_start_flag == '01111110' :
							is_start_flag_detected = True ;
						
						if len( detect_start_flag ) == 8 :
							detect_start_flag = detect_start_flag[1:]  ;
					
					
						 				
				temp = alpha ; 
					

			time_out2 = (time.time())*1000 + time_for_receiving_data*1000 ;
			print( "total time of execution " , time_out2 - time_out1 ) ; 
			
			if serial_port.serial_close() == False : 
				print(" serial connection is still alive for receiving data") ;

			print(count) ;
			is_data_correct = False ; 				
			
			if  is_end_flag_detected == True :
				print('yeah end flag detected') ; 
				zero_removed_data = bit_stuffing.zero_bit_removal(store_data) ; 
				check_zero_removed_data = crc.crc_check(zero_removed_data ) ;
				if check_zero_removed_data == '1111000010111000' :
					is_data_correct = True ; 
					return ( is_data_correct , zero_removed_data[0:-16]) ;   # removing 16 bit crc and returning addr + control + information 
				else :	
					print('data is corrupted ') ; 
					return ( is_data_correct , '' ) ;  

			elif  is_end_flag_detected == False :
					return ( is_data_correct , '' ) ; 
				


	
				
				

 
