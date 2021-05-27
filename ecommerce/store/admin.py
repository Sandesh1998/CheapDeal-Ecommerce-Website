from django.contrib import admin

from .models import *

admin.site.site_header = "E-commerce-Site"
admin.site.site_title = " CheapDeal"
admin.site.index_title = "Welcome Admin!"


admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)