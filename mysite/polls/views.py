from django.http import HttpResponse
from django.template import loader
from .models import T_PAYMENT
from .models import M_CUSTOMER

def _index(request):
    latest_question_list = T_PAYMENT.objects
    output = ', '.join([q.bank_name for q in latest_question_list])
    return HttpResponse(output)

def index(request):
    payment_info_list = T_PAYMENT.objects.select_related('customer_id','payment_kind_id')

    template = loader.get_template('polls/index.html')
    context = {'payment_info_list': payment_info_list,}
    return HttpResponse(template.render(context, request))