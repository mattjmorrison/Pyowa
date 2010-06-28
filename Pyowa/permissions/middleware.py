from Pyowa.permissions import models, middleware

APPS = [group.name for group in models.PermissionGroup.objects.all()]

class Permissions(object):

    def process_view(self, request, view_func, view_args, view_kwargs):
        auth_perm = view_kwargs.pop('auth_perm', None)
        view_perms = view_kwargs.pop('view_perms', [])
        if auth_perm in APPS:
            return self.apply_permissions(request.user, auth_perm, view_perms)

    def apply_permissions(self, user, auth_perm, view_perms):
        if user.is_authenticated():
            print "authenticated"
        else:
            print "not authenticated"