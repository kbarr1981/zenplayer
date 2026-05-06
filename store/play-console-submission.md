# Zen MP3 Player — Google Play Console submission packet

Use this doc as a paste-as-you-go reference while filling out Play Console.
Sections are ordered roughly the way Play Console asks for them. Every
field has its final value or file path noted.

> 📁 = upload a file. 📋 = paste this text. ⚪ = single choice. ☑ = multi-select.

---

## 0. Pre-submission

- Active keystore is at `C:\Users\krist\Documents\_keystores\zenplayer\signing.keystore` (password `p1GvAcmuuBRu`, alias `my-key-alias`). Off-machine backup before first upload is highly recommended.
- Privacy policy needs to be live at a public URL **before** submission. See §10 below — currently a TODO.
- Test the APK on your phone first: `I:\zenplayer\packages\android\Zen MP3.apk`. Confirm it launches fullscreen (no URL bar) and audio playback works.

---

## 1. Create app

| Field | Value |
|---|---|
| App name | Zen MP3 Player |
| Default language | English (United Kingdom) – en-GB |
| App or game | ⚪ App |
| Free or paid | ⚪ Free |
| Declarations: Developer Program Policies | ☑ I confirm |
| Declarations: US export laws | ☑ I confirm |

---

## 2. Set up your app — Dashboard checklist

Play Console will guide you through 12-ish dashboard cards. Answers below.

### 2a. App access

⚪ **All functionality is available without special access**

(No login, no region lock, no time-limited trial.)

### 2b. Ads

⚪ **No, my app does not contain ads**

### 2c. Content rating

Click **Start questionnaire** → fill in:

| Question | Answer |
|---|---|
| Email address | littlewhitestudio.uk@gmail.com |
| Category | Reference, News, or Educational ❌ — pick **Music** |
| Does your app contain violence? | No |
| Sexual content? | No |
| Profanity / crude humour? | No |
| Drugs, alcohol, or tobacco? | No |
| Gambling? | No |
| Horror or fear-inducing themes? | No |
| User-generated content? | No |
| Live-streaming? | No |
| Social features? | No |
| Sharing user location? | No |
| Personal info collection? | No |
| Internet connectivity required? | No |
| Digital purchases? | No |
| Use of cryptocurrency? | No |

Expected outcome: **Everyone / IARC 3+**.

### 2d. Target audience and content

| Question | Answer |
|---|---|
| Target age groups | ☑ 13–15, 16–17, 18+ (Music apps typically target 13+) |
| Appeal to children? | No |
| Designed for Families? | No |
| Ads inappropriate for children? | N/A (no ads) |

### 2e. News apps

⚪ **My app is not a news app**

### 2f. Data safety

This is the longest form. Answers below match an entirely on-device,
no-network app.

**Data collection and sharing — overview**

| Question | Answer |
|---|---|
| Does your app collect or share any of the required user data types? | **No** |
| Is all of the user data collected by your app encrypted in transit? | N/A |
| Do you provide a way for users to request that their data be deleted? | N/A |

(If Play Console forces you to fill in detail anyway, the answer to **every** category — Personal info, Financial info, Health, Photos/videos, Audio files, Files & docs, Calendar, Contacts, App activity, Web browsing, App info, Device IDs — is "Not collected, not shared". Audio files: even though the user loads their own audio, it never leaves the device, so this does **not** count as collection.)

### 2g. Government apps

⚪ **No, this isn't a government app**

### 2h. Financial features

⚪ **My app does not provide financial features**

### 2i. Health

⚪ **My app does not contain health-related content**

### 2j. App category and store listing contact details

| Field | Value |
|---|---|
| Category | **Music & Audio** |
| Tags | Music Player, Audio, Equalizer (Play Console lets you pick up to 5 — these are the most relevant) |
| Email address (public) | littlewhitestudio.uk@gmail.com |
| Phone (public) | leave blank |
| Website (public) | https://kbarr1981.github.io/zenplayer/ |

### 2k. External marketing

⚪ **No, do not market my app outside of Google Play**
(can change later)

### 2l. Government rebates and offers

⚪ **No**

---

## 3. Main store listing

### App name (30 chars max)
📋 `Zen MP3 Player`

### Short description (80 chars max)
📋 `Quiet offline MP3 player with 8-band equalizer, live visualizer, dark theme.`

### Full description (4000 chars max)
📋 paste from `store/listing.md` → "Google Play Store" → "Full Description" section. (Already authored, includes ★ KEY FEATURES ★ block etc.)

### Graphics

| Asset | Spec | File |
|---|---|---|
| App icon | 512×512 PNG, 32-bit | 📁 `I:\zenplayer\icons\icon-512.png` |
| Feature graphic | 1024×500 PNG/JPG | 📁 `I:\zenplayer\store\feature-graphic.png` |
| Phone screenshots (need 2-8) | 1080×1920 portrait | 📁 `I:\zenplayer\store\screenshots\marketing\android-phone-mkt-01.png` |
|  |  | 📁 `…\marketing\android-phone-mkt-02.png` |
|  |  | 📁 `…\marketing\android-phone-mkt-03.png` |
| 7-inch tablet screenshots | optional | skip for v1 |
| 10-inch tablet screenshots | optional | skip for v1 |
| Promo video | YouTube URL | leave blank |

The marketing variants have tagline overlays. If you'd rather show clean
device-only shots without the marketing strip, swap in
`store/screenshots/android-phone-0{1,2,3}.png` instead.

---

## 4. Store settings

| Field | Value |
|---|---|
| App or game | App |
| Tags | Music Player, Audio, Equalizer |
| Category | Music & Audio |
| Email | littlewhitestudio.uk@gmail.com |
| Website | https://kbarr1981.github.io/zenplayer/ |
| Phone | leave blank |

---

## 5. Production release

When you reach **Releases → Production → Create new release**:

### App bundle
📁 upload `I:\zenplayer\packages\android\Zen MP3.aab`

### Release name
📋 `1.0.0 (1)` — Play Console will autopopulate from the AAB version code; just confirm

### Release notes (per language, 500 chars)
en-GB:
📋
```
First release of Zen MP3 Player — a quiet, offline music player with an
8-band equalizer, live visualizer, and a dark zen-themed UI. Bring your
own audio files; the app does the rest.
```

Click **Save** → **Review release** → **Send for review**.

---

## 6. Countries / regions and pricing

When prompted at the end of Production setup:

| Field | Value |
|---|---|
| Countries | ☑ All countries (deselect any you want to exclude) |
| Distribution | ☑ Available on Google Play |
| Pricing | Free (already set in §1) |
| In-app products | None |

---

## 7. Closed / Internal testing (optional — recommended)

Before promoting to Production, you can test via the **Internal testing**
track. Same AAB upload. Add tester emails (your own + a friend's) on the
"Testers" tab. Generates an opt-in URL you can share. Lets you verify
install + launch on real devices through the Play Store flow without
your app being publicly listed yet. Skip if you're confident in the APK
sideload test.

---

## 8. App signing

Play Console will say something like:

> Use Play App Signing? **Yes (recommended).**

This means Google holds your **upload certificate** + an internal **app signing certificate**. You upload AABs signed with `signing.keystore`; Google re-signs them with their own key for distribution. Your local keystore becomes the *upload key*, which is recoverable if lost.

⚪ **Use Play App Signing** ← pick this.

---

## 9. Misc declarations Play Console may surface

| Question | Answer |
|---|---|
| Is your app a VPN? | No |
| Does your app use Accessibility Services? | No |
| Does your app contain weapons-related content? | No |
| Does your app target children under 13? | No |
| Does your app use background location? | No |
| Does your app use exact alarms? | No |
| Does your app use SMS / Call Log permissions? | No |
| Does your app use foreground services? | No (audio playback is foreground via media session, but not declared as a foreground service in this build) |

---

## 10. ⚠ Privacy policy — TODO before submission

Play Console **requires** a publicly hosted privacy policy URL even when
your app collects nothing. Currently `https://kbarr1981.github.io/zenplayer/privacy`
is referenced in the Apple listing but not yet hosted.

**Quickest path:** add a `privacy.html` to the project root. Suggested
contents:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Privacy Policy — Zen MP3 Player</title>
  <style>
    body{font-family:system-ui,-apple-system,Segoe UI,sans-serif;max-width:680px;margin:40px auto;padding:0 20px;line-height:1.55;color:#222;background:#fff}
    h1{font-weight:300;letter-spacing:.05em}
    h2{margin-top:1.6em;font-weight:500}
  </style>
</head>
<body>
  <h1>Privacy Policy — Zen MP3 Player</h1>
  <p>Last updated: 2026-05-06</p>
  <p>Zen MP3 Player ("the app") is a music player that runs entirely on your device.
  This page explains what the app does and does not do with your data.</p>

  <h2>What we collect</h2>
  <p>Nothing. The app does not collect, store, or transmit any personal information,
  usage analytics, device identifiers, or audio file metadata to any server.</p>

  <h2>What the app accesses on your device</h2>
  <ul>
    <li><strong>Audio files you choose</strong>: when you select audio files for playback,
    the app reads them locally to play them back. They are never uploaded.</li>
  </ul>

  <h2>Third parties</h2>
  <p>None. The app contains no analytics SDKs, no advertising libraries, and no
  third-party tracking of any kind.</p>

  <h2>Network</h2>
  <p>The app makes no network requests during playback. The only network activity is
  the initial download of the page bundle when you first install the app.</p>

  <h2>Children</h2>
  <p>The app is rated for general audiences. It collects no personal information
  from anyone, including children under 13.</p>

  <h2>Changes</h2>
  <p>If this policy ever changes, the updated date at the top of this page will
  reflect the change. Material changes will be announced in the app's release notes.</p>

  <h2>Contact</h2>
  <p>littlewhitestudio.uk@gmail.com</p>
</body>
</html>
```

Save as `privacy.html` at the project root, then create a `privacy/` redirect
or rename to `privacy/index.html` so the URL `…/zenplayer/privacy` resolves.
Once `https://kbarr1981.github.io/zenplayer/privacy` returns 200, paste that
URL into Play Console's **App content → Privacy policy** field.

---

## 11. Submission order in Play Console

The dashboard will block "Send for review" until every required card is
green. Suggested order:

1. Create app (§1)
2. Privacy policy (§10) — host it first, then paste URL
3. App access (§2a)
4. Ads (§2b)
5. Content rating questionnaire (§2c)
6. Target audience (§2d)
7. News (§2e), Government (§2g), Financial (§2h), Health (§2i)
8. Data safety (§2f)
9. App category + contact details (§2j)
10. Main store listing (§3) — paste copy + upload graphics
11. Store settings (§4)
12. Production release (§5) — upload AAB, release notes
13. Countries (§6)
14. Review & send for review

Review takes anywhere from a few hours to a few days. First submissions
sometimes get one round of clarification questions about Data Safety —
the answers are all in §2f above.

---

## 12. After approval — minor follow-ups

- Drop the old fingerprint from `https://kbarr1981.github.io/.well-known/assetlinks.json` (currently lists both old + new). Only the active one needs to remain once the new AAB is the only build in circulation.
- Bump version code for any future update: regenerate AAB via PWABuilder, increment `appVersionCode`, upload new AAB to Production.
