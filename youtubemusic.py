import pygame
from googleapiclient.discovery import build
from pytube import YouTube
from moviepy.editor import AudioFileClip

# Variables globales
paused = False

# Función para buscar y reproducir música en YouTube
def reproducir_musica(query):
    api_key = "AIzaSyASVnIWxXJKhYS6DqN8XynC6H3y22vBd-M"  # Reemplaza con tu propia API key
    youtube = build('youtube', 'v3', developerKey=api_key)
    
    # Realizar la búsqueda en YouTube
    search_response = youtube.search().list(
        q=query,
        part='id',
        maxResults=1,
        type='video'
    ).execute()
    
    # Obtener el ID del video de la primera coincidencia
    video_id = search_response['items'][0]['id']['videoId']
    
    # Construir la URL del video
    video_url = f"https://www.youtube.com/watch?v={video_id}"
    
    # Descargar el audio del video en formato MP3 y reproducirlo
    descargar_audio(video_url)

# Función para descargar el audio en formato MP3 desde YouTube
def descargar_audio(video_url):
    yt = YouTube(video_url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    if audio_stream:
        audio_path = "./audio/" + audio_stream.default_filename
        audio_stream.download("./audio/")
        mp3_path = audio_path[:-4] + ".mp3"
        convertir_a_mp3(audio_path, mp3_path)
        reproducir_audio(mp3_path)
    else:
        print("No se encontró ninguna transmisión de audio para este video.")

# Función para convertir el archivo de audio a formato MP3
def convertir_a_mp3(audio_path, mp3_path):
    audio = AudioFileClip(audio_path)
    audio.write_audiofile(mp3_path)

# Función para reproducir el audio
def reproducir_audio(ruta):
    pygame.mixer.init()
    pygame.mixer.music.load(ruta)
    pygame.mixer.music.play()

# Función principal
def main():
    global paused
    # Solicitar al usuario el nombre del artista de la canción
    artista = input("Introduce el nombre del artista de la canción: ")
    cancion = input("Introduce el nombre de la canción: ")
    query = f"{artista} {cancion}"
    reproducir_musica(query)
    
    while True:
        opcion = input("Pulsa 'p' para pausar, 'r' para reanudar, o 'q' para detener: ")
        if opcion.lower() == 'p':
            if not paused:
                pygame.mixer.music.pause()
                paused = True
        elif opcion.lower() == 'r':
            if paused:
                pygame.mixer.music.unpause()
                paused = False
        elif opcion.lower() == 'q':
            pygame.mixer.music.stop()
            break
        else:
            print("Opción no válida. Por favor, selecciona 'p', 'r' o 'q'.")

if __name__ == "__main__":
    main()

