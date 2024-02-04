from voucher import Voucher

index = 1
while index <= 5:
    voucher = Voucher(75, "Greg", "RF", index)
    index += 1
    print(voucher.code)