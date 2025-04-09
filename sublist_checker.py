import subprocess
import os

def run_sublist3r(domain):
    output_file = f"{domain}"
    command = ["sublist3r", "-d", domain, "-o", output_file]

    try:
        print(f"\n[⚙️] Menjalankan Sublist3r untuk domain: {domain}\n")
        result = subprocess.run(command, capture_output=True, text=True)

        if result.returncode == 0:
            print(f"[✅] Hasil subdomain telah disimpan di: {output_file}\n")
            # Menampilkan hasil juga ke layar (opsional)
            with open(output_file, "r") as f:
                print(f.read())
        else:
            print("[❌] Terjadi kesalahan saat menjalankan Sublist3r:")
            print(result.stderr)

    except FileNotFoundError:
        print("❗ Sublist3r tidak ditemukan. Pastikan sudah terinstall!")

def main():
    print("=== Sublist3r Auto Scanner V1 ===")
    domain = input("Masukkan domain (contoh: example.com): ").strip()

    if domain == "":
        print("❗ Domain tidak boleh kosong.")
        return

    run_sublist3r(domain)

if __name__ == "__main__":
    main()
