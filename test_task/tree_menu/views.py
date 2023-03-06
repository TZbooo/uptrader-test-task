from django.views.generic import DetailView


class TreeMenuDetailView(DetailView):
    template_name = 'tree.html'