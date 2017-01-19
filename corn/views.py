import random

from django.shortcuts import render
# Create your views here.
from django.views import View
from django.http import HttpResponse


def index(request):
    print (1)
    return render(request, 'base.html')



data = {'goods': []}
for i in range(1, 5):
    data['goods'].append(
        {
            'id': i,
            'title': '{0}{1}'.format('Товар №', i),
            'description': 'Товар № '+ str(i),
            'text': 'Описание товара',
            'date': '28.12.2016'
        }
    )


def main_page(request):
    return render(request, 'goods.html', data)


class goods_view(View):
    def get(self, request, id):
        data_good = {
            'good': data['goods'][int(id) - 1]
        }
        return render(request, 'good.html', data_good)