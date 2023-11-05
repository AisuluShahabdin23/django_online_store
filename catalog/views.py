from django.shortcuts import render
from catalog.models import Product, Category


def home(request):
    category_list = Category.objects.all()
    context = {
        'object_list': category_list,
        'title': 'Главная'
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    context = {
        'title': 'Контакты',
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Name: {name}\n Phone: {phone}\n Message: {message}')
    return render(request, 'catalog/contacts.html', context)


def product(request, product_id):
    product_list = Product.objects.get(pk=product_id)
    context = {
        'product': product_list,
    }
    return render(request, 'catalog/product.html', context)


