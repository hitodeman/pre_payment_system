from genericpath import exists
import imp
from django.core import serializers
from django.http import HttpResponse,JsonResponse
from django.template import loader
from .models import T_PAYMENT
from .models import M_CUSTOMER
from polls import my_logic 
from django.shortcuts import render
import datetime
import calendar
import json

def _index(request):
    latest_question_list = T_PAYMENT.objects
    output = ', '.join([q.bank_name for q in latest_question_list])
    return HttpResponse(output)

def index(request):
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
            updated_at__range=[begin_date,late_date]
        )

    #取得したobjectの合計値を算出する
    payment_total = my_logic.total_payment(payment_info_list)
    template = loader.get_template('polls/index.html')

    nav_key = 0

    context = {'payment_info_list': payment_info_list,'payment_total':payment_total,'nav_key':nav_key}
    
    #動的form生成
    if request.method == "POST":
        payment_form = ''
        payment_totalDisp = ''
        if payment_info_list:
            for payment_info in payment_info_list:
                payment_info.customer_name = payment_info.customer_id.customer_name
                payment_info.payment_kind_name = payment_info.payment_kind_id.payment_kind_name
            for payment_info in payment_info_list:
                payment_form += '<tr>'
#                payment_form += '<button type="button" data-toggle="modal" data-target="#exampleModal">'
#                payment_form += '<td><div class="form-check"><input class="form-check-input" type="checkbox" value="" id="flexCheckDefault"><label class="form-check-label" for="flexCheckDefault"></label></div></td>'
                payment_form += '<td>'+str(payment_info.id)+'</td>'
                payment_form += '<td>'+str(payment_info.updated_at)+'</td>'
                payment_form += '<td>'+payment_info.customer_id.customer_name+'</td>'
                payment_form += '<td>'+payment_info.bank_name+'</td>'
                payment_form += '<td>'+payment_info.payment_kind_id.payment_kind_name+'</td>'
                payment_form += '<td>'+payment_info.payment_money+'</td>'
                payment_form += '<td>((φ(・ω・´*)ﾒﾓﾒﾓ</td></tr>'
                payment_form += '</button>'
        payment_totalDisp += '<p class="total-money text-right">合計金額　　　'+str(payment_total)+'円</p>'
        d = {'payment_form': payment_form,'payment_totalDisp':payment_totalDisp}
        return JsonResponse(d)
    
    return render(request, 'polls/index.html', context)

