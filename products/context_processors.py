from .models import Collection
from tradelogins.models import AccountInfo

def collection(request):
    return {'collection': Collection.objects.all()}

def accountinfo(request):
    return {'accountinfo': AccountInfo.objects.all()}