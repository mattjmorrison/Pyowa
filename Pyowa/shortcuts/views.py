from django.shortcuts import render_to_response
from django.template import RequestContext

def render_to(template):
    def decorator(func):
        def func_wrap(request, *args, **kw):
            result = func(request, *args, **kw)
            if isinstance(result, dict):
                result = render_to_response(template, result, RequestContext(request))
            return result
        return func_wrap
    return decorator