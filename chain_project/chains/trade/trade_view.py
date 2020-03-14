from rest_framework.generics import ListCreateAPIView, UpdateAPIView
from rest_framework.pagination import PageNumberPagination

from chains.trade.trade_serializers import TradingSellingSerializer
from chains.trade.trade import Trading, Trade


class TradePagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    page_query_param = 'page'


# 出售列表

class TradeSelView(ListCreateAPIView, UpdateAPIView):
    serializer_class = TradingSellingSerializer
    queryset = Trading.objects.filter(status=1, type=1)
    pagination_class = TradePagination

    def perform_create(self, serializer):
        return self.create(user=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(self, *args, **kwargs)


# 求购

class TradeBuyView(ListCreateAPIView):
    serializer_class = TradingSellingSerializer
    queryset = Trading.objects.filter(status=1, type=2)
    pagination_class = TradePagination

    def perform_create(self, serializer):
        return self.create(user=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
