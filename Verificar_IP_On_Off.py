import subprocess
import os

with open(os.devnull, "wb") as limbo:
    for n in range(1, 255):
        ip="192.168.1.{0}".format(n)
        result=subprocess.Popen(["ping", "-n", "1", "-w", "200", ip],
        stdout=limbo, stderr=limbo).wait()
        if result:
            arq2 = open("C:/Users/adminbh/Desktop/Estudo/DATASCIENCE/PythonFundamentos-master/Cap04/Notebooks/arquivos/off.txt", "a")
            arq2.write("192.168.1.{0}\n".format(n))
        else:
            arq2 = open("C:/Users/adminbh/Desktop/Estudo/DATASCIENCE/PythonFundamentos-master/Cap04/Notebooks/arquivos/on.txt", "a")
            arq2.write("192.168.1.{0}\n".format(n))
            arq2.close()
