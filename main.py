from core.utils import Ip_utils
from core.ip_data import IpData
from core.io import *
from File_writer import FileWriter

def main():
    ipd = IpData()
    fw = FileWriter()
    fw.student_id = get_student_id()

    ip_add = get_ip_add()
    ip_mask = get_ip_mask()

    ipd.Input_ip = ip_add

    ipd.subnet_mask = ip_mask

    ipd.network_address = Ip_utils.get_network_add(ip_add,ip_mask)

    ipd.broadcast_address = Ip_utils.get_broadcast_address(ip_add,ip_mask)

    ipd.Number_of_Hosts_in_this_subnet = Ip_utils.get_number_of_hosts(ip_mask)

    ipd.CIDR_Mask = Ip_utils.get_cidr(ip_mask)

    ipd.class_type = Ip_utils.get_class_type(ip_mask)

    fw.get_data(ipd.__dict__)

    fw.write_to_file()

if __name__ == "__main__":
    main()    







