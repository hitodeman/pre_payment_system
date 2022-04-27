from django.contrib import admin

# Register your models here.



from .models import M_CUSTOMER
from .models import M_PAYMENT_KIND
from .models import T_PAYMENT


admin.site.register(M_CUSTOMER)
admin.site.register(M_PAYMENT_KIND)
admin.site.register(T_PAYMENT)
