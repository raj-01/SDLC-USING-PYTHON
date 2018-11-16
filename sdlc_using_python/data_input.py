import math 

def int_to_binary_8_bit( N ) :
	
	bit_str = '' ; 
	for i in range(0 , 8):
        	bit_str = bit_str + str( int(N%2) );
        	N = math.floor(N/2) ;
         
	return bit_str ; 





#taking input data in hex format in range 0 - ff  
hex_info_field = raw_input('give input data in hex format (in range 0 - ff ) = ') ;
hex_info_field = str(hex_info_field ) ;
info_field = int_to_binary_8_bit(int( hex_info_field , 16 )) ; 



# address field 
hex_addr_field = raw_input("give address field in hex format (in range 0 - ff ) : " );
hex_addr_field = str(hex_addr_field ) ;
addr_field = int_to_binary_8_bit(int( hex_addr_field , 16 )) ; 



# control field 
hex_control_field = raw_input("give control field in hex format (in range 0 - ff ) : " );
hex_control_field = str(hex_control_field ) ;
control_field = int_to_binary_8_bit(int( hex_control_field , 16 )) ; 



#int to list conversion ( list of ints )
input_a_c_i =  addr_field + control_field + info_field; 



