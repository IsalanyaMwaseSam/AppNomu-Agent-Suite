from django.shortcuts import render, redirect
from main_app.forms import AirtimeForm,DataForm
from django.views import View
import africastalking
from django.conf import settings

africastalking.initialize(settings.USERNAME, settings.API_KEY)

# Create your views here.
def home(request):
    return render(request, 'main_app/agentdashboard.html', {})

def airtime_topup(request):
    if request.method == "POST":
        form = AirtimeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('airtime_topup')

    else:
        form = AirtimeForm()
    return render(request, 'main_app/airtime-topup.html', {'form': form})

def data_topup(request):
    if request.method == "POST":
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('data_topup')

    else:
        form = DataForm()
    return render(request, 'main_app/data-topup.html', {'form': form})

def airtime_history(request):
    return render(request, 'main_app/airtime_history.html', {})

class AirtimeView(View):
    def post(self, request, *args, **kwargs):
        airtime = africastalking.Airtime
        line_items = [
            {
                "errorMessage": "None",
                "numSent": 1,
                "totalAmount": "KES 1000.0000",
                "totalDiscount": "KES 40.0000",
                "responses": [{
                    "phoneNumber": "+254711XXXYYY",
                    "errorMessage": "None",
                    "amount": "KES 1000.0000",
                    "status": "Sent",
                    "requestId": "ATQid_1be914ac47845eef1a1dab5d89ec50ff",
                    "discount": "KES 40.0000"
                }]
            }
        ]
