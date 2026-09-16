---
name: budo-seedance-3d-cgi
description: Generate 3D CGI and rendered video prompts for Seedance 2.0 on Higgsfield. Use whenever the user wants 3D rendered, CGI, Pixar-style, Unreal Engine, photorealistic 3D, computer-generated, or digitally rendered video content. Triggers on: 3D animation, CGI, rendered, Blender, Unreal Engine, octane render, ray tracing, volumetric, subsurface scattering, physically based rendering, or any 3D/CG video request. Always use even if the user just says "make it look 3D" or describes a rendered aesthetic. Reads BUDOSKILL_Seedance_Base.md first for platform specs, the 2-Second Hook framework, the visual-quality vocabulary library (especially §3.3 render engines), prompt principles, common mistakes, platform table, master template, and output workflow.
---

# BUDO — 3D CGI & Rendered Videos for Seedance 2.0 on Higgsfield

> **Inherits from `BUDOSKILL_Seedance_Base.md`.** Read that file first for the shared foundation. The §3.3 (render-engine vocabulary) is especially important here. This file adds only what's **specific to 3D CGI / rendered aesthetics.**

---

## 1. What this vertical optimizes for

3D CGI prompts succeed on **technical specificity**. The difference between a generic "make it look 3D" request and a production-ready CGI prompt lies in: render engine terminology, material properties, lighting language, camera dynamics, and the architectural "hooks" that grab attention in the first two seconds.

Quality vocabulary from Base §3.3 (render engines) is essential here — they are the strongest style anchors. Stack engine + lighting + material + camera signals aggressively.

---

## 2. CGI hook library (10 hooks)

1. **Dramatic Camera Fly-Through** — Camera moves through impossible geometry at high speed. *"Camera hurtles through a crystalline tunnel, refracting light into fractals as we move."*
2. **Scale Reveal (Tiny to Massive)** — Begin on extreme closeup (water droplet, sand grain, single fiber), pull back to reveal it's part of something enormous.
3. **Impossible Camera Angle** — Camera positions human cameras can't occupy: inside glass, on surface tension of water, through a cross-section. *"Camera rotates around a spinning hourglass, rotating through its surface to show the sand inside in real time."*
4. **Object Materializing from Particles** — Thousands of small particles (dust, light, pixels, data) coalesce into a recognizable 3D object.
5. **Photorealistic Object in Surreal Setting** — Hyper-real object (glass sphere, perfect product) in an impossible/dreamlike environment.
6. **Transformative Morph Sequence** — One object smoothly transitions into another, often defying physics. *"Marble rolls, morphing mid-motion into a silver sphere, then a water droplet."*
7. **Revealing Through Transparency** — Solid opaque object becomes transparent, revealing internal structure. *"Stone statue cracks; light pours through fissures; exterior dissolves to reveal molten light core."*
8. **Depth Shift with Depth of Field** — Three layered planes, focus racks dramatically between them; geometry behind reveals as focus changes.
9. **Liquid / Fluid Dynamic Hook** — Photoreal fluid simulation — pour, splash, ripple — as the opening visual. Tests Seedance's physics inference.
10. **Light-Emission Reveal** — Object glows from within, then the emission fills the frame, then we see what the object is. Inverse of darkness-to-light.

---

## 3. Style Spectrum Guide (10 levels, hyper-stylized → photoreal)

Pick one level. This sets material, lighting, and proportion expectations.

**1. Ultra-Stylized Cartoon 3D.** Exaggerated proportions, bright primary colors, toon shading, zero photorealism, thick bold outlines, 10:1 head-to-body ratio. Comedy / kids / playful brand.

**2. Stylized with Soft Shading.** Pixar-range. Realistic proportions, soft painterly shading, warm palette, golden-hour mood. Animated features, character spotlights.

**3. Painterly / Illustrative 3D.** Surfaces appear hand-painted. Visible brush strokes, watercolor finish, impasto effect. Artistic shorts.

**4. Stylized Realism (SFX Hybrid).** Realistic proportions and lighting but exaggerated materials, colors, or environments. *"Realistic proportions with surreal colors."* Advertising, high-concept products.

**5. Cel-Shaded with Depth.** Comic-book aesthetic + sophisticated lighting. Cel-shaded + rim lighting + bold outlines + specular highlights. *Arcane, Spider-Verse* lineage. Action sequences, gaming cinematics.

**6. Low-Poly Realistic.** Faceted geometric forms with realistic PBR materials and lighting. Minimalist advertising, architectural concepts.

**7. Isometric with Detail.** Perfect 45° isometric perspective with photo-accurate detail and materials. Technical explainers, game cinematics.

**8. Cinematic Hyperreal (High-Poly).** Mega-polygon counts, real-time ray tracing, every pore/wrinkle/hair-strand visible. HDRI or complex multi-light scenes. High-end advertising, film pre-vis.

**9. Photorealistic (Digital Photography).** Indistinguishable from photographed reality. 8K, every lens imperfection simulated, perfect chromatic aberration. Product photography, architecture, luxury goods.

**10. Hyper-Photorealistic with Impossible Physics.** Photoreal rendering quality on surreal/impossible scenarios. Sci-fi, high-concept advertising, dream sequences.

---

## 4. Material & Surface Library

Reference these directly in prompts for material accuracy.

**Metallics:** mirror-polished chrome, brushed steel, anodized aluminum, hammered copper, oxidized brass, rose gold (18k), titanium with anisotropic streaks, gunmetal, liquid mercury.

**Transparents:** crown glass, sapphire crystal, leaded crystal, frosted glass, frosted acrylic, water (clear), water (turbulent), oil-on-water surface, soap film with iridescence.

**Organics:** human skin (subsurface scattering, pore detail), animal fur (anisotropic, multi-layer), hair (strand-level), feathers, leather (cognac, distressed), wood grain (oak, walnut, ebony), stone (marble, granite, slate), concrete (raw, polished).

**Fabrics:** silk (specular highlight, drape), velvet (anisotropic absorption), cashmere (soft halo), denim (weave), satin (smooth specular), linen (loose weave).

**Special effects materials:** holographic foil, dichroic glass, iridescent shell, gemstone fire (path-traced caustics), wet skin/wet fabric, snow (sparkle highlights), ice (refractive interior).

---

## 5. Lighting Setup Encyclopedia

**HDRI environment lighting.** Image-based ambient illumination from a 360° HDR. The single most efficient lighting setup for photoreal CGI.

**Three-point lighting (key-fill-rim).** Classic studio setup. Key (main, directional, hard), fill (soft, opposite, 30% intensity), rim (back, separates subject from background).

**Volumetric / God rays.** Visible light beams through atmospheric particles. Requires dust/fog/smoke present in the scene.

**Global illumination (GI) with color bleeding.** Light bouncing between surfaces, picking up color from each. Essential for realism.

**Caustics.** Light focused/refracted through transparent objects (glass, water) creating bright concentrated patterns.

**Subsurface scattering (SSS).** Light penetrating slightly translucent materials (skin, wax, marble, leaves) and re-emerging diffused.

**Path-traced lighting.** Most accurate but expensive — every ray traced through the entire scene. Vocabulary signal for top-tier photoreal.

**Real-time ray tracing.** UE5-era — reflections and shadows ray-traced but the rest rasterized. Vocabulary for game-cinematic register.

**Studio softbox.** Large diffuse source from one or more directions. Product photography standard.

**Practicals in CG.** Light sources visible in the 3D scene (lamps, neon, screens) that also illuminate.

---

## 6. Particle & Effects Library

**Smoke:** dense smoke, wispy smoke, atmospheric haze, cigarette curl, factory plume.
**Fire:** roaring fire, candle flame, ember sparks, blast burst, torch flicker.
**Water:** splash, droplet, mist spray, fluid pour, surface ripple, beading.
**Dust / Debris:** dust motes in light, settling powder, kicked-up dirt, ash, paper confetti.
**Magical / Sci-fi:** glowing particles, light streaks, holographic noise, data visualization (cubes/lines), warp/portal effects, energy ribbons.
**Natural environment:** rain (vertical or wind-driven), snow (heavy or sparse), leaves blowing, pollen drifting.

---

## 7. CGI master-template additions

Layer onto Base §7. Use Base §3.3 render-engine vocabulary as primary quality anchor:

```
[STYLE LEVEL FROM §3]
Pick exactly one (1–10). Determines material/lighting/proportion expectations.

[RENDER ENGINE VOCAB FROM BASE §3.3]
Layer: engine name (Octane / UE5 / Blender Cycles / Arnold / V-Ray) +
lighting tech (ray-traced GI / path-traced / HDRI / volumetric) +
material spec (PBR / SSS / caustics).
Example: "Octane Render, path-traced GI, HDRI environment, PBR materials,
ray-traced reflections, volumetric atmosphere, 8K detail."

[MATERIAL CALLOUTS FROM §4]
Name 2–4 specific materials with their properties.

[LIGHTING SETUP FROM §5]
Pick one. Specify direction, color temp, ratio.

[CAMERA — physics-driven]
DOF, motion blur per frame, lens distortion if any, camera body/lens reference.

[EFFECTS LAYER FROM §6]
Particle/atmospheric effects keyed to timestamps.
```

---

## 8. Example prompts (3)

### Example 1 — Pixar-Style Character Reveal (16:9, 5s)

```
[STYLE LEVEL] Level 2 — Stylized with Soft Shading (Pixar-range).
[RENDER ENGINE VOCAB] Arnold render, HDRI environment lighting, subsurface
scattering on fur, soft shading throughout, 8K detail, warm saturated palette.

[OPENING HOOK — 0 to 2s]
Hook: Object Materializing from Particles. A crystalline cube slowly
materializes from swirling golden particles, rotating to reveal a character
trapped inside.

[MAIN ACTION — 2 to 5s]
Reveal: anthropomorphic fox character, large expressive eyes, warm orange fur
with white chest markings. Standing upright, arms at sides, slight confident
posture. Character is translucent initially, solidifying as particles coalesce.
At 3.5s the character blinks, looks directly at camera, slight confident smile.
Eyes follow camera motion subtly.

[CAMERA]
Slow orbital rotation 45°/sec around the floating cube, mid-distance.
24fps cinematic. Easing motion with smooth interpolation.

[LIGHTING — HDRI Golden Hour]
Golden-hour HDRI base. Warm key light from upper-left (3200K), cool blue fill
from right side creating subtle shadow gradation. Rim light from back creating
luminous character separation. Volumetric god rays through particles.

[MATERIALS]
Soft fur with SSS in backlighting, especially the ears. Fabric clothing (blue
vest) with natural wrinkles and textile weave. Eyes: glossy with sharp
specular highlights, warm amber iris.

[COLOR PALETTE]
Warm golds, oranges, soft pastels. Background cool gradient (pale blue to
lavender). Character warm and saturated against cool background.

[EFFECTS]
Golden particles swirl around character, coalescing onto form. Particle trails
linger before settling. Glow intensity peaks during materialization, fades
once complete. Dust motes settle realistically.

[CLOSING BEAT — 5s]
Character holds the smile; final frame composed with character centered, cube
floating slightly above centerline.

[TECHNICAL]
resolution: 1080p; mode: std; genre: auto; aspect_ratio: 16:9; duration: 5
```

### Example 2 — Photorealistic Luxury Product Reveal (1:1, 6s)

```
[STYLE LEVEL] Level 9 — Photorealistic (Digital Photography).
[RENDER ENGINE VOCAB] Octane Render, path-traced lighting, ray-traced
reflections, caustics, PBR materials, 8K photographic quality, every lens
imperfection simulated, chromatic aberration on edges, professional product
photography polish.

[OPENING HOOK — 0 to 2s]
Hook: Depth Shift / Rack Focus. A single water droplet suspended on a
polished surface catches light and refracts a product hidden in the
background. At 1.5s, focus racks from droplet to product.

[MAIN ACTION — 2 to 5s]
Push-in dolly from 2 meters away, moving toward product over 3 seconds.
Watch catches light and "blooms" as camera focuses — highlights brighten
subtly. Water droplet refracts and rolls slightly across the polished bezel
as camera approaches (gravity-accurate physics).

[CAMERA]
50mm equivalent macro, f/2.8 shallow depth. 24fps cinematic. Slight chromatic
aberration on edges.

[LIGHTING — Studio Hybrid]
Hybrid warm + cool. Warm key (3100K) from upper-left creating golden
reflection. Cool blue fill (7500K) from right reflecting off metal edge. Rim
light crisp and warm, halo on curved surfaces. HDRI from professional studio
shoot. Soft penumbra throughout.

[MATERIALS]
Rose gold (18k): mirror-polished, warm color temperature, perfect specular
reflections, zero distortion. Watch face: pure black with diamond-hard
sapphire crystal, sharp Fresnel reflections. Leather strap: rich cognac,
visible grain, subtle SSS. Sapphire crown shows microscopic scratches
catching light.

[EFFECTS]
Clean studio environment, minimal dust. Subtle caustics from water droplet
on metal beneath. Light scattering through sapphire crystal.

[CLOSING BEAT — 5 to 6s]
Final frame: watch perfectly centered, fully focused, fully illuminated.

[TECHNICAL]
resolution: 1080p; mode: std; genre: drama; aspect_ratio: 1:1; duration: 6;
medias: [watch product photo as role=image]
```

### Example 3 — Isometric Sci-Fi City Walkthrough (16:9, 8s)

```
[STYLE LEVEL] Level 7 — Isometric with Detail.
[RENDER ENGINE VOCAB] Unreal Engine 5 cinematic, real-time ray tracing,
Nanite virtualized geometry, Lumen GI, HDRI environment, volumetric
atmosphere, 8K detail, hyperdetailed photoreal textures.

[OPENING HOOK — 0 to 2s]
Hook: Object Materializing from Wireframe. An isometric view of a sprawling
futuristic city materializes from a blueprint wireframe, gaining color and
detail layer-by-layer.

[MAIN ACTION — 2 to 7s]
Slow tracking downward and forward through the city, maintaining isometric
perspective throughout. Reveals multiple layers: skyscrapers with curved
glass facades, flying vehicles (hovercars, drones), bridge structures,
terraced gardens with vegetation, water features, pedestrian plazas, holo-ads.

[CAMERA]
Fixed 45° isometric angle. 30fps. Constant velocity slow track. Zero
perspective distortion.

[LIGHTING — Dual-Sun]
Dual-sun system: cyan sun from upper-left, warm sun from upper-right. Cyan
light creates cool shadows; warm light creates warm highlights. Shadows cast
at 45° matching isometric perspective. GI with color bleeding between
surfaces. Volumetric atmospheric haze for depth.

[MATERIALS]
Curved glass facades (Fresnel + reflections), vegetation (SSS on leaves),
water (caustics, refraction), holographic ads (emission + noise), metallic
structural elements (anisotropic).

[EFFECTS]
Flying vehicle motion blur. Atmospheric haze. Light flares from holographic
displays. Drifting pollen-particles in the warm light.

[CLOSING BEAT — 7 to 8s]
Camera comes to rest on a central plaza. Final frame composed with city
extending in all directions.

[TECHNICAL]
resolution: 1080p; mode: std; genre: epic; aspect_ratio: 16:9; duration: 8
```

---

## 9. CGI-specific mistakes (in addition to Base §5)

- **"Make it look 3D" with no engine.** Without naming an engine and a render technique, "3D" is just "non-flat." Pick from Base §3.3.
- **Mixing style levels.** "Pixar-style photorealistic Unreal Engine cel-shaded" is incoherent. Pick one §3 level.
- **No material specs.** "A chrome car" is undirectable. *"Mirror-polished chrome with sharp specular highlights, slight orange-peel surface imperfection, ray-traced reflections of an HDRI environment"* is.
- **Vague lighting.** "Cinematic lighting" is meaningless in CGI. Name a setup from §5 with directions and color temps.
- **Particle effects with no source.** "Sparkles everywhere" reads as noise. Anchor particles to a source object or motion event.
- **Asking for "real-time" or "interactive."** Seedance generates final video, not playable scenes. "Real-time ray tracing" is a style signal, not a delivery promise.

---

## 10. Final pre-publish checklist

- [ ] Style level from §3 chosen (single level, not mixed)
- [ ] Render engine + lighting tech from Base §3.3 specified
- [ ] At least 2 specific materials called out from §4
- [ ] Lighting setup from §5 named with direction and K
- [ ] One hook from §2 in the first 2 seconds
- [ ] Camera physics (DOF, motion blur) specified
- [ ] Effects from §6 anchored to specific timestamps or source objects
- [ ] Genre parameter set
