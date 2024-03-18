class AngkaTercetak:
    def __init__(self, nim):
        self.dua_digit_terakhir_nim = int(nim[-2:])
        self.angka_tercetak = 0

    def cetak_angka(self):
        for i in range(1, 51):
            if i != self.dua_digit_terakhir_nim:
                print(i, end=" ")
                self.angka_tercetak += 1
                if self.angka_tercetak % 26 == 0:
                    print()  # Pindah ke baris baru

nim = input("Masukkan dua digit terakhir NIM Anda: ")

angka_tercetak = AngkaTercetak(nim)

angka_tercetak.cetak_angka()
