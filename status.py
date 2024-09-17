import psutil
import platform
import datetime
from ping3 import ping, verbose_ping

def get_system_info():
    """Obtiene información del sistema."""
    info = {}
    
    # Información básica
    uname_info = platform.uname()
    info['System'] = uname_info.system
    info['Node Name'] = uname_info.node
    info['Release'] = uname_info.release
    info['Version'] = uname_info.version
    info['Machine'] = uname_info.machine
    info['Processor'] = uname_info.processor

    # Uso de CPU
    info['CPU Usage (%)'] = psutil.cpu_percent(interval=1)
    
    # Memoria
    mem = psutil.virtual_memory()
    info['Total Memory (GB)'] = round(mem.total / (1024 ** 3), 2)
    info['Available Memory (GB)'] = round(mem.available / (1024 ** 3),2)
    info['Used Memory (GB)'] = round(mem.used / (1024 ** 2),2)
    
    # Espacio en disco
    disk = psutil.disk_usage('/')
    info['Total Disk Space (GB)'] = round(disk.total / (1024 ** 3),2)
    info['Used Disk Space (GB)'] = round(disk.used / (1024 ** 3),2)
    info['Free Disk Space (GB)'] = round(disk.free / (1024 ** 3),2)

    # Tiempo de actividad
    uptime_seconds = psutil.boot_time()
    uptime = datetime.datetime.fromtimestamp(uptime_seconds)
    info['System Uptime'] = datetime.datetime.now() - uptime

    response_time = ping("8.8.8.8")
    if response_time is not None:
        info['ping'] = f"Reachable, response time: {response_time:.2f} seconds"
    else:
        info['ping'] = "Not Reachable"
    
    return info

def save_to_file(info, filename):
    """Guarda la información del sistema en un archivo plano."""
    with open(filename, 'w') as f:
        f.write("Información del Sistema:\n")
        for key, value in info.items():
            f.write(f"{key}: {value}\n")

def main():
    """Función principal del script."""
    system_info = get_system_info()

    # Guardar la información en un archivo plano
    filename = f"{system_info['Node Name']}_status.txt"
    save_to_file(system_info, filename)

if __name__ == "__main__":
    main()