#4) Implementar uma função que retorne verdadeiro se o número for primo
#(falso caso contrário). Testar de 1 a 100.

lista = []

for i in range(1,101):
    
    contador = 0
    for c in range(1, i + 1):
        if i % c == 0:
            contador += 1
           
    if contador != 1 and contador <= 2:
        lista.append(i)  
       
print(lista)
            
    

    
    
    
        
    
     
        
        

    

        
        

        
    
  