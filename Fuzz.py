import ctypes, sys, struct, random
from ctypes import *
from subprocess import *
 
cases_byte = ["\xff","\x00","\x7fff","\x7ffe"]

def main():
    kernel32 = windll.kernel32
    ntdll = windll.ntdll
	
    hevDevice = kernel32.CreateFileA(\\\\.\\HackSysExtremeVulnerableDriver_mbks , 0xC0000000, 0, None, 0x3, 0, None)
	 
    if not hevDevice or hevDevice == -1:
        print "*** Couldn't get Device Driver handle."
        sys.exit(0)
 
    a = int(input("Buffer mutation (1)\nEnumerating IOCTL codes (2): "))
    if a == 1:
	for i in range (1, 40):
		buf = cases_byte[random.randint(0, 3)]*random.randint(1, 600)
		print("#", i,") buf: ", buf, " size: ", len(buf))
    		buf_ad = id(buf) + 20
    		kernel32.DeviceIoControl(hevDevice, 2237455, buf_ad, len(buf), None, 0, byref(c_ulong()), None)
    if a == 2:
	for i in range (0x222400, 0x222500):
		buf = "A"*500
    		buf_ad = id(buf) + 20
		print("IOCTL: ", i)
		kernel32.DeviceIoControl(hevDevice, i, buf_ad, len(buf), None, 0, byref(c_ulong()), None)
		
if __name__ == "__main__":
    main()