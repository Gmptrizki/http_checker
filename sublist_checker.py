import subprocess

def run_sublist3r(domain):
    command = ["sublist3r", "-d", domain]

    try:
        print(f"\n[⚙️] Menjalankan Sublist3r untuk domain: {domain}\n")
        result = subprocess.run(command, capture_output=True, text=True)

        if result.returncode == 0:
            print("[✅] Hasil subdomain yang ditemukan:\n")
            print(result.stdout)
        else:
            print("[❌] Terjadi kesalahan saat menjalankan Sublist3r:")
            print(result.stderr)

    except FileNotFoundError:
        print("❗ Sublist3r tidak ditemukan. Pastikan sudah terinstall!")

def main():
    print("=== Sublist3r Auto Scanner ===")
    domain = input("Masukkan domain (contoh: example.com): ").strip()

    if domain == "":
        print("❗ Domain tidak boleh kosong.")
        return

    run_sublist3r(domain)

if __name__ == "__main__":
    main()
