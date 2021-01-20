## Show current setting
(venv) [root@localhost intro-ansible]# ansible-playbook ansible-02-ios-modules/02-ios_command_show.yaml

PLAY [Sample IOS show version for Ansible 2.5] *******************************************************************************  

TASK [GATHERING FACTS] *******************************************************************************************************  
ok: [ios-xe-mgmt.cisco.com]  

TASK [display current IOS version] *******************************************************************************************  
ok: [ios-xe-mgmt.cisco.com] => {  
    "ansible_net_version": "16.09.03"  
}  

TASK [run show ip int brie] **************************************************************************************************  
ok: [ios-xe-mgmt.cisco.com]  

TASK [display value of "myint" variable] *************************************************************************************  
ok: [ios-xe-mgmt.cisco.com] => {  
    "myint[\"stdout_lines\"][0]": [  
        "Interface              IP-Address      OK? Method Status                Protocol",  
        "GigabitEthernet1       10.10.20.48     YES NVRAM  up                    up      ",  
        "GigabitEthernet2       unassigned      YES NVRAM  administratively down down    ",  
        "GigabitEthernet3       unassigned      YES NVRAM  administratively down down"  
    ]  
}  

TASK [run show users] ********************************************************************************************************  
ok: [ios-xe-mgmt.cisco.com]  

TASK [display value of "shuser" variable] ************************************************************************************
ok: [ios-xe-mgmt.cisco.com] => {
    "shuser[\"stdout_lines\"][0]": [
        "Line       User       Host(s)              Idle       Location",
        "*  1 vty 0     developer  idle                 00:00:00 184.145.119.144",
        "   4 vty 3     developer  idle                 00:00:00 201.163.95.237",
        "",
        "  Interface    User               Mode         Idle     Peer Address",
        "  unknown      NETCONF(ONEP)      com.cisco.ne 00:00:31 ",
        "  unknown      a(ONEP)            com.cisco.sy 00:00:29"
    ]
}

PLAY RECAP *******************************************************************************************************************
ios-xe-mgmt.cisco.com      : ok=6    changed=0    unreachable=0    failed=0

## Create new loopback interface

(venv) [root@localhost intro-ansible]# ansible-playbook ansible-02-ios-modules/02-loopback_create.yaml

PLAY [Sample IOS config for Ansible 2.5] *************************************************************************************

TASK [Create loopback 155] ***************************************************************************************************
changed: [ios-xe-mgmt.cisco.com]

TASK [Assign IP to loopback] *************************************************************************************************
changed: [ios-xe-mgmt.cisco.com]

PLAY RECAP *******************************************************************************************************************
ios-xe-mgmt.cisco.com      : ok=2    changed=2    unreachable=0    failed=0

## Verify the new loopback interface exist 
(venv) [root@localhost intro-ansible]# ansible-playbook ansible-02-ios-modules/02-ios_command_show.yaml

PLAY [Sample IOS show version for Ansible 2.5] *******************************************************************************

TASK [GATHERING FACTS] *******************************************************************************************************
ok: [ios-xe-mgmt.cisco.com]

TASK [display current IOS version] *******************************************************************************************
ok: [ios-xe-mgmt.cisco.com] => {
    "ansible_net_version": "16.09.03"
}

TASK [run show ip int brie] **************************************************************************************************
ok: [ios-xe-mgmt.cisco.com]

TASK [display value of "myint" variable] *************************************************************************************
ok: [ios-xe-mgmt.cisco.com] => {
    "myint[\"stdout_lines\"][0]": [
        "Interface              IP-Address      OK? Method Status                Protocol",
        "GigabitEthernet1       10.10.20.48     YES NVRAM  up                    up      ",
        "GigabitEthernet2       unassigned      YES NVRAM  administratively down down    ",
        "GigabitEthernet3       unassigned      YES NVRAM  administratively down down    ",
        "Loopback155            10.111.155.1    YES manual up                    up"
    ]
}

TASK [run show users] ********************************************************************************************************
ok: [ios-xe-mgmt.cisco.com]

TASK [display value of "shuser" variable] ************************************************************************************
ok: [ios-xe-mgmt.cisco.com] => {
    "shuser[\"stdout_lines\"][0]": [
        "Line       User       Host(s)              Idle       Location",
        "   2 vty 1     developer  idle                 00:00:00 201.163.95.237",
        "*  4 vty 3     developer  idle                 00:00:08 184.145.119.144",
        "",
        "  Interface    User               Mode         Idle     Peer Address",
        "  unknown      NETCONF(ONEP)      com.cisco.ne 00:00:10 ",
        "  unknown      a(ONEP)            com.cisco.sy 00:00:00"
    ]
}

PLAY RECAP *******************************************************************************************************************
ios-xe-mgmt.cisco.com      : ok=6    changed=0    unreachable=0    failed=0

## Delete the new loopback interface
(venv) [root@localhost intro-ansible]# ansible-playbook ansible-02-ios-modules/02-loopback_delete.yaml

PLAY [Sample IOS config for Ansible 2.5] *************************************************************************************

TASK [Delete loopback 155] ***************************************************************************************************
changed: [ios-xe-mgmt.cisco.com]

PLAY RECAP *******************************************************************************************************************
ios-xe-mgmt.cisco.com      : ok=1    changed=1    unreachable=0    failed=0

## Verify the removal
(venv) [root@localhost intro-ansible]# ansible-playbook ansible-02-ios-modules/02-ios_command_show.yaml

PLAY [Sample IOS show version for Ansible 2.5] *******************************************************************************

TASK [GATHERING FACTS] *******************************************************************************************************
ok: [ios-xe-mgmt.cisco.com]

TASK [display current IOS version] *******************************************************************************************
ok: [ios-xe-mgmt.cisco.com] => {
    "ansible_net_version": "16.09.03"
}

TASK [run show ip int brie] **************************************************************************************************
ok: [ios-xe-mgmt.cisco.com]

TASK [display value of "myint" variable] *************************************************************************************
ok: [ios-xe-mgmt.cisco.com] => {
    "myint[\"stdout_lines\"][0]": [
        "Interface              IP-Address      OK? Method Status                Protocol",
        "GigabitEthernet1       10.10.20.48     YES NVRAM  up                    up      ",
        "GigabitEthernet2       unassigned      YES NVRAM  administratively down down    ",
        "GigabitEthernet3       unassigned      YES NVRAM  administratively down down"
    ]
}

TASK [run show users] ********************************************************************************************************
ok: [ios-xe-mgmt.cisco.com]

TASK [display value of "shuser" variable] ************************************************************************************
ok: [ios-xe-mgmt.cisco.com] => {
    "shuser[\"stdout_lines\"][0]": [
        "Line       User       Host(s)              Idle       Location",
        "*  1 vty 0     developer  idle                 00:00:00 184.145.119.144",
        "",
        "  Interface    User               Mode         Idle     Peer Address",
        "  unknown      NETCONF(ONEP)      com.cisco.ne 00:00:23 ",
        "  unknown      a(ONEP)            com.cisco.sy 00:00:36"
    ]
}

PLAY RECAP *******************************************************************************************************************
ios-xe-mgmt.cisco.com      : ok=6    changed=0    unreachable=0    failed=0

## Show NTP setting
(venv) [root@localhost intro-ansible]# ansible-playbook ansible-02-ios-modules/02-ios_command_show_ntp.yaml

PLAY [Sample IOS show ntp for Ansible 2.5] ***********************************************************************************

TASK [run show ntp associations] *********************************************************************************************
ok: [ios-xe-mgmt.cisco.com]

TASK [display value of "myntp" variable] *************************************************************************************
ok: [ios-xe-mgmt.cisco.com] => {
    "myntp[\"stdout_lines\"][0]": [
        ""
    ]
}

PLAY RECAP *******************************************************************************************************************
ios-xe-mgmt.cisco.com      : ok=2    changed=0    unreachable=0    failed=0

## Create new NTP entries
(venv) [root@localhost intro-ansible]# ansible-playbook ansible-02-ios-modules/02-ntp_create.yaml

PLAY [Sample IOS NTP config for Ansible 2.5] *********************************************************************************

TASK [set ntp server 10.{{item}}.{{pod_number}}.65 via CLI] ******************************************************************
changed: [ios-xe-mgmt.cisco.com] => (item=11)
changed: [ios-xe-mgmt.cisco.com] => (item=12)
changed: [ios-xe-mgmt.cisco.com] => (item=13)
changed: [ios-xe-mgmt.cisco.com] => (item=14)

PLAY RECAP *******************************************************************************************************************
ios-xe-mgmt.cisco.com      : ok=1    changed=1    unreachable=0    failed=0

## Verify new NTP entries
(venv) [root@localhost intro-ansible]# ansible-playbook ansible-02-ios-modules/02-ios_command_show_ntp.yaml

PLAY [Sample IOS show ntp for Ansible 2.5] ***********************************************************************************

TASK [run show ntp associations] *********************************************************************************************
ok: [ios-xe-mgmt.cisco.com]

TASK [display value of "myntp" variable] *************************************************************************************
ok: [ios-xe-mgmt.cisco.com] => {
    "myntp[\"stdout_lines\"][0]": [
        "address         ref clock       st   when   poll reach  delay  offset   disp",
        " ~10.11.155.65    .INIT.          16      -   1024     0  0.000   0.000 15937.",
        " ~10.12.155.65    .INIT.          16      -   1024     0  0.000   0.000 15937.",
        " ~10.13.155.65    .INIT.          16      -   1024     0  0.000   0.000 15937.",
        " ~10.14.155.65    .INIT.          16      -   1024     0  0.000   0.000 15937.",
        " * sys.peer, # selected, + candidate, - outlyer, x falseticker, ~ configured"
    ]
}

PLAY RECAP *******************************************************************************************************************
ios-xe-mgmt.cisco.com      : ok=2    changed=0    unreachable=0    failed=0

## Delete new NTP entries
(venv) [root@localhost intro-ansible]# ansible-playbook ansible-02-ios-modules/02-ntp_delete.yaml

PLAY [Sample IOS NTP config for Ansible 2.5] *********************************************************************************

TASK [delete ntp server 10.{{item}}.{{pod_number}}.65 via CLI] ***************************************************************
changed: [ios-xe-mgmt.cisco.com] => (item=11)
changed: [ios-xe-mgmt.cisco.com] => (item=12)
changed: [ios-xe-mgmt.cisco.com] => (item=13)
changed: [ios-xe-mgmt.cisco.com] => (item=14)

PLAY RECAP *******************************************************************************************************************
ios-xe-mgmt.cisco.com      : ok=1    changed=1    unreachable=0    failed=0

## Verify the removal
(venv) [root@localhost intro-ansible]# ansible-playbook ansible-02-ios-modules/02-ios_command_show_ntp.yaml

PLAY [Sample IOS show ntp for Ansible 2.5] ***********************************************************************************

TASK [run show ntp associations] *********************************************************************************************
ok: [ios-xe-mgmt.cisco.com]

TASK [display value of "myntp" variable] *************************************************************************************
ok: [ios-xe-mgmt.cisco.com] => {
    "myntp[\"stdout_lines\"][0]": [
        ""
    ]
}

PLAY RECAP *******************************************************************************************************************
ios-xe-mgmt.cisco.com      : ok=2    changed=0    unreachable=0    failed=0

(venv) [root@localhost intro-ansible]#
