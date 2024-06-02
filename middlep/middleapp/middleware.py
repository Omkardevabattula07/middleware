from django.core.cache import cache
from django.http import HttpResponseForbidden
from django.utils.deprecation import MiddlewareMixin
class visitlimit(MiddlewareMixin):
    def process_request(self,request):#This is a basic request that is defiend by us but when the middleware run this function also runs
        path=request.path
        user_ip=request.META.get("REMOTE_ADDR")
        cache_key=f'visit_count_{user_ip}_{path}'
        visit_count=cache.get(cache_key,0)
        if path =='/restrict/':#basic if statement that restrict one page but not others
            limit = 5
            timeout =60
        else:
            limit =float("inf")#no limit for other paths
            timeout =0#no time out needed
        if visit_count>=limit:
            return HttpResponseForbidden("If you havent girl problems i fell bad for you son i have 99 problems and bitch aint one")
        cache.set(cache_key,visit_count+1,timeout=timeout)

        