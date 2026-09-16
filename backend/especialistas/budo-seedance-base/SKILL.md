---
name: budo-seedance-base
description: Shared foundation for all BUDO Seedance 2.0 on Higgsfield video skills. Defines the real platform specifications, the universal 2-Second Hook framework, universal prompt engineering principles, the visual-quality vocabulary library (4K, 8K, ray tracing, HDRI, anamorphic, etc.), common mistakes, platform delivery optimization, the master prompt template, and the output workflow. ALL category-specific BUDO skills (Cinematic, AnimeAction, FoodBeverage, RealEstate, BrandStory, FashionLook, FightScene, ProductAd, CGI, Cartoon, ComicToVideo, MotionDesign, MusicVideo, Product360, SocialHook) inherit from this file. When generating any Seedance 2.0 prompt, read this skill first to ground platform limits and shared vocabulary, then apply the category-specific skill on top of it.
---

# BUDO Seedance 2.0 on Higgsfield — Shared Foundation

This file is the **single source of truth** for everything that is the same across all BUDO Seedance 2.0 prompt-generation skills. Category skills (Cinematic, AnimeAction, FoodBeverage, FightScene, ProductAd, etc.) extend this foundation with vertical-specific hooks, vocabulary, templates, and examples. Do not repeat platform specs, generic hook theory, the quality vocabulary library, common mistakes, or output workflow inside each category skill — reference this file instead.

---

## 1. Real Seedance 2.0 Platform Specifications (delivery, not prompt vocabulary)

These are the **actual** specs returned by the Higgsfield MCP `models_explore` tool for `seedance_2_0`. Use these numbers when setting the **API parameters** for a generation. They are **not** the same thing as the visual-quality vocabulary you write inside the **prompt text** — see §3 for that.

**Model identifier:** `seedance_2_0`
**Provider:** Bytedance
**Output type:** video

### Parameters

| Parameter | Type | Default | Options |
|---|---|---|---|
| `resolution` | string (optional) | `720p` | `480p`, `720p`, `1080p` |
| `mode` | string (optional) | `std` | `std`, `fast` |
| `genre` | string (optional) | `auto` | `auto`, `action`, `horror`, `comedy`, `noir`, `drama`, `epic` |

### Duration

- **Range:** 4 to 15 seconds (integer values)
- There is no native support for "60-second" or "multi-minute" generations. Longer pieces must be assembled from multiple 4–15s clips in an external editor.

### Aspect ratios

`auto`, `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16`

### Reference media (the `medias` array)

Seedance 2.0 accepts the following media roles via the `medias` input:

- `image` — general reference image
- `start_image` — first-frame anchor
- `end_image` — last-frame anchor
- `video` — motion / style reference clip
- `audio` — audio reference (the model uses it; there is **no** separate `generate_audio` parameter)

### Tags / strengths

`reference`, `identity`, `consistent`, `product`, `multi-sku`, `e-commerce`, `audio-reference`, `video-reference`, `start-frame`, `end-frame`

### Honest constraints

- Maximum delivered output is **1080p**, maximum duration **15 seconds**. (This is separate from prompt vocabulary — see §3.)
- The `genre` parameter is a real lever — use it before reaching for descriptive prose ("noir lighting…") when the user wants one of the six preset moods.
- `mode: fast` trades quality for speed; use it during iteration, switch to `std` for the final pass.

---

## 2. The 2-Second Hook Framework (universal)

Every Seedance 2.0 clip lives or dies in the first ~2 seconds. This is true regardless of category, platform, or audience. Each category skill defines **its own hook library** (e.g., anime eye close-up, drone swoop for real estate, weapon clash for fight scene, beat drop for music video). The shared rules below apply to all of them.

### Why 2 seconds

- On vertical feeds (TikTok, Reels, Shorts), the algorithm bails on videos whose retention drops sharply in the first 2 seconds.
- Human attention commits or scrolls unconsciously in 0.5–2 seconds.
- Even in long-form contexts (YouTube pre-roll, brand films, real estate listings), 2 seconds is when "is this worth my time?" gets answered.

### Rules of a good hook

1. **Visual-first.** Never open on a logo, title card, or talking head explaining what the video is about. Open on the most visually striking moment of the entire clip.
2. **Movement or contrast.** Static perfectly-lit hero shots lose to motion. If you have to open static, make the contrast (color, scale, framing) extreme.
3. **Pose a question the rest of the video answers.** "Wait, where is this?" / "What is that?" / "What happens next?" The hook plants the question; seconds 2–15 pay it off.
4. **Don't waste the hook on context.** Establish context in seconds 2–4. The hook itself is the bait.
5. **Match the hook to the genre param.** If you set `genre: action`, the hook should be kinetic. If `genre: drama`, the hook should be charged but quieter (a held look, a single object).

### Universal hook shortlist (works in any category)

- **Scale shift** — start tiny, pull out to massive; or start massive, push in to tiny detail.
- **Impossible angle** — POV positions a normal camera can't physically occupy.
- **Movement into frame** — subject enters from offscreen with motion blur, then settles.
- **Light hit / reveal** — darkness or silhouette → sudden directional light reveals the subject.
- **Texture macro** — extreme close-up of a surface (fabric, skin, water, metal) before pulling out.
- **Reaction first, cause second** — show the effect (a flinch, a smile, a shockwave); withhold the cause for 1–2 seconds.

---

## 3. Visual-Quality Vocabulary Library (prompt language, NOT delivery specs)

**Critical distinction:** terms like "4K", "8K", "60fps", "ray-traced", "HDRI", "anamorphic" do **two completely different things** depending on where they live:

- **As API parameters** (§1): they would be specs of the actual rendered file. Seedance 2.0 caps at 1080p, so most of those numbers can't be set as parameters.
- **As prompt vocabulary** (this section): they are **signals to the model about the visual register you want** — sharpness, depth, polish, professional production value. They steer the aesthetic. You write them inside the prompt text, and the model uses them to push the output toward that visual quality even though the actual file is delivered at 1080p.

This is standard practice in AI video/image prompting. The model has been trained on data labeled with these terms tied to high-quality references, so the terms work as quality signals even when the literal spec is out of range.

**Use this vocabulary freely inside prompts. Do not write these into the API `resolution` parameter.**

### 3.1 Resolution & sharpness signals (puxar nitidez e detalhe)

Use these to push for crisp detail, edge clarity, and absence of compression artifacts:

`4K`, `8K`, `ultra-HD`, `ultra high resolution`, `crisp detail`, `tack-sharp focus`, `pixel-perfect`, `no compression artifacts`, `clean edges`, `hyper-detailed`, `microscopic texture detail`, `every fiber visible`, `every pore visible`, `photographic clarity`.

### 3.2 Frame rate & motion signals (puxar suavidade ou cadência)

- High-fps signals (suave / hiper-real): `60fps`, `120fps`, `240fps`, `ultra-smooth motion`, `slow-motion clarity`, `high-speed cinematography`, `phantom-style slow-mo`.
- Filmic-fps signals (cinematográfico / com texture de cinema): `24fps cinematic cadence`, `film-rate motion`, `theatrical 24p`, `motion blur per frame`.

### 3.3 Render-engine & 3D signals (puxar look fotorrealista ou estilizado-render)

For CGI / 3D / product-vis verticals, these engine names are strong style anchors:

`Octane Render`, `Blender Cycles`, `Unreal Engine 5`, `UE5 cinematic`, `Arnold render`, `V-Ray`, `RenderMan`, `Redshift`, `Corona Renderer`, `Houdini Mantra`, `Cinema 4D physical render`.

Lighting/physics signals that ride alongside engines:

`ray-traced reflections`, `ray-traced global illumination`, `path-traced lighting`, `physically-based rendering`, `PBR materials`, `subsurface scattering`, `SSS`, `caustics`, `volumetric lighting`, `volumetric fog`, `HDRI environment`, `image-based lighting`, `IBL`, `bounce light`, `radiosity`, `ambient occlusion`, `screen-space reflections`.

### 3.4 Camera & lens signals (puxar look profissional de câmera real)

Lens characteristics:

`anamorphic lens`, `anamorphic 2.39:1`, `anamorphic flare`, `cinemascope`, `Cooke S4`, `Zeiss Master Prime`, `Arri Signature`, `vintage lens character`, `Petzval bokeh`, `oval bokeh`, `shallow depth of field`, `f/1.4 bokeh`, `f/1.2 cinematic depth`, `35mm full-frame look`, `medium-format depth`.

Camera bodies (as quality signals):

`shot on ARRI Alexa`, `shot on RED Komodo`, `shot on Sony Venice`, `shot on Blackmagic URSA`, `shot on IMAX`, `shot on Phantom Flex`, `shot on 70mm film`, `shot on 35mm film`, `shot on 16mm`, `shot on Super 8`.

Camera movement (as polish signals):

`gimbal-stabilized`, `Steadicam shot`, `dolly track`, `crane shot`, `jib arm`, `MoVI gimbal`, `Technocrane`, `Russian Arm car mount`.

### 3.5 Lighting signals (puxar polimento profissional)

`three-point lighting`, `key-fill-rim setup`, `softbox key`, `book light`, `bounce fill`, `negative fill`, `practical lighting`, `motivated lighting`, `golden hour`, `blue hour`, `magic hour`, `chiaroscuro`, `Rembrandt lighting`, `butterfly lighting`, `clamshell lighting`, `Kelvin-accurate white balance`, `3200K tungsten`, `5600K daylight`, `mixed color temperature`.

### 3.6 Color & grade signals (puxar acabamento de pós)

`color-graded`, `DaVinci Resolve grade`, `teal-and-orange`, `bleach bypass`, `cross-process`, `film stock emulation`, `Kodak Vision3`, `Fujifilm Eterna`, `Portra 400 look`, `Ektachrome look`, `LUT applied`, `ARRI LogC`, `RED IPP2`, `cinema color science`, `Rec. 709`, `DCI-P3 gamut`, `HDR grade`, `Dolby Vision`, `10-bit color`, `wide color gamut`.

### 3.7 Film & texture signals (puxar autenticidade analógica)

`35mm film grain`, `16mm grain`, `Super 8 texture`, `halation`, `lens breathing`, `gate weave`, `film burn`, `analog imperfection`, `light leaks`, `vignetting`, `lens vignette`, `slight barrel distortion`, `chromatic aberration on highlights`.

### 3.8 Production-value signals (puxar percepção de "isto custou caro")

`broadcast-quality`, `theatrical-quality`, `feature-film production value`, `Super Bowl commercial polish`, `Apple-keynote-grade`, `Vogue editorial`, `Vanity Fair cover`, `Architectural Digest interior`, `Michelin-quality food cinematography`, `Madison Avenue ad polish`.

### How to use the library

- **Layer 2–4 terms from different subsections** rather than stacking 8 from one subsection. Example: `8K` (3.1) + `anamorphic` (3.4) + `teal-and-orange grade` (3.6) + `35mm grain` (3.7) reads as "modern cinematic feature film".
- **Match the layer to the genre param.** If `genre: drama`, lean §3.4 / §3.5 / §3.6. If `genre: action`, add §3.2 high-fps + §3.4 gimbal. If `genre: horror`, lean §3.5 chiaroscuro + §3.7 analog grit.
- **Don't contradict yourself.** "Shot on iPhone 15" + "shot on ARRI Alexa" in the same prompt confuses the model. Pick one register and commit.
- **The vocabulary is additive, not magical.** It steers the look but cannot rescue a vague hook or weak action description. §4's specificity rule still applies.

---

## 4. Universal prompt-engineering principles

These apply to every category. Each category skill adds its own vocabulary on top.

### Specificity beats adjectives

| Vague | Specific |
|---|---|
| "fast" | "3 ft/s lateral dolly" |
| "shallow depth of field" | "f/1.4, focus on the eyes, background bokeh" |
| "warm lighting" | "3000K key from camera left, 1.5 stops above fill" |
| "intense fight" | "three-step backward retreat, two parries on the forearms, pivot 45°, elbow to ribs" |
| "make it look cinematic" | "anamorphic 2.39:1, lens flare on highlights, halation on practicals, film grain" |

Vague prompts get generic outputs. Specific prompts get directable outputs.

### Visual information only

Seedance 2.0 renders what is **seen**, not what is **felt**. Translate internal states into visible cues:

- ❌ "the character feels sad"
- ✅ "shoulders slumped, head tilted down, single tear forming at the inner corner of the eye, mouth in a slight frown, eyebrows tilted inward-upward"

### Structure the prompt in labeled sections

Long unstructured paragraphs are parsed worse than the same content split into labeled blocks. Use a sectioned structure (see §7 for the master template).

### Lead with the hook

The first sentence of the prompt should describe the first second of the video. Don't bury the hook under setup; the model weighs early tokens more heavily.

### Use timing markers

Seedance 2.0 responds to explicit timing inside the prompt:
- "At 0.8s, the camera begins to push in."
- "From 2.0s to 4.5s, hold on the subject's face."
- "Final beat at 6.0s: cut to black."

### Don't fight the model's strengths

Seedance 2.0 is **reference-driven** (its main differentiator). When the user has reference images, character photos, product shots, or audio, **pass them via the `medias` array** rather than describing them in words. The model will hold identity and material fidelity better from a reference than from a description.

### Use the `genre` parameter before describing genre in prose

If the user wants noir, set `genre: noir` — don't only say "noir lighting, hard shadows, venetian blinds" in the prompt. Use the parameter **and** the prose for additive effect.

---

## 5. Universal common mistakes (and how to fix them)

These show up in every category. Category skills only need to document mistakes that are **specific to their domain** (e.g., "anime = big eyes only" stays in the AnimeAction skill).

### Mistake A — The hook isn't a hook

**Symptom:** Opens on a logo, a title card, an establishing wide shot, or a slow fade-in.
**Fix:** Pick a hook from §2 or from the category's hook library, and make it the first sentence of the prompt.

### Mistake B — Vague descriptors instead of specifications

**Symptom:** "fast", "warm", "moody", "epic", "cinematic", "intense".
**Fix:** Replace each vague word with a measurable specification (numbers, named techniques, named references). Layer in §3 vocabulary for visual register.

### Mistake C — Describing internal states instead of visual cues

**Symptom:** "the character is determined / nervous / proud / heartbroken".
**Fix:** Translate to the body, face, light, and color cues that *show* that state.

### Mistake D — Confusing prompt vocabulary with API parameters

**Symptom:** Setting `resolution: 4K` in the API call (rejected — max is 1080p), or alternately, refusing to write "8K, ray-traced" in the prompt text because "the model can't deliver that."
**Fix:** §1 governs API parameters (max 1080p / 15s). §3 governs prompt text (write 4K/8K/60fps freely — it's quality vocabulary). Both can be true in the same generation.

### Mistake E — Burying the prompt under adjectives

**Symptom:** Three lines of mood words before anything actually happens.
**Fix:** Lead with the action and the camera. Atmospheric words go in modifiers, not in the lead.

### Mistake F — Ignoring aspect ratio for the destination platform

**Symptom:** Generating 16:9 then complaining TikTok crops the sides.
**Fix:** Pick aspect ratio from the §6 platform table *before* writing the prompt.

### Mistake G — Single monolithic prompt with no structure

**Symptom:** 300-word paragraph with no section breaks.
**Fix:** Use the master template in §7 with explicit `[OPENING HOOK]`, `[ACTION]`, `[CAMERA]`, `[LIGHTING]`, `[CLOSE]` sections.

### Mistake H — Reference media described in words instead of attached

**Symptom:** "a character that looks like a young woman with red hair, freckles, green eyes, wearing a leather jacket…" repeated across multiple prompts hoping for consistency.
**Fix:** Train a Soul character or pass the reference image via `medias` with role `image` or `start_image`. The model's identity-consistency feature works from references, not descriptions.

### Mistake I — Contradictory quality vocabulary

**Symptom:** "shot on iPhone, vintage VHS, IMAX 70mm" in the same prompt.
**Fix:** Pick one register from §3 and commit. Layer across subsections, not within them.

---

## 6. Platform delivery optimization (aspect ratio / duration cheat-sheet)

Pick the row that matches the user's destination *before* writing the prompt. This replaces the per-skill "Platform Optimization" sections — category skills should only call out platform notes that are genuinely category-specific (e.g., "Zillow accepts 5-minute walkthroughs" lives in the RealEstate skill).

| Destination | Aspect | Duration (per Seedance clip) | Hook window | Notes |
|---|---|---|---|---|
| TikTok | 9:16 | 4–15s per clip; total 15–60s edited | 0–1s | Trending audio matters. Captions expected. |
| Instagram Reels | 9:16 | 4–15s per clip; total 15–30s | 0–1s | Muted by default — captions essential. |
| Instagram Feed | 1:1 or 4:5 | 4–15s | 0–2s | Thumbnail-friendly first frame. |
| YouTube Shorts | 9:16 | 4–15s; total ≤60s | 0–2s | Loop-friendly endings boost retention. |
| YouTube standard | 16:9 | 4–15s per shot; assemble longer | 0–3s (pre-skip) | Captions boost engagement ~20–30%. |
| LinkedIn | 16:9 or 1:1 | edited 30–90s | 0–3s | Professional tone; muted-default. |
| Website hero | 16:9 or 21:9 | edited 10–30s, looping | 0–2s | Auto-play muted; loop seamlessly. |
| Amazon / Shopify product page | 16:9 or 1:1 | edited 15–30s | 0–2s | Clear product visibility from second 1. |
| Zillow / real estate portals | 16:9 | edited up to 2–5 min | 0–2s | Audio narration accepted. |
| Cinema / brand film | 21:9 | edited any length | 0–3s | Letterboxed; color grading matters most. |

---

## 7. Universal master prompt template

Every category skill should produce prompts that fit this skeleton. Categories add their own vocabulary inside each section; they don't reinvent the skeleton.

```
[GENRE / STYLE]
- Set the Seedance genre parameter explicitly (auto / action / horror / comedy / noir / drama / epic).
- Name the visual style (cinematic, anime, cel-shaded cartoon, photoreal product, CGI, etc.).
- Layer in 2–4 quality-vocabulary terms from §3 (resolution signal + camera signal + grade signal + texture signal).
- Name the dominant color palette and tonal register.

[OPENING HOOK — 0 to ~2s]
- Pick from the category's hook library (or §2 universal list).
- Describe the exact first frame and the motion that follows.
- This is the first sentence of the prompt.

[MAIN ACTION — ~2s to ~12s]
- Subject + action + spatial relationships.
- Visible emotional cues, not internal states.
- Timing markers ("at 4.2s, …").

[CAMERA]
- Lens / focal length / depth of field.
- Movement (static / pan / push / pull / dolly / orbit / handheld).
- Speed in physical units when possible.
- Optionally a §3.4 "shot on …" signal for register.

[LIGHTING]
- Key direction, color temperature in K, ratio to fill, practicals.
- Time of day / weather / atmosphere.
- Optionally a §3.5 named setup ("Rembrandt", "chiaroscuro", etc.).

[COLOR & GRADE]
- Palette, saturation, contrast.
- Optionally a §3.6 named grade ("teal-and-orange", "bleach bypass", film stock).

[CLOSING BEAT — last ~1–2s]
- Where the eye should land at the final frame.
- Loop-friendly if the destination needs looping.

[TECHNICAL — API parameters, not prompt text]
- resolution: 480p / 720p / 1080p
- mode: std / fast
- genre: auto / action / horror / comedy / noir / drama / epic
- aspect_ratio: from §6
- duration: 4–15
- medias: list any reference images / videos / audio passed in by the user
```

---

## 8. Output workflow — what to deliver to the user

When any category skill produces a prompt, structure the response like this:

1. **Brief plan** (1–3 sentences): the chosen hook, the chosen genre/style, the destination platform, and why.
2. **The prompt block** in the master template above, ready to paste.
3. **Recommended Seedance 2.0 API parameters** as a small block:
   ```
   model: seedance_2_0
   resolution: 1080p
   mode: std
   genre: <picked value>
   aspect_ratio: <picked value>
   duration: <4–15>
   ```
4. **Reference-media advice** (one line): which references the user should attach via `medias`, if any.
5. **Iteration tip** (one line): the single most likely thing to tweak on the next pass.

Do **not** pad responses with marketing language about how powerful the platform is — that belongs in this shared file, not in every reply. The user already knows; they want the prompt.

---

## 9. How category skills inherit from this file

A category skill (e.g., `budo-seedance-cinematic`, `budo-seedance-anime-action`, `budo-seedance-food-beverage`) is responsible **only** for:

- Its own hook library (10+ hooks specific to the vertical).
- Its own vocabulary table — vertical-specific terms (lens choreography for fight, plating for food, drone moves for real estate, etc.) that aren't already in §3.
- Its own master-template *variant* — the same skeleton from §7 with vertical-specific section labels and example content.
- Its own example prompts (3–5 complete prompts, ready to paste).
- Mistakes that are unique to the vertical (not the universal ones in §5).
- Platform notes only when the vertical has a destination that isn't in §6 (e.g., Zillow for real estate, App Store preview for app demos).

A category skill should **not** repeat:

- The platform specs from §1.
- The general theory of why hooks matter (§2 lead-in).
- The visual-quality vocabulary library (§3) — reference it instead.
- The universal prompt-engineering principles (§4).
- The universal common mistakes (§5).
- The general platform-by-platform table (§6).
- The master-template skeleton (§7).
- The output workflow (§8).

If a category skill needs to override something here (e.g., "for real estate, hold the hook a beat longer — 2.5s instead of 2s"), it should say so explicitly with a one-line override note, not by re-stating all of §2.
