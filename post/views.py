from django.shortcuts import render
from .models import Post

def HomePageView(request):
    object_list = Post.objects.all()
    context = {'object_list': object_list}
    return render(request, 'post/home.html', context)


