import minecraft_launcher_lib
import os
import subprocess

user_windows = os.environ['USERNAME']
minecraft_directory = f"C://Users//{user_windows}//AppData//Roaming//.personlauncher"

current_max = 0

def set_status(status: str):
    print(status)

def set_progress(progress: int):
    if current_max != 0:
        print(f"{progress}/{current_max}")

def set_max(new_max: int):
    global current_max
    current_max = new_max

def install_minecraft():
    # Pedir al usuario que ingrese la versión de Minecraft que desea descargar
    minecraft_version = input('Ingrese la versión de Minecraft que desea descargar: ')

    # Devoluciones de llamada para mostrar el progreso de la instalación
    callback = {
        "setStatus": set_status,
        "setProgress": set_progress,
        "setMax": set_max
    }

    # Instalación de Minecraft
    minecraft_launcher_lib.install.install_minecraft_version(
        minecraft_version, minecraft_directory, callback=callback)
    print(f'Instalada la versión {minecraft_version}')

def install_forge():
    forge_ver = input('Dime la Versión de Forge: ')
    forfe = minecraft_launcher_lib.forge.find_forge_version(forge_ver)
    print(forfe)
    minecraft_launcher_lib.forge.install_forge_version(
        forfe, minecraft_directory)
    print(f'Instalado Forge {forfe}')

def ejecuta_mine(mine_user):
    forts = minecraft_launcher_lib.utils.get_installed_versions(
        minecraft_directory)
    for fort in forts:
        print(fort['id'])
    version = input('Versión: ')

    options = {
        'username': mine_user,
        'uuid': '',
        'token': '',
        "jvmArguments": ["-Xmx4G", "-Xms4G"],  # The jvmArguments
        "launcherVersion": "0.0.1",
    }

    # Ejecutar Minecraft
    minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(
        version, minecraft_directory, options)
    subprocess.run(minecraft_command)

def menu():
    mine_user = input('Nombre: ')
    print(f'Bienvenido al Luancher Personal {mine_user}\n\n')
    print('▐Instalar Minecraft (0). \n▐Instalar Forge (1)\n▐Ejecutar Minecraft (2)')
    formulario = input('Dime que deseas: ')
    if formulario == "0":
        install_minecraft()
    if formulario == "1":
        install_forge()
    if formulario == "2":
        ejecuta_mine(mine_user)

if __name__ == '__main__':
    menu()
