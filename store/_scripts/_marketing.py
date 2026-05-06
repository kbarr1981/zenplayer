"""Generate App Store / Play Store marketing screenshots with taglines."""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

OUT = Path("store/screenshots/marketing")
OUT.mkdir(parents=True, exist_ok=True)
SRC = Path("store/screenshots")

# (source-suffix, tagline, accent kanji)
SHOTS = [
    ("01-empty",   "Pure focus.\nJust play.",       "禅"),
    ("02-playing", "Eight bands.\nFull control.",   "音"),
    ("02-playing", "Your music,\nundisturbed.",     "静"),
]

DEVICES = ["iphone-6.9", "iphone-6.5", "android-phone"]

GOLD = (212, 165, 116)
BROWN = (176, 122, 81)
CREAM = (245, 237, 224)
BG = (12, 10, 9)

def find_font(weight_keywords, size):
    candidates = [
        r"C:\Windows\Fonts\seguisb.ttf",   # Segoe UI Semibold
        r"C:\Windows\Fonts\segoeui.ttf",
        r"C:\Windows\Fonts\arial.ttf",
        r"C:\Windows\Fonts\arialbd.ttf",
    ]
    for c in candidates:
        if Path(c).exists():
            try:
                return ImageFont.truetype(c, size)
            except Exception:
                pass
    return ImageFont.load_default()

def find_jp_font(size):
    candidates = [
        r"C:\Windows\Fonts\YuMincho-Regular.ttf",
        r"C:\Windows\Fonts\YuMin.ttc",
        r"C:\Windows\Fonts\msmincho.ttc",
        r"C:\Windows\Fonts\YuGothR.ttc",
        r"C:\Windows\Fonts\meiryo.ttc",
    ]
    for c in candidates:
        if Path(c).exists():
            try:
                return ImageFont.truetype(c, size)
            except Exception:
                continue
    return None

def render(device, src_suffix, tagline, kanji, idx):
    src_path = SRC / f"{device}-{src_suffix}.png"
    src = Image.open(src_path).convert("RGB")
    W, H = src.size

    # Canvas same size as device screenshot
    canvas = Image.new("RGB", (W, H), BG)

    # Top band: 30% of height
    band_h = int(H * 0.30)
    inner_h = H - band_h
    inner_w = int(W * 0.86)
    inner_w_to_h = src.size[0] / src.size[1]
    inner_h_target = int(inner_w / inner_w_to_h)
    if inner_h_target > inner_h - int(H * 0.05):
        inner_h_target = inner_h - int(H * 0.05)
        inner_w = int(inner_h_target * inner_w_to_h)

    # Resize the screenshot
    inner = src.resize((inner_w, inner_h_target), Image.LANCZOS)
    px = (W - inner_w) // 2
    py = band_h + int(H * 0.02)
    # Rounded-corner mask
    mask = Image.new("L", (inner_w, inner_h_target), 0)
    md = ImageDraw.Draw(mask)
    radius = int(min(inner_w, inner_h_target) * 0.06)
    md.rounded_rectangle((0, 0, inner_w, inner_h_target), radius=radius, fill=255)
    canvas.paste(inner, (px, py), mask)

    # Subtle gold border on the inner phone-frame
    bd = ImageDraw.Draw(canvas)
    bd.rounded_rectangle((px, py, px + inner_w, py + inner_h_target),
                         radius=radius, outline=(40, 30, 22), width=2)

    # Tagline text
    fs = int(W * 0.075)
    font = find_font(["semibold"], fs)
    lines = tagline.split("\n")
    line_h = int(fs * 1.18)
    total_h = line_h * len(lines)
    ty = (band_h - total_h) // 2 - int(H * 0.005)
    for i, line in enumerate(lines):
        bbox = font.getbbox(line)
        tw = bbox[2] - bbox[0]
        bd.text(((W - tw) // 2, ty + i * line_h), line, fill=CREAM, font=font)

    # Accent kanji (small, top-left)
    jp_font = find_jp_font(int(W * 0.045))
    if jp_font:
        bd.text((int(W * 0.06), int(H * 0.04)), kanji, fill=BROWN, font=jp_font)

    # Brand strip: "ZEN PLAYER" small, top-right
    brand_font = find_font([], int(W * 0.022))
    bd.text((W - int(W * 0.30), int(H * 0.05)),
            "ZEN PLAYER", fill=(140, 120, 95), font=brand_font)

    out = OUT / f"{device}-mkt-{idx:02d}.png"
    canvas.save(out, optimize=True)
    print(" ->", out)

for device in DEVICES:
    print(f"Device: {device}")
    for i, (suffix, tagline, kanji) in enumerate(SHOTS, start=1):
        render(device, suffix, tagline, kanji, i)
print("done")
