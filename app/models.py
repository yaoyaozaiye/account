from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.
from django.db import models

class Statement(models.Model):
    CHOICES = [
        (0, '收入'),
        (1, '支出')
    ]

    # 声明一个字段，并将其设为枚举类型
    id = models.IntegerField(primary_key=True, auto_created=True)
    usage = models.CharField(max_length=100)
    type = models.IntegerField(choices=CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    ctime = models.DateTimeField(auto_now_add=True)
    mtime = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"ID: {self.id}"

    def type_str(self):
        for value, description in self.CHOICES:
            if value == self.type:
                return description

        return '未知选择'