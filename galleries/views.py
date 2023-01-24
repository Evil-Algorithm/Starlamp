from common.sglib import Starlamp
from django.shortcuts import render
from .models import Contact, About
from django.core.paginator import Paginator


# The index only displays the galleries themselves. Subgalleries are displayed within galleries.


def index(req):
    sl = Starlamp()
    thumbnails = sl.list_thumbnails()
    page_number = req.GET.get("page")
    paginator = Paginator(thumbnails, 21)
    page_obj = paginator.get_page(page_number)

    return render(req, "galleries/home.html", {"thumbnail": page_obj})


def directory(req, data):
    sl = Starlamp()

    direc = data
    albums = sl.folder_path(data, include_gallery=True)
    img_list = sl.list_files(direc)
    paginator = Paginator(img_list, 21)
    page_number = req.GET.get("page")
    page_obj = paginator.get_page(page_number)
    filename = sl.list_files(direc, include_gallery=False)

    context = {"album": albums, "images": page_obj, "fn": filename}

    return render(req, "galleries/galleries.html", context)


def contact(req):

    context = {"contact_obj": Contact.objects.all()}
    return render(req, "galleries/contact.html", context)


def about(req):

    context = {"about_fields": About.objects.all()}

    return render(req, "galleries/about.html", context)
