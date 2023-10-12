from django.shortcuts import render
from django.views import View
from .models import Worker, Store, Visit
# Create your views here.


class IndexView(View):

    def get(self, request, phone):
        worker = Worker.objects.get(phone=phone)
        stores = Store.objects.filter(workers=worker.id)
        context = {'stores': stores, 'phone' : phone}
        return render(request, 'for_test/index.html', context=context)

class VisitView(View):
    #я конечно тоже параноик, но зачем проверять привязан ли телефон к точке если запрос по нему не вывел бы точку в списке
    def get(self, request, phone, pk, latitude, longtitude):
        store = Store.objects.get(id=pk)
        worker = Worker.objects.get(phone=phone)
        visit = Visit(store=store, worker=worker, latitude=latitude, longtitude=longtitude)
        visit.save()
        return render(request, 'for_test/Store.html', context={ 'visit' : visit})
