from voucher import Voucher

index = 1
while index <= 10:
    voucher = Voucher(7500, "Greg", "RF", index)
    index += 1
    print(voucher.code)
    print(voucher.date_created)