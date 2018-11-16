import sender
import receiver

time_for_receiving_data =  10 ;

for _try_ in range(3) :
	print("try" , _try_  + 1) ; 
	if sender.send_data() == True :
		print( 'now u can transmit data ' ) ; 
		(is_data_received_correct , data ) = receiver.data_received( time_for_receiving_data ); 
		
	else :
		print("data is not sent there is some problem in sender.py");
		is_data_received_correct = False ; 
	
	
	if is_data_received_correct == True :
		
		address = data[7:0:-1] + data[0];
		print( " ADDRESS :" ,  hex(int( address , 2 ) )) ;

		control = data[15:7:-1] ;	
 		print("CONTROLL :" , hex(int(control , 2)));

		information = data[16:-1] + data[-1] ; 


		n = (len(information))/8 ;  
		for idx in range( n ):
			temp = information[0:8];
			temp = temp[::-1] ;
			print("INFORMATIONA   " + str(n) ,hex( int( temp , 2))) ; 
			information = information[8:-1] + information[-1] ; 

	else :
		
		print("time out for try " , _try_ + 1  ) 








		
		
