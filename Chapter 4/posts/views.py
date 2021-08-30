from django.views.generic import TemplateView


class PostsBoard(TemplateView):
    template_name = 'posts.html'