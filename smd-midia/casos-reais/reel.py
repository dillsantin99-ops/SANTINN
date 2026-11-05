"""Monta o Reel 'Preventiva no exaustor' (1080x1920, ~24s) a partir dos vídeos e fotos reais."""
import subprocess, pathlib
from PIL import Image, ImageDraw, ImageFont

BASE = pathlib.Path(__file__).parent
SRC = BASE / "src"
VID = pathlib.Path("/mnt/user-data/uploads/FOTOS MANUTENÇÃO/Manutenção Exaustores")
TMP = pathlib.Path("/tmp/claude-0/-home-claude/e87bcf54-73d0-5df6-a0fe-d132738fe209/scratchpad/reel")
TMP.mkdir(parents=True, exist_ok=True)
FB = "/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf"
FL = "/usr/share/fonts/truetype/google-fonts/Poppins-Light.ttf"
W, H, FPS = 1080, 1920, 30
RED, SLATE = (217, 71, 74), (54, 90, 104)

def run(cmd):
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)

def overlay(text, sub=None, name="ov"):
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    f = ImageFont.truetype(FB, 72); fs = ImageFont.truetype(FL, 44)
    y = 1380
    for line in text.split("\n"):
        tw = d.textlength(line, font=f)
        d.rectangle((60, y, 60 + tw + 50, y + 104), fill=RED + (240,))
        d.text((85, y + 8), line, font=f, fill="white"); y += 116
    if sub:
        fs = ImageFont.truetype(FB, 44)
        sw = d.textlength(sub, font=fs)
        d.rectangle((60, y + 6, 60 + sw + 50, y + 82), fill=(20, 30, 36, 215))
        d.text((85, y + 14), sub, font=fs, fill="white")
    logo = Image.open(SRC / "logo_smd_slate.png").convert("RGBA")
    logo = logo.resize((300, int(300 * logo.height / logo.width)))
    pad = Image.new("RGBA", (logo.width + 30, logo.height + 20), SLATE + (230,))
    pad.paste(logo, (15, 10)); im.paste(pad, (W - pad.width - 50, 90), pad)
    p = TMP / f"{name}.png"; im.save(p); return p

VF_FIT = f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS},format=yuv420p"

def seg_video(src, ss, dur, text, sub, n):
    ov = overlay(text, sub, f"ov{n}")
    out = TMP / f"s{n}.mp4"
    run(["ffmpeg", "-y", "-ss", str(ss), "-t", str(dur), "-i", str(src), "-i", str(ov),
         "-filter_complex", f"[0:v]{VF_FIT}[v];[v][1:v]overlay=0:0[o]", "-map", "[o]",
         "-an", "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", str(out)])
    return out

def seg_foto(src, dur, text, sub, n):
    ov = overlay(text, sub, f"ov{n}")
    out = TMP / f"s{n}.mp4"; fr = int(dur * FPS)
    zoom = f"scale={W*2}:{H*2}:force_original_aspect_ratio=increase,crop={W*2}:{H*2},zoompan=z='1+0.0015*on':d={fr}:s={W}x{H}:fps={FPS},format=yuv420p"
    run(["ffmpeg", "-y", "-loop", "1", "-i", str(src), "-i", str(ov), "-filter_complex",
         f"[0:v]{zoom}[v];[v][1:v]overlay=0:0[o]", "-map", "[o]", "-t", str(dur),
         "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", str(out)])
    return out

def end_card(dur, n):
    im = Image.new("RGB", (W, H), SLATE); d = ImageDraw.Draw(im)
    logo = Image.open(SRC / "logo_smd_slate.png"); logo = logo.resize((640, int(640 * logo.height / logo.width)))
    im.paste(logo, ((W - logo.width) // 2, 560))
    f = ImageFont.truetype(FB, 64); fs = ImageFont.truetype(FL, 44)
    for i, (t, ft, y) in enumerate([("Preventiva evita parada.", f, 900), ("Manutenção industrial na Serra Gaúcha", fs, 1000)]):
        d.text(((W - d.textlength(t, font=ft)) / 2, y), t, font=ft, fill="white")
    t = "WhatsApp (54) 99934-3297"; tw = d.textlength(t, font=f)
    d.rounded_rectangle(((W - tw) / 2 - 50, 1150, (W + tw) / 2 + 50, 1270), 60, fill=RED)
    d.text(((W - tw) / 2, 1162), t, font=f, fill="white")
    p = TMP / "end.png"; im.save(p); out = TMP / f"s{n}.mp4"
    run(["ffmpeg", "-y", "-loop", "1", "-i", str(p), "-t", str(dur), "-vf", f"fps={FPS},format=yuv420p",
         "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", str(out)])
    return out

segs = [
    seg_video(VID / "Rotor exaustor sujo.mp4", 3, 3.5, "Rotor do exaustor\nassim?", "Pó acumulado = vibração e perda de ar", 1),
    seg_foto(SRC / "ex_rotor_limpo.jpg", 2.5, "Limpeza do rotor", None, 2),
    seg_foto(SRC / "ex_mancal_aberto.jpg", 2.5, "Mancais abertos", "rolamento conferido e lubrificado", 3),
    seg_foto(SRC / "ex_temp_mancal.jpg", 2.5, "Temperatura medida", "mancais e motores", 4),
    seg_foto(SRC / "ex_correia_velha.jpg", 2.5, "Correias gastas", None, 5),
    seg_video(VID / "Correias trocadas, teste de ruido e alinhamento.mp4", 10, 6, "4 correias B80 novas", "alinhamento e teste de ruído", 6),
    end_card(3.5, 7),
]
lst = TMP / "list.txt"; lst.write_text("".join(f"file '{s}'\n" for s in segs))
silent = TMP / "silent.mp4"
run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy", str(silent)])
# trilha: som ambiente real do teste das correias, baixo, com fade (Instagram exige faixa de áudio)
out = BASE / "reel_exaustor.mp4"
run(["ffmpeg", "-y", "-i", str(silent), "-ss", "5", "-i", str(VID / "Correias trocadas, teste de ruido e alinhamento.mp4"),
     "-filter_complex", "[1:a]volume=0.6,afade=t=in:d=1,afade=t=out:st=21:d=2[a]", "-map", "0:v", "-map", "[a]",
     "-shortest", "-c:v", "copy", "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart", str(out)])
print(out)
