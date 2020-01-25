from django.views import generic


class Index(generic.TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        print("here")
        context = super().get_context_data(**kwargs)
        return context
