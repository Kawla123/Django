from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import BlogPost, Author


class BlogPostListView(ListView):
    """Affiche la liste de tous les articles"""
    model = BlogPost
    template_name = 'Posts/blogView.html'
    context_object_name = 'posts'
    paginate_by = 10
    
    def get_queryset(self):
        return BlogPost.objects.filter(published=True)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_posts'] = BlogPost.objects.count()
        return context


class BlogPostDetailView(DetailView):
    """Affiche les détails d'un article"""
    model = BlogPost
    template_name = 'Posts/blogPost_detail.html'
    context_object_name = 'post'


class BlogPostCreateView(CreateView):
    """Formulaire pour créer un nouvel article"""
    model = BlogPost
    template_name = 'Posts/blogPost_form.html'
    fields = ['title', 'content', 'author', 'published']
    
    def form_valid(self, form):
        print(f"Nouvel article créé : {form.instance.title}")
        return super().form_valid(form)


class BlogPostUpdateView(UpdateView):
    """Formulaire pour modifier un article existant"""
    model = BlogPost
    template_name = 'Posts/blogPost_form.html'
    fields = ['title', 'content', 'author', 'published']


class BlogPostDeleteView(DeleteView):
    """Confirmation de suppression d'un article"""
    model = BlogPost
    template_name = 'Posts/blogPost_confirm_delete.html'
    success_url = reverse_lazy('blogpost-list')