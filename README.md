::::::::::::::::::::::BID v1.0::::::::::::::::::::::::::::::

This is simple python3 script which uses subprocess to call functions that will help you to DOS wireless networks... 

To make this work, you will need to have python installed and you'll need to work on linux


Tools that you will need to have installed:
	-airmon-ng
	-airodump-ng
	-aireplay-ng


1. Usage

	-Download
	-Find your targets Access point MAC address and channel
	-Type in next command line;
		example: python3 BID.py --mac 00:00:00:a1:2b:cc --channel 8 -i wlan0   
		example: python3 BID.py --m 00:00:00:a1:2b:cc --c 10 -i wlan1   

	-To stop the program press CTRL-D

	
2. How it works?
	It's quite simple, just passed in list of commands to subprocess...
	First it will set your wireless card into monitoring mode,
	than it will setup the channel on which your card will monitor,
	perform airmon-ng check kill, to kill processes that could disrupt,
	start the attack with flooding Access point with deauth packets.
	
3. Turning off monitor mode
	#check the name of your interface by typing ifconfig
	
	I'll add it soon but for now type:
		
		ifconfig wlan0 down
		iwconfig wlan0 mode managed
		ifconfig wlan0 up
		
		su service networking restart
		su service network-manager start


