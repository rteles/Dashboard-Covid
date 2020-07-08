from django.shortcuts import render
from Dashboard.requests import covid_reports
from datetime import date, timedelta


# Create your views here.
def dashboard(request):
    report_data = covid_reports.get_covid_report('BRA', date.today() - timedelta(1))
    context = {
        'report_data': report_data['data']
    }
    return render(request, 'dashboard.html', context)
