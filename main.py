from voucher import Voucher
from voucher_list import VoucherList

myList = VoucherList()

firstCode = myList.add_voucher(75, 'Greg', 'RF')
secondCode = myList.add_voucher(100, 'Harry', 'RF')
thirdCode = myList.add_voucher(75, 'Josh', 'BG')

refined_vouchers = myList.search('Authoriser', 'RF', myList.vouchers)
for i in refined_vouchers:
    print(i.code)

print("\n")

highly_refined_vouchers = myList.search('Amount', 75, refined_vouchers)
for i in highly_refined_vouchers:
    print(i.code)