from django.views.generic.base import TemplateView

class HomepageView(TemplateView):
    template_name = "frontend/index.html"

homepage = HomepageView.as_view()
