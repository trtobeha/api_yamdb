# API_YAMDB — база данных и REST API с произведениями, отзывами к ним и комментариями.
# Финальный проект курса "API: интерфейс взаимодействия программ"


Проект YaMDb собирает отзывы (Review) зарегистрированных пользователей на произведения(Title).Произведения делятся на категории(Categories).Создание новых категорий доступно только *Администраторам*. К отзывам на произведения можно оставлять комментарии(Comment).
Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку. На основании оценок в отзывах высчитывается средняя оценка произведения. 

## Пользовательские роли и права доступа
- **Аноним** — может просматривать описания произведений, читать отзывы и комментарии.
- **Аутентифицированный пользователь (user)** — может читать всё, как и Аноним, может публиковать отзывы и ставить оценки произведениям (фильмам/книгам/песенкам), может комментировать отзывы; может редактировать и удалять свои отзывы и комментарии, редактировать свои оценки произведений. Эта роль присваивается по умолчанию каждому новому пользователю.
- **Модератор (moderator)** — те же права, что и у Аутентифицированного пользователя, плюс право удалять и редактировать любые отзывы и комментарии.
- **Администратор (admin)** — полные права на управление всем контентом проекта. Может создавать и удалять произведения, категории и жанры. Может назначать роли пользователям.
- **Суперюзер Django** обладает правами администратора, пользователя с правами admin. Даже если изменить пользовательскую роль суперюзера — это не лишит его прав администратора. Суперюзер — всегда администратор, но администратор — не обязательно суперюзер.
## Установка:
### Склонируйте репозиторий на локальную машину:
`git clone https://github.com/trtobeha/api_yamdb.git`
### Установите виртуальное окружение:
`python3 -m venv venv`
### Активируйте виртуальное окружение:
`venv\Scripts\activate.bat` - для Windows\
`source venv/bin/activate` - для MacOS / Linux
### Установите зависимости:
`pip install -r requirements.txt`
### Запустите локальный сервер:
`python api_yamdb/manage.py runserver 8000`
### Перейдите в документацию проекта:
`http://127.0.0.1:8000/redoc/`

## Над проектом работали:
[Владимир Подъяков](https://github.com.trtobeha "Ссылка на профиль GitHub")\
[Максим Чурочкин](https://github.com/MChurochkin "Ссылка на профиль GitHub")\
[Василий Лапко](https://github.com/VasiliyLyr "Ссылка на профиль GitHub")