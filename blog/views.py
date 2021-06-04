from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.contrib.auth.decorators import login_required

# Create your views here.


def blog(request):
    blogs = Blog.objects.all().order_by('-id')
    return render(request, 'blog/blog.html', {'blogs': blogs})


def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog_detail})


@login_required
def create(request):
    return render(request, 'blog/create.html')
    # form = ProductForm()

    # if request.method == 'POST':
    #     form = ProductForm(request.POST, request.FILES)

    #     if form.is_valid():
    #         form.save()

    #         return redirect('home')

    # context = {'form': form}
    # return render(request, 'products/product_form.html', context)
