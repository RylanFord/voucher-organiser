from voucher import Voucher
from voucher_list import VoucherList

myList = VoucherList()

firstCode = myList.add_voucher(75, 'Greg', 'RF')

firstCode = myList.vouchers[0].code
print(firstCode)

if myList.withdraw(firstCode, 76):
    print("success!")
else:
    print("Could not withdraw")

voucher = myList.vouchers[0]

print(voucher.amount)
print(voucher.current)
print(voucher.redeemed)
print(voucher.redeemed_date)