from .models import Establishment

def get_establishment_by_id(est_id: int):
    return Establishment.objects.filter(id=est_id).first()
