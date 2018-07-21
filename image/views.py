from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Image
from .forms import ImageForm


@login_required(login_url='/account/login/')
@csrf_exempt
@require_POST
def upload_image(request):
    form = ImageForm(data=request.POST)
    if form.is_valid():
        try:
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
            return JsonResponse({'status': "1"})
        except:
            return JsonResponse({"status": "0"})
    else:
        return JsonResponse({"status": 3})


@login_required(login_url='/account/login/')
def list_images(request):
    images = Image.objects.filter(user=request.user).order_by('id')
    # 分页
    paginator = Paginator(images, 3)
    page = request.GET.get('page')
    try:
        current_page = paginator.page(page)
    except PageNotAnInteger:
        current_page = paginator.page(1)
    except EmptyPage:
        current_page = paginator.page(paginator.num_pages)
    images = current_page.object_list
    return render(request, 'image/list_images.html', {"images": images, "page": current_page})


@login_required(login_url='/account/login/')
@require_POST
@csrf_exempt
def del_image(request):
    image_id = request.POST['image_id']
    try:
        image = Image.objects.get(id=image_id)
        image.delete()
        return JsonResponse({'status': "1"})
    except:
        return JsonResponse({'status': '2'})


def falls_images(request):
    images = Image.objects.all()
    return render(request, 'image/falls_images.html', {"images": images})