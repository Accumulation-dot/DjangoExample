from django.shortcuts import render


# Create your views here.


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

