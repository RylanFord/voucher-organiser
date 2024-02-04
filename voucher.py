from datetime import datetime, timedelta
import random

class Voucher:
    def __init__(self, amount: float, reciever: str, authoriser: str, index: int):
        self.amount = amount # Voucher amount $$
        self.index = index # Index of current voucher (voucher #)
        self.code = self.create_code() # Create a unique code
        self.date_created = datetime.now().date() # Time that the voucher was created
        self.date_expiry = self.date_created + timedelta(weeks=156) # (YY-MM-DD)
        self.reciever = reciever # Recieving person
        self.authoriser = authoriser # Authorising person

    def create_code(self) -> str:

        # Verify that enough digits exist to create voucher
        if self.index > 10**5:
            print("Error, no more codes available: Exiting program")
            exit()

        # Find the largest factor of voucher amount
        factors = []
        for i in range(1, self.amount):
            if self.amount % i == 0:
                factors.append(i)
        largest_factor = factors[-1]
        
        # Extract the last three digits of the largest factor
        last_digits = str(largest_factor % 1000).zfill(3)

        # First number is the voucher number of index followed by a zero
        prefix_num = str(self.index * 10)

        # Fill in the rest of the 9 digits with a random number
        num_digits = 6 - len(prefix_num)
        bounds = [10**(num_digits - 1), (10**num_digits) - 1]
        random_num = str(random.randint(bounds[0], bounds[1]))

        # Final code contains: Voucher number, zero, random number, highest factor (3 digits)
        code = ''.join([prefix_num, random_num, last_digits])
        return code
    
    def check_expired(self) -> bool:

        # Check if the voucher has expired
        if self.date_expiry < datetime.now().date():
            return True
        else:
            return False
        