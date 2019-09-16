import numpy as np
import cv2
def saveconfig(caminho,Cor,defeitog,defeitol,manchas,Y):
    cap = cv2.VideoCapture(caminho)

    imagens = []
    resultado = []
    Cor1 = []
    defeitog1 = []
    defeitol1 = []
    manchas1 = []
    y = []
    while(cap.isOpened()):
        ret, frame = cap.read()
        if frame is not None:
            frame = cv2.resize(frame,(224,224),interpolation = cv2.INTER_AREA)
            framep = np.asarray(frame,dtype=np.float)
            imagens.append(framep/255)
        elif ret==False:
            break

    cap.release()
    imagens = np.array(imagens)
    for i in range (len(imagens)+1):
        Cor1.append(Cor)
        defeitog1.append(defeitog)
        defeitol1.append(defeitol)
        manchas1.append(manchas)
        y.append(Y)
    resultado.append(imagens)
    resultado.append(np.array(Cor1))
    resultado.append(np.array(defeitog1))
    resultado.append(np.array(defeitol1))
    resultado.append(np.array(manchas1))
    saida = np.array(y)
    final = np.array(resultado)
    caminhoslp = caminho.split('/')
    np.save(caminho.split('/')[len(caminhoslp)-1].split('.')[0]+'_saidas.npy',saida)
    np.save(caminho.split('/')[len(caminhoslp)-1].split('.')[0]+'_entradas.npy', final)
    print(final[1][0])

   


def processingy(y):
    if y == '1':
        Y = np.array([1,0,0,0,0])
    elif y == '2':
        Y = np.array([0,1,0,0,0])
    elif y == '3':
        Y = np.array([0,0,1,0,0]) 
    elif y == '4':
        Y = np.array([0,0,0,1,0])
    elif y == '5':
        Y = np.array([0,0,0,0,1])             
    return Y      
