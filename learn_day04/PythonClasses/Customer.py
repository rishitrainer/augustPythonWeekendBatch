class Customer:

    def __init__(self, custName, retailStr, custId=999):
        self.customer_Id = custId
        self.customer_name = custName
        self.retail_store = retailStr
        self.percent = 0.0
        print("Customer instance is created", self.customer_Id, self.customer_name, self.retail_store)

    def discount(self, percent=0):
        self.percent= percent
        print("Discount is ", percent," % for ", self.customer_name)


class PreferredCustomer(Customer):

    def __init__(self, custName, retailStr, email, mobile, custId=999):
        self.cell_number = mobile
        self.email_address = email
        Customer.__init__(self, custName, retailStr, custId)
        print("PreferredCustomer ", self.cell_number, self.email_address)


    def promotions(self):
        print("promotional coupons sent to ", self.cell_number, self.email_address)


    def discount(self, percent=2.5):
        self.percent= percent
        print("Discount for Preferred Customer is ", percent," % for ", self.customer_name)


class CreditCardCustomer(PreferredCustomer):

    def __init__(self, custName, retailStr, email, mobile, pan_card, custId=999):
        super().__init__( custName, retailStr, email, mobile, custId)
        self.PAN_CARD = pan_card
        print("Credit Card Customer Created")


    def discount(self, percent=5):
        self.percent= percent
        print("Discount for Credit Card Customer is ", percent," % for ", self.customer_name)

    def creditOffers(self):
        print("EMI Options are sent to ", self.email_address)


ccCust = CreditCardCustomer(custName="Neil",retailStr="Northen Plaza", pan_card="ABACE4556J", email="neil@nasa.com", mobile="+1 770 380 9744")
ccCust.discount()
ccCust.promotions()
ccCust.creditOffers()


'''
cust01 = Customer(custName="Neil",retailStr="Northen Plaza")
print(cust01.customer_Id, cust01.customer_name, cust01.retail_store)
cust01.discount(2.5)

pCust = PreferredCustomer(custName="Neil",retailStr="Northen Plaza", email="neil@nasa.com", mobile="+1 770 380 9744")
pCust.promotions()
pCust.discount()
'''