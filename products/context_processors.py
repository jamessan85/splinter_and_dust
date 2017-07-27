from .models import Collection
from tradelogins.models import AccountInfo, Purchase

def collection(request):
    return {'collection': Collection.objects.all()}

def accountinfo(request):
    return {'accountinfo': AccountInfo.objects.all()}

def purchase(request):
    return {'purchase': Purchase.objects.all()}