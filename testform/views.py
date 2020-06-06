from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
from django.conf import settings
import os
import pandas as pd

from django.core.files.storage import FileSystemStorage

datetime.utcnow ()
from testform import models as m


# Create your views here.
def index(request) :
    return HttpResponse ("files uploaded succeddfully")


# Create your views here.
def form(request) :
    return render (request, 'form/formpage.html')


def formsubmit(request) :
    if request.method == 'POST' :
        uploaded_file = request.FILES['Java']
        package_name = request.POST['pkg_name']
        test_type = request.POST['tst_type']
        save_location = request.POST['sv_location']
        index_of_dot = uploaded_file.name.index ('.')
        file_name_without_extension = uploaded_file.name[:index_of_dot]

        settings.MEDIA_ROOT = save_location

        final_file_name = file_name_without_extension + test_type + '.Java'
        fs = FileSystemStorage ()
        fs.save (file_name_without_extension + test_type + '.Java', uploaded_file)
        return render (request, 'form/formpage.html')
        # reading pkg name to java file
        # src = open (save_location + final_file_name, "r")
        # fline = "newly added FIRST LINE\n"  # Prepending string
        # print (save_location + final_file_name)
        # oline = src.readlines ()
        # Here, we prepend the string we want to on first line
        # oline.insert (0, fline)
        # src.close ()
        # content = f.readlines ()
        # We again open the file in WRITE mode
        # src = open ("text.txt", "w")
        # src.writelines (oline)
        # src.close ()
        # print (test_type)
        # print (package_name)
        # print (uploaded_file.name)
        # print (uploaded_file.size)

    # return render (request, 'form/formpage.html')
    # if request.method == 'GET' :
    # return render (request, 'post/upload.html', {})
    # el
    # Upload = m.Upload.objects.create (filename=request.POST['name'],
    #                                  created_time=datetime.utcnow ())
    # No need to call post.save() at this point -- it's already saved.


def excel(request) :
    return render (request, 'form/excelgrid.html')


def excelview(request) :
    uploaded_file = request.FILES['Java']
    # out_stream = xlsx2html (uploaded_file)
    df = pd.read_excel (uploaded_file)
    return HttpResponse (df.to_html())
