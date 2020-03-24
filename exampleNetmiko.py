from netmiko import ConnectHandler
import time
import re
import json

def send_cmd(conn, command):
    output = conn.send_command(command)
    #time.sleep(1.0)
    return output

def get_hostname(conn):
    command = "uname -n"
    return send_cmd(conn, command)

def get_version(conn):
    command = "uname -a"
    pattern = r'Version(.*),'
    output = send_cmd(conn, command)
    match = re.findall(pattern, output)[0].strip()
    return match

def get_model(conn):
    command = "uname -a"
    pattern = r'IOSv Software \((.*)\),'
    output = send_cmd(conn, command)
    match = re.findall(pattern, output)[0].strip()
    return match

def get_serial_number(conn):
    command = "show inventory"
    pattern = r'Hw Serial#:(.*),'
    output = send_cmd(conn, command)
    match = re.findall(pattern, output)[0].strip()
    return match

def get_device_uptime(conn):
    command = "show version"
    pattern = r'uptime is(.*)\n'
    output = send_cmd(conn, command)
    match = re.findall(pattern, output)[0].strip()
    return match

def get_interfaces_addresses(conn):
    # command = "show ip arp"
    command = "show interfaces"
    pattern = r'bia.(.*?)\)'
    connected_interfaces_addresses = []

    output = send_cmd(conn, command)
    ethernet_interfaces = output.replace('\n', ' ').split('GigabitEthernet')
    for ip in [re.findall(pattern, interface) for interface in ethernet_interfaces if interface.find("line protocol is up    Hardware is iGbE")>1]:
          if ip:
                connected_interfaces_addresses.append(ip[0].strip())
    return connected_interfaces_addresses

def main():
    cisco1 = {
        "host": "192.168.122.189",
        "username": "hathout",
        "password": "cisco",
        "device_type": "cisco_ios",
    }

    net_connect = ConnectHandler(**cisco1)

    router_data = {
      "hostname": get_hostname(net_connect),
      "model": get_model(net_connect),
      "device_uptime": get_device_uptime(net_connect),
      "version": get_version(net_connect),
      "serial_number": get_serial_number(net_connect),
      "interfaces_mac_addresses": get_interfaces_addresses(net_connect)
    }

    router_data = json.dumps(router_data)
    # print(router_data)

    with open('data.json', 'w') as outfile:
        json.dump(router_data, outfile)

    net_connect.disconnect()


if __name__ == "__main__":
    main()

