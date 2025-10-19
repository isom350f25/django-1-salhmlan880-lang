from django.http import HttpResponse

# Create your views here.
def sulieman(request):
 
    return HttpResponse("""
  <html>
    <body>
      <h1>sulieman </h1>
      <p>2211112510 <strong>html</strong> web app!</p>
    </body>
  </html>
  """)