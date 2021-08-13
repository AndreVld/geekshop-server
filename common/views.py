class DataMixin:
    title = None

    def get_context_data(self, **kwargs):
        context = super(DataMixin, self).get_context_data(**kwargs)
        context['title'] = self.title
        return context