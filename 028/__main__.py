from classes import Termostato

def main():
    t = Termostato()
    try:
        t.temperatura = 22.3
    except Exception as e:
        print(f"Houve um problema: {e}")
    t.temperatura=25.5
    print(f"A temperatura atual é de {t.ftemperatura}")
if __name__ == "__main__":
    main()