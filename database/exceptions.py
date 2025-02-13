import werkzeug

class NotAuthorized(werkzeug.exceptions.HTTPException):
    code = 401
    description = 'Not authorized.'