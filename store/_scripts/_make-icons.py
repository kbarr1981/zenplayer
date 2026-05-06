"""Regenerate icon set from woman portrait + rename app to 'Zen MP3 Player'."""
from PIL import Image
from pathlib import Path

src_path = next(Path(".").glob("the_toffman_*.webp"))
src = Image.open(src_path).convert("RGBA")
print("source:", src_path.name, src.size)

# Crop center square (already square, but ensure)
w, h = src.size
m = min(w, h)
left = (w - m) // 2
top = (h - m) // 2
src = src.crop((left, top, left + m, top + m))

# Save a clean source for future regeneration
src.save("icon-source.png", optimize=True)

for size in (192, 512, 1024):
    img = src.resize((size, size), Image.LANCZOS)
    img.save(f"icons/icon-{size}.png", optimize=True)
    print(" ->", f"icons/icon-{size}.png")

# Maskable: pad to 80% safe area (Android crops off the edges)
canvas = Image.new("RGBA", (512, 512), (0, 0, 0, 255))
inner = src.resize((410, 410), Image.LANCZOS)
canvas.paste(inner, (51, 51), inner)
canvas.save("icons/icon-512-maskable.png", optimize=True)
print(" -> icons/icon-512-maskable.png")

# Apple no-alpha 1024
flat = Image.new("RGB", (1024, 1024), (0, 0, 0))
big = src.resize((1024, 1024), Image.LANCZOS)
flat.paste(big, mask=big.split()[3])
flat.save("store/appstore-icon-1024.png", optimize=True)
print(" -> store/appstore-icon-1024.png")

print("done")
