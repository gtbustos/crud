import json

from django.core import serializers
from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render

from .forms import AlvoForm
from .models import Alvo


def index(request):
    alvos = Alvo.objects.all()
    data = serializers.serialize('json', alvos)
    context = {
        'alvos': data
    }
    return render(request, 'index.html', context)


def create(request):
    if request.method == 'POST':
        params = json.loads(request.body.decode('utf-8'))
        form = AlvoForm(params)
        if form.is_valid():
            form.save()
            data = form.cleaned_data
            data['id'] = form.instance.id
            return JsonResponse(data=form.cleaned_data)

    return JsonResponse({})


def delete(request):
    if request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        alvo_id = body.get('id')
        try:
            Alvo.objects.get(id=alvo_id).delete()
            return JsonResponse({'delete': True, 'id': alvo_id})
        except Alvo.DoesNotExist:
            return JsonResponse({})


def get(request, alvo_id):
    try:
        alvo = Alvo.objects.get(id=alvo_id)

        data = model_to_dict(alvo)
        return JsonResponse(data)
    except Alvo.DoesNotExist:
        return JsonResponse({})
