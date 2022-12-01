from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def drink_list(request):

    if request.method == 'GET':
        drinks = Drink.objects.all()
        serializer = DrinkSerializer(drinks, many=True)
        # Return list
        # return JsonResponse(serializer.data, safe=False)
        # Return objet
        return JsonResponse({"drinks": serializer.data})

    if request.method == 'POST':
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def video_list(request):
    if request.method == 'POST':

        print (request.data)
        return Response("ok", status=status.HTTP_201_CREATED)

        # serializer = DrinkSerializer(data=request.data)
        # if serializer.is_valid():

        #     print(request)
        #     return Response("ok", status=status.HTTP_201_CREATED)
            # serializer.save()
            # return Response(serializer.data, status=status.HTTP_201_CREATED)
