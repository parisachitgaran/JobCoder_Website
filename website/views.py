from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import JsonResponse
from website.models import JobPost


def index_view(request):
    posts = JobPost.objects.order_by('creat_date')[1:]
    context = {'posts': posts}
    return render(request, 'website/Index.html', context)


def JobProfile_view(request,pid):
    post =JobPost.objects.get(pk=pid)
    # post = JobPost.objects.all(pk = pid)

    context = {'post': post}
    return render(request, 'website/JobProfile.html',context)


def Linkedin_Blog_view(request):
    return render(request, 'website/Linkedin_Blog.html')

def Jobvision_Blog_view(request):
    return render(request, 'website/Jobvision_Blog.html')

def all_post_view(request):
    posts = JobPost.objects.all()
    context = {'posts': posts}
    return render(request, 'website/all_post.html', context)


def save_value_view(request):


    if request.method == 'POST':
        selected_city = request.POST.get('selected_city')
        selected_job = request.POST.get('selected_job')
        posts = JobPost.objects.all()
        posts = posts.filter(city=selected_city,category=selected_job)
        context = {'posts': posts}
        print(selected_job)
        print(selected_city)
    return render(request, 'website/all_post.html', context)

    #     # انجام عملیات مورد نظر با selected_city و selected_job
    #
    #     return JsonResponse({'message': selected_city})
    # else:
    #     return JsonResponse({'message': 'متد مجاز نیست'})
