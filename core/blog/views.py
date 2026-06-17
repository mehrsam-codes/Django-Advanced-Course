from django.shortcuts import render , redirect
from django.views.generic import TemplateView , RedirectView , ListView , DetailView
from .models import Post
from django.shortcuts import get_object_or_404
# Create your views here.
'''
Funcation Based View Show a Template
'''
def indexView(request):
    '''
    Docstring for indexView
    a function based view to show index page
    '''
    name = 'mehrsam'
    context = {'name':name}
    return render(request , "index.html" , context)
class IndexView(TemplateView):
    '''
    Docstring for IndexView
    a class based view to show index page
    '''
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = "mehrsam"
        context['posts'] = Post.objects.all()
        return context
'''FBV for Redirect
from django.views.generic import TemplateView , RedirectView
def RedirectToMaktab(request):
    return redirect('https://maktabkhooneh.org/')
'''
class RedirectToMaktab(RedirectView):
    url = "https://maktabkhooneh.org/"
    def get_redirect_url(self, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['pk'])
        print(post)
        return super().get_redirect_url(*args, **kwargs)
class PostListView(ListView):
    model = Post
    '''
    or use : queryset = Post.objects.all()
    filter : def get_queryset(self):
                posts = Post.objects.filter(status=False)
                return posts
    '''
    context_object_name = "post"
    paginate_by = 2
    ordering = '-id' # DESC 
class PostDetailView(DetailView):
    model = Post