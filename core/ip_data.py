from dataclasses import dataclass
from typing import Optional, List

@dataclass
class IpData:
    Input_ip: Optional[str] = None
    subnet_mask: Optional[int] = None
    classes: Optional[bool] = None
    network_address: Optional[str] = None
    broadcast_address: Optional[str] = None
    Number_of_Hosts_in_this_subnet: Optional[int] = None
    CIDR_Mask: Optional[str] = None