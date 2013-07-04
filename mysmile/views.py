from django import http
from django.template import (Context, RequestContext,
                             loader, Template, TemplateDoesNotExist)
from django.views.decorators.csrf import requires_csrf_token

@requires_csrf_token
def my_custom_404_view(request, template_name = '404.html'):
    try:
        template = loader.get_template(template_name)
    except TemplateDoesNotExist:
        template = Template(
            '<h1>Not Found</h1>'
            '<p>The requested URL {{ request_path }} was not found on this server.</p>')
    return http.HttpResponseNotFound(template.render(RequestContext(request, {'request_path': request.path})))

