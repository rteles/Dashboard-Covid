import requests


def get_covid_report(iso, date):
    base_url = "https://covid-api.com/api/reports"

    if iso and date is not None:
        request_url = f"{base_url}?iso={iso}&date={date}"
    else:
        if iso is not None:
            request_url = f"{base_url}?iso={iso}"
        else:
            request_url = f"{base_url}?date={date}"

    request_result = requests.get(url=request_url)
    return request_result.json()
