from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import PictureForm, SearchForm, TagForm
from .filter import *
from django.db.models import Count
# Create your views here.


@login_required(login_url='login')
def gallery(request):
    pictures = MedlPicture.objects.all()
    return render(request, 'Gallery.html', {'pictures': pictures})


@login_required(login_url='login')
def image(request, pi):
    picture = MedlPicture.objects.get(id=pi)
    context = {'image': picture}
    print(picture.id)
    print(picture.tags.all())
    return render(request, 'image.html', context)


@login_required(login_url='login')
def cabinet(request):
    form = PictureForm
    tagform = TagForm
    if request.method == "POST":
        picture = request.POST.get('picture')
        print(picture)
        tag = request.POST.get('tag')
        print(tag)
        print(MedlTag.objects.all())
        if 'picture' in request.POST:
            form = PictureForm(request.POST)
            if form.is_valid():
                picinf = form.save()
                picinf.author = str(request.user)
                picinf.save()
        if 'tag' in request.POST:
            tagform = TagForm(request.POST)
            if tagform.is_valid():
                taginf = tagform.save()
                if MedlTag.objects.filter(tagname=taginf.tagname).count() == 0:
                    taginf.author = str(request.user)
                    taginf.save()
        else:
            print(MedlTag.objects.all())
    else:
        print(MedlTag.objects.all())
    context = {'form': form, 'tagform': tagform}
    return render(request, 'cabinet.html', context)


@login_required(login_url='login')
def search(request):
    form = SearchForm
    result = set(MedlPicture.objects.all())
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            author = form.cleaned_data.get("author")
            tags = form.cleaned_data.get("tags")
            print(name)
            if name and tags and author:
                result = set(MedlPicture.objects.filter(tags__in=tags, name=name, author=author).annotate(num_tags=Count('tags')).filter(num_tags=len(tags)))
            elif name and tags and not author:
                result = set(MedlPicture.objects.filter(tags__in=tags, name=name).annotate(num_tags=Count('tags')).filter(num_tags=len(tags)))
            elif name and not tags and not author:
                result = set(MedlPicture.objects.filter(name=name))
            elif not name and tags and author:
                result = set(MedlPicture.objects.filter(tags__in=tags, author=author).annotate(num_tags=Count('tags')).filter(num_tags=len(tags)))
            elif not name and tags and not author:
                result = set(MedlPicture.objects.filter(tags__in=tags).annotate(num_tags=Count('tags')).filter(num_tags=len(tags)))
            elif not name and not tags and author:
                result = set(MedlPicture.objects.filter(author=author))
    print(len(result))
    context = {'form': form, 'result': result, 'result_len': len(result)}
    return render(request, 'search.html', context)