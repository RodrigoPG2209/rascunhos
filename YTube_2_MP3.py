import os

# Script simples para baixar um vídeo do YTube e converter o mesmo para .mp3.

link_video = input("Cole ou digite o link do vídeo que queira baixar o MP3: ")
os.system("youtube-dl --extract-audio --audio-format mp3 --prefer-ffmpeg " + link_video + " ")

# Comando de instação do pacote: sudo apt-get install youtube-dl ffmpeg