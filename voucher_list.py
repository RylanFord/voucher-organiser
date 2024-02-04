from voucher import Voucher

class VoucherList:
    def __init__(self):
        self.vouchers = [] # List of vouchers
        self.index = 1 # Number of items in list

    def add_voucher(self, amount: float, reciever: str, authoriser: str) -> str:

        # Add a voucher to vouchers list
        self.vouchers.append(Voucher(amount, reciever, authoriser, self.index))
        self.index += 1
        return self.vouchers[-1].code

    def withdraw(self, code: str, amount: float) -> bool:

        # Withdraw by searching for code. 
        for index, voucher in enumerate(self.vouchers):
            if voucher.code == code: 
                return self.vouchers[index].redeem(amount)
            