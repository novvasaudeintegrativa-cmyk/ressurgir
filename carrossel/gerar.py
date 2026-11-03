"""Gera os slides do carrossel (1080 x 1350) a partir de HTML + Chrome.

Uso:  python carrossel/gerar.py
Saída: carrossel/slide-01.png ... slide-14.png
"""
import re
import subprocess
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PASTA = RAIZ / "carrossel"
FONTE = PASTA / "fonte"
CHROME = r"C:/Program Files/Google/Chrome/Application/chrome.exe"
FONTE.mkdir(exist_ok=True)

index = (RAIZ / "index.html").read_text(encoding="utf-8")
sprite = re.search(r'<svg width="0" height="0".*?</svg>\n', index, re.S).group(0)
bloco = re.search(r"const TEXTOS = \[(.*?)\];", index, re.S).group(1)
TEXTOS = re.findall(r'"((?:[^"\\]|\\.)*)"', bloco)
NOMES = [
    "Genética e epigenética", "Conflitos emocionais e neurotransmissores", "Geopatologias e toxinas ambientais",
    "Hidratação e qualidade da água", "Metais tóxicos", "Saúde gastrointestinal",
    "Fungos, parasitas, vírus, bactérias e vermes", "Carências nutricionais e gasto energético",
    "Sistema circulatório e imunológico", "Saúde mitocondrial", "Tríade metabólica e hormonal",
    "Conflitos sistêmicos, história familiar e espiritualidade",
]
assert len(TEXTOS) == 12 and len(NOMES) == 12
TOTAL = 14
USAR_ICONES = False  # mude para True para voltar os ícones dos pilares
USAR_FOTOS = False  # mude para True quando as fotos dos slides de imagem estiverem prontas

# recortes (deslocamento vertical em % da cena mobile, zoom) para os slides de imagem
RECORTES = {1: (14, 1.0), 3: (0, 1.15), 5: (38, 1.1), 7: (52, 1.2), 9: (100, 1.0), 11: (30, 1.35)}

CSS = """
*{box-sizing:border-box;margin:0}
body{width:1080px;height:1350px;position:relative;overflow:hidden;font-family:Outfit,sans-serif;color:#fff;background:#00454d}
.fundo{position:absolute;inset:0}
.num{position:absolute;right:-30px;bottom:80px;font-weight:800;font-size:640px;line-height:.8;letter-spacing:-.05em;color:#fff;opacity:.07}
.topo{position:absolute;left:84px;right:84px;top:190px}
.logo-topo{position:absolute;left:84px;right:84px;top:62px;display:flex;align-items:center;gap:16px}
.logo-topo img{width:70px;height:70px}
.logo-topo span{font-size:34px;font-weight:700;line-height:1.05;letter-spacing:-.01em}
.logo-topo span b{color:#00dcc0}
.logo-topo span small{display:block;font-size:17px;font-weight:300;letter-spacing:.12em;text-transform:uppercase;opacity:.85;margin-top:4px}
.chip{display:inline-block;border:2px solid #00dcc0;border-radius:99px;padding:10px 28px;font-size:28px;font-weight:400;color:#00dcc0;background:rgba(0,38,44,.45)}
h1{margin-top:34px;font-weight:800;line-height:1.02;letter-spacing:-.025em;text-shadow:0 4px 30px rgba(0,25,30,.55)}
h1 em{font-style:normal;color:#00dcc0}
.icone{position:absolute;left:84px;width:150px;height:150px;border-radius:50%;border:3px solid #00dcc0;background:rgba(0,50,56,.85);display:grid;place-items:center;color:#00dcc0}
.icone svg{width:78px;height:78px;fill:none;stroke:currentColor;stroke-width:1.6;stroke-linecap:round;stroke-linejoin:round}
.corpo{position:absolute;left:84px;right:84px;font-size:46px;line-height:1.38;font-weight:300}
.rodape{position:absolute;left:84px;right:84px;bottom:66px;display:flex;align-items:center;justify-content:space-between}
.marca{display:flex;align-items:center;gap:16px}
.marca img{width:64px;height:64px}
.marca span{font-size:30px;font-weight:700;line-height:1.1;letter-spacing:-.01em}
.marca span b{color:#00dcc0}
.marca span small{display:block;font-size:17px;font-weight:300;letter-spacing:.2em;text-transform:uppercase;opacity:.8;margin-top:4px}
.dir{display:flex;align-items:center;gap:22px;font-size:26px;font-weight:300;opacity:.9}
.seta{width:48px;height:48px;border-radius:50%;background:#00dcc0;color:#00262c;display:grid;place-items:center;font-size:24px;font-weight:700}
"""


def pagina(corpo_html, fundo_css, extra_css=""):
    return (
        '<!doctype html><meta charset="utf-8">'
        '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700;800&display=swap">'
        f"<style>{CSS}{extra_css}</style>{sprite}"
        f'<div class="fundo" style="{fundo_css}"></div>{corpo_html}'
    )


LOGO = ('<div class="logo-topo"><img src="file:///' + str(RAIZ / "assets/logo-marca.svg").replace("\\", "/") + '">'
        '<span>Ressurgir<b>:</b><small>Os 12 Pilares do Terreno Biológico</small></span></div>')


def rodape(n, ultimo=False):
    if ultimo:
        return f'<div class="rodape" style="justify-content:flex-end"><div class="dir">{n:02d}/{TOTAL}</div></div>'
    return f'<div class="rodape" style="justify-content:flex-end"><div class="dir">{n:02d}/{TOTAL}<div class="seta">&rarr;</div></div></div>'


def tamanho_titulo(nome):
    n = len(nome)
    return 108 if n <= 22 else 92 if n <= 34 else 76 if n <= 46 else 64


def destacar(nome):
    palavras = nome.split(" ")
    if len(palavras) == 1:
        return f"<em>{nome}</em>"
    return " ".join(palavras[:1]) + " <em>" + " ".join(palavras[1:]) + "</em>"


def cena(y_pct, zoom):
    img = (RAIZ / "assets/cena-mobile-final.jpg").as_posix()
    # a cena é 9:16; o recorte 4:5 mostra uma janela vertical dela
    return f"url('file:///{img}') center {y_pct}%/ {int(100 * zoom)}% auto no-repeat"


slides = []

# 01 capa
foto = (RAIZ / "assets/cena-mobile-final.jpg").as_posix()
corpo = (
    '<div class="topo" style="text-align:center;top:70px"><div style="font-size:54px;font-weight:700;letter-spacing:-.02em">Ressurgir<span style="color:#00dcc0">:</span></div>'
    
    '<div style="margin-top:34px"><span class="chip">Terreno Biológico</span></div>'
    '<h1 style="font-size:104px;font-weight:300;margin-top:26px">Os <b style="font-weight:800;color:#00dcc0">12 pilares</b><br>do terreno biológico</h1></div>'
    '<div class="rodape" style="justify-content:flex-end"><div class="dir">Deslize<div class="seta">&rarr;</div></div></div>'
)
fundo = (f"background:linear-gradient(180deg,rgba(0,38,44,.95) 0,rgba(0,38,44,.8) 24%,rgba(0,38,44,.25) 40%,rgba(0,38,44,0) 48%),linear-gradient(0deg,rgba(0,30,35,.7) 0,rgba(0,30,35,0) 20%),"
         f"url('file:///{foto}') center 150px/ 1080px auto no-repeat,#5aa9a6;")
slides.append(pagina(corpo, fundo))

for i in range(12):
    n = i + 2
    nome, texto = NOMES[i], TEXTOS[i]
    zona = "Na superfície" if i < 4 else "Na profundidade"
    fs = tamanho_titulo(nome)
    cab = (f'<div class="topo"><span class="chip">Pilar {i + 1:02d} · {zona}</span>'
           f'<h1 style="font-size:{fs}px">{destacar(nome)}</h1></div>')
    icone = f'<div class="icone" style="bottom:210px"><svg viewBox="0 0 24 24"><use href="#i{i + 1}"/></svg></div>'
    if (i + 1) % 2:  # ímpares: slide de imagem
        y, z = RECORTES[i + 1]
        if USAR_FOTOS:
            fundo = (f"background:linear-gradient(180deg,rgba(0,38,44,.88) 0,rgba(0,38,44,.45) 36%,rgba(0,38,44,0) 58%),"
                     f"linear-gradient(0deg,rgba(0,30,35,.85) 0,rgba(0,30,35,0) 30%),{cena(y, z)},#00454d;")
            vazio = ""
        else:  # sem foto: fundo liso com o ícone grande, pronto para receber a imagem depois
            fundo = "background:linear-gradient(200deg,#00595d 0%,#00454d 55%,#003a41 100%);"
            vazio = (f'<div style="position:absolute;left:0;right:0;top:470px;display:grid;place-items:center;color:#00dcc0;opacity:.16">'
                     f'<svg viewBox="0 0 24 24" width="420" height="420" fill="none" stroke="currentColor" stroke-width=".9" stroke-linecap="round" stroke-linejoin="round"><use href="#i{i + 1}"/></svg></div>')
        sub = (f'<div class="corpo" style="bottom:210px;font-size:40px;max-width:760px;left:260px">{texto}</div>')
        if not USAR_ICONES:
            vazio, icone = "", ""
            sub = sub.replace("left:260px", "left:84px").replace("max-width:760px", "max-width:900px")
        slides.append(pagina(LOGO + vazio + cab + icone + sub + rodape(n), fundo))
    else:  # pares: slide de texto
        fundo = "background:linear-gradient(160deg,#00454d 0%,#00595d 55%,#007a78 100%);"
        grande = f'<div class="num">{i + 1:02d}</div>'
        glow = '<div style="position:absolute;left:-220px;top:-220px;width:760px;height:760px;border-radius:50%;background:radial-gradient(circle,rgba(0,220,192,.4),rgba(0,220,192,0) 70%)"></div>'
        corpo_txt = (f'<div class="icone" style="top:{300 if fs < 100 else 340}px"></div>')
        bloco = (f'<div class="icone" style="top:600px"><svg viewBox="0 0 24 24"><use href="#i{i + 1}"/></svg></div>'
                 f'<div class="corpo" style="top:800px;font-size:48px">{texto}</div>')
        if not USAR_ICONES:
            bloco = f'<div class="corpo" style="top:640px;font-size:54px">{texto}</div>'
        slides.append(pagina(glow + grande + LOGO + cab + bloco + rodape(n), fundo))

# 14 final
seta_b = '<svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="#00262c" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 4v15M6 13l6 6 6-6"/></svg>'
corpo = (
    '<div style="position:absolute;left:-220px;top:-220px;width:760px;height:760px;border-radius:50%;background:radial-gradient(circle,rgba(0,220,192,.4),rgba(0,220,192,0) 70%)"></div>'
    '<div class="topo" style="top:300px"><span class="chip">Os 12 pilares do terreno biológico</span>'
    '<h1 style="font-size:96px;font-weight:300">Olhe além<br>da <b style="font-weight:800;color:#00dcc0">superfície</b></h1>'
    '<div style="margin-top:34px;font-size:40px;font-weight:300;line-height:1.4;opacity:.9">Ressurgir: Os 12 Pilares do Terreno Biológico</div></div>'
    f'<div style="position:absolute;left:84px;bottom:230px;display:flex;align-items:center;gap:18px"><div class="seta" style="width:56px;height:56px">{seta_b}</div>'
    '<div style="font-size:34px;font-weight:600;letter-spacing:-.01em">Toque em <span style="color:#00dcc0">saiba mais</span></div></div>'
    + rodape(14, ultimo=True)
)
corpo = LOGO + corpo
slides.append(pagina(corpo, "background:linear-gradient(160deg,#00454d 0%,#00595d 55%,#007a78 100%);"))

assert len(slides) == TOTAL
for k, html in enumerate(slides, 1):
    arq = FONTE / f"slide-{k:02d}.html"
    arq.write_text(html, encoding="utf-8")
    saida = PASTA / f"slide-{k:02d}.png"
    subprocess.run([CHROME, "--headless", "--disable-gpu", "--hide-scrollbars", "--virtual-time-budget=10000",
                    "--window-size=1080,1350", f"--screenshot={saida.as_posix()}", arq.as_uri()],
                   capture_output=True)
    print("ok", saida.name)
