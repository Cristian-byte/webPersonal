from django.shortcuts import render, HttpResponse

html_base = """
    <h1>Mi Web Personal</h1>
    <ul>
        <li><a href="/">Portada</a></li>
        <li><a href="/about/">Acerca de</a></li>
        <li><a href="/contact/">Contacto</a></li>
    </ul>
"""

def home(request):
    return HttpResponse(html_base + """
        <h2>Bienvenidos</h2>
        <p>Esto es la portada.</p>
    """)

def about(request):
    return HttpResponse(html_base + """
        <h2>Acerca de</h2>
        <p>Me llamo Cristian Sánchez Flores y estudio en la Universidad Tecnologica de Tlaxcala</p>
    """)

def contact(request):
    return HttpResponse(html_base + """
        <h2>Contacto</h2>
        <p>Mi correo Electronico y mis paginas web</p>
        <ul>
            <li><a href="mailto:cristian.san2908@gmail.com">Email</a></li>
            <li><a href="https://github.com/Cristian-byte">Github</a></li>
            <li><a href="https://youtu.be/o-YBDTqX_ZU">YouTube</a></li>
        </ul>
    """)
