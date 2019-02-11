from netmiko import ConnectHandler

r1 = {
	"device_type" : "ipinfusion_ocnos_ssh",
	"ip" : "172.26.1.118",
	"username" : "ocnos",
	"password" : "ocnos",
}
r2 = {
	"device_type" : "ipinfusion_ocnos_ssh",
	"ip" : "172.26.1.119",
	"username" : "ocnos",
	"password" : "ocnos",
}
r3 = {
	"device_type" : "ipinfusion_ocnos_ssh",
	"ip" : "172.26.1.120",
	"username" : "ocnos",
	"password" : "ocnos",
}
r4 = {
	"device_type" : "ipinfusion_ocnos_ssh",
	"ip" : "172.26.1.121",
	"username" : "ocnos",
	"password" : "ocnos",
}
r5 = {
	"device_type" : "ipinfusion_ocnos_ssh",
	"ip" : "172.26.1.122",
	"username" : "ocnos",
	"password" : "ocnos",
}
r6 = {
	"device_type" : "ipinfusion_ocnos_ssh",
	"ip" : "172.26.1.123",
	"username" : "ocnos",
	"password" : "ocnos",
}


device_list = [r1,r2,r3,r4,r5,r6]
for device in device_list:
    conn = ConnectHandler(**device)
    print("Connected Successfully with ", device)
    #output = conn.send_command('show ip int brief')
    #print(output)
    conn.enable()
    #output=conn.send_config_set('enable')
    output=conn.send_config_set('no feature guest-vm enable')
    print output
    conn.send_command('int ce1/1')
    conn.send_command('ip address 10.0.0.2 255.255.255.0')
    conn.send_command('no shut')
    output = conn.send_command('show ip int brief')
    print(output)
