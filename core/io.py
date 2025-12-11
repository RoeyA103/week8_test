from core.utils import Ip_utils
def get_ip_add()->str:
    while True:
        ip_add = input("enter ip: ")
        if not Ip_utils.validation_ip_check(ip_add):
            continue
        break
    return ip_add

def get_ip_mask()->str:
    while True:
        ip_mask = input("enter mask: ")
        if not Ip_utils.validation_ip_check(ip_mask):
            continue
        break
    return ip_mask

def get_student_id()->str:
    id = input("enter student id: ")
    return id
