
#objectの合計金額を算出
def total_payment(payment_object_list):
    total_payment = 0
    for payment_object in payment_object_list:
        print(payment_object.payment_money)
        total_payment += int(payment_object.payment_money)
    return total_payment