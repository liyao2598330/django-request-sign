"""
@author: liyao
@contact: liyao2598330@126.com
@time: 2020/7/30 4:42 下午
"""

from django.utils.deprecation import MiddlewareMixin
from django.utils.module_loading import import_string

from request_sign.signature import check_signature
from request_sign.settings import SIGNATURE_RESPONSE, ENABLE_REQUEST_SIGNATURE, SIGNATURE_METHOD, SIGNATURE_PASS_LIST


class RequestSignMiddleware(MiddlewareMixin):

    @staticmethod
    def process_request(request):
        if ENABLE_REQUEST_SIGNATURE and \
                request.method in SIGNATURE_METHOD and \
                request.path not in SIGNATURE_PASS_LIST:

            if not check_signature(request):
                return import_string(SIGNATURE_RESPONSE)()
