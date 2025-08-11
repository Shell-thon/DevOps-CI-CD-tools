import socket

ports = [22, 80, 443, 8000, 8080]
for port in ports:
    s = socket.socket()
    s.settimeout(1)
    try:
        s.connect(("127.0.0.1", port))
        print(f"✅ Port {port} is OPEN")
    except:
        print(f"❌ Port {port} is CLOSED")
    s.close()
