from django.contrib import admin
from watercanapp.models import Orders, Contact, Usr_can_odr, com_can_odr, Delivered_his, stock

# Register your models here.

admin.site.register(Orders)
admin.site.register(Usr_can_odr)
admin.site.register(com_can_odr)
admin.site.register(Delivered_his)
admin.site.register(Contact)
admin.site.register(stock)