# Django modules
from django.views import generic

# Local modules
from core.models.policy import Policy


class PolicyListView(generic.ListView):
    model = Policy
    template_name = "core/policy/policy_list.html"
    context_object_name = "policies"
    paginate_by = 10

    def get_queryset(self):
        return self.model.objects.active().order_by("-created")


class PolicyDetailView(generic.DetailView):
    model = Policy
    template_name = "core/policy/policy_detail.html"
