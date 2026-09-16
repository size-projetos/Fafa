---
name: budo-seedance-anime-action
description: Generate anime-style video prompts for Seedance 2.0 on Higgsfield. Use whenever the user wants anime, Japanese animation style, shonen action, seinen drama, magical girl, mecha, isekai, slice-of-life anime, or any Japanese animation aesthetic. Triggers on: anime, Japanese animation, shonen, seinen, manga style video, anime fight, anime opening, anime ending, sakura, chibi, kawaii, mecha, isekai, or any anime-style request. Use even for "make it look like an anime" or "Japanese cartoon style." Reads BUDOSKILL_Seedance_Base.md first for platform specs, the 2-Second Hook framework, the visual-quality vocabulary library, common mistakes, platform delivery, master template, and output workflow.
---

# BUDO — Anime-Style Videos for Seedance 2.0 on Higgsfield

> **Inherits from `BUDOSKILL_Seedance_Base.md`.** Read that file first for platform specs, universal hook theory, quality vocabulary, prompt principles, common mistakes, platform table, master template, and the output workflow. This file adds only what's **specific to anime-style video.**

---

## 1. What this vertical optimizes for

Anime is **not** "cartoon animation." It is a sophisticated Japanese animation tradition with distinct visual language, aesthetic principles, and storytelling conventions that evolved over decades. Generating authentic anime requires understanding how anime achieves its signature look through deliberate artistic choices, not accident.

Key principle: anime uses **limited animation with impact frames** — rather than smooth 24fps motion, key frames are strategically placed where they matter most, creating dynamic visual rhythm. The gaps between frames aren't lazy; they're intentional. Combined with dramatic lighting, color psychology, and deliberate silence, this creates emotional intensity impossible in Western animation.

Override on Base §3 quality vocabulary: anime does **not** want photoreal vocabulary. Drop "ray-traced", "8K", "shot on ARRI" — they fight the cel-shaded aesthetic. Use instead: "cel-shaded 2D", "limited animation 12fps internal", "anime keyframes", "Studio Trigger polish", "Ghibli watercolor backgrounds", "ufotable digital cel".

---

## 2. Anime hook library (12 hooks)

1. **Dramatic Eye Close-Up with Light Reflection** — Eyes are the soul of anime. Extreme close-up of an iris with star-shaped highlight or color gradation. 0.5s of stillness, then pupil contraction or expansion as the scene "activates."
2. **Speed Line Burst** — Straight perspective lines emanating from center or trailing an object, indicating sudden motion. Combine with slight zoom-in or object entrance.
3. **Transformation Sequence Flash** — White light obscures the screen, then pulls back to reveal a transformed state. The flash lasts 0.3s max.
4. **Blade Unsheath with Metal Gleam** — Sword being drawn; the moment it clears the sheath, a brilliant light reflection flashes. Pair with sharp implied sound and slight slowdown.
5. **Power-Up Aura Explosion** — Glowing energy (electric blue, golden, or purple) radiates in layers from a character, with particles trailing and momentarily distorting the background.
6. **Cherry Blossom Wind Gust** — Sakura petals swirl across frame in a gust, semi-translucent on invisible currents. Establishes "anime romance" or "nostalgia" mood.
7. **Anime Title Card Slam** — Bold stylized text (katakana, kanji, or English) appears with dynamic perspective, rotating into place from off-screen.
8. **Character Silhouette Against Dramatic Sky** — Character in silhouette against golden sunset, blue twilight, or storm clouds. Sky fills 60–70% of frame.
9. **Impact Frame with Cross-Shaped Highlight** — Punch, blade strike, or collision frozen with a bright cross-shaped highlight at center. 0.2–0.4s hold.
10. **Chibi Reaction Pop** — Character suddenly appears in exaggerated chibi proportions with oversized expression — surprise, anger, or cuteness.
11. **Sweat Drop Reaction** — Single bead of sweat appears on face/head, reflecting light, and falls — implying nervousness, effort, or comedy.
12. **Screen Tone Shift** — Image momentarily overlays with a halftone pattern or diagonal lines (manga-reminiscent). Lasts 0.1–0.3s.

---

## 3. Anime Aesthetic Philosophy (use throughout the prompt)

**Limited animation with impact frames.** Don't ask for smooth 24fps motion everywhere. Specify "limited animation, 12fps internal motion, with key impact frames held for 0.3s".

**Cel-shaded flatness.** Avoid gradients. Anime light is delineated by hard edges between shadow zones and highlight zones, not soft falloff.

**Color as emotion.** Saturation is intentional and dramatic — over-saturated for power moments (140%+), desaturated for melancholy (60–70%).

**Silence matters.** The pause before a strike, the held look before a reveal — anime breathes deliberately. Build in 0.2–0.5s holds.

**Hair physics defy gravity.** Hair floats, flutters, spikes against physics. Embrace it; don't request "realistic hair motion."

---

## 4. Anime genre guide (11 visual languages)

Match the user's intent to the right genre, then layer hooks and effects accordingly.

**1. Shonen Action** — Explosive, high-energy, bold colors. Speed lines + impact frames + power-up auras. Saturated primaries (reds, golds, blues). *Examples: Dragon Ball, Naruto, My Hero Academia.*

**2. Seinen Drama** — Dark, introspective, muted/cold palette. Limited animation with long static shots. Dramatic rim lighting, underlit faces. *Examples: Psycho-Pass, Monster, Ergo Proxy.*

**3. Magical Girl** — Whimsical, colorful, symmetrical. Transformation animations, twirls, light flashes. Sparkle effects, pastel + bright accents. Warm golden hour lighting. *Examples: Sailor Moon, Cardcaptor Sakura, Madoka Magica.*

**4. Mecha** — Metallic, industrial, imposing. Heavy reflections on metal. Rigid geometric movement. Neon cockpit lights. Tall camera angles looking up. *Examples: Gundam, Evangelion, Macross.*

**5. Isekai Fantasy** — Expansive, magical, otherworldly. Vibrant saturated palette. Glowing runes, portal effects, spell circles. Ethereal volumetric lighting. *Examples: Re:Zero, SAO, Slime.*

**6. Slice-of-Life** — Warm, nostalgic, grounded, comedic. Golden hour palette. Minimal speed lines, gentle motion. Soft watercolor backgrounds. *Examples: K-On!, Nichijou, Laid-Back Camp.*

**7. Sports Anime** — Dynamic, competitive, triumphant. Speed lines + impact frames for athletic motion. Slow-motion replays. Dramatic close-ups of determined faces. *Examples: Haikyuu!!, Kuroko's Basketball, Free!*

**8. Horror / Dark Anime** — Unsettling, shadowy. Desaturated cold palette (grays, sickly greens, purples). Heavy shadows, limited fill. Grainy film texture. *Examples: Jujutsu Kaisen, Demon Slayer, Attack on Titan.*

**9. Romance / Comedy** — Light, expressive, emotionally immediate. Pastel + warm tones. Sparkle and flower effects. Quick comic timing. *Examples: Kaguya-sama, Toradora!, Quintessential Quintuplets.*

**10. Cyberpunk / Sci-Fi Anime** — Futuristic, neon, high-tech. Dark backgrounds + neon accents (cyan, magenta, yellow, lime). Holographic overlays. *Examples: Ghost in the Shell, Akira, Cyberpunk Edgerunners.*

**11. School / Supernatural** — Ambiguous between mundane and magical. Warm base palette disrupted by otherworldly effects. *Examples: Haruhi Suzumiya, Jujutsu Kaisen.*

---

## 5. Anime-Specific Visual Effects Library (23 effects)

Reference these directly in prompts.

**Motion & Energy:** speed lines (streaks), impact frames, smear frames, motion blur trailing, pulsing glow, aura emission.

**Impact & Emotion:** white flash (impact light), screen shake, cross-shaped highlight, dramatic shadow drop.

**Particle & Environmental:** sakura petals, spark burst, dust cloud, water droplets, fire/flame effect (stylized, not realistic).

**Character Reactions:** chibi pop, sweat drop, anger veins (purple/red on forehead), blush circles, sparkle eyes.

**Screen & Digital:** screen tone overlay (halftone/diagonal), digital glitch, onomatopoeia text ("BOOM", "CRASH" in dynamic position).

---

## 6. Character Design Keywords

**Proportions:** large eyes (1/3 face width), small mouth (1/10 face), defined jawline, oversized head in action designs, thin limbs.

**Eye styles:** tsurime (cat eyes, outer corners high — sharp/confident), tareme (round eyes, outer corners low — innocent/kind), star eyes (excitement), cross eyes (impact moments), ringed iris (unusual power), slit pupils (supernatural), blank stare (comedy).

**Hair physics:** spiky hair (gravity-defying points), long flowing hair (moves as single unit), twin tails (exaggerated swing), hime cut (rectangular side locks, noble female), ahoge (single strand sticking up — main character / airhead signal), silky sheen (bright highlight streaks).

**Clothing:** sailor uniform, harem pants (fantasy/isekai), tactical gear (action), formal kimono (ceremonial), pajamas/athletic wear (slice-of-life), gender-ambiguous designs (shoujo).

---

## 7. Anime master-template additions

Layer onto Base §7. Quality vocab uses anime-specific terms, NOT the photoreal vocabulary from Base §3:

```
[ANIME-SPECIFIC QUALITY VOCAB]
Replace Base §3 photoreal terms with: "cel-shaded 2D, hand-drawn keyframes,
limited animation 12fps internal with 24fps base, anime aesthetic, Studio
Trigger / Ufotable / Ghibli polish, 4K crisp linework, saturated primary
palette" (or genre-appropriate equivalents).

[GENRE TAG]
Explicit anime genre from §4: shonen / seinen / magical-girl / mecha /
isekai / slice-of-life / sports / horror / romance / cyberpunk / school.

[CHARACTER DESIGN]
Eyes (style + color + highlight shape), hair (physics + length + color),
face proportions, clothing.

[EFFECTS LAYER]
2–4 effects from §5 keyed to specific timestamps.

[IMPACT FRAME PLACEMENT]
Identify the single most important impact frame in the clip and specify
its hold duration (0.2–0.4s) and visual treatment.
```

---

## 8. Example prompts (5)

### Example 1 — Shonen Fight Climax (16:9, 8s)

```
Generate an anime-style video using Seedance 2.0 on Higgsfield.

GENRE: Shonen action anime (climactic fight moment)
AESTHETIC: Explosive energy, high impact, dramatic lighting
QUALITY VOCAB: Cel-shaded 2D, 4K crisp linework, limited animation 12fps internal
with 24fps base, Ufotable digital cel polish, saturated primary palette.

DURATION: 8 seconds | ASPECT RATIO: 16:9

[OPENING 2-SECOND HOOK — 0:00-0:02]
Hook: Dramatic Eye Close-Up with Power-Up Aura Explosion.

Open on an extreme close-up of a male anime character's eye. The iris is
golden-amber with a four-pointed star-shaped highlight. As the eye fills the
frame, a surge of blue electric aura radiates outward from behind the head,
visible at the edge of frame. The aura pulses outward in two expanding rings,
with electric sparks trailing in its wake. Speed lines (perspective lines from
behind) zoom past the character's face to indicate acceleration. Eye pupil
contracts sharply at 0.1 seconds into the scene.

Camera zoom-out reveals the character's determined face, spiky dark hair
floating upward with impossible wind physics. A collar or clothing is visible
at frame bottom.

Art style: Cel-shaded 2D anime character on slightly abstracted blue-electric
background. Lighting: Rim light from electric aura (bright blue on edges of
face). Shadows on face are dark navy, not gradients. Highlights on cheekbones
and forehead are stark white.

Color palette: Deep blues, electric cyan, black shadows, white highlights,
skin warm peachy tone. Saturation: 140% (over-saturated for power moment).

Sound design: Electronic power-up charge tone (ascending pitch) reaching
crescendo at 0.5 seconds, followed by orchestral impact sting at 1.0 seconds.

[SCENE 1 — 0:02-0:05]
SETTING: Open valley at sunset. Golden-orange sky fills upper 70% of frame.
Ground is rocky, sparse grass. Two combatants face each other at opposite
frame edges, roughly 20 meters apart. Dramatic lighting from sun low on
horizon. Deep blue shadows on ground. Volumetric light rays visible in
dust-filled air between them.

MAIN ACTION: Character A (from previous eye close-up) stands at frame left in
power stance — legs planted shoulder-width apart, fists clenched. Aura of
electric blue energy surrounds full body in a 1-meter radius. Second
character (opponent) at frame right in neutral stance, watching.

ANIMATION STYLE: Character A's aura pulses with 0.3-second rhythm (expand,
retract, repeat). Hair and clothing flutter in response to aura pressure.
Limited animation: character body is stationary, only aura and hair moving.
Extreme 2-frame (12fps internal) movement for aura pulsing.

LIGHTING: Rim lighting on Character A from sun behind and to right — golden
outline on left silhouette. Heavy directional light from sunset creates long
shadows stretched across ground toward right. Character B is partially
backlit, appears in silhouette.

SPECIAL EFFECTS:
- Aura: Electric blue glow, 4-5 concentric rings expanding and retracting
- Sparks: White/yellow spark particles drift upward
- Speed lines: Subtle radial lines outward (contained explosive energy)
- Dust: Tan/gray particles swirl at feet
- Screen tone: Brief 0.2-second diagonal line pattern at 0.3s into scene

[SCENE 2 — 0:05-0:08]
SETTING: Same valley, rocky ground cratered at center between combatants.
Dust cloud fills lower half. Sky remains golden-orange above dust layer.

MOVEMENT SEQUENCE:
- 0:05.0-0:05.2: Character A contract pose, static hold, speed lines radiating
- 0:05.2-0:05.5: Launch forward, speed lines + blue aura motion-blur trail
- 0:05.5-0:06.0: Mid-attack smear frame — elongated/blurred extreme speed
- 0:06.0-0:06.3: IMPACT FRAME — white flash covers center 60%, fist contact
  (implied), cross-shaped highlight at impact point, 0.3s hold
- 0:06.3-0:08.0: Character B blown backward, mouth open in shock, glossy
  sweat drop falling, speed lines trail behind B's motion

EFFECTS: Motion blur trail (soft blue streaks behind A), impact flash
(white, center 60%), impact cross (bright white at fist point, 0.2s),
dust burst (tan/gray particles), afterimage (2–3 ghosted forms of A).

[AUDIO]
0:00-0:05: Rising orchestral strings + electronic power charge
0:05.0: Dramatic orchestral sting (full brass)
0:06.0: Impact crash (heavy resonant bass + high metallic crash)
0:06.3-0:08: Tense strings, B's reaction

[TECHNICAL]
resolution: 1080p; mode: std; genre: action; aspect_ratio: 16:9; duration: 8;
medias: [character reference image as role=image if available]
```

### Example 2 — Slice-of-Life Peaceful Morning (16:9, 6s)

```
GENRE: Slice-of-life anime
QUALITY VOCAB: Cel-shaded 2D, hand-drawn keyframes, Ghibli watercolor
backgrounds, soft 24fps, warm pastel palette, 4K crisp linework.

[OPENING HOOK — 0:00-0:02]
Hook: Cherry Blossom Wind Gust over a quiet morning street. Pink sakura
petals drift diagonally across frame on invisible wind, semi-translucent.
Camera tilts down slowly to reveal a young female character walking to school,
satchel over shoulder.

[MAIN — 0:02-0:05]
Walk continues at relaxed pace. Hair moves gently. She lifts her face slightly,
eyes closed for a moment, breathes in the morning air. At 3.5s she opens her
eyes (tareme style, kind/innocent) — small soft highlight reflects the bright
sky. Bird flies past upper-right corner.

LIGHTING: Warm golden 4500K morning sun from camera left, low angle, casting
long soft shadows. Cel-shaded with hard edges between sun-side and shadow-side.
Sky is pale blue with soft cloud watercolor wash (Ghibli style).

COLOR: Pastels — pale pink (petals), pale blue (sky), warm cream (skin),
soft brown (uniform), golden green (foliage). Saturation 80%.

[CLOSE — 0:05-0:06]
She smiles softly, looking forward. Final frame holds her in golden side-light
as petals continue across frame.

EFFECTS: Sakura petals throughout, single sparkle on her eye at 3.7s.

[TECHNICAL]
resolution: 1080p; mode: std; genre: drama; aspect_ratio: 16:9; duration: 6
```

### Example 3 — Mecha Battle Spectacle (21:9, 10s)

```
GENRE: Mecha anime
QUALITY VOCAB: Cel-shaded 2D with detailed mechanical inking, Sunrise studio
polish, 4K crisp linework, dramatic chiaroscuro on metal, neon cockpit pops.

[OPENING HOOK — 0:00-0:02]
Hook: Impact Frame with Cross-Shaped Highlight. A 20-meter humanoid mecha
clashes weapons mid-air with an opposing mecha — frozen frame, bright cross
highlight at the blade contact point, sparks frozen radially. 0.4s hold.

[MAIN — 0:02-0:08]
Hold releases. Both mechas push off each other, spinning backward through the
air. Camera tracks the friendly mecha (blue/white) as it lands hard on debris
field. Cockpit interior cut at 4.0s: pilot's face lit by red warning lights,
hands gripping controls. Cut back at 5.0s: mecha rises, raises a beam sword
(neon cyan blade). At 6.5s, lunges forward toward opponent.

LIGHTING: Rim lighting on metal surfaces — hard white edges, deep black core
shadows. Neon accent: cyan from sword, red from cockpit interior. Background:
ruined cityscape at dusk, deep purple sky.

COLOR: Steel grays, blacks, white rim highlights, cyan and red neons.
Saturation 90% overall, 150% on neon elements.

[CLOSE — 0:08-0:10]
Mecha mid-lunge with sword extended forward, frozen at peak extension.
Onomatopoeia text "ZAN" appears in stylized katakana, lower-right.

EFFECTS: Spark burst (impact), motion blur on mecha rotations, neon glow
(sword + cockpit), digital glitch on HUD overlay 4.2s.

[TECHNICAL]
resolution: 1080p; mode: std; genre: action; aspect_ratio: 21:9; duration: 10
```

### Example 4 — Anime Opening Sequence Style (16:9, 12s)

```
GENRE: Shonen/sports anime OP montage
QUALITY VOCAB: Cel-shaded 2D, MAPPA studio polish, 4K crisp linework, dynamic
saturated palette, anime title-card typography.

[OPENING HOOK — 0:00-0:02]
Hook: Anime Title Card Slam. Black frame. Bold red kanji + English title
explodes into frame from upper-right with rotation, landing center with white
outline and drop shadow. Speed lines burst radially behind it.

[MONTAGE — 0:02-0:11]
Rapid-cut character intros, each held 0.8s:
- 2.0-2.8s: Protagonist sprinting toward camera, determined tsurime eyes, hair
  streaming back, speed lines behind
- 2.8-3.6s: Rival character profile against red sky, smug half-smile, single
  spark drifting up
- 3.6-4.4s: Mentor figure, back to camera, holding weapon at side
- 4.4-5.2s: Female teammate, hair twin-tails, sparkle eyes, palm extended with
  small glowing energy ball
- 5.2-6.0s: Antagonist silhouette against full moon, slit pupils visible in shadow
- 6.0-7.0s: Group shot — five characters posed dynamically, looking up-camera
- 7.0-8.5s: Action montage — punch impact (cross highlight), blade swing
  (metal gleam), explosion (white flash)
- 8.5-11s: Slow push-in on protagonist face, eye close-up, single tear/sweat
  drop, then sudden determined expression, fire aura ignites behind

COLOR: Saturated reds, golds, blues throughout. Saturation 130%.

[CLOSE — 0:11-0:12]
Final logo card with protagonist silhouette over title. Burst of sakura petals
across frame.

[TECHNICAL]
resolution: 1080p; mode: std; genre: action; aspect_ratio: 16:9; duration: 12
```

### Example 5 — Emotional Farewell Scene (16:9, 8s)

```
GENRE: Seinen drama / emotional anime
QUALITY VOCAB: Cel-shaded 2D, KyoAni emotional polish, 4K crisp linework,
desaturated muted palette, limited animation with held expressions.

[OPENING HOOK — 0:00-0:02]
Hook: Dramatic Eye Close-Up. Extreme close-up of a young woman's eye (tareme
style). A single tear forms at the inner corner, swelling, then breaking
free. Slow camera pull-back over 1.5s.

[MAIN — 0:02-0:06]
Pull-back reveals her standing at a train platform at twilight, facing camera.
Behind her, a train begins to move slowly. Wind moves her hair gently. She
holds her arm with the opposite hand — closed body language. Static hold
0.5s on her face at 3.5s; she mouths a word silently.

Cut at 4.5s to a young man's face inside the train, looking out window at her,
mouth slightly parted, pupils slightly dilated (held shock/sorrow). Static
hold 0.8s. Train begins to accelerate.

LIGHTING: Cool 4000K blue twilight from above. Single warm sodium platform
lamp from camera right adds amber rim on left side of her face. Cel-shaded
hard edges between blue and amber zones.

COLOR: Desaturated 65%. Cool blues dominate, single warm amber accent on her
face. Black for her clothing, muted gray for the train.

[CLOSE — 0:06-0:08]
Slow camera return to her face. Train sound fades. She closes her eyes. Single
sakura petal drifts past — out of season, unexplained. Final frame: her face
in half-shadow, eyes closed, petal floating away.

EFFECTS: Single petal, slight glow on the amber rim light, no speed lines (this
genre uses stillness).

[TECHNICAL]
resolution: 1080p; mode: std; genre: drama; aspect_ratio: 16:9; duration: 8
```

---

## 9. Anime-specific mistakes (in addition to Base §5)

- **Anime = big eyes only.** Anime is a holistic visual language: hair physics, color saturation, speed lines, impact frames, limited animation, watercolor or detailed backgrounds. Eyes are one element among many.
- **Confusing anime with cartoon.** Western cartoons: rounder shapes, softer edges, pastel palettes, exaggeration of form. Anime: sharper lines, defined edges, dramatic lighting, realistic proportions except eyes/hair, color psychology, emotional intensity. Don't write "cartoon anime style" — just "anime style".
- **Static characters in slice-of-life.** Even peaceful anime has micro-animations: hair flutter, blink every 2s, slight breath. Describe these explicitly.
- **Forgetting limited animation philosophy.** Don't ask for smooth movement everywhere. Specify limited animation: 12fps internal, key frames held 0.2–0.4s, smear frames between extremes.
- **Wrong quality vocabulary.** Photoreal terms (ray-traced, shot on ARRI, HDRI) actively fight the anime aesthetic. Use cel-shaded terms instead.
- **Over-saturated default.** Match saturation to genre: shonen action 130–140%, seinen drama 60–70%, slice-of-life pastels at 80%, cyberpunk neons at 150% over dark base.

---

## 10. Final pre-publish checklist

- [ ] Genre from §4 explicitly named
- [ ] Quality vocabulary uses cel-shaded/limited-animation language (not photoreal)
- [ ] At least one impact frame placed with explicit hold duration
- [ ] Character design specified (eyes, hair, proportions)
- [ ] Effects from §5 keyed to specific timestamps
- [ ] Color saturation level appropriate for genre
- [ ] Limited animation philosophy applied (don't overspecify smooth motion)
- [ ] Reference character image attached via `medias` if continuity matters
