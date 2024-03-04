cadenaLarga = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque dapibus nunc vehicula nulla tincidunt faucibus. Aenean a tempus urna. Aenean sollicitudin mi sit amet tincidunt efficitur. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Nunc et turpis nec mi pellentesque tempor sed in velit. In in ultricies ipsum, ac egestas ligula. Fusce ac purus non ipsum facilisis lobortis. Vivamus dignissim sodales augue, vel vestibulum ligula tincidunt et. Vivamus ultricies iaculis tincidunt. Fusce risus libero, elementum eu viverra nec, vestibulum a mi. Mauris fringilla orci sed justo consectetur efficitur. Quisque tincidunt gravida odio eu ultricies.

Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Aliquam ut sapien hendrerit sapien lacinia feugiat. Proin fringilla nibh sit amet est finibus porta. Mauris id neque arcu. In rutrum augue non diam hendrerit rutrum. Maecenas magna odio, pharetra at viverra in, porttitor non magna. Suspendisse potenti. Morbi consectetur odio nibh. Nulla eros metus, eleifend non metus tincidunt, consequat lobortis mauris. Vestibulum vitae quam hendrerit, feugiat justo in, suscipit arcu.

Praesent volutpat, felis nec eleifend gravida, nibh metus cursus risus, ac posuere dui mauris in lacus. Donec leo est, commodo quis magna quis, consequat euismod nibh. Proin magna erat, scelerisque finibus eros ut, malesuada tempus diam. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Mauris est dui, mattis vel dui et, feugiat porttitor nisi. Fusce nisl libero, pulvinar vel sollicitudin ac, molestie eget urna. Interdum et malesuada fames ac ante ipsum primis in faucibus.

Quisque euismod imperdiet turpis, ut sagittis magna ultrices eu. In eleifend venenatis sapien, ut dignissim enim semper in. Praesent et efficitur augue. Nulla at mi vel felis volutpat tempor eu non mauris. Pellentesque nec mattis leo. Pellentesque a sapien in quam semper fringilla mattis eu turpis. Aenean luctus in leo ac lacinia.

Donec tincidunt commodo ante ut dictum. Curabitur suscipit dictum libero, at lacinia nunc iaculis eget. Vivamus gravida ante eu dui pellentesque, vel convallis mi venenatis. Proin molestie libero massa, ut dictum nulla bibendum sit amet. Proin id massa hendrerit, pulvinar tortor eget, pharetra tellus. Proin faucibus magna eu nisi tincidunt, eget molestie dolor scelerisque. Mauris quis tincidunt risus, at malesuada mauris. Ut at nibh porttitor, fringilla risus eu, ultrices leo."""

cadenaLarga = cadenaLarga.lower()

letras = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
caracteres = ['a', 'e', 'i', 'o', 'u', ' ', ',', '.']
estadisticas = ['Total de caracteres:', 'Total de letras : ', 'Total de vocales a :', 'Total de vocales e :', 'Total de vocales i :', 'Total de vocales o :', 'Total de vocales u :', 'Total de espacios :', 'Total de comas :', 'Total de puntos :']
totales = [0,0,0,0,0,0,0,0,0,0]

for caracter in cadenaLarga:
    totales[0] += 1

for caracter in cadenaLarga:
    if caracter in letras:
        totales[1] += 1
    

for i in range(len(caracteres)):
    for caracter in cadenaLarga:
        if caracter == caracteres[i]:
            totales[i+2] += 1

for i in range(len(estadisticas)):
    print(estadisticas[i], totales[i])
