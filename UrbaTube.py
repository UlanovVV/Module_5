import re
import time


"""
Создаем класс пользователя. Указываем: ник, пароль, возраст.
"""


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname

"""
Создаем класс видео. Указываем: заголовок, продолжительность, секунда остановкиЮ ограничение по возрасту.
"""


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


'''
Создаем класс Уртуба).
'''


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == password:
                self.current_user = user
                print(f"Вход выполнен успешно, {self.current_user.nickname}!")
                return True
        print("Неверный логин или пароль.")
        return False

    def register(self, nickname, password, age):
        for user in self.users:
            if nickname == user.nickname:
                return print(f'Пользователь {nickname} уже существует')
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for movie in videos:
            if not any(existing_movie.title == movie.title for existing_movie in self.videos):
                self.videos.append(movie)

    def get_videos(self, word):
        found_videos = []
        for video in self.videos:
            if re.search(word, video.title, re.IGNORECASE):
                found_videos.append(video.title)
        return found_videos

    def watch_video(self, title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return
                else:
                    video.time_now = 0
                    while video.time_now < video.duration:
                        print(f"Просмотр: {video.time_now} секунда")
                        video.time_now += 1
                        time.sleep(1)
                    print("Конец видео")
                    return


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
