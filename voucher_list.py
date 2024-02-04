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

    def claim(self, code: str, amount: float) -> bool:

        # Withdraw by searching for code. 
        for index, voucher in enumerate(self.vouchers):
            if voucher.code == code: 
                return self.vouchers[index].redeem(amount)
            
    def search(self, category: str, searchInput, list):

        # List of vouchers in input list that correspond to search parameters
        results_list = []

        # For each element in voucher list, see if there is a match for search input
        for index, voucher in enumerate(list):   
            category_dict = {'Amount': str(voucher.amount), 
                                    'Current': str(voucher.current), 
                                    'Code': voucher.code, 
                                    'Date created': str(voucher.date_created), 
                                    'Reciever': voucher.reciever, 
                                    'Authoriser': voucher.authoriser}

            # Target data member for a given search category.
            target_var = str(category_dict[category])
            if str(searchInput) in target_var:
                results_list.append(voucher)

        return results_list
