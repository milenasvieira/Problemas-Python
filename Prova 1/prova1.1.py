tipo_vinho, pais, valor_compra = input () .split()
valor_compra = float (valor_compra)

valor_venda = 0

if pais == "IT":
    if valor_compra <= 200:
        valor_venda = valor_compra * 1.9
    else:
        valor_venda = valor_compra * 1.95
        
if pais == "FR":
    if tipo_vinho == "R" or tipo_vinho == "T":
        valor_venda = valor_compra * 1.75
    else:
        valor_venda = valor_compra * 1.80
        
if pais == "ES":
    valor_venda = valor_compra * 1.40
    
if pais == "PT":
    if tipo_vinho == "T":
        valor_venda = valor_compra * 1.75
    elif tipo_vinho == "R":
        valor_venda = valor_compra * 1.80
    else:
        valor_venda = valor_compra * 1.70
        
print ("{:.2f}" .format (valor_venda))