#######################################################################
# VPN_connecter.py                                                    #
#								      #
# A simple Script to automate and simplify connecting to the  VPN     #
# ------------------------------------------------------------------- #
# INSTRUCTIONS                                                        #
#                                                                     #
# 1. pip install pexpect                                              #
# 2. Move this script to the same directory as forticlientsslvpn_cli  #
# 3. Enter your VPN/domain credentials in this script and save it.    #
# 4. Run this script using the command `python connect_vpn.py`        #
#                                                                     #
# Shubham Gupta Precog@IIITD                                          #
#######################################################################

import pexpect

#Enter credentials here:
username = 'Enter username'
password = 'Enter password'

server_url = "https://vpn.iiitd.edu.in:10443" #Do not edit this
child = pexpect.spawn ('./forticlientsslvpn_cli  --server '+server_url+' --vpnuser '+username+'  --keepalive')
child.expect ('Password for VPN:')
child.sendline (password+'\r')

#Answer to do you want to connect ?
child.sendline ('y\r')
#handback control to user
child.interact()
