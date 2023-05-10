from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from . models import Flower
from django.views.decorators.csrf import csrf_protect
from .serializers import FlowerSerializer
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


def detail(request, flower_id=None):
    if flower_id:
        try:
            flower = Flower.objects.get(pk=flower_id)
        except flower.DoesNotExist:
            raise Http404("Flower does not exist")
        return render(request, "flowers/detail.html", {"flower": flower})
    else:
        return render(request, "flowers/detail.html", {})


@csrf_protect
def create(request):
        print(request.FILES.get('image'))
        flower_serializer = FlowerSerializer(data=request.POST)
        if flower_serializer.is_valid():
            # Save the flower instance
            flower = flower_serializer.save()
            # Get the uploaded image
            image = request.FILES.get('image')
            if image:
                # If an image was uploaded, save it to the flower instance
                flower.image = image
                flower.save()
            return redirect('home')
        else:
            return render(request, "flowers/detail.html", {})


@csrf_protect
def update(request, flower_id):
        try:
            flower = Flower.objects.get(pk=flower_id)
            flower_serializer = FlowerSerializer(instance=flower, data=request.POST, partial=True)
            if flower_serializer.is_valid():
                # Save the flower instance
                flower = flower_serializer.save()
                # Get the uploaded image
                image = request.FILES.get('image')
                if image:
                    # If an image was uploaded, save it to the flower instance
                    flower.image = image
                    flower.save()
                return redirect('home')
            else:
                return render(request, "flowers/detail.html", {})
        except flower.DoesNotExist:
            raise Http404("Flower does not exist")
    
def home(request):
    try:
        flowers = Flower.objects.all()
    except:
        raise Http404("No flowers available")
    return render(request, "flowers/home.html",{"flowers": flowers})

@api_view(['GET'])
def get_flowers(request):
    try:
        flowers = Flower.objects.all()
        serializer = FlowerSerializer(flowers,many=True)
        if(serializer.is_valid):
            return Response({"flowers": serializer.data}, status=status.HTTP_200_OK)
    except:
        return Response({"flowers": []},status=status.HTTP_200_OK)
