from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, PostComment
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from .models import Post
from .forms import CommentForm
import os
import pickle


# Index view
def index(request):
    return render(request, 'index.html')


# Logout view
def logoutuser(request):
    logout(request)
    return redirect('/')


# Home page view
@login_required(login_url='/loginpage')
def homepage(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'homepage.html', context)

@login_required(login_url='/loginpage')
def postcreate(request):
    return render(request, 'createpost.html')

# Post list view
class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'homepage.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    login_url = '/loginpage'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comments = PostComment.objects.select_related('post').filter(post__in=context['posts'])
        context['comments'] = comments
        # Add comment form to the context
        context['comment_form'] = CommentForm()
        return context


# Post detail view
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            post = self.get_object()
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect('post-detail', pk=post.pk)
        

# Post create view
# class PostCreateView(LoginRequiredMixin, CreateView):
#     model = Post
#     template_name = 'createpost.html'  # Template for the form
#     fields = ['title', 'content']  # Fields for the form

#     def form_valid(self, form):
#         form.instance.author = self.request.user  # Associate the post with the logged-in user
#         return super().form_valid(form)

#     def get_success_url(self):
#         return reverse_lazy('homepage')  # Redirect to homepage after post is created

from sklearn.feature_extraction.text import TfidfVectorizer

model = pickle.load(open("./home/model.pkl", "rb"))
vectorizer = pickle.load(open("./home/tfidf.pkl", "rb"))

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name= 'post_form.html'
    fields = ['title', 'content']

    def classify_post(self, comment):
        x = vectorizer.transform([comment])
        value = model.predict(x)[0]
        return value
        
    def form_valid(self, form):
        canPost = not self.classify_post(self.request.POST.get("content"))
        if not canPost:
            return HttpResponse("Spam detected")
        form.instance.author = self.request.user
        return super().form_valid(form)



# Detail page view
@login_required(login_url='/loginpage')
def detailpage(request):
    return render(request, 'post_detail.html')


def postComment(request, slug):
    if request.method=="POST":
     pass
    return redirect("homepage")