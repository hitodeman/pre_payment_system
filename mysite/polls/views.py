from django.http import HttpResponse,JsonResponse
from .models import T_PAYMENT
from polls import my_logic 
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
import datetime
import calendar

from .forms import T_PAYMENT_FORM,CustomerChoiceForm,TPChoiceForm,KindChoiceForm
from polls.views_ajax import index_ajax

def _index(request):
    latest_question_list = T_PAYMENT.objects
    output = ', '.join([q.bank_name for q in latest_question_list])
    return HttpResponse(output)

#searchAndDisplayからのPOSTを受け取り、json形式で返す
def index_api_ca(request):
    d = index_ajax(request)
    return JsonResponse(d,safe=False)

def index(request):
    end_day = calendar.monthrange(datetime.datetime.today().year,datetime.datetime.today().month)[1]
    late_date  = str(datetime.datetime.today().date().replace(day=end_day))
    begin_date = str(datetime.datetime.today().date().replace(day=1))
    payment_obj_list = T_PAYMENT.objects.select_related(
            'customer_id','payment_kind_id'
        ).filter(
            payment_date__range = [begin_date,late_date]
        )

    #取得したobjectの合計値を算出する
    payment_total = my_logic.total_payment(payment_obj_list)
    payment_form_list  = my_logic.payment_form_list(payment_obj_list)

    nav_key = 0
    payment_info_list = list()
    get_flag = 1

    # 新規登録用フォーム
    payment_create_form = T_PAYMENT_FORM()
    customer_choice_form = CustomerChoiceForm()
    tp_choice_form = TPChoiceForm()
    kind_choice_form = KindChoiceForm()


    for payment_obj,payment_form in zip(payment_obj_list,payment_form_list):
        payment_info_list.append([payment_obj,payment_form])
    
    context = {
        'payment_create_form' : payment_create_form ,
        'customer_choice_form' : customer_choice_form ,
        'tp_choice_form': tp_choice_form,
        'kind_choice_form' : kind_choice_form ,
        'payment_info_list': payment_info_list,
        'payment_total':payment_total,
        'nav_key':nav_key,
        'get_flag':get_flag,
        'first_late_date':late_date,
        'first_begin_date':begin_date,
        }
    return render(request, 'polls/index.html', context)

# ** 
# Payment 追加処理
#   
#
# **
def addPayment(request):
    #リクエストがPOSTの場合
    if request.method == 'POST':
        #リクエストをもとにフォームをインスタンス化
        userForm = T_PAYMENT_FORM(request.POST)
        if userForm.is_valid():
            userForm.save()

    #user.htmlへデータを渡す
    return redirect(to = '/polls')

# ** 
# Payment 変更処理
#    
#
# **
def savePayment(request,T_PAYMENT_id):
    if request.method == 'POST':
        #リクエストをもとにフォームをインスタンス化
        userForm = T_PAYMENT_FORM(request.POST)
        if userForm.is_valid():
            payment_obj = get_object_or_404(T_PAYMENT, pk=T_PAYMENT_id)
            payment_obj.bank_name           = userForm['bank_name'].data
            payment_obj.payment_date        = userForm['payment_date'].data
            payment_obj.payment_money       = userForm['payment_money'].data
            payment_obj.payment_valid_flg   = userForm['payment_valid_flg'].data
            payment_obj.payment_memo        = userForm['payment_memo'].data

            #オブジェクトで格納しないといけない？からこの方法では変更できない
            #payment_obj.customer_id.customer_name         = userForm['customer_id']['customer_name'].data
            #payment_obj.payment_kind_id     = userForm['payment_kind_id'].data

            payment_obj.save()
    return redirect(to = '/polls')

