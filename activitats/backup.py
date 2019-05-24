from activitats.models import Activitat
activitats = Activitat.objects.all()
llista = []
for x in activitats:
    dia = str(x.dia)
    diafinal = str(x.diafinal)
    llista =llista + [{"id":x.id,"nom":x.nom,"descripcio":x.descripcio,"dia":dia,"diafinal":diafinal,"localitat":x.localitat.nom,"categoria":x.categoria.nom,"creador":x.creador}]
import json
a = json.dumps(llista)
f = open("activitats/backup.txt", "w")
f.write(a)
f.close()