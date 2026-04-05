# Network Automation Labs

This repository documents my hands-on learning journey in networking and network automation.

I have learned networking concepts, but I had not been documenting my work in a structured way. This repository is my starting point to build a portfolio of real-world networking and automation labs.

---

## 🚀 Purpose

The goal of this repository is to:

- document my networking and automation learning
- apply Python concepts to real networking problems
- build hands-on labs using real devices (Cisco DevNet Sandbox)
- create a strong portfolio for networking and automation roles

---

## 🧪 Current Lab

### Netmiko + Cisco DevNet First Lab

In this lab, I:

- connected to a real Cisco router using SSH
- verified CLI access manually
- ran `show ip interface brief`
- configured a loopback interface manually
- automated the same process using Python and Netmiko
- created a backup of the running configuration

---

## 🛠️ Tools Used

- Python
- Netmiko
- Cisco DevNet Sandbox
- SSH
- Cisco CLI

---

## 📂 Repository Structure

```text
Network-automation-labs/
│
├── README.md
├── requirements.txt
├── .gitignore
│
└── labs/
    └── netmiko-cisco-devnet-first-lab/
        ├── README.md
        ├── show_interfaces.py
        ├── configure_loopback.py
        └── backup_running_config.py
