from django.shortcuts import render, redirect
from django.views import generic
from .models import Post

from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

from django.contrib.auth import authenticate, login
from .forms import UserCreateForm


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/index.html'  # a list of all posts will be displayed on index.html


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'  # detail about each blog post will be on post_detail.html


def contact_form(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = f'Message from {form.cleaned_data["name"]}'
            message = form.cleaned_data["message"]
            sender = form.cleaned_data["email"]
            recipients = ['thekodechamp@gmail.com']
            try:
                send_mail(subject, message, sender, recipients, fail_silently=True)
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return HttpResponse('Success...Your email has been sent')
    return render(request, 'blog/contact.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            login(request, new_user)
            return redirect('home')
    else:
        form = UserCreateForm()
    return render(request, 'registration/signup.html', {'form': form})
