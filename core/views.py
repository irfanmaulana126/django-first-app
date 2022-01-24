from django.shortcuts import render

def index(req):
    return render(req,'page/index_landing.html')

def page_not_found_view(request, exception):
    return render(request,'error_404.html', status=404)

def bad_request(request, exception):
    return render(request,'error_404.html', status=400)

def server_error(request, exception):
    return render(request,'error_404.html', status=500)
