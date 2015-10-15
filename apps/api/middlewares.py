from django.core.urlresolvers import resolve, reverse


class VersionSwitchMiddleware(object):

    def process_request(self, request):
        r = resolve(request.path_info)
        version = request.META.get('HTTP_X_MYSMILE_VERSION', False)
        if r.namespace.startswith('api:') and version:
            old_version = r.namespace.split(':')[-1]
            request.path_info = reverse('{}:{}'.format(r.namespace.replace(old_version, version), r.url_name), args=r.args, kwargs=r.kwargs)
