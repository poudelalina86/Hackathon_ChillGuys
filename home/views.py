from django.http import JsonResponse
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
from django.shortcuts import render
 
 
from .models import Chat

from django.utils import timezone

import requests


import google.generativeai as genai
from django.contrib.auth.decorators import login_required



genai.configure(api_key="AIzaSyCZRp4A6x0yv5722qUOgRbT7e2o3p9ja3I")

# Define a prompt for assisting with sadness
input_prompt = """
You are a compassionate and supportive assistant.Keep it short, sweet, and always Acknowledge the user's feelings with empathy, understanding, and kindness. Provide comforting words to help them through sadness or difficult emotions. Occasionally, crack light-hearted jokes or share fun, uplifting messages to lift their spirits, ensuring that the humor remains gentle and never dismissive. Encourage the user to share their feelings and provide positive encouragement. Always remind them that it’s okay to seek professional help if needed. Make sure to always balance empathy with moments of lightheartedness to brighten their day.
"""


# Function to interact with the Gemini model
def ask_gemini(message):
    # Initialize the model (replace with the correct model if needed)
    model = genai.GenerativeModel("gemini-1.5-flash")
    
    # Create the message to send to Gemini (including the prompt and the user's message)
    full_message = input_prompt + "\n" + "User: " + message
    
    # Generate response based on the input message
    response = model.generate_content(full_message)
    
    return response.text

# Create your views here.
@login_required(login_url='/loginpage')
def chatbot(request):
    # Clear the previous chats for the user to start fresh
    Chat.objects.filter(user=request.user).delete()

    # No previous chats, so the list is empty
    chats = []

    if request.method == 'POST':
        # Get the message sent by the user
        message = request.POST.get('message')
        
        # Get response from Gemini model
        response = ask_gemini(message)

        # Save the chat to the database
        chat = Chat(user=request.user, message=message, response=response, created_at=timezone.now())
        chat.save()
        
        # Return the response as JSON
        return JsonResponse({'message': message, 'response': response})
    
    # Render the chatbot page with no previous chats
    return render(request, 'chatbot.html', {'chats': chats})

# Home page view
@login_required(login_url='/loginpage')
def homepage(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'homepage.html', context)



# Index view
def index(request):
    return render(request, 'index.html')


# Logout view
def logoutuser(request):
    return redirect('/')


# Home page view
# @login_required(login_url='/loginpage')
# def homepage(request):
#     context = {'posts': Post.objects.all()}
#     return render(request, 'homepage.html', context)

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


 
 

# from sklearn.feature_extraction.text import TfidfVectorizer

# model = pickle.load(open("./home/model.pkl", "rb"))
# vectorizer = pickle.load(open("./home/tfidf.pkl", "rb"))

# class PostDetailView(DetailView):
#     model = Post
#     template_name = 'post_detail.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['comment_form'] = CommentForm()
#         return context

#     def classify_comment(self, comment):
#         # Use the loaded vectorizer and model to classify the comment
#         x = vectorizer.transform([comment])
#         value = model.predict(x)[0]
#         return value

#     def post(self, request, *args, **kwargs):
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment_content = form.cleaned_data['comments']
#             # Check if the comment is classified as spam
#             is_spam = self.classify_comment(comment_content)

#             if is_spam:
#                 return HttpResponse("Spam detected in comment")

#             post = self.get_object()
#             comment = form.save(commit=False)
#             comment.user = request.user
#             comment.post = post
#             comment.save()
#             return redirect('post-detail', pk=post.pk)

 

# class PostCreateView(LoginRequiredMixin, CreateView):
#     model = Post
#     template_name = 'post_form.html'
#     fields = ['title', 'content']

#     def classify_text(self, text):
#         """Classify a given text (title or content) as spam or not."""
#         x = vectorizer.transform([text])
#         value = model.predict(x)[0]
#         return value

#     def form_valid(self, form):
#         # Extract title and content from the form
#         title = self.request.POST.get("title")
#         content = self.request.POST.get("content")

#         # Check if either the title or content is classified as spam
#         is_title_spam = self.classify_text(title)
#         is_content_spam = self.classify_text(content)

#         # if is_title_spam:
#         #     return HttpResponse("Spam detected in the title")
#         # elif is_content_spam:
#         #     return HttpResponse("Spam detected in the content")

#         if is_title_spam or is_content_spam:
#             # Prepare a positive message for spam detection
#             context = {
#                 'message': "Oops! It looks like some of your input was flagged as spam. Don't worry, you can try submitting again with different words. Let's create something amazing!"
#             }
#             return render(self.request, 'spam_detected.html', context)
#         # If no spam detected, associate the author and proceed
#         form.instance.author = self.request.user
#         return super().form_valid(form)
import sys
import tensorflow.keras.preprocessing.text
sys.modules['keras.src.legacy'] = tensorflow.keras

 
from tensorflow.keras.models import load_model
import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load the Keras model
model = load_model('./home/model.h5')  # Ensure the model is saved in HDF5 format

# Load the tokenizer
with open('./home/tokenizer.pkl', 'rb') as handle:
    tokenizer = pickle.load(handle)

# Load the max_length value
with open('./home/max_length.txt', 'r') as file:
    max_length = int(file.read())

# Helper function to classify text
def classify_text(text):
    """Classify a given text using the loaded model."""
    sequence = tokenizer.texts_to_sequences([text])
    padded_sequence = pad_sequences(sequence, maxlen=max_length, padding='post')
    prediction = model.predict(padded_sequence)
    predicted_class = prediction.argmax(axis=-1)[0]  # Get the predicted class (0 or 1)
    return predicted_class


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
            comment_content = form.cleaned_data['comments']
            # Classify the comment
            is_spam = classify_text(comment_content)

            if is_spam == 1:
                return HttpResponse("Spam detected in comment")

            post = self.get_object()
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect('post-detail', pk=post.pk)

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'createpost.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        # Extract title and content from the form
        title = self.request.POST.get("title")
        content = self.request.POST.get("content")

        # Classify the title and content
        is_title_spam = classify_text(title)
        is_content_spam = classify_text(content)

        if is_title_spam == 1 or is_content_spam == 1:
            # Display a positive spam detection message
            context = {
                'message': "Oops! It looks like some of your input was flagged as spam. Don't worry, you can try submitting again with different words. Let's create something amazing!"
            }
            return render(self.request, 'spam_detected.html', context)

        # If no spam detected, associate the author and proceed
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