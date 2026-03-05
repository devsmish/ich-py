'''1. Воспроизведение мультимедиа
Создайте два класса:
Класс 1
AudioFileMixin — требует наличие поля
audio_tracks (список треков).
Метод play_audio() выводит:
Воспроизведение аудио для <НазваниеКласса>:
<название трека>
<название трека>
Класс 2
VideoFileMixin — требует наличие поля
video_files (список видео).
Метод play_video() выводит:
Воспроизведение видео для <НазваниеКласса>:
<название видео>
<название видео>
Если нужное поле отсутствует — выбрасывайте AttributeError.'''
class AudioFileMixin:
    def play_audio(self):
        if not hasattr(self, "audio_tracks"):
            raise AttributeError("Не выбраны audio_tracks")
        print(f"Воспроизведение аудио для {self.__class__.__name__}:")
        for track in self.audio_tracks:
            print(track)

class VideoFileMixin:
    def play_video(self):
        if not hasattr(self, "video_files"):
            raise AttributeError("Не выбраны video_files")
        print(f"Воспроизведение видео для {self.__class__.__name__}:")
        for video in self.video_files:
            print(video)

'''2. Устройства
Создайте два класса:
● MediaPlayer — поддерживает только аудио. Принимает список треков.
● Laptop — поддерживает аудио и видео. Принимает списки треков и видео.
Проверьте работу классов, вызвав методы воспроизведения.
Данные:
tracks = ["track1.mp3", "track2.mp3"]
movies = ["movie.mp4", "trailer.mov"]
Пример вывода:
Воспроизведение аудио для MediaPlayer:
track1.mp3
track2.mp3
Воспроизведение аудио для Laptop:
track1.mp3
track2.mp3
Воспроизведение видео для Laptop:
movie.mp4
trailer.mov'''
class MediaPlayer(AudioFileMixin):
    def __init__(self, audio_tracks):
        self.audio_tracks = tracks

class Laptop(AudioFileMixin, VideoFileMixin):
    def __init__(self, audio_tracks, video_files):
        self.audio_tracks = tracks
        self.video_files = movies

tracks = ["track1.mp3", "track2.mp3"]
movies = ["movie.mp4", "trailer.mov"]

music = MediaPlayer(tracks)
movie = Laptop(tracks, movies)
try:
    music.play_audio()

    movie.play_audio()
    movie.play_video()
except AttributeError as err:
    print(err)