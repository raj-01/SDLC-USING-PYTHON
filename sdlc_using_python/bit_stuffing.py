

def  zero_bit_insertion(crc_codded_data) :
	#after five ones , zero insertion in  crc_codded_data i.e. in addr_field + controled_field + data + reminder_ byte
	temp = crc_codded_data ;

	zero_inserted_data = str('') ;

	while( len(temp) >= 5 ) :
        	if temp[:5] == '11111' : 
        	        zero_inserted_data = zero_inserted_data + '111110';
                
               
        	        if len(temp) == 5 : 
        	             temp  = '' ;
        	        else :
        	                temp  = temp[5:-1] + temp[-1];
        	        if len(temp) < 5 :
        	             zero_inserted_data = zero_inserted_data + temp;
        	else :
        	        zero_inserted_data = zero_inserted_data + temp[0];
                
        	        temp = temp[1:-1] + temp[-1];
        	        if len(temp) < 5 :
        	             zero_inserted_data = zero_inserted_data + temp;   

	return   zero_inserted_data ;    
            

def zero_bit_removal(crc_codded_data) :

#after five ones , zero removal in addr_field + controled_field + crc_codded_data 
	temp = crc_codded_data ; 
        zero_removed_data = str('') ;

        while( len(temp) >= 6 ) :
		if temp[:6] == '111110' : 
                	zero_removed_data = zero_removed_data + '11111';
                                        
                        if len(temp) == 6 : 
                        	temp  = '' ;
                        else :
                                temp  = temp[6:-1] + temp[-1];
                        if len(temp) < 6 :
                                zero_removed_data = zero_removed_data + temp;
                else :
                        zero_removed_data = zero_removed_data + temp[0];
                                        
                        temp = temp[1:-1] + temp[-1];
                        if len(temp) < 6 :
                        	zero_removed_data = zero_removed_data + temp;   

	return  zero_removed_data ; 




                                                  
                             
