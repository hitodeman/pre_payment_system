from .models import T_PAYMENT
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

    payment_info_list = T_PAYMENT.objects.select_related('customer_id','payment_kind_id'
        ).filter(
            payment_date__range=[begin_date,late_date]
        )
    #取得したobjectの合計値を算出する
    payment_total = my_logic.total_payment(payment_info_list)
    print(payment_total)
    
    if request.method == "POST":
        jpay = list(payment_info_list.values())
        for i,j in zip(jpay,payment_info_list):
            i["customer_name"] = str(j.customer_id.customer_name)
            i["payment_kind_name"] = str(j.payment_kind_id.payment_kind_name)
            i["payment_date"] = str(j.payment_date)[:10]
            i["payment_money"] = f"¥{int(j.payment_money):,}"
        d = {"jpay": jpay,"payment_total":payment_total}
        return d