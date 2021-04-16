from .models import Category


def catalog(request):
    return {'catalog': Category.objects.all()}
