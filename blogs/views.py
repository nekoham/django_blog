from django.urls import reverse_lazy
from django.views import generic
from blogs.models import Blog, Comment
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class IndexView(generic.ListView):
    model = Blog
    template_name = "blogs/index.html"
    context_object_name = "latest_blog_list"

    def get_queryset(self):
        return Blog.objects.order_by("-created_on")[:10]
    
class DetailView(generic.DetailView):
    model = Blog
    template_name = "blogs/detail.html"

class CreateBlogView(LoginRequiredMixin, generic.CreateView):
    model = Blog
    template_name = "blogs/create.html"
    fields = ["name", "tag", "content"]
    success_url = reverse_lazy("blogs:index")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class UpdateBlogView(LoginRequiredMixin, generic.UpdateView):
    model = Blog
    template_name = "blogs/update.html"
    fields = ["tag", "content"]
    def get_success_url(self):
        return reverse_lazy("blogs:detail", kwargs={'pk': self.object.pk})

class DeleteBlogView(LoginRequiredMixin, generic.DeleteView):
    model = Blog
    template_name = "blogs/delete.html"
    success_url = reverse_lazy("blogs:index")

class CreateCommentView(LoginRequiredMixin, generic.CreateView):
    model = Comment
    template_name = "comments/create.html"
    fields = ["content"]

    def get_success_url(self):
        return reverse_lazy("blogs:detail", kwargs={'pk': self.object.blog.id})

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.blog_id = self.kwargs['blog_id']
        return super().form_valid(form)

class UpdateCommentView(LoginRequiredMixin, generic.UpdateView):
    model = Comment
    template_name = "comments/update.html"
    fields = ["content"]

    def get_success_url(self):
        return reverse_lazy("blogs:detail", kwargs={'pk': self.object.blog.id})

class DeleteCommentView(LoginRequiredMixin, generic.DeleteView):
    model = Comment
    template_name = "comments/delete.html"

    def get_success_url(self):
        return reverse_lazy("blogs:detail", kwargs={'pk': self.object.blog.id})

