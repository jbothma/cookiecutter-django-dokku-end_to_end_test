from django.views import generic


class Index(generic.TemplateView):
    template_name = "initial_app/index.html"
