from .forms import Anfrage
from django.core.mail import send_mail
from servicePr.models_new import Firma
import datetime
from servicePrMail.models import TempEMail
from django.shortcuts import render
import pytz
from django.http import HttpResponse

class SendMassMail:

    def __init__(self):
        self.data = []

    def sendmailtofirms(self, request):

        form = Anfrage(request.POST)
        f = list()

        if form.is_valid():
            #
            # email = request.POST.get("eMail")
            #
            # user = User.objects.create_user(email, email=email)
            # user.is_confirmed = False
            #
            # send_email(email, 'Use %s to confirm your email' % user.confirmation_key)
            # # User gets email, passes the confirmation_key back to your server
            #
            # user.confirm_email(user.confirmation_key)
            # user.is_confirmed = True

            now = datetime.datetime.now()
            tz = datetime.timedelta(minutes=10)

            utc = pytz.UTC
            temps = TempEMail.objects.all()

            for temp in temps:
                print(temp.tempMail, temp.updated)

                time = temp.updated.replace(tzinfo=utc)
                now = now.replace(tzinfo=utc)

                if time < (now - tz):
                    TempEMail.objects.filter(updated=temp.updated).delete()

            cmail = request.POST.get("eMail")
            t = TempEMail.objects.filter(tempMail=cmail)

            if t:
                print("TRUE: t")
                return 0

            TempEMail.objects.create(tempMail=cmail)

            mail_list = request.POST.get("mailList")
            mailList = mail_list.split(", ")

            text1 = str(mailList[0])
            f += Firma.objects.filter(eMail=text1[1:])

            subject = request.POST.get("name")
            message = request.POST.get("beschreibung")
            send_from = 'test@mail.com'

            m = 0
            while m < len(mailList):
                send_mail(subject, message, send_from, [mailList[m]])
                print(m)
                f += Firma.objects.filter(eMail=mailList[m])

                m += 1

            form.save(commit=True)

        return f