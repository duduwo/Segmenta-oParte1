import cv2

# Carregue a imagem
imagem = cv2.imread('h.png', cv2.IMREAD_GRAYSCALE)

# Aplicar um filtro gaussiano para reduzir o ruído
imagem_borrada = cv2.GaussianBlur(imagem, (5, 5), 0)

# Aplique a detecção de bordas de Canny
T1 = 50  # Ajuste T1 conforme necessário
T2 = 350  # Ajuste T2 conforme necessário
bordas = cv2.Canny(imagem_borrada, T1, T2)

# Exiba a imagem com as bordas detectadas
cv2.imshow('Detecção de Bordas de Canny', bordas)

# Espere por uma tecla para fechar a janela
cv2.waitKey(0)
cv2.destroyAllWindows()
