from django.shortcuts import render
from app.models import *
# Create your views here.
def delete_all(request):
    QLAR=AccessRecord.objects.all().delete()
    d={'access_record':QLAR}

    return render(request,'delete_all.html',context=d)

def delete_specific(request):
    QLW=Webpage.objects.filter(name='gnan').delete()
    QLWO=Webpage.objects.all()
    d={'webpage':QLWO}
    return render(request,'delete_specific.html',context=d)

def all(request):
    QLWO=Webpage.objects.all()
    d={'webpage':QLWO}
    return render(request,'all.html',context=d)