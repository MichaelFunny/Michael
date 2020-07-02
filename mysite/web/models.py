from django.db import models
from django.utils.deconstruct import deconstructible

"""
from django.contrib.auth.models import (AbstractBaseUser)

# Create your models here.
class CustomUser(AbstractBaseUser):
    email = models.EmailField(max_length=255 , unique=True)
    full_name = models.CharField(max_length=255 , blank=True, null=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return

    @property
    def is_admin(self):
        return self.admin
"""
@deconstructible
class ProductCategory(models.Model):
    category = models.CharField(max_length=64, verbose_name="Категория")


    def __str__(self):
        return "%s" % self.category

@deconstructible
class ProductBrand(models.Model):
    brand = models.CharField(max_length=64, verbose_name="Брэнд")


    def __str__(self):
        return "%s" % self.brand

@deconstructible
class Product(models.Model):

    # Huawei = 'huawei'
    # Samsung = 'samsung'
    # Apple = 'aplle'
    # Nokia = 'nokia'
    # Electrolux = 'electrolux'
    #
    # BRAND_CHOICES = (
    #     (Huawei,'Huawei'),
    #     (Samsung, 'Samsung'),
    #     (Apple,'Apple'),
    #     (Nokia, 'Nokia'),
    #     (Electrolux,'Electolux'),
    # )
    #
    # CATEGORY_CHOICES = (
    #     ('телефон','Телефон'),
    #     ('наушники','Наушники'),
    #     ('холодильник','Холодильник'),
    #
    # )


    name = models.CharField(max_length=50 , verbose_name='Наименование товара')
    brand = models.ForeignKey(ProductBrand, blank=True, on_delete=models.PROTECT, verbose_name='Брэнд')
    category = models.ForeignKey(ProductCategory, blank=True, on_delete=models.PROTECT, verbose_name='Категория')
    quanity = models.CharField(max_length=50 , verbose_name='Количество товара на складе')
    cost = models.CharField(max_length=50 , verbose_name='Цена за единицу товара')


    def __str__(self):
        return " Наименование товара - %s" % (self.name )


class zapros(models.Model):
    def zapros(request):
        return render(request, 'mainApp/zapros.html')

# @deconstructible
# class Seller(models.Model): #продавцы
#
#     name_s = models.CharField(max_length=50 , verbose_name='Имя продавца')
#     phone = models.CharField(max_length=50 ,blank=True, null=True, verbose_name='Номер телефона')
#
#     def __str__(self):
#         return " Имя - %s" % ( self.name_s)
#


@deconstructible
class Order(models.Model): #заказы
    # total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)#total price for all products in order
    # customer_name = models.CharField(max_length=64, blank=True, null=True, default=None)
    # customer_email = models.EmailField(blank=True, null=True, default=None)
    # customer_phone = models.CharField(max_length=48, blank=True, null=True, default=None)
    # customer_address = models.CharField(max_length=128, blank=True, null=True, default=None)
    # created = models.DateTimeField(auto_now_add=True, auto_now=False)
    # updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    #product_id = models.IntegerField(blank=True, null=True, verbose_name='product_id') #идентификатор заказанного товара (внешний ключ к products.id)
    product = models.ForeignKey(Product, blank=True, on_delete=models.PROTECT,  verbose_name='productid')
    #product_id = Sellers(sellerid)
    #seller = models.ForeignKey(Seller,blank=True,  on_delete=models.PROTECT, verbose_name='sellerid') #идентификатор продавца оформившего продажу
    date = models.DateField(auto_now_add=False,auto_now=False , verbose_name='Дата оформления')
    cnt = models.CharField(max_length=50 , verbose_name='Количество приобретаемого товара')
    #total_price = models.DecimalField(default=True)

    def __str__(self):
        return " Продукт - %s" % (self.product)

    def save(self, *args, **kwargs):

        super(Order, self).save(*args, **kwargs)

@deconstructible
class ProductImage(models.Model):
    product = models.ForeignKey(Product, blank=True, on_delete=models.PROTECT, name="Product")
    image = models.ImageField(upload_to='products_images/')
    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.Product.name



@deconstructible
class ProductInBasket(models.Model):
    session_key = models.CharField(max_length=128, blank=True, null=True, default=None)
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    nmb = models.IntegerField(default=1)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)#price*nmb
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.product.name


    def save(self, *args, **kwargs):
        price_per_item = self.product.cost
        self.price_per_item = price_per_item
        self.total_price = int(self.nmb) * price_per_item

        super(ProductInBasket, self).save(*args, **kwargs)
