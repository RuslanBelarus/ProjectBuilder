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
### Назначение
- **Page - декоратор функции создающий страницу**
- **AddPng - добавляет на страницу картинку**
- **AddChapter - добавляет на страницу главу, состоящую из заглавия и текста**
- **AddLink - добавляет ссылку**
- **SetCustom - назначает пользовательский _javascript_ код**
## Builder
### Класс **Project** не принимает параметров
### Методы и декораторы класса Builder
- SetCss *(интидификатор, ключ, значение)*
- AddFont *(фамилия_шрифта, путь_к_шрифту)*
- BuildProject *(объект_класса_project, главная_функция, начальная_старница **по умолчанию home**)*
### Назначение
- **SetCss - функция позволяющая изменять css код элемента**
- **BuildProject - главная функция класса, служащая генератором html страницы на основе json'а класса project**
- **AddFont - функция позволяющая загружать шрифты**
# Пример Проекты
``` python
from ProjectBuilder import Builder, Project

project = Project('Japan Delicious', 'delicious, trend and history')
builder = Builder()

@project.Page
def Dishes(this):
    project.AddPng(this, 'ramen.png')
    project.AddPng(this, 'sushi.png')
    project.AddPng(this, 'udon.png')
    project.AddChapter(this, 'Sushi, Sashimi, and Rolls', 'Sushi consists of pieces of fish or seafood laid on a small ball of rice. Sashimi is thinly sliced raw fish served without rice, accompanied by soy sauce and wasabi. In rolls (norimaki), seaweed is used with fillings inside, such as avocado or cucumber. Popular types of sushi include nigiri, maki, and unagi. The use of the freshest fish is the key secret to excellent sashimi and sushi. In Japan, there are many specialized restaurants where chefs prepare sushi with impeccable technique. The flavor of sushi is highlighted with soy sauce, ginger, and wasabi. Rolls have gained popularity abroad due to their variety of fillings and visual appeal. In Japanese culture, sushi is eaten carefully with chopsticks or hands. Many Japanese prefer to eat sushi and sashimi for a light and healthy lunch or dinner.')
    project.AddChapter(this, 'Warm Dishes and Snacks', 'Yakitori is a Japanese dish of grilled meat or fish, usually served with sauce. Tempura consists of vegetables and seafood fried in batter, often served with dipping sauce. Yakisoba is fried noodles with vegetables, meat, and sauce, a popular street food. Tofu and miso soup are important components of daily Japanese diet. Kabayaki are small grilled seafood snacks. Japanese cuisine widely uses steamed and grilled dishes. The focus is on balancing flavors, textures, and beautiful presentation. Restaurants carefully select ingredients for each dish. Traditional snacks can be both hot and cold, depending on the season. These dishes help convey the richness and diversity of Japanese gastronomy.')
    project.AddChapter(this, 'Ramen and Other Noodle Dishes', 'Ramen is a dish made of broth, noodles, meat, and vegetables. Originating in China, ramen became widespread in Japan from the 19th century. There are dozens of ramen varieties in Japan, depending on the region. Broth is mainly based on soy sauce, miso, or fatty stock. Ramen noodles are typically made from wheat flour, water, salt, and kansui (alkaline water). Japan also has udon and soba — thick and thin noodles respectively. Each region has unique recipes for preparing noodles and broth. Ramen is often served with toppings such as egg, green onions, and pieces of meat. In Japan, ramen is considered a national dish loved by all social groups. Quick ramen cafes and restaurants make this dish accessible to all enthusiasts.')
    project.AddLink(this, 'youtube', 'https://www.youtube.com/@Lixpan4ik')

@project.Page
def History(this):
    project.AddPng(this, 'ramen.png')
    project.AddPng(this, 'sushi.png')
    project.AddPng(this, 'udon.png')
    project.AddChapter(this, 'Origins and Development', 'Japanese cuisine was formed based on ancient traditions and influences from China and Korea. In ancient times, the main products were rice, fish and seafood, as well as vegetables. During the Edo period (17th–19th centuries), cuisine became more sophisticated with the development of restaurants. The tradition of sushi began as a method of preserving fish using vinegar. In traditional Japanese culture, the harmonious combination of flavors and the aesthetics of presentation are important. In the 20th century, Japanese cuisine opened up to the world through the development of international restaurants. In modern Japan, ancient recipes are preserved and passed down through generations. After World War II, Japanese cuisine gained popularity abroad thanks to culinary export. Technology and globalization contributed to adapting Japanese dishes to different tastes. The formation of Japanese gastronomic culture is connected with a combination of tradition and innovation.')
    project.AddChapter(this, 'Influence of Natural Conditions', 'Japan’s geographical location determined the abundance of seafood in its cuisine. Climate varies by region, which reflects in the diversity of ingredients. In northern regions, heavier and more hearty food is popular, for example, stews. In southern areas, lighter and fresher dishes, such as sushi and salads, are preferred. Severe winters stimulated the development of preservation and salting techniques. Water resources allowed the development of a rich seafood cuisine with a variety of fish and crustaceans. The love for nature and seasonal products is a key feature of Japanese culinary art. Japanese people highly appreciate seasonal delicacies, so menus change depending on the time of year. The aesthetics of Japanese cuisine are related to depicting natural scenes and seasonal symbols. Despite internal differences, all regions are united by respect for product freshness.')
    project.AddChapter(this, 'Traditional Values and Rituals', 'In Japanese culture, observing rituals is important when serving food. Traditional dishes are often served in a specific order, for example, appetizers, main courses, and desserts. A key part is the respect for ingredients and the natural taste of the products. The serving of food is accompanied by certain gestures and words of gratitude. The traditional Japanese festival Obon is accompanied by special dishes and rituals. In Japanese culture, the tea ceremony occupies a special place, associated with serving tea and snacks. Table manners require delicacy and neatness. Traditional Japanese dishes are often served with sake, Chinese tea, or green tea. An important aspect is the use of natural colors and decorations in table setting. All this helps preserve cultural heritage and the unique identity of Japanese cuisine.')
    project.AddLink(this, 'github', 'https://github.com/RuslanBelarus/ProjectBuilder/tree/main')

@project.Page
def Trends(this):
    project.AddPng(this, 'ramen.png')
    project.AddPng(this, 'sushi.png')
    project.AddPng(this, 'udon.png')
    project.AddChapter(this, 'Modernization and Adaptation of Traditions', 'In the modern era, Japanese cuisine is actively modernizing while preserving traditional principles. Many chefs experiment with new ingredients and techniques, creating fusion dishes that combine Japanese traditions with global culinary experience. Restaurants in Japanese cities feature modern designs and menus aimed at an international audience. The popularity of healthy eating stimulates the development of dishes focusing on naturalness and minimal processing. Modern Japanese cuisine strives for innovation but pays great attention to aesthetics and flavor balance rooted in historical traditions.')
    project.AddChapter(this, 'Spread of Japanese Dishes Abroad', 'Thanks to its uniqueness and health benefits, Japanese cuisine has gained wide popularity worldwide. Sushi and ramen restaurants open in major metropolitan areas, where menus adapt to local tastes while retaining core culinary principles. International festivals and master classes popularize Japanese gastronomy and encourage cultural exchange. Japanese dishes are in demand among health-conscious people and gourmets. Through international culinary schools, young chefs learn Japanese techniques and traditions and then apply them in various countries. This contributes to the formation of a new level of culinary art and the spread of Japanese cultural heritage.')
    project.AddChapter(this, 'Influence on World Gastronomy and Public Catering', 'Japanese cuisine has had a significant influence on world gastronomy, especially in healthy eating and visual presentation of dishes. The principles of seasonality and harmony of ingredients have inspired many chefs worldwide. Serving formats such as bento and timed menus have become widespread in restaurants and cafes. The concept of umami — the fifth taste discovered by Japanese scientists — has formed a new approach to balancing flavor combinations. In public catering, Japan actively develops automated cafes and fast-service systems, setting an example for other countries. Overall, Japanese gastronomic culture contributes to shaping new standards of quality, aesthetics, and health in global cuisine.')
    project.AddLink(this, 'fonts', 'https://fonts-online.ru/fonts')

@project.Page
def Testing(this):
    pass

js_code = '''
var i = 0;
function click() {
    i++;
    document.getElementById('text').textContent = i;
}
function load() {
    document.getElementById('custom').innerHTML = `<div align="center"><h1 id="text">${i}</h1><br><button id="btn">click</button></div>`;
    document.getElementById('btn').addEventListener('click', function () { click() })
}

document.getElementById('Testing_btn').addEventListener('click', function () { load() })
'''

@builder.Generation
def index():
    [History, Dishes, Trends, Testing]

    project.SetCustom(js_code)

    builder.AddFont('Schoolbook', 'Schoolbook.ttf')
    builder.AddFont('Amrus', 'amrys.oft')

    builder.SetCss('#label', 'backgroundColor', 'smokewhite')
    builder.SetCss('#sublabel', 'backgroundColor', '#f01616')

    builder.SetCss('#sublabel', 'color', 'white')

    builder.SetCss('.chptname', 'fontFamily', 'almys')

    builder.SetCss('.chptdescribe', 'paddingLeft', '15%')
    builder.SetCss('.chptdescribe', 'paddingRight', '15%')
    builder.SetCss('.chptdescribe', 'fontSize', '25px')
    
    builder.SetCss('button', 'fontSize', '350%')
    builder.SetCss('body', 'fontFamily', 'Schoolbook')
    builder.SetCss('button', 'fontFamily', 'almys')
    builder.SetCss('button', 'marginTop', '2%')
    builder.SetCss('button', 'fontSize', '390%')

    builder.SetCss('img', 'padding', '2%')

builder.BuildProject(project, index, start_function='Dishes')
```
# Установка библиотеки в окружение
``` cmd
 To be ccontinious...
```
