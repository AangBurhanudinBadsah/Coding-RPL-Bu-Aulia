perangkat = {
    "router": {"nama": "Router Utama", "ip": "192.168.1.1", "status": "up"},
    "switch": {"nama": "Switch Utama", "ip": "192.168.1.2", "status": "up"},
    "ap1": {"nama": "AP Lantai 1", "ip": "192.168.1.3", "status": "down"},
    "server": {"nama": "Server Web", "ip": "192.168.1.4", "status": "up"}
}

def cek_semua(data):
    print("Status perangkat saat ini:")
    for key in data:
        nama = data[key]["nama"]
        ip = data[key]["ip"]
        status = data[key]["status"]
        print(f"- {nama} ({ip}) -> {status}")

def hitung_aktif(data):
    total = 0
    for key in data:
        if data[key]["status"] == "up":
            total += 1
    return total

cek_semua(perangkat)
print("Jumlah yang aktif:", hitung_aktif(perangkat))
