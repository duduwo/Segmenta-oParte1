import cv2

# Carregue a imagem
imagem = cv2.imread('v.png', cv2.IMREAD_GRAYSCALE)

# Defina o valor do limiar
limiar = 128  # Ajuste o limiar conforme necessário

# Aplicar a limiarização
_, imagem_limiarizada = cv2.threshold(imagem, limiar, 255, cv2.THRESH_BINARY)

# Exiba a imagem limiarizada
cv2.imshow('Imagem Limiarizada', imagem_limiarizada)

# Espere por uma tecla para fechar a janela
cv2.waitKey(0)
cv2.destroyAllWindows()
