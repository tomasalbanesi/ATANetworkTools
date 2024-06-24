import time
import psutil
from datetime import datetime
from atanet_tools.ata_ip import get_my_ip
import csv

def scan_bw_to_console(limit_time = 60, show_datetime = True):
    
    print("\n")
    
    my_ip = get_my_ip()
    
    print(f"# Bandwidth scan started from IP: {my_ip}")
    
    init_time = time.time()
    
    last_received = psutil.net_io_counters().bytes_recv
    last_sent = psutil.net_io_counters().bytes_sent
    last_total = last_received + last_sent
    
    while time.time() - init_time < limit_time:
        
        actual_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        bytes_received = psutil.net_io_counters().bytes_recv
        bytes_sent = psutil.net_io_counters().bytes_sent
        bytes_total = bytes_received + bytes_sent
        
        new_received = bytes_received - last_received
        new_sent = bytes_sent - last_sent
        new_total = bytes_total - last_total
        
        mb_new_received = new_received / 1024 / 1024
        mb_new_sent = new_sent / 1024 / 1024
        mb_new_total = new_total / 1024 / 1024
        
        if show_datetime == True:
            print(f"Actual date and time: {actual_datetime}, {mb_new_received:.2f} MB received, {mb_new_sent:.2f} MB sent, {mb_new_total:.2f} MB total")
        else:
            print(f"{mb_new_received:.2f} MB received, {mb_new_sent:.2f} MB sent, {mb_new_total:.2f} MB total")
    
        last_received = bytes_received
        last_sent = bytes_sent
        last_total = bytes_total
        
        time.sleep(1)
        
    print(f"# Bandwidth scan finished from IP: {my_ip}")
    
    print("\n")
        
def scan_bw_to_file(limit_time, path_csv):
    
    my_ip = get_my_ip()
    
    print("\n")
    
    print(f"# Bandwidth scan started from IP: {my_ip}")
    print(f"Please wait, currently writing the file with the data ...")
    
    with open(path_csv, mode='w', newline='') as file:
        
        writer = csv.writer(file)
        # Escribir el encabezado del CSV
        writer.writerow(['Fecha y Hora', 'IP', 'MB Received', 'MB Sent', 'MB Total'])
    
        init_time = time.time()
    
        last_received = psutil.net_io_counters().bytes_recv
        last_sent = psutil.net_io_counters().bytes_sent
        last_total = last_received + last_sent
    
        while time.time() - init_time < limit_time:
            
            actual_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            bytes_received = psutil.net_io_counters().bytes_recv
            bytes_sent = psutil.net_io_counters().bytes_sent
            bytes_total = bytes_received + bytes_sent
            
            new_received = bytes_received - last_received
            new_sent = bytes_sent - last_sent
            new_total = bytes_total - last_total
            
            mb_new_received = new_received / 1024 / 1024
            mb_new_sent = new_sent / 1024 / 1024
            mb_new_total = new_total / 1024 / 1024
            
            # Escribir la fecha, hora e IP en el archivo CSV
            writer.writerow([actual_datetime, my_ip, mb_new_received, mb_new_sent, mb_new_total])
        
            last_received = bytes_received
            last_sent = bytes_sent
            last_total = bytes_total
            
            time.sleep(1)
    
    print(f"# Bandwidth scan finished from IP: {my_ip}")
    print(f"The file with the data has saved in {path_csv}")
    
    print("\n")
        
        
def detect_bw_greater_than(mb_received_value = 0, mb_sent_value = 0):
    
    print("Method in testing")
    
def detect_bw_lower_than(mb_received_value = 0, mb_sent_value = 0):
    
    print("Method in testing")