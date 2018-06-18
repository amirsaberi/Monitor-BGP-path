#!/bin/bash

range23=`/usr/bin/python bgp-chk.py 1.1.1.0/23`
range24=`/usr/bin/python bgp-chk.py 1.1.1.0/24`

server=192.168.1.1
host="Zabbix server"
zbxconfig=/etc/zabbix/zabbix_agentd.conf

if [[ -z "$range23" || -z "$range24" ]]
then
	/usr/bin/zabbix_sender  -c $zbxconfig -k bgp.checking -o "2" -z $server -s "$host" > /dev/null
elif [[ "$range23" == "$range24" ]]
then
	/usr/bin/zabbix_sender  -c $zbxconfig -k bgp.checking -o "1" -z $server -s "$host" > /dev/null
else
        /usr/bin/zabbix_sender  -c $zbxconfig -k bgp.checking -o "0" -z $server -s "$host" > /dev/null
fi
