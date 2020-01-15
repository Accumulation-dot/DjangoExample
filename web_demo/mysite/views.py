from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from django.views.generic.list import BaseListView
from django.views.generic.detail import BaseDetailView
from .serializers import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from django.core.paginator import Paginator, QuerySetPaginator, EmptyPage, PageNotAnInteger

# Create your views here.


# class CommodityListView(BaseListView):
#     model = Commodity
#     # 每页条数
#     paginate_by = 20
#
#     def get_paginate_by(self, queryset):
#         return self.request.Get.get('page_size') or self.paginate_by
#
#     def render_to_response(self, context):
#         paginator = context['paginator']
#         current_page = context['page_obj']
#         commodities = current_page.object_list
#         data = {
#             'commodity_list': [
#                 {'id': commodity.id,
#                  'title': commodity.title,
#                  } for commodity in commodities
#             ],
#             'paginator': {
#                 'total_count': paginator.count,
#                 'num_pages': paginator.num_pages,
#             }
#         }

"""
class Category1View(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        categories = Category1.objects.all()
        return Response(Category1Serializer(categories, many=True).data)


class Category2View(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        categories = Category2.objects.all()
        return Response(Category2Serializer(categories, many=True).data)


class Category3View(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        categories = Category3.objects.all()
        return Response(Category3Serializer(categories, many=True).data)


class Category4View(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        categories = Category4.objects.all()
        return Response(Category4Serializer(categories, many=True).data, content_type='application/json; charset=utf-8')

"""


class Method(object):
    get = 'GET'
    post = 'POST'
    put = 'PUT'
    delete = 'DELETE'


@api_view(['GET', 'POST'])
def category_list(request, format=None):
    if request.method == Method.get:
        page = request.GET.get('page', 1)
        page_count = request.GET.get('page_count', 20)
        categories = Category.objects.all()
        paginator = Paginator(categories, page_count, allow_empty_first_page=True)
        total_count = paginator.count
        try:
            categ = paginator.page(page)
        except PageNotAnInteger:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        # except EmptyPage:
        #     return Response
        serializer = CategorySerializer(categ, many=True)
        return Response(serializer.data)



class CategoryView(APIView):
    renderer_classes = [JSONRenderer]
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        categories = Category.objects.all()
        # return JsonResponse(request, CategorySerializer(categories, many=True).data)
        return Response(CategorySerializer(categories, many=True).data)
