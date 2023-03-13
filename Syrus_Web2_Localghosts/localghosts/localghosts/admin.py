from django.contrib import admin
from .models import Truck
from .models import User
from .models import Test
from .models import Request_shipping
from .models import Calci

admin.site.register(Truck)
admin.site.register(User)
admin.site.register(Test)
admin.site.register(Request_shipping)
admin.site.register(Calci)