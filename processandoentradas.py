
import numpy as np
def desconpactE (entrada1):
    colunas = entrada1[1:]
    
    colunas = np.reshape(colunas,(1,1,1,4))
    ae = np.reshape(colunas[0,0,0,0],(273,1))
    ai = np.reshape(colunas[0,0,0,1],(273,1))
    ao = np.reshape(colunas[0,0,0,2],(273,1))
    au = np.reshape(colunas[0,0,0,3],(273,1))
    re = np.concatenate((ae,ai,ao,au),axis = 1)
    re = re[1:,:]
    re = re[np.newaxis]
    re = re[np.newaxis]
    
   
    

    imagens = entrada1[0][:]
    IMAGE_SHAPE = (imagens[0].shape[0],imagens[0].shape[1],imagens[0].shape[2])
    COLUNA_SHAPE = (1,4,1)
    newc = np.zeros((len(imagens),1,4,1),dtype = np.float64)
    for i in range (len(imagens)):
        newc[i,0,:,0] = re[0,0,i,:]
        
    return imagens,newc    



def getVariabels():
    entrada1 = np.load("10 second video FAIL_entradas.npy")
    entrada2 = np.load("10 second video FAIL - Copia_entradas.npy")
    saida1 = np.load("10 second video FAIL_saidas.npy")
    saida2 = np.load("10 second video FAIL - Copia_saidas.npy")
    saida1 = saida1[1:]
    saida2 = saida2[1:]
    imagem1,coluna1 = desconpactE(entrada1)
    imagem2,coluna2 = desconpactE(entrada2)
  #-------------------------------------------------------------------------------------------------------------------------------    
    Imagemcompleta = np.concatenate((imagem1, imagem2), axis=0)
    colunacompleta = np.concatenate((coluna1, coluna2), axis=0)
    saidacompleta =  np.concatenate((saida1, saida2), axis=0)
    return Imagemcompleta,colunacompleta, saidacompleta


