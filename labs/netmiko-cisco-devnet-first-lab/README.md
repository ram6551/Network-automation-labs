# Netmiko + Cisco DevNet First Lab

## 🎯 Objective

In this lab, I wanted to try real network automation for the first time.

Until now, I was learning networking and Python separately, but I didn’t clearly understand how both connect in real-world scenarios. So my goal was to take a simple networking task and automate it using Python.

---

## 🧠 Background

I already had Cisco Packet Tracer, so initially I thought I could use that for automation. But I learned that Packet Tracer does not support real SSH connections required for tools like Netmiko.

So I moved to Cisco DevNet Sandbox, which provides real Cisco devices that can be accessed over SSH.

This was my first time working with a real remote Cisco device instead of a simulator.

---

## 🛠️ Tools I Used

For this lab, I used:

- Python
- Netmiko (Python library)
- Cisco DevNet Sandbox
- SSH (Command Prompt)
- Cisco CLI

---

## 🧪 Lab Setup

I launched a **Catalyst 8000 Always-On Sandbox** from Cisco DevNet.

From there, I got:
- hostname
- username
- password

These credentials allowed me to connect to the router.

---

## 🔧 What I Did (Step by Step)

### Step 1: Connected to the Router Using SSH

First, I wanted to make sure I could access the router manually before using automation.

I used:

```bash
ssh username@hostname
After this you will be asked to enter the password and when you are entering the password you won't see anything typing there , but still actually typing and you cannot see it just for security reasons. so type and enter it.

After entering the password, I got access to the router CLI:

DevNet-Cat8k-RT#

This confirmed:

-SSH is working
-credentials are correct
-I can interact with the device

Step 2: Checked Interface Status

I ran:

show ip interface brief

This command showed me:

-all interfaces
-IP addresses
-whether they are up or down

This helped me understand the current state of the device.

Step 3: Did Configuration Manually

Before automating anything, I wanted to understand how the configuration works manually.

I created a loopback interface:

configure terminal
interface loopback10
ip address 10.10.10.1 255.255.255.255
end

Then I verified it again using:

show ip interface brief

This step was important because automation should always come after understanding the manual process.

Step 4: Installed Netmiko

On my laptop, I installed Netmiko:

pip install netmiko

Netmiko is used to connect to network devices using Python.

Step 5: Wrote My First Automation Script

Now I wrote a Python script to connect to the router and run a command automatically.

from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "host": "YOUR_HOSTNAME",
    "username": "YOUR_USERNAME",
    "password": "YOUR_PASSWORD",
}

connection = ConnectHandler(**device)

output = connection.send_command("show ip interface brief")
print(output)

connection.disconnect()

👉 This script:

-connects to the router
-runs a show command
-prints the output
-disconnects

This was the first time I saw Python interacting with a real router.

Step 6: Automated Configuration

Next, I automated the same thing I did manually.

config_commands = [
    "interface loopback20",
    "ip address 20.20.20.1 255.255.255.255"
]

connection.send_config_set(config_commands)

👉 This:

-enters config mode
-creates loopback20
-assigns IP address

Step 7: Verified the Change

After running the script, I logged back into the router using SSH and ran:

show ip interface brief

I confirmed that Loopback20 was created successfully.
Step 8: Took Configuration Backup

I also created a script to take backup of the running config:

output = connection.send_command("show running-config")

with open("backup.txt", "w") as file:
    file.write(output)

👉 This saved the router configuration into a file.

✅ Result

By the end of this lab, I was able to:

connect to a real Cisco device
run commands using Python
push configuration automatically
verify changes
take configuration backup
🧠 What I Learned

This lab helped me understand:

how Python connects to network devices
how Netmiko works
how dictionaries store device details
how lists store multiple commands
how automation reduces manual work


Adding loopback interface to a router
---

## 🔧 Configuration Automation

After verifying basic connectivity, I automated configuration changes using Python and Netmiko.

### Task

- Create loopback interface
- Assign IP address

### Commands Used

```python
config_commands = [
    "interface loopback20",
    "ip address 20.20.20.1 255.255.255.255"
]
Explanation

Instead of manually entering configuration mode and typing commands, I used Netmiko's send_config_set() method.

This method:

automatically enters configuration mode
sends commands one by one
exits configuration mode
Outcome

The loopback interface was successfully created using automation.

I verified it by logging into the router and running:

show ip interface brief

This confirmed that automation works exactly the same as manual configuration.
