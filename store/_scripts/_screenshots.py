"""Generate App Store / Play Store screenshots for ZEN PLAYER."""
from playwright.sync_api import sync_playwright
from pathlib import Path
import time

OUT = Path("store/screenshots")
OUT.mkdir(parents=True, exist_ok=True)

URL = (Path("index.html").resolve().as_uri())

# Sizes
DEVICES = {
    "iphone-6.9": {"w": 1320, "h": 2868, "scale": 3},
    "iphone-6.5": {"w": 1242, "h": 2688, "scale": 3},
    "android-phone": {"w": 1080, "h": 1920, "scale": 2.75},
}

# Inject a fake "playing" state so screenshots show a populated UI.
FAKE_STATE = """
() => {
  // populate track listing
  const T = window.T;
  if (T) {
    T.push({name: "Genjo Koan — Track 1", duration: 247});
    T.push({name: "Wabi Sabi (Sketches)", duration: 198});
    T.push({name: "Yugen — Distant Mountain", duration: 312});
    T.push({name: "Mu — The Open Field", duration: 285});
  }
  // set displays directly
  const set = (id, v) => { const el = document.getElementById(id); if (el) el.textContent = v; };
  set("nt", "Yugen — Distant Mountain");
  set("ns", "TRACK 3 / 4");
  set("tc", "1:42");
  set("td", "5:12");
  set("vn", "78");
  // progress fill ~33%
  const pf = document.querySelector(".pf"); if (pf) pf.style.width = "33%";
  const vf = document.getElementById("vf"); if (vf) vf.style.width = "78%";
  // draw something on the visualizer canvas
  const c = document.querySelector("canvas");
  if (c) {
    const ctx = c.getContext("2d");
    const W = c.width = c.clientWidth * 2;
    const H = c.height = c.clientHeight * 2;
    const grad = ctx.createLinearGradient(0, 0, 0, H);
    grad.addColorStop(0, "rgba(212,165,116,0.0)");
    grad.addColorStop(1, "rgba(212,165,116,0.6)");
    ctx.fillStyle = grad;
    const bars = 64;
    const bw = W / bars;
    for (let i = 0; i < bars; i++) {
      const t = i / bars;
      const peak = 0.4 + 0.4 * Math.sin(t * Math.PI * 2.3) + 0.2 * Math.sin(t * Math.PI * 7.1);
      const bh = Math.max(20, peak * H * 0.6);
      ctx.fillRect(i * bw + bw * 0.15, H - bh, bw * 0.7, bh);
    }
  }
}
"""

OPEN_EQ = """
() => {
  const eq = document.getElementById("eqp") || document.querySelector(".eqp, .v");
  if (eq) eq.classList.add("on");
  // attempt to find the EQ open trigger and toggle
  document.querySelectorAll(".v").forEach(el => el.classList.add("on"));
}
"""

def shot(page, path):
    page.screenshot(path=str(path), full_page=False, omit_background=False)
    print("  ->", path)

with sync_playwright() as p:
    browser = p.chromium.launch()
    for name, d in DEVICES.items():
        print(f"Device: {name} ({d['w']}x{d['h']})")
        ctx = browser.new_context(
            viewport={"width": d["w"] // d["scale"], "height": d["h"] // d["scale"]},
            device_scale_factor=d["scale"],
            is_mobile=True,
            has_touch=True,
        )
        page = ctx.new_page()
        page.goto(URL, wait_until="domcontentloaded", timeout=15000)
        time.sleep(2.0)

        # Empty state
        shot(page, OUT / f"{name}-01-empty.png")

        # Faked playing state
        page.evaluate(FAKE_STATE)
        time.sleep(0.4)
        shot(page, OUT / f"{name}-02-playing.png")

        # EQ panel open
        page.evaluate(OPEN_EQ)
        time.sleep(0.4)
        shot(page, OUT / f"{name}-03-eq.png")

        ctx.close()
    browser.close()
print("done")
