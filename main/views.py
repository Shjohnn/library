from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.db.models import Q

from .models import *
from .forms import *


def home_view(request):
    return HttpResponse(
        "<h1>Bosh sahifa!</h1>"
    )


def info_view(request):
    import datetime
    now = datetime.datetime.now()
    context = {
        "now": now
    }
    return render(request, 'info.html', context)


def kutubxonachilar_view(request):
    search=request.GET.get('search',None)
    kutubxonachilar=Kutubxonachi.objects.all()
    if search is not None:
        kutubxonachilar=kutubxonachilar.filter(ism__icontains=search)

    context={
        "kutubxonachilar" : kutubxonachilar,
    }
    if request.method=="POST":
        Kutubxonachi.objects.create(
            ism=request.POST.get('ism'),
            ish_vaqti=request.POST.get('ish_vaqti')
        )
        return redirect('kutubxonachilar')
    return render(request,'kutubxonachilar.html', context)


def talabalar_view(request):
    if request.method == "POST":
        form=TalabaForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
        Talaba.objects.create(
            ism=data['ism'],
            guruh=data['guruh'],
            kurs=data['kurs'],
            kitob_soni=data['kitob_soni']

        )
        return redirect('talabalar')
    search = request.GET.get('search', None)
    talabalar = Talaba.objects.all()
    if search is not None:
        talabalar = talabalar.filter(ism__contains=search)
        recordlar = Record.objects.filter(

        )
    form =TalabaForm()
    context = {
        'talabalar': talabalar,
        'form':form
    }
    return render(request, 'talabalar.html', context)


def talaba_view(request, student_id):
    talaba = Talaba.objects.get(id=student_id)
    context = {
        "talaba": talaba
    }
    return render(request, 'talaba-details.html', context)


def mualliflar_view(request):
    if request.method=="POST":
        Muallif.objects.create(
            ism=request.POST['ism'],
            jins=request.POST['jins'],
            tugilgan_sana=request.POST['tugilgan_sana'],
            kitob_soni=request.POST['kitob_soni'],
            tirik=request.POST['tirik']


        )
        return redirect('mualliflar')

    search = request.GET.get('search', None)
    mualliflar = Muallif.objects.all()
    if search is not None:
        mualliflar = mualliflar.filter(ism__icontains=search)

    context = {
        "mualliflar": mualliflar
    }
    return render(request, "mualliflar.html", context)


def muallif_view(request, muallif_id):

    muallif = Muallif.objects.get(id=muallif_id)
    context = {
        'muallif': muallif
    }
    return render(request, 'muallif.html', context)


def muallif_del_view(request, muallif_id):
    muallif = get_object_or_404(Muallif, id=muallif_id)
    muallif.delete()
    return redirect('mualliflar')


def kitoblar_view(request):
    if request.method=="POST":
        form=KitobForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('kitoblar')
    search = request.GET.get('search', None)
    kitoblar = Kitob.objects.all()
    if search is not None:
        kitoblar = kitoblar.filter(nom__contains=search)
    mualliflar=Muallif.objects.all()

    context = {
        'kitoblar': kitoblar,
        'mualliflar':mualliflar,
        'form':KitobForm

    }
    return render(request, 'kitoblar.html', context)


def kitob_view(request, kitob_id):
    kitob = Kitob.objects.get(id=kitob_id)
    context = {
        "kitob": kitob
    }
    return render(request, "kitob.html", context)


def records_view(request):

    records = Record.objects.all()
    mualliflar=Muallif.objects.all()
    talabalar=Talaba.objects.all()
    kitoblar=Kitob.objects.all()


    if request.method == "POST":
        kitob_id = request.POST['kitob_id']
        talaba_id = request.POST['talaba_id']
        Record.objects.create(
            talaba=request.POST.get('talaba'),
            kitob=request.POST.get('kitob'),
        )
        return redirect('records')

    search=request.GET.get('search', None)

    if search is not None:
        records=Record.objects.filter(
            Q(talaba__ism__icontains=search) |
            Q(kitob__nom__icontains=search)

        )
    # if .method=="POST":
    #     Record.objects.create(
    #         talaba=request.POST.get('talaba'),
    #         kitob=request.POST.get('kitob'),
    #     )
    #     return redirect('records')
    #

    context = {
        'records': records,
        'mualliflar': mualliflar,
        'talabalar':talabalar,
        'kitoblar':kitoblar,
        'kitob_id':kitob_id,

        'talaba_id':talaba_id,

    }
    return render(request, 'records.html', context)
def record_del_view(request,record_id):
    record=get_object_or_404(Record,id=record_id)
    record.delete()
    return redirect('recordlar')

def talaba_del_view(request, student_id):
    talaba = get_object_or_404(Talaba, id=student_id)
    talaba.delete()
    return redirect('talabalar')

#
# def recordlar_view(request):
#     search = request.GET.get('search', None)


def kitob_del_view(request, kitob_id):
    kitob = get_object_or_404(Kitob, id=kitob_id)
    kitob.delete()
    return redirect('kitoblar')



def talaba_update_view(request,student_id):
    talaba=get_object_or_404(Talaba, id=student_id)
    if request.method == "POST":
        talaba.ism=request.POST['ism']
        talaba.guruh=request.POST['guruh']
        talaba.kurs=request.POST['kurs']
        talaba.kitob_soni=request.POST['kitob_soni']
        talaba.save()
        return redirect('talabalar')
    context={
        'talaba':talaba
    }
    return render(request, 'talaba_update.html', context)


def kitoblar_update_view(request, kitob_id):
    kitob=get_object_or_404(Kitob, id=kitob_id)
    if request.method=="POST":
        muallif=get_object_or_404(Muallif, id=request.POST['muallif_id'])
        kitob.nom=request.POST['nom']
        kitob.janr=request.POST['janr']
        kitob.sahifa=request.POST['sahifa']
        kitob.muallif=muallif
        kitob.save()
        return redirect('kitoblar')



    context={
        'kitob':kitob,
        'mualliflar':Muallif.objects.all()


    }
    return render(request,'kitob_update.html', context)