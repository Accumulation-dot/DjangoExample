from django.db import models
from ..models import *


def purchase_order_summary():
    return PurchaseOrder.objects.all()


def commodity_all():
    return Commodity.objects.all()


def commodity_by_id(commodity_id):
    return Commodity.objects.get(id=commodity_id)


def category_by_desc(category_desc):
    return Category.objects.get(title=category_desc)


def commodity_by_category_desc(category_desc):
    category = category_by_desc(category_desc)
    if category:
        return Commodity.objects.filter(category=category.id)
    else:
        return Commodity.objects.none()


def tag_by_desc(tag_desc):
    return Tags.objects.get(title=tag_desc)


def commodity_by_tag_desc(tag_desc):
    tag = tag_by_desc(tag_desc)
    if tag:
        return Commodity.objects.filter()
    else:
        return Commodity.objects.none()
