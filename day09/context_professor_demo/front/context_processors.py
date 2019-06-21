from .models import User

def frontuser(request):
    user_id = request.session.get('user_id')
    context = {}
    if user_id:
        try:
            user = User.objects.get(pk=user_id)
            context['frontuser'] = user
        except:
            pass
    return context