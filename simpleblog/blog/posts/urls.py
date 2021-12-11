from django.urls import path
from .views import Blog,PostDetails,AddPost,UpdatePostView
 

urlpatterns = [
   #for helloworld we used this : path('',views.blog,name='blog'),
   path('',Blog.as_view(),name="Blog"),
   path('post/<int:pk>',PostDetails.as_view(),name="PostDetails"),
   path('add_post/',AddPost.as_view(),name="AddPost"),
   # path('create_post/',create_post)
   path('post/edit/<int:pk>',UpdatePostView.as_view(),name="UpdatePostView")
]
