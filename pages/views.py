from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings
from django.http import HttpResponseRedirect
from django.utils.translation import gettext as _
from .models import Post


class HomePageView(TemplateView):
    
    def get_context_data(self, **kwargs):
        posts = Post.objects.all()
        context = super().get_context_data(**kwargs)
        context['title'] = _('Home')
        context['posts'] = posts 
        return context
    
    def render_to_response(self, context, **response_kwargs):
    
        # from django.utils import translation
        # user_language = 'fi' 
        # translation.activate(user_language)
        response = super(HomePageView, self).render_to_response(context, **response_kwargs)
        # response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)
        response.delete_cookie(settings.LANGUAGE_COOKIE_NAME)
        return response
    
    template_name = 'pages/home.html'
    

def home(request): 
    return render(request, 
                  'pages/home.html', 
                  {'title': _('Home')})


def change_language(request):
    response = HttpResponseRedirect('/')
    if request.method == 'POST':
        language = request.POST.get('language')
        if language:
            if language != settings.LANGUAGE_CODE and [lang for lang in settings.LANGUAGES if lang[0] == language]:
                redirect_path = f'/{language}/'
            elif language == settings.LANGUAGE_CODE:
                redirect_path = '/'
            else:
                return response
            from django.utils import translation
            translation.activate(language)
            response = HttpResponseRedirect(redirect_path)
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    return response