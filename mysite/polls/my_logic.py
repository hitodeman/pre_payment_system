from .forms import T_PAYMENT_FORM

#objectの合計金額を算出
def total_payment(payment_object_list):
    total_payment = 0
    for payment_object in payment_object_list:
        if payment_object.payment_valid_flg:
                total_payment += int(payment_object.payment_money)
    return format(total_payment, ',')

def payment_form_list(payment_object_list):
    t_patnent_form_list = list()
    for payment_object in payment_object_list:
        t_patnent_form = T_PAYMENT_FORM(
            {
            'id'                :   payment_object.id, 
            'bank_name'         :   payment_object.bank_name, 
            'payment_date'      :   payment_object.payment_date,
            'payment_money'     :   payment_object.payment_money,
            'payment_memo'      :   payment_object.payment_memo,
            'customer_id'       :   payment_object.customer_id,
            'payment_kind_id'   :   payment_object.payment_kind_id,
            'payment_valid_flg' :   payment_object.payment_valid_flg,
            }
        )
        #print(payment_object.id)
        #pprint.pprint(t_patnent_form)
        t_patnent_form_list.append(t_patnent_form) 
    return t_patnent_form_list