from django.shortcuts import render
from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'
    sort_param = request.GET.get('sort')
    all_phones = Phone.objects.all()
    if sort_param == 'name':
        all_phones = all_phones.order_by('name')
    elif sort_param == 'min_price':
        all_phones = all_phones.order_by('price')
    elif sort_param == 'max_price':
        all_phones = all_phones.order_by('-price')
    context = {'phones': all_phones}
    return render(request, template, context)

def show_product(request, slug):
    template = 'product.html'
    product = Phone.objects.get(slug=slug)
    context = {'product': product}
    return render(request, template, context)

