from rest_framework.response import Response
from rest_framework.decorators import api_view
from .firebaseConfig import auth


# Create your views here.
@api_view(['POST'])
def sign_in_view(request):
    email = request.email
    password = request.password
    authentication = auth.sign_in_with_email_and_password(email, password)
    return Response()
