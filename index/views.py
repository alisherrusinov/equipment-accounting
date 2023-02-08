from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.db.utils import IntegrityError
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json
from .models import ItemModel


def index(request):
    return render(request, 'index/index.html')


@csrf_exempt
@api_view(['GET', 'POST'])
def register(request):
    body = json.loads(request.body)
    if body['password'] == body['confirm']:
        try:
            user = User.objects.create_user(username=body['username'], email=body['email'],
                                            password=make_password(body['password']))
            return Response("Success", status=202)
        except IntegrityError:
            return Response("User already exists", status=401)
    else:
        return Response("Passwords don't match", status=401)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def rights(request):
    is_editable = request.user.groups.filter(name='Редактирование').exists()
    print(is_editable)
    return JsonResponse({'edit_group': is_editable})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_items(request):
    data = ItemModel.objects.all().values()
    answer = {}
    for element in data:
        answer[element['id']] = element
    print(answer)
    return JsonResponse({'elements': answer})


@require_http_methods(['POST'])
@csrf_exempt
def sort(request):
    sort_by = request.POST['attribute']
    sort_to = request.POST['sort']
    if (sort_to == 'DESC'):
        data = ItemModel.objects.all().order_by(sort_by).values()
    else:
        data = ItemModel.objects.all().order_by(f'-{sort_by}').values()

    return JsonResponse({'elements': list(data)})


@require_http_methods(['POST'])
@csrf_exempt
def save(request):
    element_id = request.POST['element_id']
    attr_name = request.POST['attribute']
    attr_value = request.POST['value']

    element = ItemModel.objects.get(id=element_id)
    setattr(element, attr_name,
            attr_value)  # приходит один атрибут и его нужно установить динамически, через model.attr не получится
    element.save()

    return JsonResponse({'status': 'ok'})
