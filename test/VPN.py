import os
import subprocess

def run_command(command):
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        exit(1)

def install_packages():
    print("Installing necessary packages...")
    run_command("sudo yum install libreswan l2tpd ppp -y")

def configure_ipsec():
    print("Configuring IPsec...")
    ipsec_config = """
conn L2TP-PSK-NAT
    rightsubnet=vhost:%priv
    also=L2TP-PSK-noNAT

conn L2TP-PSK-noNAT
    authby=secret
    pfs=no
    auto=add
    keyingtries=3
    rekey=no
    ikelifetime=8h
    keylife=1h
    type=transport
    left=%defaultroute
    leftprotoport=17/1701
    right=%any
    rightprotoport=17/%any
    """
    with open("/etc/ipsec.conf", "a") as f:
        f.write(ipsec_config)
    run_command("sudo ipsec verify")

def configure_l2tp():
    print("Configuring L2TP...")
    l2tp_config = """
[l2tpd]
listen-addr = 0.0.0.0
ip range = 192.168.1.100-192.168.1.200
local ip = 192.168.1.1
require chap = yes
refuse pap = yes
require authentication = yes
name = l2tpd
pppoptfile = /etc/ppp/options.l2tpd
length bit = yes
"""
    with open("/etc/l2tpd/l2tpd.conf", "w") as f:
        f.write(l2tp_config)

def configure_ppp():
    print("Configuring PPP...")
    ppp_options = """
ms-dns 8.8.8.8
ms-dns 8.8.4.4
asyncmap 0
auth
crtscts
lock
hide-password
modem
debug
proxyarp
lcp-echo-interval 30
lcp-echo-failure 4
"""
    with open("/etc/ppp/options.l2tpd", "w") as f:
        f.write(ppp_options)

def set_firewall_rules():
    print("Setting firewall rules...")
    run_command("sudo firewall-cmd --permanent --add-port=1701/udp")
    run_command("sudo firewall-cmd --permanent --add-port=500/udp")
    run_command("sudo firewall-cmd --permanent --add-port=4500/udp")
    run_command("sudo firewall-cmd --reload")

def add_vpn_user(username, password):
    print(f"Adding VPN user: {username}")
    run_command(f"sudo echo '{username} * {password} *' >> /etc/ppp/chap-secrets")

def main():
    install_packages()
    configure_ipsec()
    configure_l2tp()
    configure_ppp()
    set_firewall_rules()
    username = input("Enter VPN username: ")
    password = input("Enter VPN password: ")
    add_vpn_user(username, password)
    print("L2TP VPN server setup completed successfully!")

if __name__ == "__main__":
    main()