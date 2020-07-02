from django.shortcuts import render
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_protect
from .models import Product
#from .models import Seller
from .models import Order

# Create your views here.

# def zapros(request):
#     return render(request, 'mainApp/zapros.html')
#
# def zapr1(request):
#     zapr1 = Product.objects.all()
#     zapr_s = Seller.objects.all()
#     zapr_o = Order.objects.all()
#
#     context = {
#         'zapr1' : zapr1,
#         'zapr_o' : zapr_o,
#         'zapr_s' : zapr_s,
#
#
#     }
#     return render(request, 'mainApp/zapr1.html', context)
#

def file_input(request):

    name = request.POST['name']
    brand = request.POST['brand']
    category = request.POST['category']
    quanity = request.POST['quanity']
    cost= request.POST['cost']
    some_file.write("id" + id +"\n" )
    some_file.write("Наименование продукта:" + name +"\n" )
    some_file.write("Брэнд:" + brand +"\n")
    some_file.write("Категория:" + category +"\n")
    some_file.write("Количество:" + quanity +"\n")
    some_file.write("Цена:" + cost +"\n")
    return HttpResponse("Данные успешно были записаны")

# def sellers_input(request):
#
#     name_s = request.POST['name_s']
#     phone = request.POST['phone']
#     some_file.write("id" + id +"\n" )
#     some_file.write("Имя продавца:" + name_s +"\n" )
#     some_file.write("Телефон:" + phone +"\n" )
#
#     return HttpResponse("Данные успешно были записаны")


def order_input(request):
    product = request.POST['product']

    id = request.POST['id']
    date = request.POST['date']
    cnt = request.POST['cnt']
    some_file.write("productid:" + product +"\n" )

    some_file.write("orderid:" + id +"\n" )
    some_file.write("Дата оформления заказа:" + date +"\n" )
    some_file.write("Количество приобретаемого заказа:" + cnt +"\n" )


    return HttpResponse("Данные успешно были записаны")
