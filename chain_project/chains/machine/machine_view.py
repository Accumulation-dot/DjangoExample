from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from chains.machine.machine import Machine, MachineRecord
from chains.machine.machine_serializers import MachineSerializer, MachineRecordSerializer


class MachineView(ListAPIView):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class MachineRecordListView(ListCreateAPIView):
    queryset = MachineRecord.objects.all()
    serializer_class = MachineRecordSerializer

    permission_classes = (AllowAny,)

    # def get(self, request, format=None):
    #     records = MachineRecord.objects.all()
    #     serializer = MachineRecordSerializer(records, many=True)
    #     return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

# class MachineRecordCreationView(APIView):
#
#     def post(self, request, format=None):
#         serializer = MachineRecordSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
