import csv
import json
def solucion():

    #Archivo Json
    with open('GLOBANT.csv', newline='') as globant:
        with open('detalles.json', 'w') as detalles:
            lector = csv.reader(globant)
            globantList = list(lector)
            globantList.pop(0)
            
            lowest_price=float(globantList[0][4])
            highest_price=float(globantList[0][4])
            sube = 0
            baja = 0
            estable = 0
            for accion in globantList:
                if lowest_price > float(accion[4]):
                    lowest_price = float(accion[4])
                    date_lowest_price = accion[0]
                
                if highest_price < float(accion[4]):
                    highest_price = float(accion[4])
                    date_highest_price = accion[0]
                
                if float(accion[4])-float(accion[1])>0:
                    sube = sube + 1
                elif float(accion[4])-float(accion[1])<0:
                    baja = baja + 1
                elif float(accion[4])-float(accion[1])==0:
                    estable = estable + 1
            
            solucion = {
                "date_lowest_price":date_lowest_price,
                "lowest_price":lowest_price,
                "date_highest_price":date_highest_price,
                "highest_price":highest_price,
                "cantidad_veces_sube":sube,
                "cantidad_veces_baja":baja,
                "cantidad_veces_estable":estable
            }
            json.dump(solucion,detalles)
    globant.close
        
         



#Archivo csv
    with open('GLOBANT.csv', newline='') as globant:
        with open('analisis_archivo.csv', 'w', newline='') as analisis:
            lector = csv.reader(globant)
            escritor = csv.writer(analisis, delimiter='\t')
            
            globantList = list(lector)
            globantList.pop(0)

            escritor.writerow(["Fecha","Comportamiento de la accion", "Punto Medio High Low"])

            for accion in globantList:

                #Fecha
                fecha = accion[0]

                #Comportamiento
                if float(accion[4])-float(accion[1])>0:
                    comportamiento = "SUBE"
                elif float(accion[4])-float(accion[1])<0:
                    comportamiento = "BAJA"
                elif float(accion[4])-float(accion[1])==0:
                    comportamiento = "ESTABLE"

                #Punto medio
                puntoMedio = (float(accion[2])-float(accion[3]))/2

                escritor.writerow([fecha, comportamiento, puntoMedio])
           
    globant.close


solucion()