import math
class Ip_utils:
    def validation_ip_check(ip_add:str)->bool:
        
        def format_check(ip_add:str)->bool:
            return "." in ip_add

        def brake_ip(ip_add:str)-> list:
            return ip_add.split(".")

        def check_if_all_num(ip_list:list)->bool:
            for n in ip_list:
                if not n.isdigit():
                    return False
            return True    
        
        def octat_check(ip_list:list)->bool:
            return len(ip_list) == 4

        def boundary_check(ip_list:list)->bool:
            for n in ip_list:
                if int(n) > 255 or int(n) < 0:
                    return False
            return True
            
        match True:
            case _ if not format_check(ip_add):
                print("format like 192.168.10.130 separated by dots")
                return False   
             
            case _ if not check_if_all_num(brake_ip(ip_add)):
                print("The address must contain only numbers.")
                return False
            
            case _ if not octat_check(brake_ip(ip_add)):
                print("Must contain 4 octets")
                return False
            
            case _ if not boundary_check(brake_ip(ip_add)):
                print("The range is between 0 and 255")
                return False
            
            case _ :
                print("valid ip address")
                return True
             
    def get_network_add(ip:str,mask:str)->str:
        """
        Extracts each octet into a separate part
        Then converts to a number to apply the & operation on it
        To compare bits
        (& Sets each bit to 1 if both bits are 1)
        """
        network = ''

        iOctets = ip.split('.')
        mOctets = mask.split('.')

        network = str( int( iOctets[0] ) & int(mOctets[0] ) ) + '.'
        network += str( int( iOctets[1] ) & int(mOctets[1] ) ) + '.'
        network += str( int( iOctets[2] ) & int(mOctets[2] ) ) + '.'
        network += str( int( iOctets[3] ) & int(mOctets[3] ) )

        return network
    
    def get_broadcast_address(ip:str,mask:str)->str:
        """
        Converts each octet into a separate part
        Then runs the operation | which returns 1 if one of the bits is 1
        The ~ sign is to flip each bit (if it was 1 it would be 0 and vice versa)
        The idea is that if I flip each bit in the subnet I actually find out my available possibilities, and then I connect with the bits in the current address because I start from the bottom and end according to the given address
        The result is the largest option in that octet = broadcast
        """
        ip = ip.split('.')
        mask = mask.split('.')
        broadcast = [(int(ioctet) | ~int(moctet)) & 0xff for ioctet, moctet in zip(ip, mask)]
        res = ""
        for oct in broadcast:
            res += str(oct) + "."
        return res[:-1]

    def find_number_of_zeros_in_mask_bin(mask:str)->int:
        def dec_to_bin(dec:str)->str:
            dec = int(dec)
            b = ""

            while dec > 0:
                b = str(dec % 2) + b
                dec //= 2
            return b 
    
        mask = mask.split(".")

        mask_as_bits = ""
        for oct in mask:
            if oct == "0":
                mask_as_bits += "0"*8
            else:    
                mask_as_bits += dec_to_bin(oct)

        first_zero_index = mask_as_bits.index("0")
        number_of_zeros = len(mask_as_bits[first_zero_index:])
        return number_of_zeros
    
    def get_number_of_hosts(mask:str)->int:
        zeros = Ip_utils.find_number_of_zeros_in_mask_bin(mask)
        number_of_hosts = 2 ** zeros
        return number_of_hosts - 2

    def get_cidr(mask:str)->int:
        return int(32 - Ip_utils.find_number_of_zeros_in_mask_bin(mask) )
    
    def get_class_type(mask:str)->str:
        number_of_zeros = Ip_utils.find_number_of_zeros_in_mask_bin(mask)
        match number_of_zeros:
            case 8:
                return "class A"
            case 16:
                return "class B"
            case 24:
                return "class C"
            case _:
                return "classless"

        


                
