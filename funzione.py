import numpy as np
import matplotlib.pyplot as plt

def analisi_grafica(data_frame, target_name, lista_variabili_quantitative):
 
    '''
        la funzione analisi_grafica crea un'analisi grafica delle colonne quantitative di un dataframe:

        crea n*n grafici dove n è uguale alla lunghezza di "lista_variabili_quantitative". I grafici che genera sono:
        - istogrammi quando si tratta  della stessa variabile
        - grafici a dispersione quando si tratta di variabili diverse

        INPUT:
        -data_frame: data frame letto con pandas
        -target_name: nome della colonna dataframe su cui effetturare il riconoscimeto
        -lista_variabili_quantitative: lista contente i nomi delle colonne quantitative del dataframe
        
        RETURN:
        -analisi grafica del dataframe: figura contenente grafici a 
        dispersione e istogrammi delle varibili quantitative con colori 
        diversi in base al valore del target
        
        '''
    
    unique_target_values=data_frame[target_name].unique()
    target_values_color={}
    nrows, ncols=len(lista_variabili_quantitative), len(lista_variabili_quantitative)
    for value in unique_target_values:
        target_values_color[value]=np.random.uniform(0, 1,3)
    fig, axs=plt.subplots(nrows=nrows, ncols=ncols, figsize=(nrows*nrows, ncols*ncols))
    for i in range(nrows):
        for j in range(ncols):
            if i==j:
                for value in unique_target_values:
                    axs[i, j].hist(data_frame[data_frame[target_name]==value][lista_variabili_quantitative[i]].values, color=target_values_color[value],  label=value, alpha=0.5)


                    axs[i, j].set_xlabel(lista_variabili_quantitative[i])
                    axs[i, j].set_ylabel("Frequenza")
                    axs[i, j].legend()


            else:
                for value in unique_target_values:
                    axs[i, j].scatter(data_frame[data_frame[target_name]==value][lista_variabili_quantitative[i]].values, data_frame[data_frame[target_name]==value][lista_variabili_quantitative[j]].values,   color=target_values_color[value],  alpha=0.5, label=value)


                axs[i, j].set_xlabel(lista_variabili_quantitative[i])
                axs[i, j].set_ylabel(lista_variabili_quantitative[j])
                axs[i, j].legend()

            
                

                
    
    plt.show()
        