import qrcode

imagem = qrcode.make("https://youtube.com.br")
imagem.save("primeiro_qrcode.png")