from django.views.generic import TemplateView


class hello_world(TemplateView):
    template_name = 'hello_world.html'
