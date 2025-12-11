from core.output_string import *

class FileWriter:
    def __init__(self):
        self.data = None
        self.student_id = None

    def get_data(self,ip_data:dict):
        self.data = ip_data

    def write_to_file(self):
        ip_add = self.data["Input_ip"]
        with open(f"subnet_info_{ip_add}_{self.student_id}.txt","w")  as file:
            file.write(format_input_ip(self.data["Input_ip"]))
            file.write(format_subnet_mask(self.data["subnet_mask"]))
            file.write(format_classful_status(self.data["class_type"]))
            file.write(format_network_address(self.data["network_address"]))
            file.write(format_broadcast_address(self.data["broadcast_address"]))
            file.write(format_num_hosts(self.data["Number_of_Hosts_in_this_subnet"]))
            file.write(format_cidr_mask(self.data["CIDR_Mask"]))
        print("All data was successfully written to the file")    