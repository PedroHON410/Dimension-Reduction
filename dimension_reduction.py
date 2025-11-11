#Importando bibliotecas
from PIL import Image
import os

#Criando variáveis para as pastas
INPUT_DIR = "input"
OUTPUT_DIR = "output"

#Função para acessar pasta e pegar imagem
def in_file(filename):
    return os.path.join(INPUT_DIR, filename)

#Função para acessar pasta e depositar nova imagem
def out_file(filename):
    return os.path.join(OUTPUT_DIR, filename)

#Função para tornar a imagem em tons de cinza
def grayscale(colored):
    try:
        w, h = colored.size
        img = Image.new("RGB", (w,h))

        for x in range(w):
            for y in range(h):
                pxl = colored.getpixel((x,y))
                lum = int(0.3 * pxl[0] + 0.59 * pxl[1] + 0.11 * pxl[2])
                img.putpixel((x,y), (lum, lum, lum))
        return img
    
    except (AttributeError, TypeError, IndexError, ValueError) as e:
        print(f"Erro ao processar a imagem. Motivo: {e}")
        print("Certifique-se de que o objeto de entrada é uma imagem Pillow válida e foi aberto corretamente.")
        return None
    
#Função para tornar a imagem em preto e branco
def bwscale(gray):
    try:
        w, h = gray.size
        img = Image.new("RGB", (w,h))

        for x in range(w):
            for y in range(h):
                pxl = gray.getpixel((x,y))
                if pxl[0] >= 127 and pxl[1] >= 127 and pxl[2] >= 127:
                    img.putpixel((x,y), (255, 255, 255))
                else:
                    img.putpixel((x,y), (0, 0, 0))
        return img
    
    except IndexError as e:
        print(f"Erro de acesso ao canal de cor (IndexError): A imagem de entrada (gray) pode estar no modo 'L' (tons de cinza com 1 canal) e seu código espera 3 canais (RGB). Detalhe: {e}")
        print("Tente verificar apenas o primeiro canal: pxl = gray.getpixel((x,y)); if pxl[0] >= 127...")
        return None
        
    except (AttributeError, TypeError) as e:
        print(f"Erro no tipo de objeto/imagem: Certifique-se de que 'gray' é um objeto Pillow Image válido. Detalhe: {e}")
        return None

#Executando
if __name__ == "__main__":
    img = Image.open(in_file("Lenna.png"))
    lenna_cinza = grayscale(img)
    lenna_cinza.save(out_file("lenna_cinza.png"))
    lenna_cinza.show()
    img2 = Image.open(out_file("lenna_cinza.png"))
    lenna_bw = bwscale(img2)
    lenna_bw.save(out_file("lenna_bw.png"))
    lenna_bw.show()