from django.views.generic import TemplateView


class HelloWorld(TemplateView):
    template_name = 'hello_world.html'


class AboutMe(TemplateView):
    template_name = 'about_me.html'
