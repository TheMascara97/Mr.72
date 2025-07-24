import psutil,socket
  
def get_all_local_ips():  
    addrs = psutil.net_if_addrs()  
    local_ips = []  
    for interface, addr_list in addrs.items():  
        for addr in addr_list:  
            if addr.family == socket.AF_INET:  # 只考虑IPv4地址  
                local_ips.append(addr.address)  
    return local_ips  
def desired_ip():  
#print("All Local IP Addresses:", get_all_local_ips())
    ip_addresses =get_all_local_ips()
# 假设你想要获取以'192.168.1.'开头的IP地址  
    desired_ips = [ip for ip in ip_addresses if ip.startswith('192.168.')]  
# 如果你只想要第一个匹配的IP地址  
    if desired_ips:  
        desired_ip = desired_ips[0]
        return desired_ip  
    #print(desired_ip[:10])  # 输出: 192.168.1.1（或者列表中的第一个匹配项）  
    else:  
        print("No matching IP addresses found.")
# base_url=f"{desired_ip[:10]}1"
# url_template = f"http://{base_url}"+"/cgi-bin/mycgi.cgi?ACT=GetParameter&{%22module%22:%22Token%22,%22param%22:{%22action%22:%22token%22}}"
# # ip_address = f"{desired_ip[:10]}1"
# # url = url_template.format(ip_address)
# print(url_template)  # 输出: http://192.168.1.1:8080/path/to/resour


if __name__ == '__main__':
    print(desired_ip())