"""ATA Smart Solutions Network Tools Demo
This is a complete demo of the modulo atanet_tools with many examples of functions.
"""
import atanet_tools
import atanet_tools.ata_bandwidth as bw
import atanet_tools.ata_network as net
import atanet_tools.ata_discover as disco
import atanet_tools.ata_ip as ip

print("\n")    
print("¡Welcome to ATA Network Tools Demo!\n")
print("Please, choose the predefined function to run: \n\n")
print("     * 0) About the module\n")
print("     * 1) Scan bandwidth to console\n")
print("     * 2) Scan bandwidth to file\n")
print("     * 3) Get my IPv4 Address\n")
print("     * 4) Get my network information\n")

selection = int(input("\n Select the function with the number: "))

if selection < 0:
    selection = 0
    print('Negative changed to zero')
    
elif selection == 0:
    print(f"\nAuthor: {atanet_tools.__author__}")
    print(f"Copyright: {atanet_tools.__copyright__}")
    print(f"Credits: ")
    for credit in atanet_tools.__credits__:
        print(f" * {credit}")
    print(f"License: {atanet_tools.__license__}")
    print(f"Version: {atanet_tools.__version__}")
    print(f"Mainteiner: {atanet_tools.__maintainer__}")
    print(f"Email: {atanet_tools.__email__}")
    print(f"Status: {atanet_tools.__status__}\n")
    
elif selection == 1:
    limit_time = int(input("\nEnter the limit time of the scan (in seconds): "))
    str_show_datetime = str(input("\nDo you want to show the datetime? (Y/N): "))
    show_datetime = False
    if str_show_datetime == "Y":
        show_datetime = True
    elif str_show_datetime == "N":
        show_datetime = False 
    bw.scan_bw_to_console(limit_time=limit_time, show_datetime=show_datetime)
    
else:
    print('More')

