[root@localhost PythonCodes]# python3 Get_interfaces_list.py
<Response [200]>
{
  "ietf-interfaces:interfaces": {
    "interface": [
      {
        "name": "GigabitEthernet1",
        "description": "IPv6 ADDRESS",
        "type": "iana-if-type:ethernetCsmacd",
        "enabled": true,
        "ietf-ip:ipv4": {
          "address": [
            {
              "ip": "10.10.20.48",
              "netmask": "255.255.255.0"
            }
          ]
        },
        "ietf-ip:ipv6": {
          "address": [
            {
              "ip": "2001:db8:acad:1::1",
              "prefix-length": 64
            }
          ]
        }
      },
      {
        "name": "GigabitEthernet2",
        "description": "Configured by RESTCONF",
        "type": "iana-if-type:ethernetCsmacd",
        "enabled": true,
        "ietf-ip:ipv4": {
          "address": [
            {
              "ip": "172.16.15.1",
              "netmask": "255.255.255.0"
            }
          ]
        },
        "ietf-ip:ipv6": {
        }
      },
      {
        "name": "GigabitEthernet3",
        "description": "test",
        "type": "iana-if-type:ethernetCsmacd",
        "enabled": false,
        "ietf-ip:ipv4": {
        },
        "ietf-ip:ipv6": {
        }
      },
      {
        "name": "Loopback0",
        "type": "iana-if-type:softwareLoopback",
        "enabled": true,
        "ietf-ip:ipv4": {
          "address": [
            {
              "ip": "100.100.100.100",
              "netmask": "255.255.255.255"
            }
          ]
        },
        "ietf-ip:ipv6": {
        }
      }
    ]
  }
}

[root@localhost PythonCodes]# python3 Add_new_loopback100_interface.py
<Response [201]>

[root@localhost PythonCodes]# python3 Get_interfaces_list.py
<Response [200]>
{
  "ietf-interfaces:interfaces": {
    "interface": [
      {
        "name": "GigabitEthernet1",
        "description": "IPv6 ADDRESS",
        "type": "iana-if-type:ethernetCsmacd",
        "enabled": true,
        "ietf-ip:ipv4": {
          "address": [
            {
              "ip": "10.10.20.48",
              "netmask": "255.255.255.0"
            }
          ]
        },
        "ietf-ip:ipv6": {
          "address": [
            {
              "ip": "2001:db8:acad:1::1",
              "prefix-length": 64
            }
          ]
        }
      },
      {
        "name": "GigabitEthernet2",
        "description": "Configured by RESTCONF",
        "type": "iana-if-type:ethernetCsmacd",
        "enabled": true,
        "ietf-ip:ipv4": {
          "address": [
            {
              "ip": "172.16.15.1",
              "netmask": "255.255.255.0"
            }
          ]
        },
        "ietf-ip:ipv6": {
        }
      },
      {
        "name": "GigabitEthernet3",
        "description": "test",
        "type": "iana-if-type:ethernetCsmacd",
        "enabled": false,
        "ietf-ip:ipv4": {
        },
        "ietf-ip:ipv6": {
        }
      },
      {
        "name": "Loopback0",
        "type": "iana-if-type:softwareLoopback",
        "enabled": true,
        "ietf-ip:ipv4": {
          "address": [
            {
              "ip": "100.100.100.100",
              "netmask": "255.255.255.255"
            }
          ]
        },
        "ietf-ip:ipv6": {
        }
      },
      {
        "name": "Loopback100",
        "description": "Configured by DarcyLiu",
        "type": "iana-if-type:softwareLoopback",
        "enabled": true,
        "ietf-ip:ipv4": {
          "address": [
            {
              "ip": "172.16.100.1",
              "netmask": "255.255.255.0"
            }
          ]
        },
        "ietf-ip:ipv6": {
        }
      }
    ]
  }
}

[root@localhost PythonCodes]# python3 Delete_loopback100.py
<Response [204]>

[root@localhost PythonCodes]# python3 Get_interfaces_list.py
<Response [200]>
{
  "ietf-interfaces:interfaces": {
    "interface": [
      {
        "name": "GigabitEthernet1",
        "description": "IPv6 ADDRESS",
        "type": "iana-if-type:ethernetCsmacd",
        "enabled": true,
        "ietf-ip:ipv4": {
          "address": [
            {
              "ip": "10.10.20.48",
              "netmask": "255.255.255.0"
            }
          ]
        },
        "ietf-ip:ipv6": {
          "address": [
            {
              "ip": "2001:db8:acad:1::1",
              "prefix-length": 64
            }
          ]
        }
      },
      {
        "name": "GigabitEthernet2",
        "description": "Configured by RESTCONF",
        "type": "iana-if-type:ethernetCsmacd",
        "enabled": true,
        "ietf-ip:ipv4": {
          "address": [
            {
              "ip": "172.16.15.1",
              "netmask": "255.255.255.0"
            }
          ]
        },
        "ietf-ip:ipv6": {
        }
      },
      {
        "name": "GigabitEthernet3",
        "description": "test",
        "type": "iana-if-type:ethernetCsmacd",
        "enabled": false,
        "ietf-ip:ipv4": {
        },
        "ietf-ip:ipv6": {
        }
      },
      {
        "name": "Loopback0",
        "type": "iana-if-type:softwareLoopback",
        "enabled": true,
        "ietf-ip:ipv4": {
          "address": [
            {
              "ip": "100.100.100.100",
              "netmask": "255.255.255.255"
            }
          ]
        },
        "ietf-ip:ipv6": {
        }
      }
    ]
  }
}

[root@localhost PythonCodes]#

