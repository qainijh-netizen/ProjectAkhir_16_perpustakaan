from datetime import datetime, timedelta

buku_list = []
peminjaman = []
JAM_TUTUP = 16  

buku_list = [
    {'judul': 'Laskar Pelangi', 'penulis': 'Andrea Hirata', 'tahun': 2005, 'stok': 5},
    {'judul': 'Sang Pemimpi', 'penulis': 'Andrea Hirata', 'tahun': 2006, 'stok': 4},
    {'judul': 'Edensor', 'penulis': 'Andrea Hirata', 'tahun': 2007, 'stok': 3},
    {'judul': 'Bumi', 'penulis': 'Tere Liye', 'tahun': 2014, 'stok': 6},
    {'judul': 'Bulan', 'penulis': 'Tere Liye', 'tahun': 2015, 'stok': 5},
    {'judul': 'Matahari', 'penulis': 'Tere Liye', 'tahun': 2016, 'stok': 4},
    {'judul': 'Ronggeng Dukuh Paruk', 'penulis': 'Ahmad Tohari', 'tahun': 1982, 'stok': 3},
    {'judul': 'Kubah', 'penulis': 'Ahmad Tohari', 'tahun': 1980, 'stok': 2},
    {'judul': 'Di Kaki Bukit Cibalak', 'penulis': 'Ahmad Tohari', 'tahun': 1986, 'stok': 4},
    {'judul': 'Bumi Manusia', 'penulis': 'Pramoedya Ananta Toer', 'tahun': 1980, 'stok': 5},
    {'judul': 'Anak Semua Bangsa', 'penulis': 'Pramoedya Ananta Toer', 'tahun': 1980, 'stok': 4},
    {'judul': 'Jejak Langkah', 'penulis': 'Pramoedya Ananta Toer', 'tahun': 1985, 'stok': 3},
    {'judul': 'Senja di Jakarta', 'penulis': 'Mochtar Lubis', 'tahun': 1970, 'stok': 6},
    {'judul': 'Jalan Tak Ada Ujung', 'penulis': 'Mochtar Lubis', 'tahun': 1952, 'stok': 4},
    {'judul': 'Layar Terkembang', 'penulis': 'Sutan Takdir Alisjahbana', 'tahun': 1936, 'stok': 3}
]


def tampil_daftar_buku():
    if not buku_list:
        print("Tidak ada buku.\n")
        return

    print("\n=== DAFTAR BUKU ===")
    print("=" * 80)
    print("{:<4} {:<25} {:<25} {:<10} {:<5}".format(
        "No", "Judul", "Penulis", "Tahun", "Stok"
    ))
    print("-" * 80)

    for i, b in enumerate(buku_list, start=1):
        print("{:<4} {:<25} {:<25} {:<10} {:<5}".format(
            i, b['judul'], b['penulis'], b['tahun'], b['stok']
        ))

    print("=" * 80 + "\n")


def lihat_detail_buku():
    tampil_daftar_buku()
    if not buku_list:
        return

    while True:
        idx_str = input("Pilih nomor buku: ").strip()
        if idx_str.isdigit():
            idx = int(idx_str) - 1
            if 0 <= idx < len(buku_list):
                break
        print("Nomor tidak valid.")

    buku = buku_list[idx]
    total_pinjam = sum(1 for p in peminjaman if p['judul'] == buku['judul'])

    print("\n=== DETAIL BUKU ===")
    print(f"Judul            : {buku['judul']}")
    print(f"Penulis          : {buku['penulis']}")
    print(f"Tahun Terbit     : {buku['tahun']}")
    print(f"Stok             : {buku['stok']}")
    print(f"Pernah Dipinjam  : {total_pinjam} kali\n")


def tambah_buku():
    while True:
        judul = input("Judul: ").strip()
        if judul:
            break
        print("Tidak boleh kosong.")

    while True:
        penulis = input("Penulis: ").strip()
        if penulis.replace(" ", "").isalpha():
            break
        print("Penulis harus huruf.")

    while True:
        t = input("Tahun terbit: ").strip()
        if t.isdigit() and 1000 <= int(t) <= datetime.now().year:
            tahun = int(t)
            break
        print("Tahun tidak valid.")

    while True:
        s = input("Stok: ").strip()
        if s.isdigit():
            stok = int(s)
            break
        print("Stok harus angka.")

    buku_list.append({'judul': judul, 'penulis': penulis, 'tahun': tahun, 'stok': stok})
    print("Buku ditambahkan!\n")


def update_buku():
    tampil_daftar_buku()
    if not buku_list:
        return

    while True:
        idx_str = input("Nomor buku: ").strip()
        if idx_str.isdigit():
            idx = int(idx_str)-1
            if 0 <= idx < len(buku_list):
                break
        print("Nomor tidak valid.")

    print("Kosongkan untuk tidak mengubah.")

    j = input("Judul baru: ").strip()
    if j != "":
        buku_list[idx]['judul'] = j

    p = input("Penulis baru: ").strip()
    if p != "" and p.replace(" ", "").isalpha():
        buku_list[idx]['penulis'] = p

    t = input("Tahun baru: ").strip()
    if t.isdigit() and len(t) == 4:
        ty = int(t)
        if 1000 <= ty <= datetime.now().year:
            buku_list[idx]['tahun'] = ty

    s = input("Stok baru: ").strip()
    if s.isdigit():
        buku_list[idx]['stok'] = int(s)

    print("Buku diperbarui!\n")


def hapus_buku():
    tampil_daftar_buku()
    if not buku_list:
        return

    while True:
        idx_str = input("Nomor buku: ").strip()
        if idx_str.isdigit():
            idx = int(idx_str)-1
            if 0 <= idx < len(buku_list):
                break
        print("Nomor tidak valid.")

    while True:
        konf = input("Yakin hapus? (ya/tidak): ").lower()
        if konf in ("ya", "tidak"):
            break
        print("Jawab ya/tidak.")

    if konf == "ya":
        del buku_list[idx]
        print("Dihapus.\n")
    else:
        print("Dibatalkan.\n")


def pinjam_buku():
    while True:
        print("\n=== MENU PEMINJAMAN ===")
        print("1. Lihat daftar buku")
        print("2. Lihat detail buku")
        print("3. Pilih buku untuk dipinjam")
        print("4. Kembali")

        pilih = input("Pilih: ").strip()

        if pilih == '1':
            tampil_daftar_buku()

        elif pilih == '2':
            lihat_detail_buku()

        elif pilih == '3':
            tampil_daftar_buku()

            while True:
                idx_str = input("Pilih nomor buku: ").strip()
                if idx_str.isdigit():
                    idx = int(idx_str)-1
                    if 0 <= idx < len(buku_list):
                        break
                print("Nomor salah.")

            if buku_list[idx]['stok'] <= 0:
                print("Stok habis.\n")
                continue

            while True:
                nama = input("Nama peminjam: ").strip()
                if nama.replace(" ", "").isalpha():
                    break
                print("Nama harus huruf.")

            while True:
                m = input("Apakah sudah member? (ya/tidak): ").lower()
                if m in ("ya", "tidak"):
                    member = (m == "ya")
                    break
                print("Jawab ya/tidak.")

            sekarang = datetime.now()
            tgl_pinjam = sekarang.date()

            if not member and sekarang.hour >= JAM_TUTUP:
                print(f"Jam operasional sudah tutup ({JAM_TUTUP} WIB), tidak bisa meminjam hari ini.\n")
                return

            batas = tgl_pinjam + timedelta(days=3 if member else 0)

            peminjaman.append({
                'nama': nama,
                'judul': buku_list[idx]['judul'],
                'idx': idx,
                'tgl_pinjam': tgl_pinjam,
                'batas': batas,
                'member': member,
                'perpanjangan_count': 0,
                'status': 'Dipinjam'
            })

            buku_list[idx]['stok'] -= 1

            print("\n=== STRUK PEMINJAMAN ===")
            print(f"Nama   : {nama}")
            print(f"Judul  : {buku_list[idx]['judul']}")
            print(f"Member : {'Ya' if member else 'Tidak'}")
            print(f"Pinjam : {tgl_pinjam}")
            print(f"Batas  : {batas}")
            print("=========================\n")
            return

        elif pilih == '4':
            return

        else:
            print("Pilih 1-4.\n")


def tampil_data_peminjaman():
    if not peminjaman:
        print("Tidak ada data.\n")
        return

    print("\n=== DATA PEMINJAMAN ===")
    print("{:<4} {:<20} {:<25} {:<12} {:<5}".format(
        "No", "Nama", "Judul", "Status", "Stok"
    ))
    print("-" * 75)

    for i, p in enumerate(peminjaman, start=1):
        status = 'Masih dipinjam' if p['status'] == 'Dipinjam' else 'Dikembalikan'
        stok = buku_list[p['idx']]['stok']
        print("{:<4} {:<20} {:<25} {:<12} {:<5}".format(
            i,
            p['nama'],
            p['judul'],
            status,
            stok
        ))
    print("")


def kembalikan_buku():
    tampil_data_peminjaman()
    if not peminjaman:
        return

    while True:
        idx_str = input("Nomor: ").strip()
        if idx_str.isdigit():
            idx = int(idx_str)-1
            if 0 <= idx < len(peminjaman) and peminjaman[idx]['status'] == 'Dipinjam':
                break
        print("Nomor salah atau buku sudah dikembalikan.")

    while True:
        m = input("Konfirmasi pengembalian? (ya/tidak): ").lower()
        if m in ("ya","tidak"):
            break
        print("Jawab ya/tidak.")

    if m == "ya":
        while True:
            mode = input("Tanggal pengembalian otomatis atau manual? (otomatis/manual): ").lower()
            if mode in ("otomatis", "manual"):
                break
            print("Jawab otomatis/manual.")

        if mode == "otomatis":
            tgl_kembali = datetime.now().date()
        else:
            while True:
                tgl_input = input("Masukkan tanggal pengembalian (YYYY-MM-DD): ").strip()
                try:
                    tgl_kembali = datetime.strptime(tgl_input, "%Y-%m-%d").date()
                    break
                except:
                    print("Format salah, gunakan YYYY-MM-DD.")

        telat_hari = max(0, (tgl_kembali - peminjaman[idx]['batas']).days)
        if telat_hari > 0:
            denda = telat_hari * 10000
            print(f"Telat {telat_hari} hari. Denda: Rp {denda}")
        else:
            denda = 0
            print("Tidak ada denda.")

        buku_list[peminjaman[idx]['idx']]['stok'] += 1
        peminjaman[idx]['status'] = 'Dikembalikan'
        peminjaman[idx]['tgl_kembali'] = tgl_kembali
        print("Buku berhasil dikembalikan.\n")
    else:
        print("Dibatalkan.\n")


def submenu_kelola_buku():
    while True:
        print("\n=== KELOLA BUKU ===")
        print("1. Tambah")
        print("2. Lihat")
        print("3. Update")
        print("4. Hapus")
        print("5. Kembali")

        pilih = input("Pilih: ")
        if pilih == '1':
            tambah_buku()
        elif pilih == '2':
            tampil_daftar_buku()
        elif pilih == '3':
            update_buku()
        elif pilih == '4':
            hapus_buku()
        elif pilih == '5':
            break
        else:
            print("Pilih 1-5.\n")


def menu_pustakawan():
    while True:
        print("\n=== MENU PUSTAKAWAN ===")
        print("1. Pinjam Buku")
        print("2. Pengembalian Buku")
        print("3. Kelola Buku")
        print("4. Data Buku Dipinjam")
        print("5. Keluar")

        pilih = input("Pilih: ")
        if pilih == '1':
            pinjam_buku()
        elif pilih == '2':
            kembalikan_buku()
        elif pilih == '3':
            submenu_kelola_buku()
        elif pilih == '4':
            tampil_data_peminjaman()
        elif pilih == '5':
            break
        else:
            print("Pilih 1-5.\n")


if __name__ == '__main__':
    menu_pustakawan()
