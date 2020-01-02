import json

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView

from .serializers import *


# Create your views here.


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json; charset=utf-8'
        super(JSONResponse, self).__init__(content, **kwargs)


class OrdersView(APIView):
    """
    获取所有的订单
    """
    # renderer_classes = [JSONRenderer]
    #
    # def get(self, request, format=None):
    #     orders = EntryOrder.objects.all()


class RequestError:

    @staticmethod
    def bad_request(request):
        return render(request, '400.html')

    @staticmethod
    def permission_denied(request):
        return render(request, '403.html')

    @staticmethod
    def page_not_found(request):
        return render(request, '404.html')

    @staticmethod
    def page_error(request):
        return render(request, '500.html')


def orders_list(request):
    order_all = EntryOrder.objects.all()
    serializer = EntryOrderModelSerializer(order_all, many=True)  ## json.dumps(dict_all, cls=DecimalEncoder)
    return JSONResponse(serializer.data)


def order_details(request, id):
    # good_query_list = Goods.objects.filter(order=id)
    order = EntryOrder.objects.get(id=id)
    detail = EntryOrderDetail.objects.filter(order=order.id)
    serializer = GoodsModelSerializer(detail, many=True)
    return JSONResponse(serializer.data)
