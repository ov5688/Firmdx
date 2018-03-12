from django.shortcuts import render
from servicePrMail.forms import EintragFormular, Anfrage
from servicePrMail.form_req import SendMassMail
from servicePrMail.models import OffertenAnfrage
from .firm import Firmeneintrag_new
from search.search_plz import Search
from googleMapsAPI.geocoords import geo
from .models_new import Firma
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import random
from django.contrib import messages

firm_list = Firma.objects.all()
a = OffertenAnfrage.objects.all()
geocode = geo.getAllGeocoords(firm_list)

#TODO eMail confirmation
#TODO Anfrage formatiert senden

def index(request):

    fl = list(firm_list)
    random.shuffle(fl)
    q = request.POST.get("query")

    if q and q.isnumeric() and len(q) == 4:
        if request.POST.get("select") != 'X':
            return show(request, request.POST.get('select'))
        else:
            messages.warning(request, 'Postleitzahl eintragen und Branche wählen')
    elif q and q.isnumeric() == False:
        messages.warning(request, 'Postleitzahl eintragen und Branche wählen')

    if request.POST.get("name"):
        sendTo = SendMassMail()
        mail_list = sendTo.sendmailtofirms(request)

        if mail_list == 0:
            return render(request, 'responses/res_email_not.html')

        context = {
            'mail_list': mail_list,
            'form': request.POST
        }

        return render(request, 'responses/offerResponseSite.html', context)

    context = {
        'firma_new': fl[:12],
        'anz_f': firm_list.count(),
        'anz_a': a.count()*3
    }

    return render(request, 'home.html', context)

def show(request, name):

    global firm_list
    n = name
    q = request.POST.get("query")
    page = request.GET.get('page', 1)

    firma = Firmeneintrag_new()
    f = firma.getFirm(n, firm_list)
    f_mix = list(f)
    # random.shuffle(f_mix)

    lat, lng = geocode[n]
    form = Anfrage()

    # Anfrageformular
    if request.POST.get("name"):

        sendTo = SendMassMail()
        mail_list = sendTo.sendmailtofirms(request)

        if mail_list == 0:
            return render(request, 'responses/res_email_not.html')

        context = {
            'mail_list': mail_list,
            'form': request.POST
        }

        return render(request, 'responses/offerResponseSite.html', context)

    # Suche nach Postleitzahl
    if q and q.isnumeric() and len(q) == 4:
        search = Search()
        lat, lng = geocode[n]
        firm_search = search.filter_plz(f, q)

        paginator = Paginator(firm_search, 30)

        try:
            firm_search = paginator.page(page)
        except PageNotAnInteger:
            firm_search = paginator.page(1)
        except EmptyPage:
            firm_search = paginator.page(paginator.num_pages)

        context = {
            's_id': request.session.session_key,
            'title': n,
            'firma_new': firm_search,
            'query': q,
            'form': form,
            'lat': lat,
            'lng': lng,
            'anz': search.filter_plz(f, q).count(),
            'anz_f': firm_list.count(),
            'anz_a': a.count()*3
        }

        return render(request, 'branchen/show.html', context)
    elif q and len(q) < 4:
        messages.warning(request, 'Schweizer Postleitzahl eintragen. Beispiel: "8000" für Zürich')
    elif q and q.isnumeric() == False:
        messages.warning(request, 'Schweizer Postleitzahl eintragen. Beispiel: "8000" für Zürich')

    paginator = Paginator(f_mix, 30)

    try:
        f_mix = paginator.page(page)
    except PageNotAnInteger:
        f_mix = paginator.page(1)
    except EmptyPage:
        f_mix = paginator.page(paginator.num_pages)

    context = {
        's_id': request.session.session_key,
        'title': n,
        'firma_new': f_mix,
        'form': form,
        'lat': lat,
        'lng': lng,
        'anz': f.count(),
        'anz_f': firm_list.count(),
        'anz_a': a.count()*3
    }

    return render(request, 'branchen/show.html', context)


def impressum(request):

    context = {
        'title': 'Impressum',
    }

    return render(request, 'nav/impressum.html', context)


def aboutUs(request):
    context = {
        'title': 'About us',
    }

    return render(request, 'nav/aboutUs.html', context)


def agb(request):
    context = {
        'title': 'AGB',
    }

    return render(request, 'nav/agb.html', context)

def kontakt(request):
    context = {
        'title': 'Kontakt',
    }

    return render(request, 'nav/kontakt.html', context)


# ****FORM****
def firmaForm(request):
    form = EintragFormular()
    if request.POST.get("name"):
        form = EintragFormular(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return render(request, 'nav/form_bestaetigung.html', {})

    context = {
        'form': form,
    }

    return render(request, 'nav/firmaForm.html', context)
