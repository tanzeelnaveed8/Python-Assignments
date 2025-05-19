class bank :
    bank_name = "ABC bank"

    @classmethod
    def change_bank_name(cls, name):
       cls.bank_name = name

if __name__ == "__main__" :
    user1 = bank()
    user2 = bank()

    print("before change the name")
    print(f"user1 bank name is {bank.bank_name}")
    print(f"user2 bank name is {bank.bank_name}")

    bank.change_bank_name("Xyz Bank")

    print("after the change name ")
    print(f"user1 bank name is {bank.bank_name}")
    print(f"user2 bank name is {bank.bank_name}")




