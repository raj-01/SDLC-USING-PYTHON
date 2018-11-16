 


def crc_remainder(input_data) :

#int to list conversion ( list of ints )                  
	crc_polynomial = '10001000000100001' ; 
	input_data = map(int, input_data); 
        remainder_bits = [];
        for i in range(len(crc_polynomial)-1):
        	remainder_bits.append(1) ;  # initiatlising reminder bit 

                  
	# calculating reminder of crc 

        for itr in input_data : 
        	zor_ = (remainder_bits[-1])^itr ; 
       		remainder_bits.insert(0,zor_) ;
        	del remainder_bits[-1];
        	remainder_bits[12] = (remainder_bits[12])^zor_ ;
        	remainder_bits[5] = (remainder_bits[5])^zor_ ;
        
	for idx in range(len(remainder_bits)) :
		if remainder_bits[idx] == 1 :
			remainder_bits[idx] = 0 ;
		elif remainder_bits[idx] == 0 :
			remainder_bits[idx] = 1 ;

	remainder_bits = remainder_bits[::-1] ;
	# list to string conversion 
	remainder_bits = ''.join( str( itr )  for itr in remainder_bits ) ;
	return remainder_bits ;  


def crc_check( input_data) :

#int to list conversion ( list of ints )                  
	crc_polynomial = '10001000000100001' ;
	input_data = map(int, input_data); 
        remainder_bits = [];
        for i in range(len(crc_polynomial)-1):
        	remainder_bits.append(1) ;  # initiatlising reminder bit 

                  
	# calculating reminder of crc 

        for itr in input_data : 
        	zor_ = (remainder_bits[-1])^itr
       		remainder_bits.insert(0,zor_) ;
        	del remainder_bits[-1];
        	remainder_bits[12] = (remainder_bits[12])^zor_ ;
        	remainder_bits[5] = (remainder_bits[5])^zor_ ;
	# list to string conversion 
	remainder_bits = ''.join( str( itr )  for itr in remainder_bits ) ;
	return remainder_bits ; 









        
		
