
from django.views.generic import TemplateView, FormView
from .forms import SearchForm
from django.urls import reverse_lazy
import google.generativeai as genai
from .models import Search

GOOGLE_API_KEY='AIzaSyAW-jJTfT5Vz2LKEZ_skHMwpBlAnxYbDGo'

class HomePageView(TemplateView):
    template_name = "home.html"

class InputView(FormView):
    template_name = "chat.html"
    form_class = SearchForm
    success_url = '/chat'

    def form_valid(self, form):
        variable = form.cleaned_data['text']

        genai.configure(api_key=GOOGLE_API_KEY)
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(variable)

        new_object = Search.objects.create(
            text = form.cleaned_data['text'],
            result = response.text
        )

        context = self.get_context_data(output=response.text)
        return self.render_to_response(context)
        
    
class OutputView(TemplateView):
    template_name = "result.html"
    
    
   
