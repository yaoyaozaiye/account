from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Statement
from .forms import StatementForm

from rest_framework import viewsets
from .serializers import MyModelSerializer
from .utils import *

class MyModelView(viewsets.ModelViewSet):
    queryset = Statement.objects.all()
    serializer_class = MyModelSerializer

def index(request):
    list = Statement.objects.all()
    return render(request, 'index.html', {'list': list})





def create(request, id):
    if request.method == 'POST':
        form = StatementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # 重定向到 Model 列表页
    else:
        print(f">>>: {request.GET}")
        if  noneOrEmpty(id) == False:
            print(f"xxx: {id}")
            obj = get_object_or_404(Statement, pk=id )
            form = StatementForm(instance=obj)
        else:
            form = StatementForm()

    return render(request, 'create.html', {'form': form})


def delete(request, id):
    # 根据主键获取要删除的对象，如果不存在则返回 404 错误
    obj = get_object_or_404(Statement, pk=id)
    obj.delete()
    return redirect('index')  # 删除后重定向到指定页面