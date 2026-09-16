---
name: budo-seedance-cartoon
description: Generate cartoon and animation style video prompts for Seedance 2.0 on Higgsfield. Use whenever the user wants cartoon, 2D animation, cel-shaded, hand-drawn, illustrated, flat animation, or motion graphics animation style video. Triggers on: cartoon, animation, cel shading, hand-drawn, illustrated, flat design animation, vector animation, retro cartoon, rubber hose, motion graphics, or any cartoon/animated style request. Use even for vague requests like "make it look animated" or "fun colorful style." Reads BUDOSKILL_Seedance_Base.md first for platform specs, the 2-Second Hook framework, the visual-quality vocabulary library, prompt principles, common mistakes, platform table, master template, and output workflow.
---

# BUDO — Cartoon & Animation Videos for Seedance 2.0 on Higgsfield

> **Inherits from `BUDOSKILL_Seedance_Base.md`.** Read that file first for all the shared foundation. This file adds only what's **specific to Western cartoon / animation aesthetics.** For Japanese anime specifically, use `BUDOSKILL_AnimeAction.md` instead.

---

## 1. What this vertical optimizes for

Cartoon and Western animation rely on **principles of squash-and-stretch, exaggeration, anticipation, and snappy timing**. Unlike anime (limited animation with held keyframes), classic cartoon uses fluid, often physics-defying motion as a comedic and expressive language.

Override on Base §3 quality vocab: cartoon does NOT want photoreal terms. Drop "ray-traced", "shot on ARRI", "anamorphic". Use instead: "hand-drawn cel animation", "rubber-hose limbs", "flat vector design", "Disney smooth easing", "Warner Bros snappy timing", "Ghibli watercolor backgrounds", "cel-shaded 2D".

---

## 2. Cartoon hook library (10 hooks)

1. **Character Smash-Zoom** — The protagonist violently zooms into the camera plane with exaggerated scale change and comedic impact frames. Eyes bulging, motion blur trails.
2. **Rubber-Hose Stretch Entrance** — A character enters by impossibly stretching limbs/body, then snaps back into proportion with rubbery physics-defying motion.
3. **Color Explosion** — A burst of vibrant color, sparkles, or gradient wash floods the screen.
4. **Fourth-Wall Break** — Character turns to camera with conspiratorial grin and wink, eyebrow raised. Acknowledges the viewer.
5. **Exaggerated Reaction Face** — Enormous facial expression change — eyes pop wide, mouth stretches, face contorts. Holds 0.3–0.5s for comedic impact.
6. **Object Transforms Unexpectedly** — Inanimate object morphs, grows, or shifts shape. Sets surreal/whimsical tone.
7. **Speed-Line Burst** — Curved speed lines, motion trails, or streaks explode across the frame behind primary action.
8. **Particle Shower / Confetti Cascade** — Rapid rain of sparkles, confetti, hearts, stars, or debris.
9. **Blink/Wink Cut** — Character's eyes slam shut, screen goes black for 0.1s, then cut to new scene/angle.
10. **Gravity Flip / Environmental Inversion** — Gravity reverses, objects float upward, character defies physics mid-motion.

---

## 3. Animation Style Encyclopedia (15 styles)

Pick the style first; it determines line weight, color treatment, motion philosophy, and timing.

**1. Classic Disney (1940s–1960s).** Smooth liquid movement, expressive proportions, warm naturalistic palettes with rich gradients, soft anti-aliased 2–3px line work, large sparkling eyes with white pupils. 24fps with slow-in/slow-out easing. *Ideal for fairy tales, emotional moments, magical sequences.*

**2. Cartoon Network / Warner Bros Rubber Hose.** Thick bold black outlines (4–6px), exaggerated impossible anatomy, high-contrast color blocks, comedic "takes", speed lines, impact frames. Snappy 24fps with rapid key-pose transitions. *Ideal for comedy, slapstick, energetic interactions.*

**3. Flat Vector / Modern Minimalist.** Solid color shapes, NO gradients, geometric construction, uniform thin or no outlines, 3–5 color palette per scene. 30 or 60fps smooth mathematical motion. *Ideal for explainer videos, motion graphics, modern apps.*

**4. Retro Rubber Hose (1920s–1930s).** Black-and-white or limited color, noodle-like limbs, dot-and-pie-cut eyes, jazzy fluid motion. Mickey/Felix the Cat lineage. *Ideal for retro / vintage moods.*

**5. Pencil Sketch / Hand-Drawn.** Visible pencil grain, slightly imperfect lines, sketchy shading, monochrome or limited palette. 12–24fps with conscious imperfection. *Ideal for art, journaling, intimate storytelling.*

**6. Watercolor / Painterly.** Soft washes, bleeding edges, atmospheric backgrounds dominate over characters. Ghibli lineage. 24fps slow easing. *Ideal for nature, fantasy, contemplative work.*

**7. Paper Cutout / Papier-Mâché.** Layered flat shapes with visible texture (paper grain, torn edges), parallax depth, limited rotation. South Park / Lotte Reiniger lineage. *Ideal for whimsy, naive aesthetics.*

**8. Pixel Art / 8-bit & 16-bit Retro.** Visible pixel grid, limited palette (16–64 colors), snapping-to-grid motion. 12 or 24fps with chunky animation. *Ideal for gaming, retro nostalgia, tech humor.*

**9. Neon Line Art / Glow.** Black background, glowing line strokes (cyan, magenta, lime), minimal fill, vector-clean motion. *Ideal for futuristic, club, tech-launch aesthetics.*

**10. Manga / Anime.** See `BUDOSKILL_AnimeAction.md` instead.

**11. Stop-Motion / Claymation.** Discrete frame-to-frame jumps, visible texture (clay, felt, paper), 12fps deliberate jerkiness. Aardman / Laika lineage. *Ideal for craft feel, quirky narrative.*

**12. Oil Painting / Impressionist.** Visible brush strokes per frame, painterly textures, color over precise line. *Loving Vincent* lineage. *Ideal for art films, dreams, memory.*

**13. Silhouette / Shadow Puppet.** Pure black silhouettes against backlit color, no internal detail, all read by shape. Lotte Reiniger lineage. *Ideal for fables, mystery, theatrical moments.*

**14. Doodle / Cartoon Comic.** Sketchy outlines, simple shapes, whiteboard or notebook aesthetic, often with handwritten text. *Ideal for explainer, educational, casual content.*

**15. CGI Stylized / 3D Cel-Shading.** 3D models rendered to look 2D — hard cel shadows, outlines on geometry, flat-color fills. *Spider-Verse* and *Arcane* lineage. *Ideal for premium animation, hybrid 2D-3D feel.*

---

## 4. Character Animation Keywords

**Movement principles:** squash-and-stretch (compression on impact, elongation on motion), anticipation (wind-up before action), follow-through (secondary motion after primary), arc motion (no straight-line travel), exaggeration (push every pose beyond realistic), staging (clear silhouette readability).

**Timing:** snappy 24fps with 2-frame holds on extremes; for flat vector use 30/60fps mechanical interpolation; for stop-motion use 12fps with frame-by-frame jumps.

**Facial expression:** rapid eye/mouth shape changes, "takes" (sudden extreme reactions held 0.3–0.5s), pupil dilation/contraction for surprise, mouth shapes that exceed face dimensions for emotion.

**Limb deformation:** rubber-hose limbs (no joints, continuous curves), squash on impact (compresses 30–40% vertically), stretch on speed (elongates 200% during fast motion).

---

## 5. Transition & Effect Library

**Cartoon-specific transitions:** smash cut, iris in/out (Looney Tunes circle wipe), screen wipe with character drag-across, paint splat reveal, page turn, comic panel slide.

**Effects:** speed lines (curved or straight), impact stars (radial bursts on contact), motion smears (one-frame elongation), screen shake on impact (3–5 frames), color flash (white or accent color full-screen for 1–2 frames), sweat drop, anger steam from ears, hearts/stars/birds around dazed head.

---

## 6. Color Palette Guide

**Disney warm:** soft pastels with golden accents, sky blues, sage greens, cream/peach skin tones.
**Warner Bros graphic:** primary saturated colors (red, yellow, blue), black outlines, minimal gradient.
**Flat vector modern:** 3–5 highly saturated tones, hot pink + electric yellow + lime + magenta + black.
**Ghibli natural:** sage greens, golden yellows, sky blues, with watercolor edge bleed.
**Retro rubber hose:** sepia, cream, single accent color (red lips, blue suit).
**Pixel art:** 16-color limited palette, often warm/cold contrast.
**Neon line art:** black base with cyan, magenta, lime, hot pink line glows only.

---

## 7. Cartoon master-template additions

Layer onto Base §7. Quality vocab is cartoon-specific:

```
[ANIMATION STYLE FROM §3]
Pick exactly one style; describe its line weight, color rule, motion rule.

[QUALITY VOCAB — NON-PHOTOREAL]
"Hand-drawn 2D cel animation" or "flat vector design, mathematical motion" or
"stop-motion 12fps with visible material texture" — match to chosen style.

[CHARACTER DESIGN]
Body proportions (rubber-hose / Disney natural / flat geometric / pixel-block),
face design (eye style, mouth shape, line weight), color rule.

[MOVEMENT PRINCIPLES]
Which of §4's principles dominate this clip? (squash/stretch, anticipation,
follow-through, exaggeration)

[TRANSITION / EFFECT LAYER]
Pick 1–3 from §5.

[COLOR PALETTE]
Specific palette from §6 or custom 3–7 colors.
```

---

## 8. Example prompts (4)

### Example 1 — Action Cartoon Sequence (Classic Warner Bros Style, 16:9, 6s)

```
[ANIMATION STYLE]
Cartoon Network / Warner Bros rubber hose. Bold 5px black outlines, rubber
hose proportions, exaggerated anticipation and follow-through.

[QUALITY VOCAB]
Hand-drawn 2D cel animation, snappy 24fps with 2-frame holds on extreme poses,
classic Warner Bros polish.

[OPENING HOOK — 0 to 2s]
Hook: Character Smash-Zoom. Lanky anthropomorphic rabbit with oversized ears
(2x head height), round nose, 3-finger gloves, SMASH-ZOOMS directly into
camera with bulging eyes, motion blur trails, speed-line burst.

[MAIN ACTION — 2 to 5s]
Pull back to reveal vibrant cartoon landscape — rolling green hills, puffy
clouds. Rabbit runs toward camera with rapid leg cycles, launches into a
massive jump. Mid-air: body stretches vertically (rubber-hose stretch), ears
flap like helicopter blades. At 3.5s, fist grows to massive size (squash-stretch
exaggeration) winding up for punch. At 4.2s, impact frame — white flash 0.1s,
character compresses 40% vertically on landing.

[CAMERA] Static wide, brief whip-pan on the jump apex.
[COLOR PALETTE] Warm pastels with bright magenta accent on gloves/nose, golden
yellow hills, sky blue.
[EFFECTS] Speed lines on punch, white impact flash, dust burst on landing.

[CLOSING BEAT — 5 to 6s]
Character rebounds upright in surprised "take" expression — eyes huge, mouth
silent-scream, holds 0.4s.

[TECHNICAL]
resolution: 1080p; mode: std; genre: comedy; aspect_ratio: 16:9; duration: 6
```

### Example 2 — Peaceful Ghibli-Inspired Scene (16:9, 10s)

```
[ANIMATION STYLE]
Studio Ghibli 1990s aesthetic. Soft anti-aliased lines 2px weight, watercolor
backgrounds, naturalistic character proportions.

[QUALITY VOCAB]
Hand-drawn 2D cel animation, watercolor painted backgrounds, 24fps with slow
comfortable easing, Ghibli polish.

[OPENING HOOK — 0 to 2s]
Hook: Atmospheric reveal. Gentle camera pan left across a misty forest
clearing. Golden light rays penetrate the mist; dust particles float lazily.
At 1.5s, a serene character silhouette emerges in the shafts of golden sun.

[MAIN ACTION — 2 to 8s]
Reveal: young girl (8 years old), simple flowered dress, soft wavy hair,
sitting on weathered wooden bench. Hair moves gently with almost-imperceptible
breeze. Chest rises/falls subtle breath. Eyes blink slowly every 2–3 seconds,
gaze distant. At 5s a butterfly drifts past her face; she watches it without
turning her head. At 7s, slight smile.

[CAMERA] Slow continuous pan left throughout, 1ft/s. f-stop irrelevant — this
is painted depth.
[LIGHTING] Directional warm sunlight, golden quality overall. Shadows are
translucent blues and greens, NOT black. Atmospheric perspective with mist
creating depth.
[COLOR PALETTE] Sage greens, golden yellows, sky blues. Watercolor edge bleed
on background elements.
[EFFECTS] Light dust particles, single butterfly, breath visible only as chest motion.

[CLOSING BEAT — 8 to 10s]
Camera comes to rest. Hold on the girl looking off into the trees. Faint
distant bird call (implied audio).

[TECHNICAL]
resolution: 1080p; mode: std; genre: drama; aspect_ratio: 16:9; duration: 10
```

### Example 3 — Flat Vector Explainer / Motion Graphics (1:1, 8s)

```
[ANIMATION STYLE]
Flat vector / modern minimalist. Solid color shapes, NO gradients, geometric
construction, no outlines.

[QUALITY VOCAB]
Flat vector design, 30fps mathematical interpolation, Apple-keynote-grade polish.

[OPENING HOOK — 0 to 1.5s]
Hook: Color Explosion synced to beat. Pure black background. Upbeat electro
musical beat hits. Sun (yellow circle) drops into frame from top at 0.3s.

[MAIN ACTION — 1.5 to 7s]
Wind turbine (teal lines forming triangle) slides in from left at 2.0s.
Battery (orange rectangle) expands from center at 3.0s. Each entrance is a
snappy 0.3s animation, synced to a beat. At 4.5s, all three rearrange into
a flow diagram with thin white connecting lines drawing themselves. At 6s,
the diagram pulses once with the bass.

[CAMERA] Static throughout. No camera moves in flat vector.
[COLOR PALETTE] Yellow #FFD60A, Teal #20B2AA, Orange #FF8C00, white 1px
connector lines, on pure black.
[EFFECTS] Each shape pauses 0.5s once positioned. Precise audio sync.

[CLOSING BEAT — 7 to 8s]
All shapes hold position. Title "Clean Energy. Now." fades up in white,
center-bottom.

[TECHNICAL]
resolution: 1080p; mode: std; genre: auto; aspect_ratio: 1:1; duration: 8;
medias: [optional brand audio as role=audio]
```

### Example 4 — Retro Rubber Hose Short (1:1, 5s)

```
[ANIMATION STYLE]
Retro rubber hose, 1920s style. Black-and-white with single sepia accent.
Noodle-like limbs, dot-and-pie eyes, jazzy fluid motion.

[QUALITY VOCAB]
Hand-drawn 2D cel animation, 24fps with visible film grain, Felix-the-Cat
lineage, retro animation polish.

[OPENING HOOK — 0 to 1.5s]
Hook: Rubber-Hose Stretch Entrance. A small cartoon dog character stretches
across the screen from off-frame-right — body and limbs noodling impossibly,
then snaps into compact stand-pose center-frame at 1.2s.

[MAIN ACTION — 1.5 to 4s]
Dog character does a quick jazz-step shuffle in place, hat (top hat) tilts
side-to-side with each beat. Cane appears in paw via a poof of cartoon smoke
at 2.5s. Dog tips hat at camera (fourth-wall break with wink) at 3.2s.

[COLOR PALETTE] Cream/sepia base, black ink for character, single accent of
red on the hat band.
[EFFECTS] Visible film grain overlay, slight gate weave (subtle frame jitter),
small "BOIIING" onomatopoeia text when cane appears.

[CLOSING BEAT — 4 to 5s]
Dog freezes in tip-hat pose, eyes pie-slice closed in friendly wink. Iris
closes (Looney Tunes circle wipe) to "That's all, folks!" feel.

[TECHNICAL]
resolution: 1080p; mode: std; genre: comedy; aspect_ratio: 1:1; duration: 5
```

---

## 9. Cartoon-specific mistakes (in addition to Base §5)

- **Photoreal quality vocab in a cartoon prompt.** "Ray-traced, shot on ARRI" fights cel-shaded animation. Use hand-drawn / cel / flat vector terms.
- **Confusing cartoon with anime.** Western cartoon: rubber-hose limbs, squash-and-stretch, comedic exaggeration. Anime: limited animation, impact frames, dramatic stillness. Pick one and commit.
- **Missing the animation principle.** Cartoon without squash-and-stretch (or its style equivalent) reads as stiff. Specify the principle.
- **Style mixing without reason.** "Disney + Warner Bros + flat vector" produces visual chaos. Pick one style from §3.
- **Frame-rate mismatch with style.** Flat vector at 12fps reads as broken; Ghibli at 60fps reads as digital. Match fps to the style.
- **Overdetailed backgrounds in flat vector.** Flat vector wants minimal backgrounds; Ghibli wants painted ones. Don't blend.

---

## 10. Final pre-publish checklist

- [ ] Animation style from §3 picked and named
- [ ] Quality vocabulary uses cel/hand-drawn/flat-vector language (NOT photoreal)
- [ ] Frame rate matches the style
- [ ] At least one animation principle from §4 specified
- [ ] Color palette from §6 (or appropriate custom)
- [ ] One hook from §2 in the first 2 seconds
- [ ] Character design described (proportions, eye/mouth style, line weight)
- [ ] Effects from §5 keyed to specific timestamps
