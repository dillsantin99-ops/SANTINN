"""Gera os carrosséis 'Casos reais' da SMD no padrão visual servicos-v3 (1080x1350)."""
import base64, pathlib
from playwright.sync_api import sync_playwright

BASE = pathlib.Path(__file__).parent
SRC = BASE / "src"
ASSETS = BASE.parent.parent / "assets"
OUT = BASE

def b64(p):
    p = pathlib.Path(p)
    mime = "image/svg+xml" if p.suffix == ".svg" else "image/jpeg" if p.suffix in (".jpg", ".jpeg") else "image/png"
    return f"data:{mime};base64," + base64.b64encode(p.read_bytes()).decode()

SIMB = b64(ASSETS / "simbolo-branco.svg")
SIMB_COR = b64(ASSETS / "simbolo.svg")
LOGO_BR = b64(SRC / "logo_smd_slate.png")

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
*{margin:0;padding:0;box-sizing:border-box}
body{width:1080px;height:1350px;font-family:Poppins,sans-serif;overflow:hidden}
.cover{position:relative;width:1080px;height:1350px;background:#222}
.cover img.bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.cover .grad{position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,0) 35%,rgba(205,60,62,.55) 60%,rgba(200,58,60,.96) 82%)}
.cover .tag{position:absolute;top:56px;left:56px;background:#fff;color:#C8383C;font-weight:700;font-size:26px;letter-spacing:2px;padding:12px 22px;border-radius:6px}
.cover .tit{position:absolute;left:0;bottom:250px;background:#D9474A;color:#fff;font-weight:600;font-size:66px;padding:10px 26px 10px 26px;line-height:1.15}
.cover .sub{position:absolute;left:26px;bottom:170px;color:#fff;font-weight:300;font-size:44px}
.cover .ic{position:absolute;left:50%;bottom:48px;width:64px;transform:translateX(-50%)}
.col{width:1080px;height:1350px;background:#fff;position:relative;padding:70px 64px}
.col h1{font-weight:300;font-size:58px;color:#365A68;line-height:1.1}
.col h1 b{display:block;font-weight:700;color:#D9474A}
.grid{margin-top:50px;display:grid;gap:14px}
.grid .c{position:relative;overflow:hidden;border-radius:4px}
.grid img{width:100%;height:100%;object-fit:cover;display:block}
.grid .lb{position:absolute;left:14px;bottom:14px;background:#D9474A;color:#fff;font-size:22px;font-weight:600;padding:6px 14px;border-radius:4px}
.grid .lb.ok{background:#2E8B57}
.col .dots{position:absolute;left:0;right:0;bottom:0;height:150px;background-image:radial-gradient(#d5dadd 2px,transparent 2px);background-size:22px 22px;opacity:.7}
.col .ic{position:absolute;left:50%;bottom:52px;width:58px;transform:translateX(-50%)}
.lst{width:1080px;height:1350px;background:#365A68;color:#fff;position:relative;padding:90px 70px}
.lst .k{font-weight:600;font-size:26px;letter-spacing:3px}
.lst h1{font-weight:400;font-size:62px;margin-top:8px}
.lst ul{list-style:none;margin-top:60px}
.lst li{font-size:34px;font-weight:300;margin:0 0 30px 34px;position:relative;line-height:1.3}
.lst li:before{content:'';position:absolute;left:-34px;top:16px;width:10px;height:10px;background:#E26534;border-radius:50%}
.lst p{font-size:27px;font-weight:300;opacity:.75;margin-top:24px;line-height:1.45;max-width:880px}
.lst .cta{margin-top:46px;display:inline-block;background:#D9474A;font-weight:600;font-size:30px;padding:18px 34px;border-radius:40px}
.lst .logo{position:absolute;left:70px;bottom:70px;width:330px}
.lst .arc{position:absolute;right:-120px;bottom:-120px;width:560px;opacity:.12}
"""

def page(html):
    return f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{html}</body></html>"

def cover(foto, tit, sub, tag="CASO REAL"):
    return page(f"""<div class='cover'><img class='bg' src='{b64(SRC/foto)}'><div class='grad'></div>
    <div class='tag'>{tag}</div><div class='tit'>{tit}</div><div class='sub'>{sub}</div><img class='ic' src='{SIMB}'></div>""")

def collage(h1a, h1b, layout, cells):
    cs = "".join(f"<div class='c' style='{st}'><img src='{b64(SRC/f)}'><span class='lb {cls}'>{lb}</span></div>" for f, lb, cls, st in cells)
    return page(f"""<div class='col'><h1>{h1a}<b>{h1b}</b></h1><div class='grid' style='{layout}'>{cs}</div>
    <div class='dots'></div><img class='ic' src='{SIMB_COR}'></div>""")

def lista(titulo, itens, texto):
    li = "".join(f"<li>{i}</li>" for i in itens)
    return page(f"""<div class='lst'><div class='k'>SERVIÇOS REALIZADOS</div><h1>{titulo}</h1><ul>{li}</ul><p>{texto}</p>
    <div class='cta'>Orçamento no WhatsApp (54) 99934-3297</div>
    <img class='arc' src='{SIMB}'><img class='logo' src='{LOGO_BR}'></div>""")

G2x2 = "grid-template-columns:1fr 1fr;grid-template-rows:470px 470px"
G1_2 = "grid-template-columns:1fr 1fr;grid-template-rows:560px 380px"

POSTS = {
 "c1": [  # Elevamen
   cover("elev_depois1.jpg", "Preventiva no Elevamen", "porcas de segurança e transmissão"),
   collage("Antes e depois:", "porca limpa e lubrificada", G2x2, [
     ("elev_antes1.jpg", "Antes", "", ""), ("elev_depois1.jpg", "Depois", "ok", ""),
     ("elev_antes2.jpg", "Antes", "", ""), ("elev_depois2.jpg", "Depois", "ok", "")]),
   lista("Elevador Elevamen", ["Limpeza das porcas de segurança e do fuso",
        "Lubrificação das porcas de segurança", "Vistoria das correias e polias", "Ajuste da transmissão"],
        "Preventiva programada em indústria metal mecânica da Serra Gaúcha. Porca limpa e lubrificada dura mais e mantém a segurança do elevador."),
 ],
 "c2": [  # Lubrificação mancais
   cover("lub_ins3.jpg", "Lubrificação de mancais", "insufladores e exaustores industriais"),
   collage("Graxa no ponto certo,", "máquina sem parada", G2x2, [
     ("lub_ins1.jpg", "Insuflador", "", ""), ("lub_exa.jpg", "Exaustor", "", ""),
     ("lub_maq.jpg", "Mancal da máquina", "", ""), ("lub_ins2.jpg", "Insuflador", "", "")]),
   lista("Mancais e rolamentos", ["Lubrificação dos mancais de insufladores", "Lubrificação dos mancais de exaustores",
        "Vistoria de rolamentos e fixações", "Registro do serviço por equipamento"],
        "Rolamento sem lubrificação aquece, faz ruído e trava. Um plano de lubrificação simples evita a troca do conjunto e a parada da linha."),
 ],
 "c3": [  # Bombas ETE + sopradores
   cover("sopradores.jpg", "Sopradores e bombas", "manutenção preventiva e corretiva"),
   collage("Utilidades da fábrica", "funcionando sem susto", G1_2, [
     ("sopradores.jpg", "Sopradores de ar", "", "grid-column:1 / span 2"),
     ("ete_bombas.jpg", "Bombas da ETE", "", ""), ("motor_ins.jpg", "Motor do insuflador", "", "")]),
   lista("Bombas, sopradores e motores", ["Corretiva nas bombas da ETE", "Preventiva e corretiva nos sopradores de ar",
        "Inspeção dos motores e transmissões", "Testes de funcionamento após o serviço"],
        "Quando a bomba da ETE ou o soprador para, o problema vai além da máquina. Manutenção em dia mantém a fábrica dentro da norma."),
 ],
 "c4": [  # Correias e polias
   cover("elev_polia2.jpg", "Correias e polias", "vistoria, alinhamento e ajuste"),
   collage("Correia frouxa", "é energia jogada fora", G2x2, [
     ("correias.jpg", "Vistoria das correias", "", ""), ("elev_polia1.jpg", "Polias ajustadas", "ok", ""),
     ("lub_vist.jpg", "Transmissão do exaustor", "", ""), ("lub_prev.jpg", "Preventiva", "", "")]),
   lista("Transmissões por correia", ["Vistoria do desgaste das correias", "Alinhamento de polias",
        "Ajuste da tensão", "Teste de funcionamento"],
        "Correia desalinhada patina, aquece e desgasta a polia. Ajuste periódico reduz consumo de energia e troca de peças."),
 ],
}

POSTS["c5"] = [  # Preventiva completa exaustor 004 (descrição do técnico)
   cover("ex_rotor_limpo.jpg", "Preventiva completa", "exaustor de cabine, passo a passo"),
   collage("Rotor sujo", "perde ar e vibra", G2x2, [
     ("ex_rotor_sujo.jpg", "Antes: rotor sujo", "", ""), ("ex_rotor_limpo.jpg", "Depois: limpo", "ok", ""),
     ("ex_motor1.jpg", "Motor limpo", "ok", ""), ("ex_rotor_graxa.jpg", "Graxa aplicada no rotor", "ok", "")]),
   collage("Mancais abertos,", "rolamento conferido", G2x2, [
     ("ex_mancal_aberto.jpg", "Mancal aberto", "", ""), ("ex_lub2.jpg", "Lubrificação", "ok", ""),
     ("ex_lub1.jpg", "Mancais e eixos", "ok", ""), ("ex_temp_mancal.jpg", "Temperatura do mancal", "", "")]),
   collage("Correias e motor", "medidos e anotados", G2x2, [
     ("ex_correia_velha.jpg", "Correias a trocar", "", ""), ("ex_correia_nova.jpg", "4 correias B80 novas", "ok", ""),
     ("ex_temp_motor.jpg", "Temperatura do motor", "", ""), ("ex_motor2.jpg", "Motor avaliado", "ok", "")]),
   lista("Exaustor de cabine", ["Limpeza do rotor e aplicação de graxa", "Mancais abertos, rolamentos conferidos e lubrificados",
        "Motores limpos, com ruído, vibração e folgas avaliados", "Corrente medida e comparada com a nominal na OS",
        "Troca das 4 correias B80, alinhamento e teste de ruído"],
        "Conexões, conduítes e calhas elétricas verificados e reparados. Tudo registrado na ordem de serviço."),
]

if __name__ == "__main__":
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1080, "height": 1350})
        for k, slides in POSTS.items():
            for i, h in enumerate(slides, 1):
                pg.set_content(h, wait_until="networkidle")
                pg.wait_for_timeout(300)
                pg.screenshot(path=str(OUT / f"{k}_s{i}.jpg"), type="jpeg", quality=90)
                print("ok", k, i)
        b.close()
