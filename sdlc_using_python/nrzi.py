

def nrzi_encode(sdlc_codded_data) :

	store = sdlc_codded_data ; 
	nrzi_data = '1' ;
	for itr in store :
    		if itr == '1' :
        		nrzi_data = nrzi_data + nrzi_data[-1] ; # if the iterator pints to '1' in store then net bit should same as latst bit of nrzi_data 
    		elif itr == '0' :
			if nrzi_data[-1] == '0' :
         			nrzi_data = nrzi_data + '1' ; 
   			else :	
         			nrzi_data = nrzi_data + '0' ; 

    
	return nrzi_data ; 


def nrzi_decode(a , b ):

    		if (b != a) :
        		 return '0' ;
    		else :
        		 return '1' ; 
    
    	    	
