from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to the blog!")

def post_detail(request, id):
    return HttpResponse(f"Post {id}")
