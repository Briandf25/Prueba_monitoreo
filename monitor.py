import psutil
import platform
import os
from datetime import datetime

def get_size(bytes, suffix="B"):
    # Escala para bytes (ej. KB, MB, GB)
    factor = 1024
    for unit in ["", "K", "M", "G", "T"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def system_info():
    print("="*40, "Información del Sistema", "="*40)
    uname = platform.uname()
    print(f"Sistema: {uname.system}")
    print(f"Nombre del Nodo: {uname.node}")
    print(f"Versión: {uname.version}")
    print(f"Máquina: {uname.machine}")
    print(f"Procesador: {uname.processor}")

def cpu_info():
    print("="*40, "Información de CPU", "="*40)
    print(f"Uso de CPU: {psutil.cpu_percent(interval=1)}%")
    print(f"Núcleos físicos: {psutil.cpu_count(logical=False)}")
    print(f"Núcleos lógicos: {psutil.cpu_count(logical=True)}")

def memory_info():
    print("="*40, "Memoria", "="*40)
    svmem = psutil.virtual_memory()
    print(f"Total: {get_size(svmem.total)}")
    print(f"Disponible: {get_size(svmem.available)}")
    print(f"Usada: {get_size(svmem.used)}")
    print(f"Porcentaje: {svmem.percent}%")

def disk_info():
    print("="*40, "Disco", "="*40)
    partitions = psutil.disk_partitions()
    for partition in partitions:
        try:
            usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            continue
        print(f"Partición {partition.device}")
        print(f"  Total: {get_size(usage.total)}")
        print(f"  Usado: {get_size(usage.used)}")
        print(f"  Libre: {get_size(usage.free)}")
        print(f"  Porcentaje: {usage.percent}%")

def uptime_info():
    boot_time = datetime.fromtimestamp(psutil.boot_time())
    now = datetime.now()
    uptime = now - boot_time
    print("="*40, "Uptime del Sistema", "="*40)
    print(f"Desde: {boot_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Uptime: {str(uptime).split('.')[0]}")

def process_info():
    print("="*40, "Procesos", "="*40)
    processes = psutil.pids()
    print(f"Cantidad total de procesos: {len(processes)}")

if __name__ == "__main__":
    system_info()
    cpu_info()
    memory_info()
    disk_info()
    uptime_info()
    process_info()
