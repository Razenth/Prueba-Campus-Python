import os
from datetime import datetime
import core
ramas = ['Odontología','Oftomología','Pediatría','Ginecología','Nutrición','General']
diccCitas = {'data': []}

# Funciones para Uso en Main

def errorNoCitas():
    print('Error en busqueda, aún no se han ingresado citas')
    print('Volviendo al menú de citas')
    os.system('pause')
    input('')
    mainMenu()

def crearCita(nombrePaciente):
    try:
        fechaCita = input('║ Ingrese la fecha de cita (DD/MM/AAAA): ')
        if datetime.strptime(fechaCita, "%d/%m/%Y"):
            if datetime.strptime(fechaCita, "%d/%m/%Y").date() >= datetime.now().date():
                horaCita = input('║ Ingrese hora de la cita (ej.15:00): ')
                if datetime.strptime(horaCita, "%j:%M"):
                    os.system('cls')
                    print("╔══════════════════════════════════╗")
                    print(f"║         TIPO DE CONSULTA         ║")
                    print("╠══════════════════════════════════╝")
                    for i,item in enumerate(ramas):
                        print(f'║ {i+1}.{item}')
                    print("╚══════════════════════════════//")
                    opcionRama = int(input('Ingrese opción: '))
                    consulta = ramas[opcionRama-1]
                    os.system('cls')
                    motivoConsulta = input('Ingrese motivo de su consulta\n:)')
                    data = {
                        'nombrePaciente':nombrePaciente,
                        'fechaCita':fechaCita,
                        'horaCita':horaCita,
                        'tipoConsulta':consulta,
                        'motivo':motivoConsulta
                    }
                    os.system('cls')
                    print("╔═══════════════════════════════════════════╗")
                    print(f"║         CITA AGENDADA CON ÉXITO           ║")
                    print("╠═══════════════════════════════════════════╝")
                    print(f'║ Nombre Paciente: {nombrePaciente}')
                    print(f'║ Fecha de Cita: {fechaCita}')
                    print(f'║ Hora de Cita: {horaCita}')
                    print(f'║ Tipo de Consulta: {consulta}')
                    print(f'║ Motivo: {motivoConsulta}')
                    print("╚══════════════════════════════════════════//")
                    print('Cita ingresada con éxito')

                    core.crearInfo('citas.json',data)
                    LoadInfoCitas()
    except ValueError as e:
        os.system('cls')
        print('Error en dato digitado')
        print('Volviendo al menu de citas')


def LoadInfoCitas():
    global diccCitas
    if(core.checkFile('citas.json')):
        diccCitas = core.loadInfo('citas.json')
    else:
        core.crearInfo('citas.json', diccCitas)

# FUNCION PRINCIPAL

def mainMenu():
    LoadInfoCitas()
    flagMenu = True
    while flagMenu: 
        os.system('cls')
        print("╔══════════════════════════════════════════════════════╗")
        print("║                     MENU DE CITAS                    ║")
        print("╠══════════════════════════════════════════════════════╝")
        print('║ 1. Agregar Cita                                      ║')
        print('║ 2. Buscar Cita                                       ║')
        print('║ 3. Modificar Cita                                    ║')
        print('║ 4. Cancelar Cita                                     ║')
        print('║ 5. Salir del Programa                                ║')                        
        print("╚══════════════════════════════════════════════════════╝")

        try:
            opcion = int(input('Ingrese Opción: '))

        except ValueError as e:
            print('Error en dato ingresado, volviendo al menú de  citas')
            os.system('cls')
            mainMenu()

        else:
            os.system('cls')

            if opcion == 1:
                if len(diccCitas['data']) == 0:
                    print("╔═══════════════════════════════════════════╗")
                    print(f"║               AGREGANDO CITA              ║")
                    print("╠═══════════════════════════════════════════╝")
                    nombrePaciente = input('║ Ingrese el nombre del Paciente: ').upper()
                    while nombrePaciente == '':
                        os.system('cls')
                        print('Error en el nombre digitado')
                        nombrePaciente = input('║ Ingrese nombre del Paciente de nuevo: ')
                        os.system('clear')
                    crearCita(nombrePaciente)
                    os.system('pause')

                elif len(diccCitas['data']) >= 1:
                    print("╔═══════════════════════════════════════════╗")
                    print(f"║               AGREGANDO CITA              ║")
                    print("╠═══════════════════════════════════════════╝")
                    nombrePaciente = input('║ Ingrese el nombre del Paciente: ').upper()
                    while nombrePaciente == '':
                        print('Error en el nombre digitado')
                        nombrePaciente = input('║ Ingrese nombre del Paciente de nuevo: ')
                        os.system('cls')
                    repetido = False
                    for i,item in enumerate (diccCitas['data']):
                        if nombrePaciente == item['nombrePaciente']:
                            repetido = True
                            break
                    if repetido == False:
                        crearCita(nombrePaciente)
                        os.system('pause')
                        input('')
                    else:
                        os.system('cls')
                        print('Error en nombre ingresado, ya existe una cita a ese nombre')
                        print('Volviendo al menú de citas')
                        os.system('pause')
                        input('')
                        mainMenu()

            elif opcion == 2:
                if len(diccCitas['data']) == 0:
                    errorNoCitas()
                else:
                    os.system('cls')
                    print("╔═════════════════════════════════════╗")
                    print("║              BUSCAR CITA            ║")
                    print("╠═════════════════════════════════════╝")
                    print('║ 1. Buscar por Nombre                ║')
                    print('║ 2. Buscar por Fecha                 ║')
                    print("╚═════════════════════════════════════╝")
                    tipoBusqueda = input('Ingrese opción: ')
                    os.system('cls')
                    if tipoBusqueda == '1':
                        encontradoFlag = False
                        nombreBuscar = input('Ingrese nombre del Paciente: ').upper()
                        os.system('cls')
                        for i,item in enumerate(diccCitas['data']):
                            if nombreBuscar in item['nombrePaciente']:
                                encontradoFlag = True
                                print("╔═══════════════════════════════════════════╗")
                                print(f"║                   CITA                    ║")
                                print("╠═══════════════════════════════════════════╝")
                                print('║ Nombre Paciente: '+ item['nombrePaciente'])
                                print('║ Fecha Cita: '+ item['fechaCita'],',',item['horaCita'])
                                print('║ Tipo de Consulta: '+ item['tipoConsulta'])
                                print('║ Motivo: '+ item['motivo'])
                                print("╚══════════════════════════════════//")
                        os.system('pause')
                    elif tipoBusqueda == '2':
                        os.system('cls')
                        try:
                            encontradoFlag = False
                            fechaBusqueda = input('Ingrese fecha de cita (DD/MM/AAAA): ')
                            if datetime.strptime(fechaBusqueda, "%d/%m/%Y"):
                                for j,item in enumerate (diccCitas['data']):
                                    if fechaBusqueda in item['fechaCita']:
                                        print("╔═══════════════════════════════════════════╗")
                                        print(f"║                   CITA                    ║")
                                        print("╠═══════════════════════════════════════════╝")
                                        print('║ Nombre Paciente: '+ item['nombrePaciente'])
                                        print('║ Fecha Cita: '+ item['fechaCita'],',',item['horaCita'])
                                        print('║ Tipo de Consulta: '+ item['tipoConsulta'])
                                        print('║ Motivo: '+ item['motivo'])
                                        print("╚══════════════════════════════════//")
                                os.system('pause')
                                input('')
                            else:
                                os.system('cls')
                                print('Fecha Ingresada Incorrecta')
                                print('Volviendo al menú de citas')
                                os.system('pause')

                            if encontradoFlag == False:
                                print(f'No se encontró a ningún paciente')
                                os.system('pause')

                        except ValueError as e:
                            os.system('cls')
                            print('Valor ingresado no válido')
                            print('Volviendo al menú de citas')
                            os.system('pause')
            elif opcion == 3:
                if len(diccCitas['data']) == 0:
                    errorNoCitas()

                else:
                    nomb = input('Ingrese nombre del Paciente: ').upper()
                    encontradoFlag = False
                    for i,item in enumerate(diccCitas['data']):
                        if nomb == item['nombrePaciente']:
                            os.system('cls')
                            encontradoFlag = True
                            print("╔═════════════════════════════════════╗")
                            print("║            CITA ENCONTRADA          ║")
                            print("╠═════════════════════════════════════╝")
                            print('║ Qué desea modificar de la cita?     ║')
                            print('║                                     ║')
                            print('║ 1. Nombre del Paciente              ║')
                            print('║ 2. Fecha de Cita                    ║')
                            print('║ 3. Todas las anteriores             ║')
                            print("╚═════════════════════════════════════╝")
                            try:
                                opt = input('Ingrese Opción: ')
                                if opt == '1':
                                    os.system('cls')
                                    item['nombrePaciente'] = input('Ingrese el nuevo nombre del Paciente: ').upper()
                                    os.system('cls')
                                    print("╔═══════════════════════════════════════════╗")
                                    print(f"║             CITA ACTUALIZADA              ║")
                                    print("╠═══════════════════════════════════════════╝")
                                    print('║ Nuevo Nombre Paciente: '+ item['nombrePaciente'])
                                    print('║ Fecha Cita: '+ item['fechaCita'],',',item['horaCita'])
                                    print("╚══════════════════════════════════//")
                                    core.editarData('citas.json', diccCitas)
                                    os.system('pause')
                                    break

                                elif opt == '2':
                                    os.system('cls')
                                    item['fechaCita'] = input('Ingrese la nueva fecha de la cita (DD/MM/AAAA): ')
                                    if datetime.strptime(item['fechaCita'], "%d/%m/%Y"):
                                        if datetime.strptime(item['fechaCita'], "%d/%m/%Y").date() >= datetime.now().date():
                                            item['horaCita'] = input('Ingrese la nueva hora de la cita (ej.15:00): ')
                                            if datetime.strptime(item['horaCita'], "%j:%M"):
                                                os.system('cls')
                                                print("╔═══════════════════════════════════════════╗")
                                                print(f"║             CITA ACTUALIZADA              ║")
                                                print("╠═══════════════════════════════════════════╝")
                                                print('║ Nombre Paciente: '+ item['nombrePaciente'])
                                                print('║ Nueva Fecha Cita: '+ item['fechaCita'],',',item['horaCita'])
                                                print("╚══════════════════════════════════//")
                                                core.editarData('citas.json', diccCitas)
                                                os.system('pause')
                                                break
                                elif opt == '3':
                                    os.system('cls')
                                    item['nombrePaciente'] = input('Ingrese el nuevo nombre del Paciente: ').upper()
                                    item['fechaCita'] = input('Ingrese la nueva fecha de la cita (DD/MM/AAAA): ')
                                    if datetime.strptime(item['fechaCita'], "%d/%m/%Y"):
                                        if datetime.strptime(item['fechaCita'], "%d/%m/%Y").date() >= datetime.now().date():
                                            item['horaCita'] = input('Ingrese la nueva hora de la cita (ej.15:00): ')
                                            if datetime.strptime(item['horaCita'], "%j:%M"):
                                                os.system('cls')
                                                print("╔═══════════════════════════════════════════╗")
                                                print(f"║             CITA ACTUALIZADA              ║")
                                                print("╠═══════════════════════════════════════════╝")
                                                print('║ Nuevo Nombre Paciente: '+ item['nombrePaciente'])
                                                print('║ Nueva Fecha Cita: '+ item['fechaCita'],',',item['horaCita'])
                                                print("╚══════════════════════════════════//")
                                                core.editarData('citas.json', diccCitas)
                                                os.system('pause')
                                                break
                                else:
                                    os.system('cls')
                                    print('Error en opción ingresada')
                                    print('Volviendo al menú de citas')
                                    os.system('pause')

                                if encontradoFlag == False:
                                    print(f'No se encontró a ningún paciente por el nombre de {nomb.upper()}')
                                    os.system('pause')

                            except ValueError as e:
                                os.system('cls')
                                print('Valor ingresado no válido')
                                print('Volviendo al menú de citas')
                                os.system('pause')

            elif opcion == 4:
                if len(diccCitas['data']) == 0:
                    errorNoCitas()

                else:
                    nombrePaciente = input('Ingrese el nombre del paciente: ').upper()
                    for i,item in enumerate (diccCitas['data']):
                        if nombrePaciente == item['nombrePaciente']:
                            os.system('cls')
                            print("╔═════════════════════════════════════╗")
                            print("║            CITA ENCONTRADA          ║")
                            print("╠═════════════════════════════════════╝")
                            print('║ Está segur@ que deseala             ║')
                            print('║  eliminar la cita?                  ║')
                            print("╚═════════════════════════════════════╝")
                            if bool(input('Si(S) No(Enter)\n:)')):
                                os.system('cls')
                                citaBorrada = diccCitas['data'].pop(i)
                                print("╔═══════════════════════════════════════════╗")
                                print(f"║             CITA ELIMINADA                ║")
                                print("╠═══════════════════════════════════════════╝")
                                print('║ Nombre Paciente: '+ citaBorrada['nombrePaciente'])
                                print('║ Fecha de Cita: '+ citaBorrada['fechaCita'])
                                print('║ Hora de Cita: '+ citaBorrada['horaCita'])
                                print('║ Tipo de Consulta: '+ citaBorrada['tipoConsulta'])
                                print('║ Motivo: '+ citaBorrada['motivo'])
                                print("╚══════════════════════════════════//")
                                core.editarData('citas.json', diccCitas)
                                os.system('pause')
                            else:
                                print("╔═══════════════════════════════════════════╗")
                                print(f"║    SE CANCELO LA ELIMINACION DE CITA      ║")
                                print("╠═══════════════════════════════════════════╝")
                                print('Volviendo al menú')
                                os.system('cls')
            elif opcion == 5:
                os.system('clear')
                flagMenu = False
                print('Adiós!!')
mainMenu()

