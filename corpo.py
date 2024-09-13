produtos = []




mev = float('inf')
mav = -1
for produto in produtos:
    if produto['quantidade'] > mav:
        produto['nome'] = mav
    if produto['quantidade'] < mev:
        produto['nome'] = mev


print(f"produto menos vendido: {mev}")
print(f"produto mais vendido: {mav}")