produtos = []




mais_vendido = max(produtos, key=lambda p: p['quantidade'])
menos_vendido = min(produtos, key=lambda p: p['quantidade'])

print(f"mais vendido: {mais_vendido}\nMenos vendido: {menos_vendido}")
