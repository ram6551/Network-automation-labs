from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "host": "YOUR_HOSTNAME",
    "username": "YOUR_USERNAME",
    "password": "YOUR_PASSWORD"
}

connection = ConnectHandler(**device)

output = connection.send_command("show ip interface brief")
print(output)

connection.disconnect()
