import re

inp = input("Please Input a string with Ip Addresses => ")
ip_pattern = re.compile('(\d+\.\d+\.\d+\.\d+)')
ip_add = re.findall(ip_pattern, inp)
ip_no_lead_zeros = [re.sub("(\.?:)0+", "", ip) for ip in ip_add]
print(ip_no_lead_zeros)
