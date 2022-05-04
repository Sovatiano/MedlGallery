from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import PictureForm, SearchForm, TagForm, ChangeTags
from .filter import *
from django.db.models import Count


# Create your views here.


@login_required(login_url='login')
def gallery(request):
    pictures = MedlPicture.objects.all().order_by('-date_created')
    return render(request, 'Gallery.html', {'pictures': pictures})


@login_required(login_url='login')
def image(request, pi):
    chnagetag = ChangeTags
    picture = MedlPicture.objects.get(id=pi)
    if request.method == "POST":
        form = ChangeTags(request.POST)
        if form.is_valid() and 'tags' in request.POST:
            if "submit" in request.POST:
                picture.tags.set(request.POST.getlist('tags'))
                picture.save()
            elif "add" in request.POST:
                for tag in request.POST.getlist('tags'):
                    picture.tags.add(tag)
            elif "remove" in request.POST:
                for tag in request.POST.getlist('tags'):
                    picture.tags.remove(tag)
    context = {'image': picture, 'changetag': chnagetag}
    return render(request, 'image.html', context)


@login_required(login_url='login')
def cabinet(request):
    form = PictureForm
    tagform = TagForm
    if request.method == "POST":
        picture = request.POST.get('picture')
        tag = request.POST.get('tag')
        if 'picture' in request.POST:
            form = PictureForm(request.POST)
            tags = request.POST.get('tags')
            if form.is_valid():
                picinf = form.save()
                picinf.author = str(request.user)
                picinf.save()
        if 'tag' in request.POST:
            tagform = TagForm(request.POST)
            if tagform.is_valid():
                taginf = tagform.save(commit=False)
                if MedlTag.objects.filter(tagname=taginf.tagname).count() == 0:
                    taginf.author = str(request.user)
                    taginf.save()
    context = {'form': form, 'tagform': tagform}
    return render(request, 'cabinet.html', context)


@login_required(login_url='login')
def search(request, filter=''):
    form = SearchForm
    result = MedlPicture.objects.all()
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            if "submit" in request.POST:
                name = form.cleaned_data.get("name")
                author = form.cleaned_data.get("author")
                tags = form.cleaned_data.get("tags")
                tags = list(tags)
                if name and tags and author:
                    result = MedlPicture.objects.filter(tags__in=tags, name=name, author=author).annotate(
                        num_tags=Count('tags')).filter(num_tags=len(tags))
                elif name and tags and not author:
                    result = MedlPicture.objects.filter(tags__in=tags, name=name).annotate(num_tags=Count('tags')).filter(
                            num_tags=len(tags))
                elif name and not tags and not author:
                    result = MedlPicture.objects.filter(name=name)
                elif not name and tags and author:
                    result = MedlPicture.objects.filter(tags__in=tags, author=author).annotate(num_tags=Count('tags')).filter(
                            num_tags=len(tags))
                elif not name and tags and not author:
                    result = MedlPicture.objects.filter(tags__in=tags).annotate(num_tags=Count('tags')).filter(
                        num_tags=len(tags))
                elif not name and not tags and author:
                    result = MedlPicture.objects.filter(author=author)
    else:
        if filter != '':
            tag = MedlTag.objects.filter(tagname=filter)
            print(tag)
            result = MedlPicture.objects.filter(tags__in=tag).annotate(num_tags=Count('tags')).filter(
                num_tags=len(tag))
            if len(result) == 0:
                result = MedlPicture.objects.filter(author=filter)
    # result = set(result) - set(MedlPicture.objects.filter(tags=6))
    # finalresultids = []
    # for elem in result:
    #     finalresultids.append(elem.id)
    # finalresult = MedlPicture.objects.filter(id__in=finalresultids)
    # print(finalresult)
    finalresult = result.order_by('-date_created')
    context = {'form': form, 'result': finalresult, 'result_len': len(finalresult)}
    return render(request, 'search.html', context)
