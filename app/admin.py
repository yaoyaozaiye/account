# Register your models here.
from django.contrib import admin
from .models import Statement

class StatementModelAdmin(admin.ModelAdmin):
    # 在这里定义你的模型管理选项
    pass

admin.site.register(Statement, StatementModelAdmin)


