from django.views.generic import TemplateView


class hello_world(TemplateView):
    template_name = 'pages/hello_world.html'
