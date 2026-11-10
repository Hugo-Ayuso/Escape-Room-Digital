"""Punto de entrada del prototipo Escape Room Digital."""

import time


def jugar():
    """Ejecuta una pequeña aventura de escape por consola."""
    tiempo_limite = 120
    inicio = time.monotonic()
    inventario = []
    puerta_abierta = False

    print("\\n=== ESCAPE ROOM DIGITAL ===")
    print("Despiertas en una habitación cerrada. Tienes 2 minutos para escapar.")
    print("Encuentra la llave resolviendo el acertijo: ¿Cuánto es 6 x 7?")

    while time.monotonic() - inicio < tiempo_limite and not puerta_abierta:
        restante = max(0, int(tiempo_limite - (time.monotonic() - inicio)))
        print(f"\\nTiempo restante: {restante} segundos")
        print("1. Examinar la habitación")
        print("2. Resolver el acertijo")
        print("3. Consultar inventario")
        print("4. Intentar abrir la puerta")
        print("5. Salir")
        opcion = input("> ").strip()

        if opcion == "1":
            print("Ves una mesa, un cuadro y una puerta cerrada.")
            print("Detrás del cuadro hay una nota: «La respuesta abre el camino».")
        elif opcion == "2":
            respuesta = input("Introduce la respuesta: ").strip()
            if respuesta == "42":
                if "llave" not in inventario:
                    inventario.append("llave")
                print("¡Correcto! Has encontrado una llave.")
            else:
                print("No es correcto. Sigue buscando.")
        elif opcion == "3":
            print("Inventario:", ", ".join(inventario) if inventario else "vacío")
        elif opcion == "4":
            if "llave" in inventario:
                puerta_abierta = True
                print("¡La puerta se abre! Has escapado.")
            else:
                print("La puerta está cerrada. Necesitas una llave.")
        elif opcion == "5":
            print("Has abandonado la partida.")
            return
        else:
            print("Opción no válida.")

    if not puerta_abierta:
        print("\\nSe acabó el tiempo. ¡Inténtalo de nuevo!")


if __name__ == "__main__":
    jugar()
