# ============================================================
#  CAESAR CIPHER
#  Nama   : Yuli Indiyanti  |  NIM : 240511130  |  Kelas : TI24D
#  Matkul : Matematika Diskrit
#
#  Formula:
#    Enkripsi : C = (P + shift) mod 26
#    Dekripsi : P = (C - shift) mod 26
# ============================================================


def enkripsi(plaintext, shift):
    """Menggeser setiap huruf maju sebanyak 'shift' posisi."""
    hasil = ""
    for huruf in plaintext:
        if huruf.isalpha():
            basis = ord('A') if huruf.isupper() else ord('a')
            hasil += chr((ord(huruf) - basis + shift) % 26 + basis)
        else:
            hasil += huruf
    return hasil


def dekripsi(ciphertext, shift):
    """Menggeser setiap huruf mundur sebanyak 'shift' posisi."""
    hasil = ""
    for huruf in ciphertext:
        if huruf.isalpha():
            basis = ord('A') if huruf.isupper() else ord('a')
            hasil += chr((ord(huruf) - basis - shift) % 26 + basis)
        else:
            hasil += huruf
    return hasil


def brute_force(ciphertext):
    """Mencoba semua 25 kemungkinan kunci secara otomatis."""
    print(f"\nBrute Force — Ciphertext: \"{ciphertext}\"")
    print(f"{'Shift':<8} {'Hasil Dekripsi'}")
    print("-" * 40)
    for k in range(1, 26):
        print(f"{k:<8} {dekripsi(ciphertext, k)}")


# ============================================================
#  PROGRAM UTAMA
# ============================================================
if __name__ == "__main__":

    print("=" * 50)
    print("   CAESAR CIPHER — Yuli Indiyanti | TI24D")
    print("=" * 50)

    # Contoh 1
    print("\n▶ Contoh 1")
    pt, sh = "MATEMATIKA DISKRIT", 3
    ct = enkripsi(pt, sh)
    dc = dekripsi(ct, sh)
    print(f"  Plaintext  : {pt}")
    print(f"  Shift      : {sh}")
    print(f"  Ciphertext : {ct}")
    print(f"  Dekripsi   : {dc}")
    print(f"  Verifikasi : {'✓ Berhasil' if dc == pt else '✗ Gagal'}")

    # Contoh 2
    print("\n▶ Contoh 2")
    pt, sh = "Hello World", 7
    ct = enkripsi(pt, sh)
    dc = dekripsi(ct, sh)
    print(f"  Plaintext  : {pt}")
    print(f"  Shift      : {sh}")
    print(f"  Ciphertext : {ct}")
    print(f"  Dekripsi   : {dc}")
    print(f"  Verifikasi : {'✓ Berhasil' if dc == pt else '✗ Gagal'}")

    # Contoh 3
    print("\n▶ Contoh 3")
    pt, sh = "Yuli Indiyanti", 5
    ct = enkripsi(pt, sh)
    dc = dekripsi(ct, sh)
    print(f"  Plaintext  : {pt}")
    print(f"  Shift      : {sh}")
    print(f"  Ciphertext : {ct}")
    print(f"  Dekripsi   : {dc}")
    print(f"  Verifikasi : {'✓ Berhasil' if dc == pt else '✗ Gagal'}")

    # Demo Brute Force (pakai ciphertext dari Contoh 1)
    print("\n▶ Demo Brute Force")
    ct1 = enkripsi("MATEMATIKA DISKRIT", 3)
    brute_force(ct1)

    # Mode Interaktif
    print("\n" + "=" * 50)
    print("  MODE INTERAKTIF")
    print("=" * 50)
    teks  = input("  Masukkan teks  : ")
    kunci = int(input("  Masukkan shift : "))
    ct = enkripsi(teks, kunci)
    dc = dekripsi(ct, kunci)
    print(f"\n  Ciphertext : {ct}")
    print(f"  Dekripsi   : {dc}")
    print(f"  Verifikasi : {'✓ Berhasil' if dc == teks else '✗ Gagal'}")
    print("=" * 50)
