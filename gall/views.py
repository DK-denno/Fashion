from django.shortcuts import render
from .models import Posts,Category
# Create your views here.
def index(request):
    posts = Posts.objects.all()
    categories = Category.objects.all()
    return render(request,'index.html',{"categories":categories,'images':posts,})

def full_pic(request,pic_id):
    posts = Posts.objects.filter(id=pic_id)
    return render(request,'one.html',{'posts':posts})

def category(request,category_id):
    posts = Posts.objects.filter(category=category_id)
    return render(request,'location.html',{'posts':posts})

# def categories(request):
#     categories = Category.objects.all()
#     return render(request,'navbar.html',{"categories":categories})

def search_results(request):
    
    if 'image' in request.GET or request.GET['image']:
        search_item = request.GET.get('image')
        searched_images = Posts.search_by_category(search_item)
        print(searched_images)
        message = f"{search_item}"
        return render(request, 'search.html',{"message":message,"posts": searched_images})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})