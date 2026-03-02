import socket

ip_objetivo = "10.0.2.15"
timeout = 2

print(f"Escaneando la IP: {ip_objetivo}\n")

for puerto in range(1, 201):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)

        resultado = s.connect_ex((ip_objetivo, puerto))

        if resultado == 0:
            print(f"[+] Puerto {puerto} ABIERTO")

            try:
                banner = s.recv(1024)
                print(f"    Banner: {banner.decode().strip()}")
            except:
                print("    Banner: No disponible")

        s.close()

    except:
        pass
