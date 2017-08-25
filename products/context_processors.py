from .models import Collection
from tradelogins.models import AccountInfo, Purchase

#context processor added so items can be viewed in all views
def collection(request):
    return {'collection': Collection.objects.all()}

def accountinfo(request):
    return {'accountinfo': AccountInfo.objects.all()}

def purchase(request):
    return {'purchase': Purchase.objects.all()}