import subprocess
import platform
import time
import json

def ping(host):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", host]
    try:
        output = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=3)
        if output.returncode == 0:
            return f" {host} está activo"
        else:
            return f" {host} no responde"
    except subprocess.TimeoutExpired:
        return f"{host} tiempo de espera agotado"

def cargar_hosts(ruta_archivo):
    with open(ruta_archivo, "r") as archivo:
        data = json.load(archivo)
        return data["hosts"]

if __name__ == "__main__":
    hosts = cargar_hosts("hosts.json")
    for host in hosts:
        resultado = ping(host)
        print(resultado)
        time.sleep(1)  # Espera 1 segundo entre cada ping

