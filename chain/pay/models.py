from django.db import models

from tools.base import BaseModel
from tools.choices import pay_choices
from user import models as um


class Pay(BaseModel):
    """
    支付信息
    """
    user = models.ForeignKey(um.CoinUser, on_delete=models.DO_NOTHING)
    type = models.CharField(max_length=20, choices=pay_choices)
    name = models.CharField(max_length=10)
    number = models.CharField(max_length=30)
    use = models.BooleanField(default=True, verbose_name='use_state', help_text='是否在使用')

    class Meta:
        verbose_name = verbose_name_plural = '支付信息'
        # unique_together = ('type', 'name', 'number', 'user')
