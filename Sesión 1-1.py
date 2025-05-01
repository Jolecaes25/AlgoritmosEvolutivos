# Castañeda Esquivel Jorge Leonardo
# 0202114002

import numpy;
precios = numpy.array([2.50,3.00,1.75,2.20])
cafes = numpy.array(['A','B','C','D'])
max_cafes = numpy.floor(10/precios)

# print (max_cafes);
# print (max_cafes.max(),max_cafes.argmax());
# print (precios.min(),precios.argmin());
for i, cafe in enumerate(cafes):
    print ("Cafe: ",cafe,", precio: ",precios[i],", máximo:",round(max_cafes[i]),"cafés")
print ("Con S/. 10, puedo comprar como máximo ",round(max_cafes.max()),"cafés en la cafetería C (precio mínimo S/.",precios.min(),")")