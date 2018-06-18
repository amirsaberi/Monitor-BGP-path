# Monitor-BGP-path
Monitoring IP range BGP path AS and send result to the ZABBIX.

If you have multiple subnet mask with different routes and you want to make sure the routes doesn't be same, you need to monitor BGP path and make alert if one of the ranges go out of routing or both range have same route.

# Requirements
- python
- zabbix-sender
