from inpc import busca_inpc

inpc = busca_inpc()

inpc_inicio = float(inpc['inpc1'])
inpc_fin = float(inpc['inpc2'])
inpc_reciente = 132.373

#print(inpc_inicio)
#print(inpc_fin)

# FACTOR DE INFLACION = ( INPC mas reciente / INPC  del primer periodo ) - 1
factor_inflacion = (inpc_reciente / inpc_inicio) - 1
print("Factor de inflacion: ", round(factor_inflacion, 4))

