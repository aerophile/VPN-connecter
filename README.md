# VPN-connecter
A python script to make the process of connecting to forticlient VPN automatic and less painful for Ubuntu/Debian Systems

## Instructions to use
1. Obtain forticlient for Ubuntu/Debian. For IIIT Delhi users, see this [link](http://it.iiitd.edu.in/VPN.pdf).
2. Clone this Repo and copy forticlientsslvpn_cli into this repo.
3. Install pexpect by pip  `pip install pexpect    `
4. Edit VPN_connecter.py to enter your username and password.
5. run using `python VPN_connecter.py `

**Note:** forticlientsslvpn_cli can be found at the location`forticlientsslvpn_linux_4.4.2/forticlientsslvpn/64bit/forticlientsslvpn_cli` or `forticlientsslvpn_linux_4.4.2/forticlientsslvpn/32bit/forticlientsslvpn_cli`
