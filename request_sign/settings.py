from django.conf import settings
from request_sign.utils import handle_pass_list

__all__ = ['ENABLE_REQUEST_SIGNATURE', 'SIGNATURE_SECRET', 'SIGNATURE_ALLOW_TIME_ERROR', 'SIGNATURE_RESPONSE',
           'SIGNATURE_PASS_LIST', 'SIGNATURE_METHOD']

http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']

ENABLE_REQUEST_SIGNATURE = settings.ENABLE_REQUEST_SIGNATURE if \
    hasattr(settings, 'ENABLE_REQUEST_SIGNATURE') else False  # 开启签名校检

SIGNATURE_SECRET = settings.SIGNATURE_SECRET if \
    hasattr(settings, 'SIGNATURE_SECRET') else None  # 私钥

SIGNATURE_ALLOW_TIME_ERROR = settings.SIGNATURE_ALLOW_TIME_ERROR if \
    hasattr(settings, 'SIGNATURE_ALLOW_TIME_ERROR') else 600  # 允许时间误差

SIGNATURE_RESPONSE = settings.SIGNATURE_RESPONSE if \
    hasattr(settings, 'SIGNATURE_RESPONSE') else 'request_sign.utils.default_response'  # 签名不通过返回方法

SIGNATURE_PASS_LIST = handle_pass_list(settings.SIGNATURE_PASS_LIST) if \
    hasattr(settings, 'SIGNATURE_PASS_LIST') else []  # 不效验签名的url,可传入django的url name字段

SIGNATURE_METHOD = settings.SIGNATURE_METHOD if \
    hasattr(settings, 'SIGNATURE_METHOD') else http_method_names  # 检查的请求类型，默认全部检查
