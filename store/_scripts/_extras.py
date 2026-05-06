"""Generate Play Store feature graphic and Apple no-alpha 1024 icon."""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

OUT = Path("store")
OUT.mkdir(exist_ok=True)

GOLD = (212, 165, 116)
BROWN = (176, 122, 81)
CREAM = (245, 237, 224)
DIM = (140, 120, 95)
BG = (12, 10, 9)

def font(size, bold=False):
    candidates = [
        r"C:\Windows\Fonts\seguisb.ttf" if bold else r"C:\Windows\Fonts\segoeui.ttf",
        r"C:\Windows\Fonts\arialbd.ttf" if bold else r"C:\Windows\Fonts\arial.ttf",
    ]
    for c in candidates:
        if Path(c).exists():
            try:
                return ImageFont.truetype(c, size)
            except Exception:
                pass
    return ImageFont.load_default()

def jp_font(size):
    for c in (r"C:\Windows\Fonts\YuMincho-Regular.ttf",
              r"C:\Windows\Fonts\YuMin.ttc",
              r"C:\Windows\Fonts\msmincho.ttc",
              r"C:\Windows\Fonts\YuGothR.ttc"):
        if Path(c).exists():
            try:
                return ImageFont.truetype(c, size)
            except Exception:
                continue
    return None

# --- Feature graphic 1024x500 ---
W, H = 1024, 500
fg = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(fg)

# Soft radial accent (manual gradient circle)
for r in range(380, 0, -8):
    alpha = max(0, int(40 * (1 - r / 380)))
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    od.ellipse((W - 200 - r, H // 2 - r, W - 200 + r, H // 2 + r),
               fill=(176, 122, 81, alpha))
    fg.paste(overlay, (0, 0), overlay)

# Embed app icon on the right
icon = Image.open("icons/icon-512.png").convert("RGBA")
icon = icon.resize((300, 300), Image.LANCZOS)
fg.paste(icon, (W - 300 - 70, (H - 300) // 2), icon)

# Tagline left
jp = jp_font(72)
if jp:
    d.text((70, 110), "禅", fill=BROWN, font=jp)
d.text((130, 130), "ZEN PLAYER", fill=CREAM, font=font(44, bold=True))
d.text((130, 200), "Quiet music player.", fill=CREAM, font=font(38, bold=True))
d.text((130, 250), "8-band EQ.", fill=CREAM, font=font(38, bold=True))
d.text((130, 340), "Bring your own files.", fill=DIM, font=font(26))

fg.save(OUT / "feature-graphic.png", optimize=True)
print("->", OUT / "feature-graphic.png")

# --- Apple App Store icon: 1024x1024 PNG, no alpha ---
src = Image.open("icons/icon-1024.png").convert("RGBA")
flat = Image.new("RGB", src.size, BG)
flat.paste(src, mask=src.split()[3])
flat.save(OUT / "appstore-icon-1024.png", optimize=True)
print("->", OUT / "appstore-icon-1024.png")

print("done")
