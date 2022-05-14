from django.db import models

#### master_tables ####################################################################################

class M_CUSTOMER(models.Model):
    customer_name                = models.CharField(max_length=200,help_text='客名')
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
    payment_valid_flg           = models.BooleanField(help_text='有効フラグ（Trueで有効）',default = True)
    #payment_date                = models.DateTimeField(auto_now_add=True,help_text='支払い日時')
    created_at                  = models.DateTimeField(auto_now_add=True,help_text='作成日時')
    updated_at                  = models.DateTimeField(auto_now=True,help_text='更新日時')

#########################################################################################################

