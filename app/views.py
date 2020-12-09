from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import ContainmentZones, EssentialsRequest, CovidData


def index(request):
    data = CovidData.objects.last()
    data.totalConfirmed = "{:,}".format(data.totalConfirmed)
    data.activeCases = "{:,}".format(data.activeCases)
    data.recoveredCases = "{:,}".format(data.recoveredCases)
    data.totalDeaths = "{:,}".format(data.totalDeaths)
    print(data)
    return render(request, "index.html", {"data": data})


def containment_zones(request):
    containmentZones = ContainmentZones.objects.all()
    return render(request, 'ui-tables.html', {
        'title': 'Containment Zones',
        'table_heads': ['Sl No.', 'District', 'Area', 'Ward'],
        'dataList': containmentZones
    })


@login_required(login_url="/login/")
def essential_items_list(request):
    itemRequests = EssentialsRequest.objects.all()
    return render(request, 'ui-tables.html', {
        'title': 'Essentials Request',
        'table_heads': [
            'Request ID',
            'Name',
            'Contact Number',
            'Items Required'
        ],
        'dataList': itemRequests
    })


def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        print(1)

        load_template = request.path.split('/')[-1]
        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:
        print(404)
        html_template = loader.get_template('error-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        print(500)
        html_template = loader.get_template('error-500.html')
        return HttpResponse(html_template.render(context, request))
