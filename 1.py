import cv2

# Carregue a imagem
imagem = cv2.imread('p.png', cv2.IMREAD_COLOR)

# Converta a imagem para escala de cinza
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Aplique o operador de Laplaciano
laplaciano = cv2.Laplacian(imagem_cinza, cv2.CV_64F)

# Calcule o valor absoluto do resultado
laplaciano_absoluto = cv2.convertScaleAbs(laplaciano)

# Aplique um limiar para destacar os pontos de interesse
limiar = 90  # Ajuste o limiar conforme necessário
pontos_interesse = cv2.inRange(laplaciano_absoluto, limiar, 255)

# Exiba a imagem com os pontos de interesse destacados
cv2.imshow('Detecção de Pontos de Interesse (Laplaciano)', pontos_interesse)

# Espere por uma tecla para fechar a janela
cv2.waitKey(0)
cv2.destroyAllWindows()
