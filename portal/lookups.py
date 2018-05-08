from ajax_select import register, LookupChannel
from .models import User, Category


@register('user')
class UserLooKup(LookupChannel):
    model = User

    def get_query(self, q, request):
        return self.model.objects.filter(username__icontains=q).order_by('username')


@register('categories')
class CategoryLooKup(LookupChannel):
    model = Category

    def get_query(self, q, request):
        return self.model.objects.filter(name__icontains=q).order_by('name')