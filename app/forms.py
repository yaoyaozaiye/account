# @Time: 2023/6/24 22:11
# @Author: 田莉
# @File: forms.py
# @Software: PyCharm

from django import forms
from .models import Statement

class StatementForm(forms.ModelForm):
    class Meta:
        model = Statement
        fields = ['id', 'usage', 'type', 'amount']  # 如果只想显示特定字段，请使用列表替代 '__all__'

