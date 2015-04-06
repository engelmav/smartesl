from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

class User():
    # ...

    def generate_auth_token(self, expiration = 600):
        s = Serializer('secret_key', expires_in = expiration)
        return s.dumps({ 'id': self.id })

    @staticmethod
    def verify_auth_token(token):
        s = Serializer('secret_key')
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None # valid token, but expired
        except BadSignature:
            return None # invalid token
        user = User.query.get(data['id'])
        return user