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
    success_url = reverse_lazy('kudos_given')

    # automatically add the giver based on the current user
    def form_valid(self, form):
        form.instance.giver = self.request.user
        return super(KudoCreate, self).form_valid(form)

    # override the queryset on the receivers model so you can't give any kudos
    # to yourself. this needs to be here so we have access to the request.user
    # instance
    #
    # inspiration from http://stackoverflow.com/a/16685089/564709
    def get_form(self, *args, **kwargs):
        form = super(KudoCreate, self).get_form(*args, **kwargs)
        form.fields['receivers'].queryset = \
            form.fields['receivers'].queryset.exclude(
                username=self.request.user.username,
            )
        return form

class KudoList(LoginRequiredMixin, ListView):
    model = Kudo

class KudosGiven(KudoList):
    template_name = "base/kudos_given.html"
    def get_queryset(self):
        return self.model.objects.filter(
            giver=self.request.user,
        )

class KudosReceived(KudoList):
    template_name = "base/kudos_received.html"
    def get_queryset(self):
        return self.model.objects.filter(
            receivers=self.request.user,
        )
