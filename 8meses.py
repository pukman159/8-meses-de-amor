# main.py

def mostrar_mensaje_especial():
    mensaje = """
    ¡Feliz 8 meses, mi niña Cecilia Pari! 💖

    Estos 8 meses han sido los mejores de mi vida gracias a ti.
    Cada día a tu lado es un regalo que atesoro con todo mi corazón.
    Eres mi razón para sonreír, mi inspiración y mi mejor compañía,
    tambien quiero que viajes conmigo a todos lados.

    Te amo más de lo que las palabras pueden expresar.
    ¡Aquí está para muchos meses más juntos!  😍🎉

    Con todo mi amor,
    [Domingo Palacios]
    """
    print(mensaje)

def mostrar_fotos():
    # Aquí puedes agregar enlaces a fotos o recuerdos que hayas subido al repositorio
    fotos = [
        "WhatsApp Image 2025-02-17 at 2.07.11 PM.jpeg",
        "WhatsApp Image 2025-02-17 at 2.07.12 PM (1).jpeg",
        "WhatsApp Image 2025-02-17 at 2.07.12 PM.jpeg"
    ]
    print("\nAlgunos de nuestros mejores recuerdos juntos:")
    for foto in fotos:
        print(foto)

if __name__ == "__main__":
    mostrar_mensaje_especial()
    mostrar_fotos()
