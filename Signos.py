date = input("Coloque a sua data de nascimento no formato dd/mm \n")
dm = date.split('/')


r = 0

a = 0

#Definindo as regras de signos:
sig = [0, 'Áries', 'Touro', 'Gêmeos', 'Câncer', 'Leão', 'Virgem', 'Libra', 'Escorpião', 'Sagitário', 'Capricórnio', 'Aquário', 'Peixes']


tam_mes =  [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 0]

while r != int(dm[1]):
    
    a = a + tam_mes[r]
    
    r = r + 1

a = a + int(dm[0])



#print(a ,r)

#Definição dos signos(bissexto):
    #Aquario
if 21< a <49 :    
    print(sig[11]) 
    #Peixes
elif 50< a < 80:
    print(sig[12])
    #Aries
elif 80< a <111 :
    print(sig[1])  
    #Touro
elif 112< a <141 :    
    print(sig[2])
    #Gêmeos
elif 142< a <172 :    
    print(sig[3])
    #Câncer
elif 173< a <204 :    
    print(sig[4])
    #Leão
elif 205< a <235 :    
    print(sig[5])    
    #Virgem
elif 236< a <266 :    
    print(sig[6])  
    #Libra
elif 267< a <296 :    
    print(sig[7])  
    #Escorpião
elif 297< a <326 :    
    print(sig[8]) 
    #Sagitário
elif 327< a <356 :    
    print(sig[9])  
    #Capricornio
else:
    print(sig[10])
    
#Corringindos as possíveis datas incorretas:
    
if int(dm[1]) > 12 or int(dm[0]) > 31:
    print("Formato de data Incorreta")

#print(dm)