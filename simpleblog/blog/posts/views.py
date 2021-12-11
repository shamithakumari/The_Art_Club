from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from .models import Post
# Create helloworld display on main page
# def blog(request):
    # return render(request,'blog.html',{})
# def create_post(request):
#     if request.method == 'POST':
#          name=request.POST['name']
#          title=request.POST['title']
#          content=request.POST['content']
#          posts=Post(name=name,title=title, content=content)
#          posts.save()
#          return render(request,'thankyou.html')

class Blog(ListView):
    model=Post
    template_name="blog.html"

class PostDetails(DetailView):
    model=Post
    template_name='blogpost.html'

class AddPost(CreateView):
    model=Post
    template_name='add_post.html'
    fields='__all__'
    #field=('title','content')

class UpdatePostView(UpdateView):
    model=Post
    template_name='update_post.html'
    feilds=['title','title_tag','body']
    