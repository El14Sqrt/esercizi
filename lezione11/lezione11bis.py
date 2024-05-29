class ContoBancario:

    total_accounts = 0

    def __init__(self, iban, nome, saldo):
        self.iban = iban
        self.nome = nome 
        self.saldo = saldo

        ContoBancario.total_accounts += 1

    def deposito(self, importo):
        self.saldo += importo

        print(f"{importo} depositato. Il nuovo saldo è {self.saldo}")

    def prelievo(self, importo):
        self.saldo -= importo

        print(f"{importo} prelevato. Il nuovo saldo è {self.saldo}")

    @classmethod
    def get_total_accounts(cls):
        print(f"Account totali creati: {cls.total_accounts}")
    
    @staticmethod
    def valida_account(iban):
        if isinstance(iban, int) and len(str(iban)) == 10:
            print("iban valido")
            return True
        else:
            print("iban non valido")
            return False
        

account1 = ContoBancario(1234567890, 0, "Alice")
account2 = ContoBancario(9876543210, 1000, "Bob")

account1.deposito(520)
account1.prelievo(70)

account2.deposito(432)
account2.prelievo(402)

ContoBancario.get_total_accounts()

ContoBancario.valida_account(1234567890)
ContoBancario.valida_account("nejd58f455")
