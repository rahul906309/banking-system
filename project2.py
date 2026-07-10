import pickle


class Account:
    def __init__(self, acc_no, name, acc_type, balance):
        self.acc_no = acc_no
        self.name = name
        self.acc_type = acc_type
        self.balance = balance


class bank:

    def __init__(self):
        self.data = []
        self.load_data()

    def save_data(self):
        with open("data.txt", "wb") as f:
            pickle.dump(self.data, f)

    def load_data(self):
        try:
            with open("data.txt", "rb") as f:
                self.data = pickle.load(f)
        except:
            self.data=[]

    def new_acc(self):
        acc_no = int(input("Enter Your Account Number: "))
        for acc in self.data:
            if acc.acc_no==acc_no:
                print("Account already exists")
                return
            
        name = input("Enter Your Name: ")
        acc_type = input("Enter Account Type (S/C): ")
        balance = float(input("Enter Initial Amount: "))

        acc = Account(acc_no, name, acc_type, balance)
        self.data.append(acc)
        self.save_data()
        print("Account Created Successfully")

    def deposit(self):
        acc_no = int(input("Enter Your Account Number: "))

        for acc in self.data:
            if acc.acc_no == acc_no:
                amount = float(input("Enter amount to deposit: "))
                acc.balance += amount
                self.save_data()
                print("\nAmount Deposited Successfully\n")
                return

        print("\nAccount Not Found\n")

    def withdraw(self):
        acc_no = int(input("Enter Your Account Number: "))

        for acc in self.data:
            if acc.acc_no == acc_no:
                amount = float(input("Enter amount to withdraw: "))
                if amount <= acc.balance:
                    acc.balance -= amount
                    self.save_data()
                    print("\nAmount Withdrawn Successfully\n")
                else:
                    print("\nInsufficient Balance\n")
                return

        print("\nAccount Not Found\n")

    def balance(self):
        acc_no = int(input("Enter Your Account Number: "))

        for acc in self.data:
            if acc.acc_no == acc_no:
                print(f"\nBalance for account name {acc.name}: ₹{acc.balance}\n")
                return

        print("\nAccount Not Found\n")

    def display_acc_list(self):
        print("\nACC NO   NAME     TYPE   BALANCE")
        for acc in self.data:
            print(f"{acc.acc_no}     {acc.name}      {acc.acc_type}      {acc.balance}")
        print()

    def close_acc(self):
        acc_no = int(input("Enter Your Account Number: "))

        for acc in self.data:
            if acc.acc_no == acc_no:
                self.data.remove(acc)
                self.save_data()
                print("\nAccount Closed Successfully\n")
                return

        print("\nAccount Not Found\n")


obj = bank()
while True:
    print("                       --------------")
    print("                       BANKING SYSTEM")
    print("                       --------------")

    print("\nMAIN MENU\n")
    print("1. NEW ACCOUNT")
    print("2. DEPOSIT")
    print("3. WITHDRAW")
    print("4. BALANCE")
    print("5. DISPLAY ACCOUNT LIST")
    print("6. CLOSE ACCOUNT")
    print("7. EXIT\n")

    choice = input("Enter your choice: ")

    match choice:
        case '1':
            obj.new_acc()
        case '2':
            obj.deposit()
        case '3':
            obj.withdraw()
        case '4':
            obj.balance()
        case '5':
            obj.display_acc_list()
        case '6':
            obj.close_acc()
        case '7':
            break
        case _:
            print("Invalid Choice\nSelect between (1–7)")
