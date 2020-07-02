from django.contrib import admin
from .models import Product
#from .models import Seller
from .models import Order
from .models import ProductImage
from .models import ProductCategory
from .models import ProductBrand
from .models import ProductInBasket

# from . import zapros
admin.site.register(ProductInBasket)
admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(ProductBrand)
admin.site.register(ProductImage)
#admin.site.register(Seller)
admin.site.register(Order)
#admin.site.register(zapros)
# Register your models here.
