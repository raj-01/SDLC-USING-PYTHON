
import hex_lookup 


def decode_utf8( utf8_bytes ):

	#if len(utf8_bytes) == 1:
		 
		#return int(utf8_bytes)   ;
	
	if  len(utf8_bytes) == 2 :
		z = hex_lookup.hex_int(utf8_bytes[0]);
		y = hex_lookup.hex_int(utf8_bytes[1]);
		return ( (z-192)*64 + (y-128) ) ;
		
	elif len(utf8_bytes) == 3 :
		z = hex_lookup.hex_int(utf8_bytes[0]);
		y = hex_lookup.hex_int(utf8_bytes[1]);
		x = hex_lookup.hex_int(utf8_bytes[2]);
		return ((z-224)*4096 + (y-128)*64 + (x-128) ) ;

	elif len( utf8_bytes ) == 4 :
		z = hex_lookup.hex_int(utf8_bytes[0]);
		y = hex_lookup.hex_int(utf8_bytes[1]);
		x = hex_lookup.hex_int(utf8_bytes[2]);
		w = hex_lookup.hex_int(utf8_bytes[3]);
		return  ((z-240)*262144 + (y-128)*4096 + (x-128)*64 + (w-128) ) ;

	elif len( utf8_bytes ) == 5 :
		z = hex_lookup.hex_int(utf8_bytes[0]);
		y = hex_lookup.hex_int(utf8_bytes[1]);
		x = hex_lookup.hex_int(utf8_bytes[2]);
		w = hex_lookup.hex_int(utf8_bytes[3]);
		v = hex_lookup.hex_int(utf8_bytes[4]);
		return ((z-248)*16777216 + (y-128)*262144 + (x-128)*4096 + (w-128)*64 + (v-128));

	elif len( utf8_bytes ) == 6 :
		z = hex_lookup.hex_int(utf8_bytes[0]);
		y = hex_lookup.hex_int(utf8_bytes[1]);
		x = hex_lookup.hex_int(utf8_bytes[2]);
		w = hex_lookup.hex_int(utf8_bytes[3]);
		v = hex_lookup.hex_int(utf8_bytes[4]);
		u = hex_lookup.hex_int(utf8_bytes[5]);
		return ((z-252)*1073741824 + (y-128)*16777216 + (x-128)*262144 + (w-128)*4096 + (v-128)*64 + (u-128) ) ;




#If z is between and including 0 - 127, then there is 1 byte z. The decimal Unicode value ud = the value of z.

#If z is between and including 192 - 223, then there are 2 bytes z y; ud = (z-192)*64 + (y-128)

#If z is between and including 224 - 239, then there are 3 bytes z y x; ud = (z-224)*4096 + (y-128)*64 + (x-128)

#If z is between and including 240 - 247, then there are 4 bytes z y x w; ud = (z-240)*262144 + (y-128)*4096 + (x-128)*64 + (w-128)

#If z is between and including 248 - 251, then there are 5 bytes z y x w v; ud = (z-248)*16777216 + (y-128)*262144 + (x-128)*4096 + (w-128)*64 + (v-128)

#If z is 252 or 253, then there are 6 bytes z y x w v u; ud = (z-252)*1073741824 + (y-128)*16777216 + (x-128)*262144 + (w-128)*4096 + (v-128)*64 + (u-128)

#If z = 254 or 255 then there is something wrong! 

#http://home.kpn.nl/vanadovv/uni/utf8conversion.html     	


