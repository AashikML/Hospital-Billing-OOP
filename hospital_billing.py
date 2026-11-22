class HospitalBill:
    def __init__(self, patient_name, doctor_name, consultation_fee):
        self.patient_name = patient_name
        self.doctor_name = doctor_name
        self.consultation_fee = consultation_fee
        self._charges = []      # Encapsulated list for tests/medicines
        self._is_paid = False   # Tracks whether bill is already settled

    @staticmethod
    def is_valid_amount(amount):
        return isinstance(amount, (int, float)) and amount > 0

    def add_charge(self, item_name, cost):
        if self._is_paid:
            print("Cannot add charges: Bill is already paid.")
            return
        if not self.is_valid_amount(cost):
            print(f"Invalid amount for '{item_name}': {cost}")
            return
        self._charges.append({"item": item_name.strip(), "cost": cost})
        print(f"Added '{item_name.strip()}' ({cost})")

    def calculate_total(self):
        charges_sum = sum(entry["cost"] for entry in self._charges)
        return self.consultation_fee + charges_sum

    def pay_bill(self, amount):
        if self._is_paid:
            print("Bill is already paid.")
            return
        if not self.is_valid_amount(amount):
            print(f"Invalid payment amount: {amount}")
            return

        total = self.calculate_total()
        if amount < total:
            remaining = total - amount
            print(f"Insufficient payment. Need {remaining} more to settle total ({total}).")
            return

        self._is_paid = True
        change = amount - total
        print(f"Payment successful! Total: {total}, Paid: {amount}, Change: {change}")

    def print_receipt(self):
        print("\n" + "=" * 40)
        print("         HOSPITAL BILL RECEIPT")
        print("=" * 40)
        print(f"Patient      : {self.patient_name}")
        print(f"Doctor       : {self.doctor_name}")
        print(f"Consult Fee  : {self.consultation_fee}")
        print("-" * 40)
        if not self._charges:
            print("Additional Charges: None")
        else:
            print("Additional Charges:")
            for entry in self._charges:
                print(f"  - {entry['item']}: {entry['cost']}")
        print("-" * 40)
        print(f"Total Amount : {self.calculate_total()}")
        print(f"Status       : {'PAID' if self._is_paid else 'UNPAID'}")
        print("=" * 40 + "\n")


if __name__ == "__main__":
    bill = HospitalBill("Aashik Pandit", "Dr. swati shrama", 500)
    bill.add_charge("Blood Test", 800)
    bill.add_charge("Paracetamol", 150)
    bill.add_charge("Invalid Item", -50)   # Should be rejected
    bill.print_receipt()
    bill.pay_bill(1000)                  # Should show insufficient payment
    bill.pay_bill(1500)                  # Should pay & show change 50
    bill.add_charge("X-Ray", 1200)       # Should be blocked because paid
    bill.print_receipt()