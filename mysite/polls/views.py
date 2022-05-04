from django.http import HttpResponse
from django.template import loader
from .models import T_PAYMENT
from .models import M_CUSTOMER
from polls import my_logic 

def _index(request):
    latest_question_list = T_PAYMENT.objects
    output = ', '.join([q.bank_name for q in latest_question_list])
    return HttpResponse(output)

def index(request):
    payment_info_list = T_PAYMENT.objects.select_related('customer_id','payment_kind_id')
    #取得したobjectの合計値を算出する
    payment_total = my_logic.total_payment(payment_info_list)

    template = loader.get_template('polls/index.html')
    context = {'payment_info_list': payment_info_list,'payment_total':payment_total}
    return HttpResponse(template.render(context, request))