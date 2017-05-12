import jwt

PRIVATE_KEY = 'secret'  # TODO: where to put the private key?


def authenticate(token):
    try:
        jwt.decode(token, PRIVATE_KEY)
    except jwt.InvalidTokenError:
        print 'Token invalid'
        return False
    except jwt.DecodeError:
        print 'Signature verification failed'
        return False
    except jwt.ExpiredSignatureError:
        print 'Token has expired'
        return False
    return True


class JWTAuthenticationMiddleWare(object):
    def process_request(self, request):
        token = request.GET.get('jwt')
        if token is not None and authenticate(token):
            return jwt.decode(token, verify=False).get('username')  # TODO: get username, return or what?
