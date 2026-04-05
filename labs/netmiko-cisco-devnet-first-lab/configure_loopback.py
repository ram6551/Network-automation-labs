from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "host": "YOUR_HOSTNAME",
    "username": "YOUR_USERNAME",
    "password": "YOUR_PASSWORD"
}

config_commands = [
    "interface loopback20",
    "ip address 20.20.20.1 255.255.255.255"
]

connection = ConnectHandler(**device)

output = connection.send_config_set(config_commands)
print(output)

connection.disconnect()
