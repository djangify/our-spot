from django.views.generic import ListView
from locations.models import Location


class Index(ListView):
    template_name = 'home/index.html'
    model = Location
    context_object_name = 'location'

    def get_queryset(self):
        return self.model.objects.all()[:7]
