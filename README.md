# VPN-connecter
A python script to make the process of connecting to forticlient VPN automatic and less painful for Ubuntu/Debian Systems

## Instructions to use
1. Obtain forticlient for Ubuntu/Debian. For IIIT Delhi users, see this [link](http://it.iiitd.edu.in/VPN.pdf).
2. Clone this Repo and move VPN_connecter.py in the same directory as forticlientsslvpn_cli.
3. Install pexpect by pip  `pip install pexpect    `
4. Run `./helper/setup.linux.sh` inside the folder containing forticlientsslvpn_cli and accept terms and conditions by entereing `yes`. You will also need to enter root password here.
5. Edit VPN_connecter.py to enter your username and password.
6. run using `python VPN_connecter.py `

**Note:** forticlientsslvpn_cli can be found at the location`forticlientsslvpn_linux_4.4.2/forticlientsslvpn/64bit/forticlientsslvpn_cli` or `forticlientsslvpn_linux_4.4.2/forticlientsslvpn/32bit/forticlientsslvpn_cli`
