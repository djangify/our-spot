from django.views.generic import ListView
from locations.models import Locations


class Index(ListView):
    template_name = 'home/index.html'
    # model = locations
    # context_object_name = 'location'

    # def get_queryset(self):
    #     return self.model.objects.all()[:3]
