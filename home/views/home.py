from django.shortcuts import render
from django.views.generic import TemplateView

from home.models import Slider, AboutUs, Mision, Vision, SocialResponsability
from company.models import Company


class Home(TemplateView):
    template_name = 'home/home.html'

    def get(self, request, *args, **kwargs):
        home_sliders = Slider.objects.all()
        about_us = AboutUs.objects.all().first()
        companies = Company.objects.all()
        mision = Mision.objects.all().first()
        vision = Vision.objects.all().first()
        social = SocialResponsability.objects.all().first()
        data = {
            'sliders': home_sliders,
            'about_us': about_us,
            'companies': companies,
            'mision': mision,
            'vision': vision,
            'social': social
        }
        return render(request, self.template_name, data)
