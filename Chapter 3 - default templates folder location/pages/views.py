from django.views.generic import TemplateView

# Create your views here.


class hello_world(TemplateView):
    template_name = 'pages/hello_world.html'