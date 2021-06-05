from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

from .models import Company, Device, Location
from .serializers import CompanySerializer, DeviceSerializer, LocationSerializer


@login_required
def admin_page(request):
    locs = []
    devices = Device.objects.all()
    for device in devices:
        loc = Location.objects.filter(device_id=device.id).latest('id')
        locs.append(loc)
    locs_serialized = serializers.serialize('json', locs)
    if request.is_ajax():
        return JsonResponse(locs_serialized, safe=False)
    return render(request, 'map_admin.html', {'locs': locs_serialized})


class CompanyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Company.objects.all().order_by('id')
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]


class DeviceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [permissions.IsAuthenticated]



class LocationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [permissions.IsAuthenticated]
