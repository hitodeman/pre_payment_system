from genericpath import exists
from django.http import HttpResponse
from django.template import loader
from .models import T_PAYMENT
from .models import M_CUSTOMER
from polls import my_logic 
from django.shortcuts import render
import datetime
import calendar

def _index(request):
    latest_question_list = T_PAYMENT.objects
    output = ', '.join([q.bank_name for q in latest_question_list])
    return HttpResponse(output)

def index(request):
    try:
        late_date = request.POST['late_date']
    except:
        late_date = str(datetime.datetime.today().date()+datetime.timedelta(days=1))

    try :
        begin_date = request.POST['begin_date']
    except:
        begin_date  = str(datetime.datetime.today().year)+"-"+str(datetime.datetime.today().month)+"-01"

    payment_info_list = T_PAYMENT.objects.select_related('customer_id','payment_kind_id'
        ).filter(
            updated_at__range=[begin_date,late_date]
        )
    #取得したobjectの合計値を算出する
    payment_total = my_logic.total_payment(payment_info_list)
    template = loader.get_template('polls/index.html')

    nav_key = 0

    context = {'payment_info_list': payment_info_list,'payment_total':payment_total,'nav_key':nav_key}
    return render(request, 'polls/index.html', context)

