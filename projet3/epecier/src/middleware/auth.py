from django.shortcuts import redirect


class Auth(object):
    def __init__(self, get_response):
        """
        One-time configuration and initialisation.
        """
        self.get_response = get_response

    def __call__(self, request):

        if  request.path.find("/admin/login")==-1 and request.path.find("/admin/register")==-1:
            if 'user_id' not in request.session:
                return redirect('/admin/login')
            else:
                print("user id not exist")
            if request.session['user_id']==None:
                return redirect('/admin/login')
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        
        
        return None

    def process_exception(self, request, exception):
        """
        Called when a view raises an exception.
        """
        return None

    def process_template_response(self, request, response):
        """
        Called just after the view has finished executing.
        """
        return response

