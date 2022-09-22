from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Post
from .form import PostForm
from cloudinary.forms import cl_init_js_callbacks


def index(request):
    # Get all posts
    #if the method is POST
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save() 
    
        # If the form is valid
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.errors.as_json())

    
    posts = Post.objects.all()[:20]
     #Show
     
    return render(request, 'posts.html',{'posts':posts}) 

def delete(request, post_id):
    #Find User
    post = Post.objects.get(id = post_id)
    post.delete()
    return HttpResponseRedirect('/')
   
def edit(request, post_id):
    posts = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=posts)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.errors.as_json())
    form = PostForm
    return render(request, 'edit.html', {'post':posts,'form':form})

def likes(request, id):
    liked = Post.objects.get(id=id)
    liked.like_count +=1
    liked.save()
    
    return HttpResponseRedirect('/')