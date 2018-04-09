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
from HT import GOOGLE_KEY

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
    global geocode
    print(geocode)

    n = name
    q = request.POST.get("query")

    firma = Firmeneintrag_new()
    f = firma.getFirm(n, firm_list)
    f_mix = list(f)
    random.shuffle(f_mix)

    lat, lng, firm_id = geocode[n]
    form = Anfrage()

    # Anfrageformular
    if request.POST.get("name"):

        sendTo = SendMassMail()
        mail_list = sendTo.sendmailtofirms(request)

        if mail_list == 0:
            return render(request, 'responses/res_email_not.html')

        context = {
            'mail_list': mail_list,
            'form': request.POST,
        }

        return render(request, 'responses/offerResponseSite.html', context)

    # Suche nach Postleitzahl
    if q and q.isnumeric() and len(q) == 4:
        search = Search()
        lat, lng, firm_id = geocode[n]
        print(firm_id)
        firm_search, dist = search.filter_plz(f, q)

        #GET DISTANCE WITH MATH
        # dist_math = geo.get_distance(q, geocode[n], firm_search)
        # dist_math.sort()
        # print("DIST_MATH : ", dist_math)

        # PAGINATOR
        # firm_search = pagi(request, firm_search, 30)

        context = {
            's_id': request.session.session_key,
            'title': n,
            'firma_new': firm_search[:30],
            'query': q,
            'form': form,
            'lat': lat,
            'lng': lng,
            'distance': dist,
            'anz': len(firm_search),
            'anz_f': firm_list.count(),
            'anz_a': a.count()*3,
            'id': firm_id,
            'GOOGLE_KEY': GOOGLE_KEY
        }

        return render(request, 'branchen/show.html', context)
    elif q and len(q) < 4:
        messages.warning(request, 'Schweizer Postleitzahl eintragen. Beispiel: "8000" für Zürich')
    elif q and q.isnumeric() == False:
        messages.warning(request, 'Schweizer Postleitzahl eintragen. Beispiel: "8000" für Zürich')

    # PAGINATOR
    # f_mix = pagi(request, f_mix, 30)

    context = {
        's_id': request.session.session_key,
        'title': n,
        'firma_new': f_mix[:30],
        'form': form,
        'lat': lat,
        'lng': lng,
        'anz': f.count(),
        'anz_f': firm_list.count(),
        'anz_a': a.count()*3,
        'id': firm_id,
        'GOOGLE_KEY': GOOGLE_KEY
    }

    return render(request, 'branchen/show.html', context)

def pagi(request, f, anz):

    page = request.GET.get('page', 1)
    paginator = Paginator(f, anz)

    try:
        f = paginator.page(page)
    except PageNotAnInteger:
        f = paginator.page(1)
    except EmptyPage:
        f = paginator.page(paginator.num_pages)

    return f

# ****FIRMFORM
def firmaForm(request):
    form = EintragFormular()
    if request.POST:
        print("Request Firmeneintrag")
        form = EintragFormular(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return render(request, 'nav/form_bestaetigung.html', {})

    context = {
        'form': form,
    }

    return render(request, 'nav/firmaForm.html', context)

############################### INFOSITES ######################################

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
