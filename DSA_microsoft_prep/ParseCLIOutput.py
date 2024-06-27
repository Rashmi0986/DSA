import re

s = """
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 172.17.106.119  netmask 255.255.240.0  broadcast 172.17.111.255
        inet6 fe80::215:5dff:fe01:2501  prefixlen 64  scopeid 0x20<link>
        ether 00:15:5d:01:25:01  txqueuelen 1000  (Ethernet)
        RX packets 7084  bytes 10362206 (10.3 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 1405  bytes 108877 (108.8 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 38  bytes 4592 (4.5 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 38  bytes 4592 (4.5 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
"""

# Function to parse the network data
def parse_network_data(data):
    interfaces = {}
    current_interface = None
    
    for line in data.strip().split('\n'):
        line = line.strip()
        
        # Match the interface name
        if re.match(r'^\S+:', line):
            current_interface = line.split(':')[0]
            interfaces[current_interface] = {}
        
        elif current_interface:
            # Match the inet line for IPv4
            if 'inet ' in line and current_interface == 'lo':
                match = re.search(r'inet (\S+)', line)
                if match:
                    interfaces[current_interface]['inet'] = {
                        'address': match.group(1)
                }
            elif 'inet ' in line:
                match = re.search(r'inet (\S+)  netmask (\S+)  broadcast (\S+)', line)
                if match:
                    interfaces[current_interface]['inet'] = {
                        'address': match.group(1),
                        'netmask': match.group(2),
                        'broadcast': match.group(3)
                    }
            
            # Match the ether line for MAC address
            elif 'ether ' in line:
                match = re.search(r'ether (\S+)', line)
                if match:
                    interfaces[current_interface]['ether'] = match.group(1)
            # Match RX and TX packets
            elif 'RX packets' in line:
                match = re.search(r'RX packets (\d+)  bytes (\d+)', line)
                if match:
                    interfaces[current_interface]['RX'] = {
                        'packets': match.group(1),
                        'bytes': match.group(2)
                    }
            elif 'TX packets' in line:
                match = re.search(r'TX packets (\d+)  bytes (\d+)', line)
                if match:
                    interfaces[current_interface]['TX'] = {
                        'packets': match.group(1),
                        'bytes': match.group(2)
                    }

    return interfaces

# Parse the network data
parsed_data = parse_network_data(s)
print(parsed_data)
