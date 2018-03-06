from numpy import arange, linspace, savetxt, array
import subprocess

xmin = 0.3
xmax = 4.
npts = 700
x = linspace(0.3,4,npts)
print "Distancias a analizar desde {:.3f} hasta {:.3f}".format(x[0],x[-1])
energias = []

# Abro el inoutfile y lo leo
inputfile = open("parsec.in", "r")
archivo = []
for line in inputfile:
    archivo.append(line)

inputfile.close()

for num in x:
    #print("Distancia actual = " + str(num) + " / " + str(x[-1]), end="\r", flush=True)
    print "Distancia actual = {:.3f} / {:.3f}\r".format(num, x[-1])

    # Modifico las nuevas condiciones
    archivo[19] = " " + str(num) + "00000      .000000      .000000\n"
    archivo[20] = str(-num) + "00000      .000000      .000000\n"

    # Abro el inputfile y escribo las nuevas condiciones
    input_w = open("parsec.in", "w")
    input_w.writelines(archivo)
    input_w.close()

    # Corro el programa de parsec con las nuevas condiciones
    subprocess.call("./parsec.ser", shell=True)

    # Abro el output file para leer la energia resultante
    output = open("parsec.out", "r")

    lineas = []
    for line in output:
        lineas.append(line)

    output.close()

    for i in range(len(lineas)-1,len(lineas)-70,-1):
        if "Total Energy" in lineas[i]:
            ener = float(lineas[i][28:35])

    energias.append(ener)

# Guardo los datos en un archivo de texto
d_e = array([x, energias])
savetxt("energias.txt", d_e, delimiter=",")
