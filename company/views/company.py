from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.views.generic import TemplateView

from company.models import Company, Slider


class CompanyView(TemplateView):
    template_name = 'company/company.html'

    def get(self, request, *args, **kwargs):
        slug = kwargs.get('url', None)
        if slug:
            try:
                company = Company.objects.filter(slug=slug).first()
                if company.description_block_3:
                    company.description_block_3 = company.description_block_3.replace('\n', '<br>')
                sliders = Slider.objects.filter(company=company)
                companies = Company.objects.all()
                if company:
                    data = {
                        'sliders': sliders,
                        'company': company,
                        'companies': companies
                    }
                    return render(request, self.template_name, data)
                else:
                    return HttpResponseNotFound("not found")
            except Exception as e:
                return HttpResponseNotFound("not found")
        else:
            return HttpResponseNotFound("not found")
