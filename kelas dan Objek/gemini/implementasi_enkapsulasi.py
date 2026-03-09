class BankAccount:
    def __init__(self, nama, saldo):
        self._nama = nama
        self._saldo = saldo

    def get_nama(self):
        return self._nama

    def set_nama(self, nama_baru):
        self._nama = nama_baru

    def get_saldo(self):
        return self._saldo

    def setor(self, nominal):
        self._saldo += nominal

    def tarik(self, nominal):
        if nominal > self._saldo:
            print("Saldo tidak mencukupi")
        else:
            self._saldo -= nominal


akun_saya = BankAccount("Budi", 10000)
print(f"Nama: {akun_saya.get_nama()}")
print(f"Saldo: {akun_saya.get_saldo()}")

akun_saya.set_nama("Andi")
print(f"Nama Baru: {akun_saya.get_nama()}")

akun_saya.setor(80090)
print(f"saldo setelah setor: {akun_saya.get_saldo()}")

akun_saya.tarik(12003)
print(f"saldo setelah tarik: {akun_saya.get_saldo()}")
