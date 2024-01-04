from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostAddForm, PostEditForm, MyLoginForm


# Create your views here.
def posts_list(request):
    searchTerm=request.GET.get('searchpost')
    if searchTerm:
        posts_list=Post.objects.filter(post_title__icontains=searchTerm)
    else:
        posts_list = Post.objects.all()
    return render(request,template_name='posts.html',context={'searchTerm':searchTerm,'posts_list':posts_list})


def post_details_view(request,passed_id):
    post_details=get_object_or_404(Post,id=passed_id)
    print(post_details)
    return render(request,template_name='postdetails.html',context={'post_details':post_details})

def add_post(request):
    add_post_form=PostAddForm(request.POST,request.FILES)
    if request.method=='POST':
        if add_post_form.is_valid():
           new_post=add_post_form.save(commit=False)
           if request.user.is_authenticated:
               new_post.post_author = request.user
           else:

               new_post.post_author = None
           new_post.save()
           return redirect('home_path')
        # else:
        #    add_post_form=PostAddForm()
    return render(request,template_name='account/add_post.html',context={'add_post_form':add_post_form})

def edit_post(request,passed_id):
    post_details=get_object_or_404(Post,id=passed_id)
    edit_post_form=PostEditForm(request.POST or None,request.FILES or None,instance=post_details)
    if edit_post_form.is_valid():
        edit_post_form.save()
        return redirect('home_path')
    return render(request,template_name='account/edit_post.html',context={'edit_post_form':edit_post_form})


# def delete_post(request,passed_id):
#     post_details=get_object_or_404(Post,id=passed_id)
#     post_details.delete()
#     return redirect("home_path")
#     return render(request,template_name='account/delete_post.html',context={'post_details':post_details})


def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        # Confirm the delete action
        post.delete()
        messages.success(request, f'The post "{post.post_title}" has been deleted.')
        return redirect('home_path')  # Redirect to the posts list page or another appropriate URL

    return render(request, 'account/delete_post.html', {'post': post})


def user_login_view(request):
    if request.method == 'POST':
        login_form = MyLoginForm(request.POST)

        if login_form.is_valid():
            cleaned_data = login_form.cleaned_data
            auth_user = authenticate(request, username=cleaned_data['username'], password=cleaned_data['password'])

            if auth_user is not None:
                login(request, auth_user)
                return redirect('home_path')
            else:
                return HttpResponse('<h1>Not Authenticated</h1>')
    else:
        login_form = MyLoginForm()  # Initialize the form for GET requests

    return render(request, 'useraccount/login_form.html', {'login_form': login_form})
