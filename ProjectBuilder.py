import webbrowser

class Project:

    def __init__(self, label : str, describe : str):
        self.json = {"label": label, "describe": describe, "data": {}, "custom": 'function custom() {}'}

    def Page(self, func):
        self.json['data'][func.__name__.replace(' ', '')] = {"png": [], "chapter": [], "link": []}
        return func(func.__name__)
    
    def AddPng(self, page_name : str, src : str):
        self.json['data'][page_name]['png'].append({"src": src})

    def AddChapter(self, page_name : str, label : str, text : str):
        self.json['data'][page_name]['chapter'].append({"label": label, "text": text})

    def AddLink(self, page_name : str, text : str, href : str):
        self.json['data'][page_name]['link'].append({"href": href, "text": text})

    def SetCustom(self, code : str):
        self.json['custom'] = code

class Builder:
    
    def __init__(self):
        self.css = '#label { padding-left:10%; margin-bottom:0px; margin-top:0px; font-size:650%; } #sublabel { padding-left:10%; margin-bottom:0px; margin-top:0px; font-size:450%; } #menu { text-align:center; } #png { padding-top:1%; text-align:center; } #link { text-align:center; } button { font-size:300%; } .chptname { text-align:center; font-size:350%; } .chptdescribe { text-align:justify; padding-left:15%; padding-right:15%; font-size:250%; } a { font-size:200%; } img { height:200px; width:300px; }'
        self.javascript = 'function Page(ipng, ichapter, ilink){return {png:ipng,chapter:ichapter,link:ilink}} var curr_page; $page_data$ function setPage(data){const png=document.getElementById("png"),chapter=document.getElementById("chapter"),link=document.getElementById("link");let innerHTML="";for(let i=0;i<data.png.length;i++){innerHTML+=`<img src="${data.png[i]}">`}png.innerHTML=innerHTML;innerHTML="";for(let i=0;i<data.chapter.length;i++){innerHTML+=`<h1 class="chptname">${data.chapter[i][0]}</h1>`;innerHTML+=`<h2 class="chptdescribe">${data.chapter[i][1]}</h2>`}chapter.innerHTML=innerHTML;innerHTML="";for(let i=0;i<data.link.length;i++){innerHTML+=`<a href="${data.link[i][1]}">${data.link[i][0]}</a>`}link.innerHTML=innerHTML;curr_page=data;$cssswap$}$button_click$ $custom$ custom(); $cssswap$'
        self.html = '<!DOCTYPE html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><style>$css$</style><title></title></head><body><h1 id="label">$label$</h1><h2 id="sublabel">$sublabel$</h2><hr><div id="menu">$menu$</div><div id="png"></div><br><div id="chapter"></div><br><element id="custom"></element><br><div id="link"></div><script type="text/javascript">$javascript$</script></body></html>'
        self.flname, self.cssswaps = '', ''

    def SetCss(self, idifer: str, key : str, item : str):
        if idifer.find('.') != -1:
            self.cssswaps += f'document.querySelectorAll("{idifer}").forEach(element => [element.style.{key}="{item}";]);'.replace('[', '{').replace(']', '}')
        elif idifer.find('#') != -1:
            self.cssswaps += f'document.querySelector("{idifer}").style.{key}="{item}";'
        else:
            self.cssswaps += f'document.querySelectorAll("{idifer}").forEach(element => [element.style.{key}="{item}";]);'.replace('[', '{').replace(']', '}')

    def _fileFormat(self):
        open(f'{self.flname}.html', 'w', encoding='utf-8').write(self.html)
        webbrowser.open(f'{self.flname}.html')

    def BuildProject(self, project : Project, func, start_function : str = 'home'):
        func()

        output_arrays = ''

        self.html = self.html.replace('$label$', project.json['label'])
        self.html = self.html.replace('$sublabel$', project.json['describe'])

        self.html = self.html.replace('$css$', self.css)

        for page in list(project.json['data'].keys()):
            png_list = []
            for img in project.json['data'][page]['png']:
                png_list.append(img['src'])

            chapter_list = []
            for chapter in project.json['data'][page]['chapter']:
                chapter_list.append([chapter['label'], chapter['text']])

            link_list = []
            for chapter in project.json['data'][page]['link']:
                link_list.append([chapter['text'], chapter['href']])

            output_arrays += f'{page}_page = Page({png_list}, {chapter_list}, {link_list});'.replace(']', ')').replace('[', 'new Array(')
        self.javascript = self.javascript.replace('$page_data$', output_arrays)

        menu_div = ''
        for page in list(project.json['data'].keys()):
            menu_div += f'<button id="{page}_btn">{page}</button>'
        self.html = self.html.replace('$menu$', menu_div)

        event_listener = ''
        for page in list(project.json['data'].keys()):
            event_listener += 'document.getElementById("$page$_btn").addEventListener("click", function() {setPage($page$_page)});'.replace('$page$', page)

        event_listener += f'setPage({start_function}_page);'

        self.javascript = self.javascript.replace('$button_click$', event_listener)
        self.javascript = self.javascript.replace('$custom$', project.json["custom"])
        self.javascript = self.javascript.replace('$cssswap$', self.cssswaps)

        self.html = self.html.replace('$javascript$', self.javascript)

        self._fileFormat()

    def Generation(self, func):
        self.flname = func.__name__
        return func