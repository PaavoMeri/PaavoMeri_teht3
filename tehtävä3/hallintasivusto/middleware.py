from .models import SivunLataukset

class SivunLatauksetMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        # Estä laskemasta pyyntöjä, jotka alkavat /admin/ ja varmista, että vastauksen tilakoodi on 200
        if not request.path.startswith('/admin/') and response.status_code == 200:
            ip = self.get_client_ip(request)
            SivunLataukset.objects.create(ip_address=ip)
        
        return response

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

