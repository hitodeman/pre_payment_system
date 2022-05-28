from cProfile import label
from django import forms
from django.forms import ModelChoiceField
from .models import M_CUSTOMER, T_PAYMENT,M_PAYMENT_KIND

class CustomModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj): # label_from_instance 関数をオーバーライド
        return obj.brand_nm # 表示したいカラム名を return

class T_PAYMENT_FORM(forms.ModelForm):
    class Meta:
        model = T_PAYMENT
        fields = ('bank_name','payment_date', 'payment_money','payment_memo','customer_id','payment_kind_id', 'payment_valid_flg' )
        labels={
            'bank_name'         :'銀行名',
            'payment_date'      :'支払い日',
            'payment_money'     :'支払い金額',
            'payment_memo'      :'メモ',
            'customer_id'       :'客先ID',
            'payment_kind_id'   :'支払い種別ID',
            'payment_valid_flg' :'有効',
            }
        f_bank_name = forms.FloatField(label="体重", initial="45", widget=forms.NumberInput(attrs={'class':'body-weight'}))
        f_payment_date = forms
        f_payment_money = forms
        f_payment_memo = forms
        f_customer_id = forms
        f_payment_kind_id = forms
        f_valid_flg = forms

# カスタムフィールドクラスの作成
class MyModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return "%i" % obj.id + " %s" % obj.name

# forms.py

class CustomerChoiceForm(forms.ModelForm):
    customer_name = forms.ModelChoiceField(M_CUSTOMER.objects.distinct().values_list("customer_name", flat=True),empty_label="取引先選択")

    class Meta:
        model = M_CUSTOMER
        fields = ('customer_name',)

class TPChoiceForm(forms.ModelForm):
    bank_name = forms.ModelChoiceField(T_PAYMENT.objects.distinct().values_list("bank_name", flat=True),empty_label="銀行選択")
    money_choice = forms.ModelChoiceField(T_PAYMENT.objects.distinct().values_list("payment_money", flat=True),empty_label="金額選択")
    memo_choice = forms.ModelChoiceField(T_PAYMENT.objects.distinct().values_list("payment_memo", flat=True),empty_label="メモ選択")

    class Meta:
        model = T_PAYMENT
        fields = (
            'bank_name',
            'payment_money',
            'payment_memo',
            )

class KindChoiceForm(forms.ModelForm):
    kind_name = forms.ModelChoiceField(M_PAYMENT_KIND.objects.distinct().values_list("payment_kind_name", flat=True),empty_label="種別選択")

    class Meta:
        model = M_PAYMENT_KIND
        fields = ('payment_kind_name',)


"""
class MoneyChoiceForm(forms.ModelForm):
    money_choice = forms.ModelChoiceField(T_PAYMENT.objects.distinct().values_list("payment_money", flat=True),empty_label="金額選択")

    class Meta:
        model = T_PAYMENT
        fields = ('payment_money',)

class MemoChoiceForm(forms.ModelForm):
    memo_choice = forms.ModelChoiceField(T_PAYMENT.objects.distinct().values_list("payment_memo", flat=True),empty_label="メモ選択")

    class Meta:
        model = T_PAYMENT
        fields = ('payment_memo',)
"""