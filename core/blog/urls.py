from django.urls import path
from . import views
from django.views.generic import TemplateView , RedirectView
from .views import indexView
app_name = "blog"
urlpatterns = [ 
    path('post/' , views.PostListView.as_view() , name = "post-list") ,
    path('post/<int:pk>/' , views.PostDetailView.as_view() , name="post-detail")

]
