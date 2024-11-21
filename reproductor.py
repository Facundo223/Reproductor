import pygame
import tkinter as tk
from tkinter import messagebox
import configparser
import os

config = configparser.ConfigParser()
config.read('config.ini')


audio_file = config['settings']['audio_file']
volume = float(config['settings']['volume'])  

pygame.mixer.init()

class ReproductorAudio:
    def __init__(self, root):
        self.root = root
        self.is_playing = False

        
        self.root.title("Reproductor De Audio")
        self.root.geometry("300x200")

        
        pygame.mixer.music.set_volume(volume)

        
        self.play_button = tk.Button(self.root, text="Reproducir", command=self.play_audio)
        self.play_button.pack(pady=10)

        self.pause_button = tk.Button(self.root, text="Pausar", command=self.pause_audio)
        self.pause_button.pack(pady=10)

        self.stop_button = tk.Button(self.root, text="Detener", command=self.stop_audio)
        self.stop_button.pack(pady=10)

    def play_audio(self):
        """Reproducir la música"""
        if not self.is_playing:
            if os.path.exists(audio_file):  
                pygame.mixer.music.load(audio_file)
                pygame.mixer.music.play(loops=0, start=0.0)
                self.is_playing = True
                self.play_button.config(state="disabled")  
            else:
                messagebox.showerror("Error", f"El archivo de audio {audio_file} no se encuentra.")

    def pause_audio(self):
        """Pausar la música"""
        if self.is_playing:
            pygame.mixer.music.pause()
            self.is_playing = False
            self.play_button.config(state="normal")  

    def stop_audio(self):
        """Detener la música"""
        pygame.mixer.music.stop()
        self.is_playing = False
        self.play_button.config(state="normal")  


def main():
    
    root = tk.Tk()

    
    reproductor = ReproductorAudio(root)

    
    root.mainloop()

if __name__ == "__main__":
    main()

