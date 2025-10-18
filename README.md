# Библиотека ProjectBuilder
Библиотека **ProjectBuilder** была создана в целях упрощения создания небольших сайтов в краткие сроки. Эта библиотека имеет функционал, дающий неограниченный контроль над страницей.
## Project
### Класс **Project** принимает 2 параметра:
- Label *(Заголовок)*
- Describe *(Подзаголовок)*
### Методы и декораторы класса Project
- Page *декоратор*
- AddPng *(имя_страницы, путь_до_изображения)*
- AddChapter *(имя_страницы, заглавие, текст)*
- AddLink *(текст, ссылка)*
- SetCustom *(javascript код)*
<hr>
- **Page - декоратор функции создающий страницу**
- **AddPng - добавляет на страницу картинку**
- **AddChapter - добавляет на страницу главу, состоящую из заглавия и текста**
- **AddLink - добавляет ссылку**
- **SetCustom - назначает пользовательский _javascript_ код**
## Builder
### Класс **Project** не принимает параметров
### Методы и декораторы класса Builder
- SetCss *(интидификатор, ключ, значение)*
- BuildProject *(объект_класса_project, главная_функция, начальная_старница **по умолчанию home**)*
- **SetCss - функция позволяющая изменять css код элемента**
- **BuildProject - главная функция класса, служащая генератором html страницы на основе json'а класса project**

### Пример кода
``` python
from ProjectBuilder import Builder, Project

project = Project('Test', 'descr')
builder = Builder()

@project.Page
def home(this):
    project.AddPng(this, 'test.png')
    project.AddPng(this, 'test.png')
    project.AddPng(this, 'test.png')
    project.AddChapter(this, 'Introduction', 'text')
    project.AddLink(this, 'link', 'https://www.youtube.com/')

@project.Page
def info(this):
    project.AddPng(this, 'test.png')
    project.AddChapter(this, 'Info', 'text')
    project.AddLink(this, 'link', 'https://www.youtube.com/')

@builder.Generation
def index():
    [home, info]
    builder.SetCss('.chptname', 'backgroundColor', 'red')

builder.BuildProject(project, index, start_function='home')
```
# Установка библиотеки в окружение
``` cmd
 To be ccontinious...
```
