---
name: budo-seedance-fashion-look
description: Generate fashion-look and apparel video prompts for Seedance 2.0 on Higgsfield. Use whenever the user wants fashion video, outfit showcase, lookbook, runway, model walk, apparel campaign, beauty fashion, streetwear, haute couture, athleisure, or any fashion-styling content. Triggers on: fashion video, lookbook, outfit, runway, model walk, apparel, OOTD, fashion film, designer collection, fashion campaign, streetwear, haute couture, or any clothing/styling video request. Use even for "show this outfit" or "fashion vibe video." Reads BUDOSKILL_Seedance_Base.md first for platform specs, the 2-Second Hook framework, the visual-quality vocabulary library, prompt principles, common mistakes, platform table, master template, and output workflow.
---

# BUDO — Fashion-Look Videos for Seedance 2.0 on Higgsfield

> **Inherits from `BUDOSKILL_Seedance_Base.md`.** Read that file first for the shared foundation. This file adds only what's **specific to fashion / apparel video.**

---

## 1. What this vertical optimizes for

Fashion video sells **movement, fit, fabric, and attitude**. Photographs sell the *moment*; video sells the *life* in the garment. A successful fashion clip answers: how does it move, how does it drape, how does it transform the wearer?

Quality vocabulary from Base §3 is essential — fashion lives or dies on the editorial register signal. Stack: §3.4 anamorphic + §3.5 named lighting setup + §3.7 35mm grain + §3.8 *Vogue editorial* polish.

---

## 2. Fashion hook library (12 hooks)

1. **Dramatic Outfit Reveal (Curtain/Door)** — Model behind sheer curtain or walks through door. Curtain pulls back or door swings open. Outfit fully revealed, camera holds 0.5s. *Best for: haute couture, launch reveals, formal wear.*
2. **Model Power-Walk Directly at Camera** — Model walks straight at camera, confidence radiating. Camera tilts down as they approach. *Best for: streetwear, athleisure, bold campaigns.*
3. **Rapid Outfit Change Flash Cuts** — 2–4 different outfit angles in 1 second, each 0.3–0.5s. *Best for: lookbooks, collections.*
4. **Fabric Texture Extreme Macro** — Camera starts extreme close-up on fabric weave/sequins/leather. Pulls back to reveal model. *Best for: luxury materials, sustainable fabrics.*
5. **Slow-Motion Hair and Fabric Wind** — Hair and fabric billow in slow-motion wind. Sensual, dramatic. *Best for: evening wear, luxury brands.*
6. **Mirror or Reflection Reveal** — Reflection appears in mirror/window before full body. Elegant, editorial. *Best for: formal wear, accessories.*
7. **Color-Coordinated Environment Match** — Outfit matches or complements background (blue on blue wall, green dress in garden). Monochromatic harmony. *Best for: minimalist editorial.*
8. **Accessory Close-Up to Full Look** — Detailed shot of shoes/bag/jewelry. Camera pulls back to full model. *Best for: accessory campaigns.*
9. **Silhouette Shadow Spin** — Model's shadow on wall/ground spins, reveals outfit shape. Mysterious, modern. *Best for: contemporary fashion.*
10. **Elevator or Descent Reveal** — Model descends stairs, exits elevator, walks down ramp. *Best for: luxury, power fashion.*
11. **Zoom or Scale Shift** — Rapid zoom from wide (full outfit) to medium (torso/face) or vice versa. *Best for: detail-oriented lookbooks.*
12. **Rotation Spin (360°)** — Model rotates slowly. *Best for: fit showcases, tailoring.*

---

## 3. Fashion Video Philosophy

**Movement reveals what photos can't.** A garment's drape, swing, weight, fall, and elasticity all live in motion. Plan the movement that *demonstrates* the fabric.

**Attitude is half the product.** The wearer's posture, gaze, micro-gestures sell the lifestyle as much as the garment. Direct attitude explicitly.

**Editorial > Commercial when in doubt.** Even mass-market brands benefit from editorial-register cinematography. Restraint reads as quality.

**Specificity sells.** "A dress" is undirectable. "Floor-length emerald silk gown, asymmetrical neckline, graduated skirt layers, gold-thread beading across the bodice" is.

---

## 4. Fashion category guide

**Haute couture / Evening wear.** Slow, regal pace. Anamorphic widescreen. Soft directional light. Train and drape are the demo. Genre: drama.

**Streetwear.** Energetic, urban, attitude-led. Handheld or gimbal tracking. Hard mixed-temperature lighting. Genre: action or auto.

**Athleisure.** Movement-demonstrating: stretch, breath, sweat. Bright daylight or studio softbox. Body in motion is the product.

**Luxury accessories.** Macro, slow rotation, hard directional light, dark background. Genre: drama.

**Minimalist / Editorial.** Restrained palette, static or slow camera, single light source. Genre: drama or auto.

**Avant-garde / Conceptual.** Surreal environments, unusual angles, color shifts. Genre: epic.

**Bridal.** Soft white-balanced light, slow camera, hair/veil movement, intimate close-ups.

**Workwear / Office.** Clean studio or aspirational office environment. Confidence-driven attitude.

**Vintage / Retro.** Period-accurate environment, film-stock emulation (Portra 400 / Ektachrome), grain.

**Activewear / Sports.** High-energy, fast cuts, multi-angle. Genre: action.

---

## 5. Model Direction Keywords

**Walk styles:** runway power-walk, catwalk glide, street confident pace, slow editorial stroll, athletic stride, hesitant intimate walk, march, sashay.

**Poses:** hand on hip, hands in pockets, arms crossed (rare — closed), arms relaxed at sides, one arm raised, hair-touch, neck-elongated, contrapposto, asymmetric weight shift.

**Expressions:** subtle lift at mouth (not full smile), direct gaze, distant gaze, eyes closed introspective, slight head-tilt, neutral composed, mischievous half-smile, mid-laugh candid.

**Attitude descriptors:** regal, defiant, playful, intimate, vulnerable, powerful, contemplative, joyful, mysterious, electric.

---

## 6. Fabric & Material Showcase

**Silk:** specular sheen, fluid drape, gentle wind reveal, soft folds following body.
**Denim:** weave visible in macro, structured fall, weight when walking.
**Leather:** highlight reflections on edges, grain texture, slight creak implied by movement.
**Cashmere/Wool:** soft halo edge, fiber density, warm matte light response.
**Velvet:** anisotropic light absorption (dark from one angle, lit from another), deep saturation.
**Sequins/Beading:** individual point-light reflections, light dance with movement.
**Lace:** intricate pattern catching light, semi-transparency.
**Satin:** smooth specular highlight running along folds.
**Linen:** loose breathable weave, slight wrinkle as design feature.
**Synthetic / Technical:** matte uniformity, structured silhouette, sometimes reflective panels.

---

## 7. Fashion master-template additions

Layer onto Base §7:

```
[QUALITY VOCAB FROM BASE §3 — STACK EDITORIAL]
Example: "8K, shot on ARRI Alexa, anamorphic 2.39:1, 35mm grain, Vogue
editorial polish, Kodak Vision3 emulation, teal-and-orange grade."

[CATEGORY FROM §4]
Single category — sets pace, palette, attitude register.

[OUTFIT — extreme specificity]
Garment type, fabric, color, fit, length, neckline, sleeve, hem, structure.
Styling layer (hair, jewelry, shoes).

[MODEL DIRECTION FROM §5]
Walk + pose + expression + attitude.

[FABRIC SHOWCASE FROM §6]
What does the fabric DO in motion? Drape? Sheen? Sparkle? Fall?

[LIGHTING]
Direction, K, ratio. Often: soft key + rim light for editorial.

[ENVIRONMENT]
Where (studio infinite white / urban / nature / interior / surreal).
```

---

## 8. Example prompts (3)

### Example 1 — Haute Couture Reveal (16:9, 12s)

```
[GENRE / STYLE]
Genre: drama. Photoreal haute couture editorial register.
QUALITY VOCAB: 8K, shot on ARRI Alexa, anamorphic 2.39:1, 35mm grain, Vogue
editorial polish, Kodak Vision3 emulation.
Palette: pure white studio, deep emerald gown, gold-thread accent.

[OPENING HOOK — 0 to 2s]
Hook: Dramatic Outfit Reveal (Curtain). Dramatic silhouette of model
against backlit white curtain at 0s. Curtain pulls away slowly over 1.5s,
revealing model in full haute couture gown. Silhouette emphasized first;
details follow.

[MAIN ACTION — 2 to 10s]
Slow, deliberate catwalk-style walk toward camera at measured pace, 2 ft/s.
At 6s the model reaches the camera line and rotates slowly clockwise 270° to
show train and side silhouette. At 9s, comes to stationary final pose: hands
relaxed at sides, slight head tilt toward camera.

[OUTFIT]
Floor-length haute couture gown. Deep emerald silk with intricate beading
across bodice and shoulder. Asymmetrical neckline on right side. Graduated
silk layers create volume. Train extends 2 feet behind. Underside of sleeves
features subtle gold silk lining.
Styling: hair in sleek low bun. Single gold cuff bracelet. Neutral polished
makeup. Nude heels.

[MODEL DIRECTION]
Walk: slow catwalk. Pose: contrapposto with hands relaxed at sides, slight
head tilt. Expression: subtle lift at mouth (not full smile), direct
engaged gaze, regal composed demeanor.

[FABRIC SHOWCASE]
Silk specular sheen catches light at each step. Beading creates individual
point-light reflections during the rotation. Train fluid drape sweeps the
floor on the spin.

[CAMERA]
24mm equivalent on the curtain hook (wide); 50mm for the walk. Slight
elevation, looking down at 15°. Slow orbit during rotation (or subtle
tracking with model rotation).

[LIGHTING]
Studio flash, key from camera-left at 45°, fill from right at 30%, subtle
backlight (10%) creating rim on gown edges defining silhouette and train.
White floor reflects light gently upward.

[COLOR & GRADE]
Clean editorial. Slight teal in shadows, warm in skin tone. Kodak Vision3
emulation, light grain. Beading and gold lining stay pure.

[CLOSING BEAT — 10 to 12s]
Camera pulls back slowly, widening frame to show full gown and studio.
Brand mark fades up.

[TECHNICAL]
resolution: 1080p; mode: std; genre: drama; aspect_ratio: 16:9; duration: 12;
medias: [gown reference photo as role=image, model reference photo as role=image]
```

### Example 2 — Streetwear Lookbook (9:16, 10s)

```
[GENRE / STYLE]
Genre: action. Photoreal streetwear urban register.
QUALITY VOCAB: 4K, shot on Sony Venice, gimbal-stabilized, slight teal-and-
orange grade, light 35mm grain, urban editorial polish.
Palette: charcoal gray, deep black, white logo accent, urban concrete tones.

[OPENING HOOK — 0 to 2s]
Hook: Accessory Close-Up to Full Look. Extreme close-up of sneaker sole
hitting pavement — macro at 0.5s. Quick cut at 1.0s to model's legs walking
toward camera at fast confident pace. Model's upper body enters frame by 1.5s.

[MAIN ACTION — 2 to 8s]
Model continues power-walk directly toward camera, 4 ft/s, attitude-led.
At 3.5s slight head turn to the side as if reacting to street activity.
At 5s the model passes the camera (whip past at 5.2s); camera spins 180° to
track from behind for 1 second. At 6.5s model stops, turns over shoulder to
look back at camera.

[OUTFIT]
Oversized charcoal gray hoodie with white logo print on chest, slightly
cropped (hits just below hips), kangaroo pocket. Black cargo pants with side
pockets, slight taper. White chunky sneakers. Crossbody bag in black canvas.
Styling: hair loose, simple silver hoop earrings, single chain.

[MODEL DIRECTION]
Walk: street confident pace, energetic. Pose: hands relaxed swinging slightly,
shoulder roll on whip-past. Expression: mid-laugh candid at 3.5s reaction;
direct mischievous half-smile on the turn-back.

[FABRIC SHOWCASE]
Hoodie fabric weight visible in subtle swing during fast walk. Cargo pants
structured fall. Canvas bag moves naturally with body.

[CAMERA]
35mm equivalent. MoVI gimbal, slight handheld micro-shake for energy. Forward
push at 4 ft/s, then 180° spin behind, then static for the look-back.

[LIGHTING]
Available-light urban: golden hour sun camera-left, fill from white building
on the right. Practical neon sign visible upper-right in some frames adds
magenta accent in shadows.

[COLOR & GRADE]
Teal-and-orange split. Crushed blacks (urban grit). Skin retains warm cast.

[CLOSING BEAT — 8 to 10s]
Model walks off frame-right. Camera holds on empty sidewalk for a beat.
Brand mark + "SS26 / available now" fades up.

[TECHNICAL]
resolution: 1080p; mode: std; genre: action; aspect_ratio: 9:16; duration: 10;
medias: [outfit references, model reference, sneaker product photo as role=image]
```

### Example 3 — Minimalist Editorial Color Story (1:1, 8s)

```
[GENRE / STYLE]
Genre: drama. Photoreal minimalist editorial register.
QUALITY VOCAB: 8K, shot on RED Komodo, 50mm prime, f/2.0, restrained
saturation, Fujifilm Eterna emulation, Architectural Digest interior polish.
Palette: monochromatic terracotta — outfit, walls, floor all in graduated
terracotta-clay-rust tones.

[OPENING HOOK — 0 to 2s]
Hook: Color-Coordinated Environment Match. Static frame: a terracotta-walled
interior with a model standing centered, wearing a terracotta linen dress
that matches the walls within 5% tonal range. At 1.0s a single butterfly drifts
past (only saturated element is the white butterfly).

[MAIN ACTION — 2 to 6s]
Model turns slowly to her right, hand lifting to her hair. Dress drapes as
arm moves. At 4s, she stops in profile against the wall — the silhouette is
the entire composition. At 5s a subtle wind from camera-left moves the dress
hem and a strand of hair.

[OUTFIT]
Mid-length linen dress in dusty terracotta. Loose A-line silhouette. Three-
quarter sleeves. Round neckline. Hand-stitched seams visible in macro.
Styling: hair loose, bare feet on terracotta floor, single thin gold ring.

[MODEL DIRECTION]
Walk: none — stationary pivot. Pose: profile silhouette, hand at hair.
Expression: eyes closed introspective at 4.5s. Attitude: contemplative,
vulnerable, intimate.

[FABRIC SHOWCASE]
Linen loose weave visible at edges of dress. Slight wrinkle as design feature.
Hem moves with the gentle wind at 5s. Breath visible as slight chest rise.

[CAMERA]
50mm, f/2.0. Static throughout — no movement.

[LIGHTING]
Single soft 3000K window light from camera-right at 30°. Long warm shadows
on the wall. No fill. Practical only.

[COLOR & GRADE]
Monochromatic terracotta gradient, restrained saturation 70%. Light grain.
White butterfly is the only out-of-palette element.

[CLOSING BEAT — 6 to 8s]
Wind subsides. Model exhales slowly. Final hold on the profile silhouette.

[TECHNICAL]
resolution: 1080p; mode: std; genre: drama; aspect_ratio: 1:1; duration: 8;
medias: [dress product photo as role=image, model reference photo as role=image]
```

---

## 9. Fashion-specific mistakes (in addition to Base §5)

- **Vague garment description.** "A dress" is undirectable. Specify fabric, color, fit, length, neckline, sleeve, hem.
- **No fabric showcase.** Video sells what photos can't — fabric *in motion*. Specify what the fabric DOES (drape, swing, sparkle, fall).
- **Model attitude undirected.** Without explicit attitude, the model reads as "model posing." Specify regal / defiant / playful / vulnerable.
- **Light-skin default.** Always check skin tone explicitly in the prompt to avoid default biases.
- **Forgetting accessories.** Shoes, jewelry, bag complete the look. List them.
- **Studio default for everything.** Many garments come alive in real environments. Match category to environment.
- **Background competes with outfit.** Busy background pulls focus. Either match (color-coordinated) or simplify.

---

## 10. Final pre-publish checklist

- [ ] Category from §4 named, drives pace and palette
- [ ] Outfit described with extreme specificity (fabric, color, fit, length, etc.)
- [ ] Model direction explicit (walk, pose, expression, attitude)
- [ ] Fabric showcase moment identified
- [ ] Quality vocabulary layered editorially (4–6 terms from Base §3)
- [ ] One hook from §2 in the first 2 seconds
- [ ] Lighting setup named with direction and K
- [ ] Reference photos for garment and model attached via `medias`
