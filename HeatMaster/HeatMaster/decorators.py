from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied

def manager_required(view_func):
    def _check_user(user):
        if user.is_authenticated:
            if user.groups.filter(name='Manager').exists() or user.is_superuser:
                return True
        raise PermissionDenied
    
    return user_passes_test(_check_user)(view_func)
