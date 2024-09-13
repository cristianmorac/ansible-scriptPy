import psutil
import platform
import datetime

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
    
    return info

def save_to_file(info, filename):
    """Guarda la información del sistema en un archivo plano."""
    with open(filename, 'w') as f:
        f.write("Información del Sistema:\n")
        for key, value in info.items():
            f.write(f"{key}: {value}\n")

def print_system_info(info):
    """Imprime la información del sistema."""
    print("\nInformación del Sistema:")
    for key, value in info.items():
        print(f"{key}: {value}")

def main():
    """Función principal del script."""
    system_info = get_system_info()
    print_system_info(system_info)

    # Guardar la información en un archivo plano
    filename = f"{system_info['Node Name']}_status.txt"
    save_to_file(system_info, filename)
    print("\nLa información del servidor ha sido guardada en 'server_status.txt'.")

if __name__ == "__main__":
    main()