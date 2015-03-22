from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy

from .models import Kudo

# https://docs.djangoproject.com/en/1.7/topics/class-based-views/intro/#mixins-that-wrap-as-view
class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **kwargs):
        view = super(LoginRequiredMixin, cls).as_view(**kwargs)
        return login_required(view)


class KudoCreate(LoginRequiredMixin, CreateView):
    model = Kudo
    success_url = reverse_lazy('kudo_list')

    # automatically add the giver based on the current user
    def form_valid(self, form):
        form.instance.giver = self.request.user
        return super(KudoCreate, self).form_valid(form)


class KudoDetail(LoginRequiredMixin, DetailView):
    model = Kudo


class KudoList(LoginRequiredMixin, ListView):
    model = Kudo
