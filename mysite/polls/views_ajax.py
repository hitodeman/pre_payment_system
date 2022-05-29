from .models import T_PAYMENT,M_CUSTOMER,M_PAYMENT_KIND
from django.db.models import Q
from polls import my_logic 
import datetime



def index_ajax(request):
    try:
        late_date = request.POST.get('late_date')
    except:
        late_date = str(datetime.datetime.today().date()+datetime.timedelta(days=1))
    try :
        begin_date = request.POST['begin_date']
    except:
        begin_date  = str(datetime.datetime.today().year)+"-"+str(datetime.datetime.today().month)+"-01"
    try:
        selected_customer_name = request.POST.get('selected_customer_name')
    except:
        selected_customer_name = ""
    if  not selected_customer_name:
        q_customer_name = ~Q(customer_id__customer_name = "")
    else:
        q_customer_name = Q(customer_id__customer_name = selected_customer_name)
    try :
        selected_bank_name = request.POST['selected_bank_name']
    except:
        selected_bank_name  = ""
    if  not selected_bank_name:
        q_bank_name = ~Q(bank_name = "")
    else:
        q_bank_name = Q(bank_name = selected_bank_name)
    try:
        selected_kind_name = request.POST.get('selected_kind_name')
    except:
        selected_kind_name = ""
    if  not selected_kind_name:
        q_kind_name = ~Q(payment_kind_id__payment_kind_name = "")
    else:
        q_kind_name = Q(payment_kind_id__payment_kind_name = selected_kind_name)
    try:
        selected_money = request.POST.get('selected_money')
    except:
        selected_money = ""
    if  not selected_money:
        q_money = ~Q(payment_money = "")
    else:
        q_money = Q(payment_money = selected_money)
    try :
        selected_memo = request.POST['selected_memo']
    except:
        selected_memo  = ""
    if  not selected_memo:
        q_memo = ~Q(payment_memo = "")
    else:
        q_memo = Q(payment_memo = selected_memo)
#    print(f'selected_customer_name:{selected_customer_name},selected_bank_name:{selected_bank_name},selected_kind_name:{selected_kind_name},selected_money:{selected_money},selected_memo:{selected_memo}')

    payment_info_list = T_PAYMENT.objects.select_related('customer_id','payment_kind_id'
        ).filter(
            payment_date__range=[begin_date,late_date],
        ).filter(
        q_customer_name & 
        q_bank_name &
        q_kind_name &
        q_money &
        q_memo
        )

    #取得したobjectの合計値を算出する
    payment_total = my_logic.total_payment(payment_info_list)
    if request.method == "POST":
        jpay = list(payment_info_list.values())
        for i,j in zip(jpay,payment_info_list):
            i["customer_name"] = str(j.customer_id.customer_name)
            i["payment_kind_name"] = str(j.payment_kind_id.payment_kind_name)
            i["payment_date"] = str(j.payment_date)[:10]
            i["payment_money"] = f"¥{int(j.payment_money):,}"
        d = {"jpay": jpay,"payment_total":payment_total}
        return d


"""selected_customer_name:$('option:selected').text(),
                selected_bank_name:$('option:selected').text(),
                selected_kind_name:$('option:selected').text(),
                selected_money:$('option:selected').text(),
                selected_memo:$('option:selected').text(),"""
"""class M_CUSTOMER(models.Model):
    customer_name                = models.CharField(max_length=200,help_text='得意先名称')
    customer_valid_flg           = models.BooleanField(help_text='有効フラグ（Trueで有効）', default = True)
    created_at                  = models.DateTimeField(auto_now_add=True,help_text='作成日時')
    updated_at                  = models.DateTimeField(auto_now=True,help_text='更新日時')

class M_PAYMENT_KIND(models.Model):
    payment_kind_name           = models.CharField(max_length=200,help_text='支払い種別名')
    payment_kind_valid_flg      = models.BooleanField(help_text='有効フラグ（Trueで有効）', default = True)
    created_at                  = models.DateTimeField(auto_now_add=True,help_text='作成日時')
    updated_at                  = models.DateTimeField(auto_now=True,help_text='更新日時')

class T_PAYMENT(models.Model):
    customer_id                 = models.ForeignKey(M_CUSTOMER, on_delete=models.CASCADE,help_text='客ID')
    payment_kind_id             = models.ForeignKey(M_PAYMENT_KIND, on_delete=models.CASCADE,help_text='支払い種別id')
    bank_name                   = models.CharField(max_length=200,help_text='取引銀行名')
    payment_money               = models.CharField(max_length=200,help_text='支払い、振り込み金額')
    payment_date                = models.DateTimeField(help_text='支払い日時')
    payment_memo                = models.CharField(max_length=2000,help_text='memo')
    payment_valid_flg           = models.BooleanField(help_text='有効フラグ（Trueで有効）',default = True)
    created_at                  = models.DateTimeField(auto_now_add=True,help_text='作成日時')
    updated_at                  = models.DateTimeField(auto_now=True,help_text='更新日時')"""