#!/usr/bin/env python3
"""Chat para dos personas por TCP. Solo necesita Python 3.

Comparte ESTE archivo con tu compañero por WhatsApp.
Ambos deben estar en la misma red local (Wi-Fi o Ethernet).

1. Una persona ejecuta:  python chat_lan.py servidor
2. La otra ejecuta:      python chat_lan.py cliente IP_DEL_SERVIDOR
   Ejemplo:             python chat_lan.py cliente 192.168.1.25

Sin argumentos, el programa pregunta qué hacer. Escribe /salir para terminar.
Puerto opcional: python chat_lan.py servidor --puerto 5001
Usa ese mismo --puerto en el cliente. Si tu sistema usa python3, úsalo.
Si el firewall pregunta, permite Python en la red privada.
Los mensajes viajan como texto sin cifrar; no envíes contraseñas.
"""

import argparse
import socket
import threading


def ip_local():
    """Consulta la ruta local sin enviar datos ni necesitar Internet."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as probe:
            probe.connect(("192.0.2.1", 1))
            return probe.getsockname()[0]
    except OSError:
        return "(consulta tu IPv4 con ipconfig en Windows o ip addr en Linux)"


def conversar(conn):
    terminado = threading.Event()
    salida = threading.Lock()

    def cerrar():
        terminado.set()
        try:
            conn.shutdown(socket.SHUT_RDWR)
        except OSError:
            pass

    def enviar():
        while not terminado.is_set():
            try:
                mensaje = input()
                if mensaje.strip() == "/salir":
                    break
                if mensaje.strip():
                    conn.sendall((mensaje + "\n").encode("utf-8"))
                    with salida:
                        print("Tú: " + mensaje, flush=True)
            except (EOFError, OSError):
                break
        cerrar()

    print("Conectados. Escribe y pulsa Enter. /salir para terminar.", flush=True)
    threading.Thread(target=enviar, daemon=True).start()
    try:
        # TCP entrega un flujo: las líneas delimitan mensajes aunque se fragmenten.
        with conn.makefile("r", encoding="utf-8", errors="replace") as mensajes:
            for mensaje in mensajes:
                with salida:
                    print("Compañero: " + mensaje.rstrip("\n"), flush=True)
    finally:
        cerrar()
        print("Chat cerrado.", flush=True)


def main():
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("modo", nargs="?", choices=("servidor", "cliente"))
    parser.add_argument("ip", nargs="?", help="IP local de quien abre el servidor")
    parser.add_argument("--puerto", type=int, default=5000)
    args = parser.parse_args()
    if not 1 <= args.puerto <= 65535:
        parser.error("El puerto debe estar entre 1 y 65535.")
    if args.modo is None:
        opcion = input("¿Crear chat (1) o conectarte (2)? ").strip()
        if opcion not in ("1", "2"):
            parser.error("Elige 1 o 2.")
        args.modo = "servidor" if opcion == "1" else "cliente"

    if args.modo == "servidor":
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
            servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            servidor.bind(("0.0.0.0", args.puerto))
            servidor.listen(1)
            print("Tu IP local: " + ip_local(), flush=True)
            print(f"Esperando a tu compañero en el puerto {args.puerto}…", flush=True)
            conn, direccion = servidor.accept()
            print(f"Se conectó {direccion[0]}.", flush=True)
            with conn:
                conversar(conn)
    else:
        ip = args.ip or input("IP local de tu compañero: ").strip()
        print(f"Conectando a {ip}:{args.puerto}…", flush=True)
        with socket.create_connection((ip, args.puerto), timeout=10) as conn:
            conn.settimeout(None)
            conversar(conn)


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nChat cerrado.")
    except OSError as error:
        print(f"No se pudo continuar: {error}")
        print("Revisa la IP, el puerto, el firewall y que estén en la misma red.")
        raise SystemExit(1)
