---
name: budo-seedance-product-ad
description: Generate product advertisement video prompts for Seedance 2.0 on Higgsfield. Use whenever the user wants product ads, e-commerce videos, product showcases, unboxing, product demos, shopping ads, fashion ads, beauty ads, food ads, or any commercial product video for online selling. Triggers on: product ad, e-commerce, product showcase, Amazon video, Shopify ad, Instagram shop, TikTok shop, product commercial, fashion video, beauty ad, food ad, product demo, dropshipping video, or any product promotional video request. Use even for "make a video for my product" or "product promo." Reads BUDOSKILL_Seedance_Base.md first for platform specs, the 2-Second Hook framework, visual-quality vocabulary, universal prompt rules, common mistakes, platform delivery table, master template, and output workflow.
---

# BUDO — Product Ad Videos for Seedance 2.0 on Higgsfield

> **Inherits from `BUDOSKILL_Seedance_Base.md`.** Read that file first for platform specs (§1), universal hook theory (§2), the visual-quality vocabulary library (§3), prompt principles (§4), common mistakes (§5), platform table (§6), master template (§7), and the output workflow (§8). This file adds only what's **specific to product / shopping ad video.**

---

## 1. What this vertical optimizes for

Product advertising video has one job: **convert a scroller into a buyer.** That changes priorities versus other verticals:

- **Product clarity is non-negotiable.** Even the prettiest lifestyle shot fails if the viewer can't tell what the product *is* by second 3.
- **Three audiences must be served at once:** the cold scroller (hook + visual), the considering shopper (feature/benefit), the ready buyer (CTA + price/proof).
- **The ad is one click from a checkout button.** Friction must be removed by the visual, not added by it.

Override on Base §6: for product-page video (Amazon, Shopify), the hook can be 0–2s instead of 0–1s — these viewers already clicked, they're evaluating, not scrolling.

---

## 2. Product-ad hook library (12 hooks)

In addition to the universal shortlist in Base §2, use these category-specific hooks. Pick exactly one per ad.

1. **Product Drop with Dramatic Impact** — Product descends with motion blur into a minimal, dark background; light catches it mid-fall. Signals "premium / new arrival." *Example: luxury watch falling onto black silk.*
2. **Satisfying Texture ASMR Macro** — Extreme close-up of surface (fabric weave, metal grain, cream texture). Pulls the scroll thumb back. *Example: finger gliding across velvet, revealing logo beneath.*
3. **Before / After Snap** — Quick cut or split-screen showing problem → solved state. Communicates benefit before the brain reads anything. *Example: dull skin → glowing skin; messy desk → organized.*
4. **"Stop Scrolling" Direct Address** — Model looks into camera, hand stop-gesture, text overlay. Breaks fourth wall, feels personal. Use sparingly — overused on TikTok.
5. **Unboxing Reveal** — Hands open premium packaging; product emerges into directional light. Taps unboxing ASMR. Best for skincare, electronics, jewelry, fashion.
6. **Color / Variant Cascade** — Products line up, rotating through SKUs in 2 seconds. Works when range is the selling point (lipstick, sneakers, phone cases). Pairs with Seedance 2.0's `multi-sku` tag.
7. **Ingredient / Component Explosion** — Constituent parts splinter outward from the product. Communicates "natural ingredients" or "engineered build." *Example: honey, oats, lavender explode from a skincare jar.*
8. **Problem → Solution Snap** — Text overlay "Problem:" → cut → "Solution:" with product reveal. Direct, no fluff. Best for utility products.
9. **In-Hand Usage Tease** — Hands demonstrate the key feature in under 2 seconds. Shows context immediately. *Example: phone case absorbs a drop, survives intact.*
10. **Lifestyle Aspiration Flash** — Quick cut to a relatable aspirational moment with the product integrated. Sells the life, not the spec sheet.
11. **Scarcity / Urgency Signal** — Stock counter, countdown, or "last drop" text over the product. Use honestly; fake scarcity tanks trust.
12. **Social Proof Hook** — Star rating, "1M+ sold", or a creator's reaction shot crops into frame. Works only with real numbers / real people.

---

## 3. Product-ad philosophy: what actually sells

**Visuals do 70% of the work; copy does 30%.** Don't pile text overlays on top of a weak visual. If the visual already tells the story, the text just punctuates it.

**One key message per 5 seconds of screen time.** Cap text overlays at 5–8 words. The 15-second TikTok ad has, at most, three messages.

**Hierarchy of information: benefit → feature → price.** Don't lead with "10,000 mAh battery." Lead with "your phone, charged 4 times." The feature is *how* it works; the benefit is *why* it matters.

---

## 4. Product category playbook

**Fashion / Apparel.** Movement is the demo — the fabric moving, the silhouette walking. Use `genre: drama` or `auto`. Lifestyle 60% / product clarity 40%. Aspect 9:16 (Reels) or 4:5 (Feed). Quality vocab: layer §3.4 anamorphic + §3.7 grain for editorial feel.

**Beauty / Skincare.** Texture, application, before/after. Macro is your friend. Use `genre: auto`. Avoid hyper-warm grades that distort skin tone. Test on actual skin tones, not just the model's. Quality vocab: §3.1 "8K, every pore visible" + §3.5 clamshell lighting.

**Electronics / Tech.** Show *use*, not specs. The phone unlocks, the headphones cancel noise, the camera focuses. Use `genre: auto` or `epic` for hero reveals. 16:9 for product page; 9:16 for social. Quality vocab: §3.3 ray-traced reflections + §3.4 Steadicam.

**Food & Beverage.** Steam, pour, texture, the bite. Sound matters more than in other categories. Plan the prompt with audio reference in `medias` if available. (See `BUDOSKILL_FoodBeverage.md` for deeper craft.)

**Jewelry / Luxury.** Hard directional light, dark background, slow rotation. Use `genre: drama`. Macro at 1:1 magnification or tighter. Cap movement speed — luxury reads as slow. Quality vocab: §3.3 path-traced + §3.4 100mm macro + §3.6 "Vanity Fair cover".

**Furniture / Home.** Scale needs a human reference. Use `genre: auto`. Show the product *in* a space, not floating. 16:9 framing reads as "real photography"; 9:16 reads as "social." Quality vocab: §3.8 "Architectural Digest interior".

**Health / Supplements.** Regulated category — keep claims visual, not textual. Show ritual (the morning routine, the gym moment) rather than promised outcomes.

---

## 5. Product-ad master-template additions

The base skeleton is in Base §7. For product ads, layer in these fields:

```
[PRODUCT IDENTITY]
- exact product name, color, material, packaging
- the single feature/benefit this ad is selling
- the SKU(s) shown if multiple

[PRODUCT CLARITY CHECK]
- by what second is the product unambiguously identifiable?
- which angle/shot delivers that recognition?

[LIFESTYLE / CONTEXT BLEND]
- ratio of in-isolation footage vs. in-use footage (typical: 40/60 in-use)
- the relatable moment the buyer should project themselves into

[TEXT / CTA INTEGRATION]
- text overlays (max 5–8 words each, max 3 across the clip)
- closing CTA in the final 2 seconds ("Shop Now", "Get Yours", "Link in Bio")
- price/proof element if applicable
```

---

## 6. Example prompts (5)

Each prompt follows the master template + the product-ad additions above. Quality vocabulary from Base §3 is layered into each. Paste into the Higgsfield `generate_video` tool with `model: seedance_2_0`.

### Example 1 — Luxury fashion outfit showcase (9:16, Reels)

```
[GENRE / STYLE]
Genre: drama. Photoreal fashion cinematography, editorial register.
Quality: 8K, ultra-HD, shot on ARRI Alexa, anamorphic 2.39:1, 35mm film grain,
Vogue editorial polish.
Palette: charcoal, cream, deep burgundy. Low saturation, high contrast.

[OPENING HOOK — 0 to 1.5s]
Hook: Texture macro. Extreme close-up of cashmere weave, single shaft of light
crossing the fibers. At 1.0s the camera pulls back rapidly.

[MAIN ACTION — 1.5 to 11s]
Pull-back reveals a model in a full burgundy cashmere coat, slow walk toward
camera in a marble corridor. At 6.0s, the model turns side-on; the coat hem
arcs through the air. At 9.0s, model stops, looks off-camera left.

[CAMERA]
35mm equivalent, f/2.0. Push-out from macro, transitions to Steadicam tracking
backward at the model's walking pace.

[LIGHTING]
3200K key from camera-front-left, hard. Cool ambient fill from marble surfaces.
Single overhead practical adds halo on hair.

[COLOR & GRADE]
Filmic teal-and-orange, mild crush in blacks, warm midtones. Kodak Vision3
emulation.

[CLOSING BEAT — 11 to 12.5s]
Final frame: model still, coat hem settling. Brand wordmark fades up bottom-third.

[PRODUCT CLARITY CHECK]
Coat is unambiguous from 2.5s onward.

[TEXT / CTA]
At 9.5s, "AW26 — now shipping" appears bottom-center, 0.8s hold.

[TECHNICAL]
resolution: 1080p; mode: std; genre: drama; aspect_ratio: 9:16; duration: 12;
medias: [coat product photo as role=image]
```

### Example 2 — Skincare illuminating serum (1:1, Feed)

```
[GENRE / STYLE]
Genre: auto. Photoreal product cinematography, clean beauty register.
Quality: 8K, every pore visible, hyper-detailed, macro photography, clamshell
lighting, Madison Avenue ad polish.
Palette: white, pale gold, soft peach.

[OPENING HOOK — 0 to 1.5s]
Hook: Drop with impact (slow). A single droplet of serum falls from the dropper
in slow motion, landing on the back of a hand and beading. Light catches the bead.

[MAIN ACTION — 1.5 to 9s]
Fingertip spreads the serum across the skin in a slow circle. Skin visibly
brightens in the path of the finger. Cut at 6.0s to the bottle standing on a
marble surface, dropper hovering above. Cut at 8.0s to a side-profile of the
model's cheek — the same patch of skin from earlier, now even-toned.

[CAMERA]
60mm macro for the drop and the skin; 50mm for the bottle. Static for both
macro shots; slow push-in on the cheek shot. Phantom-style slow-mo on the drop.

[LIGHTING]
5500K large soft source from camera-top, very soft fill from below to lift
under-eye shadows. White seamless background.

[COLOR & GRADE]
Neutral, slightly warm. No skin smoothing in post — the texture is the demo.
Rec. 709, 10-bit color.

[CLOSING BEAT — 9 to 10s]
Bottle alone on marble, label readable. Brand mark and "Illuminating Serum"
text fades up at 9.5s.

[PRODUCT CLARITY CHECK]
Bottle visible from 6.0s; label readable in the closing beat.

[TEXT / CTA]
"Brighter in 14 days. *based on user study, n=120" — bottom safe area, 8.5–10s.

[TECHNICAL]
resolution: 1080p; mode: std; genre: auto; aspect_ratio: 1:1; duration: 10;
medias: [bottle product photo as role=image, model hand reference as role=image]
```

### Example 3 — Wireless earbuds (9:16, TikTok)

```
[GENRE / STYLE]
Genre: action. Photoreal tech ad register, urban energy.
Quality: 4K, crisp detail, ray-traced reflections, gimbal-stabilized, shot on
Sony Venice, Apple-keynote-grade polish.
Palette: deep navy, silver, single accent magenta on the buds' LED.

[OPENING HOOK — 0 to 1s]
Hook: Reaction first. Close-up of a person in a loud subway car. They tap one
ear; the ambient noise drops to silence in the audio bed. Their shoulders relax.

[MAIN ACTION — 1 to 7s]
Camera pulls back to reveal the case in their other hand. Cut to a top-down
macro of the case opening; the buds rise slightly out of their cradles. Cut to
the person now walking on the platform, head-bobbing subtly to music we don't
hear (the audio bed is the music only).

[CAMERA]
28mm for the subway hook, handheld micro-shake. 90mm macro for the case shot,
static. 35mm tracking for the platform walk. MoVI gimbal on the platform.

[LIGHTING]
Available-light register. Subway: green-tinged fluorescents. Macro: directional
key from camera-left, magenta accent from the LED itself.

[COLOR & GRADE]
Crushed blacks, slight teal-orange split-tone. Magenta of the LED stays pure.
DaVinci Resolve grade.

[CLOSING BEAT — 7 to 8s]
Case closes. Logo on case lid catches light. Cut to black.

[PRODUCT CLARITY CHECK]
Case + buds clearly identified by 3.5s; LED color (the brand cue) by 4.5s.

[TEXT / CTA]
At 6.5s: "Silence. On demand." (5 words). At 8.0s: brand wordmark only.

[TECHNICAL]
resolution: 1080p; mode: std; genre: action; aspect_ratio: 9:16; duration: 8;
medias: [earbuds case product photo as role=image, ambient subway audio as role=audio]
```

### Example 4 — Specialty coffee single-origin bag (4:5, Feed)

```
[GENRE / STYLE]
Genre: drama. Photoreal food/beverage register, artisan-roaster aesthetic.
Quality: 8K, hyper-detailed, 60fps slow-mo, shot on RED Komodo, 35mm grain,
Michelin-quality food cinematography.
Palette: warm browns, cream, single deep red accent.

[OPENING HOOK — 0 to 1.5s]
Hook: Pour macro. Slow-motion espresso pour from a portafilter into a small
white cup, the crema forming in real time.

[MAIN ACTION — 1.5 to 9s]
Pull back to reveal a hand placing the cup on a wooden counter next to a kraft
coffee bag, label facing camera. At 5.0s, hand picks up the bag; thumb peels
back the resealable top; beans visible inside. At 7.0s, cut to a single bean
held between fingers, rotating; its origin stamp visible.

[CAMERA]
90mm macro for the pour and the bean; 50mm for the counter wide. Slow lateral
dolly across the counter shot. f/2.8 shallow depth of field.

[LIGHTING]
3000K window light from camera-right, soft. Single warm practical bounce from
below the counter edge. Motivated lighting.

[COLOR & GRADE]
Warm, low-contrast, slight film grain. Crema and cup-white must stay neutral
white, not tinted yellow. Portra 400 look.

[CLOSING BEAT — 9 to 10.5s]
Bag stands alone on the counter, label centered. Tagline fades up.

[PRODUCT CLARITY CHECK]
Bag visible from 2.5s; label readable by 4s; origin stamp visible at 7.5s.

[TEXT / CTA]
At 9.5s: "Single-origin Ethiopia · in stock now." Brand mark at 10.3s.

[TECHNICAL]
resolution: 1080p; mode: std; genre: drama; aspect_ratio: 4:5; duration: 10;
medias: [coffee bag product photo as role=image]
```

### Example 5 — Diamond engagement ring (1:1, product page)

```
[GENRE / STYLE]
Genre: drama. Photoreal luxury jewelry register.
Quality: 8K, ultra-HD, path-traced lighting, ray-traced reflections, 100mm
macro, shot on ARRI Alexa, Vanity Fair cover polish.
Palette: deep black, platinum white, single fire-spectrum highlight from stone.

[OPENING HOOK — 0 to 2s]
Hook: Light hit on a dark frame. The ring sits centered on black velvet in
total shadow. At 1.0s, a single hard key light sweeps across the stone from
camera-right; the diamond throws spectral flares.

[MAIN ACTION — 2 to 11s]
Slow orbit around the ring at a low angle, 360° over 8 seconds, so the stone
catches light from every facet. At 8.0s, the orbit slows; the camera pushes in
on the table of the diamond.

[CAMERA]
100mm macro, f/4 (deep enough to keep the whole stone sharp). Motorized
turntable simulates the orbit; camera itself static then dollies in.

[LIGHTING]
6500K hard key from camera-right at 30° elevation, no fill, no ambient. Black
flag bottom and rear to keep the velvet pure black. Chiaroscuro.

[COLOR & GRADE]
Neutral white point; do not boost saturation — the spectral fire from the stone
must read as the stone's, not as a grade. DCI-P3 gamut.

[CLOSING BEAT — 11 to 12s]
Push-in lands; held still for half a second on the table. Brand wordmark fades
up beneath.

[PRODUCT CLARITY CHECK]
Ring identifiable from 1.5s; stone clarity readable from 4s.

[TEXT / CTA]
No mid-clip text. At 11.5s: brand wordmark + "made to order" in small caps.

[TECHNICAL]
resolution: 1080p; mode: std; genre: drama; aspect_ratio: 1:1; duration: 12;
medias: [ring product photo as role=image]
```

---

## 7. Product-ad-specific mistakes (in addition to Base §5)

- **Product invisible until second 5.** The viewer has scrolled. Identify the product by second 3 at the latest.
- **More than 3 text overlays in a 15-second clip.** Cuts comprehension; the eye can't read and watch.
- **Lifestyle 100%, product 0%.** Beautiful useless ad. Lifestyle should sit on top of clear product moments, not replace them.
- **Aspirational lifestyle the buyer can't recognize themselves in.** A $30 product in a $30M penthouse is dissonant. Match aspirational level to price point.
- **CTA missing or buried.** Final 2 seconds must have a clear next-step verb ("Shop", "Get", "Join"). Not "Click here" — too generic.
- **Fake urgency.** "Only 5 left!" when there are 50,000 in stock tanks trust on a re-watch.

---

## 8. Final pre-publish checklist

- [ ] Hook is in the first 2 seconds and works muted
- [ ] Product is identifiable by second 3
- [ ] Genre parameter set, not just described in prose
- [ ] Quality vocabulary layered (2–4 terms across §3 subsections)
- [ ] Aspect ratio matches the destination platform
- [ ] Max 3 text overlays, max 5–8 words each
- [ ] Closing CTA in the final 2 seconds
- [ ] Reference product photo attached via `medias`
- [ ] Duration is 4–15s (single clip) — if longer, plan multi-clip edit
