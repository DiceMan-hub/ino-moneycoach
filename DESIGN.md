# Design System Inspiration of Stripe

## 1. Visual Theme & Atmosphere

Stripe's website is the gold standard of fintech design -- a system that manages to feel simultaneously technical and luxurious, precise and warm. The page opens on a clean white canvas (`#ffffff`) with deep navy headings (`#061b31`) and a signature purple (`#533afd`) that functions as both brand anchor and interactive accent. This isn't the cold, clinical purple of enterprise software; it's a rich, saturated violet that reads as confident and premium. The overall impression is of a financial institution redesigned by a world-class type foundry.

The custom `sohne-var` variable font is the defining element of Stripe's visual identity. Every text element enables the OpenType `"ss01"` stylistic set, which modifies character shapes for a distinctly geometric, modern feel. At display sizes (48px-56px), sohne-var runs at weight 300 -- an extraordinarily light weight for headlines that creates an ethereal, almost whispered authority. This is the opposite of the "bold hero headline" convention; Stripe's headlines feel like they don't need to shout. The negative letter-spacing (-1.4px at 56px, -0.96px at 48px) tightens the text into dense, engineered blocks. At smaller sizes, the system also uses weight 300 with proportionally reduced tracking, and tabular numerals via `"tnum"` for financial data display.

What truly distinguishes Stripe is its shadow system. Rather than the flat or single-layer approach of most sites, Stripe uses multi-layer, blue-tinted shadows: the signature `rgba(50,50,93,0.25)` combined with `rgba(0,0,0,0.1)` creates shadows with a cool, almost atmospheric depth -- like elements are floating in a twilight sky. The blue-gray undertone of the primary shadow color (50,50,93) ties directly to the navy-purple brand palette, making even elevation feel on-brand.

**Key Characteristics:**
- sohne-var with OpenType `"ss01"` on all text -- a custom stylistic set that defines the brand's letterforms
- Weight 300 as the signature headline weight -- light, confident, anti-convention
- Negative letter-spacing at display sizes (-1.4px at 56px, progressive relaxation downward)
- Blue-tinted multi-layer shadows using `rgba(50,50,93,0.25)` -- elevation that feels brand-colored
- Deep navy (`#061b31`) headings instead of black -- warm, premium, financial-grade
- Conservative border-radius (4px-8px) -- nothing pill-shaped, nothing harsh
- Ruby (`#ea2261`) and magenta (`#f96bee`) accents for gradient and decorative elements
- `SourceCodePro` as the monospace companion for code and technical labels

## 2. Color Palette & Roles

### Primary
- **Stripe Purple** (`#533afd`): Primary brand color, CTA backgrounds, link text, interactive highlights.
- **Deep Navy** (`#061b31`): Primary heading color. Not black, not gray -- a very dark blue that adds warmth and depth.
- **Pure White** (`#ffffff`): Page background, card surfaces, button text on dark backgrounds.

### Brand & Dark
- **Brand Dark** (`#1c1e54`): Deep indigo for dark sections, footer backgrounds.
- **Dark Navy** (`#0d253d`): The darkest neutral -- almost-black with a blue undertone.

### Accent Colors
- **Ruby** (`#ea2261`): Warm red-pink for icons, alerts, and accent elements.
- **Magenta** (`#f96bee`): Vivid pink-purple for gradients and decorative highlights.
- **Magenta Light** (`#ffd7ef`): Tinted surface for magenta-themed cards and badges.

### Interactive
- **Primary Purple** (`#533afd`): Primary link color, active states, selected elements.
- **Purple Hover** (`#4434d4`): Darker purple for hover states.
- **Purple Light** (`#b9b9f9`): Soft lavender for subdued hover backgrounds.

### Neutral Scale
- **Heading** (`#061b31`): Primary headings, nav text, strong labels.
- **Label** (`#273951`): Form labels, secondary headings.
- **Body** (`#64748d`): Secondary text, descriptions, captions.
- **Success Green** (`#15be53`): Status badges, success indicators.

### Surface & Borders
- **Border Default** (`#e5edf5`): Standard border color for cards, dividers.
- **Border Purple** (`#b9b9f9`): Active/selected state borders.

### Shadow Colors
- **Shadow Blue** (`rgba(50,50,93,0.25)`): Blue-tinted primary shadow.
- **Shadow Black** (`rgba(0,0,0,0.1)`): Secondary shadow layer.
- **Shadow Ambient** (`rgba(23,23,23,0.08)`): Soft ambient shadow.

## 3. Typography Rules

### Font Family
- **Primary**: `sohne-var`, fallback: `SF Pro Display`, `-apple-system`, `Helvetica Neue`
- **Monospace**: `SourceCodePro`, fallback: `SFMono-Regular`
- **OpenType Features**: `"ss01"` globally; `"tnum"` for tabular numbers

### Hierarchy

| Role | Size | Weight | Line Height | Letter Spacing |
|------|------|--------|-------------|----------------|
| Display Hero | 56px | 300 | 1.03 | -1.4px |
| Display Large | 48px | 300 | 1.15 | -0.96px |
| Section Heading | 32px | 300 | 1.10 | -0.64px |
| Sub-heading | 22px | 300 | 1.10 | -0.22px |
| Body Large | 18px | 300 | 1.40 | normal |
| Body | 16px | 300-400 | 1.40 | normal |
| Button | 16px | 400 | 1.00 | normal |
| Caption | 13px | 400 | normal | normal |

## 4. Component Stylings

### Buttons
- **Primary**: `#533afd` bg, white text, 4px radius, 8px 16px padding
- **Ghost**: transparent bg, `#533afd` text, `1px solid #b9b9f9` border, 4px radius
- **Hover**: `#4434d4` background

### Cards
- Background: `#ffffff`
- Border: `1px solid #e5edf5`
- Radius: 5px-6px
- Shadow: `rgba(50,50,93,0.25) 0px 30px 45px -30px, rgba(0,0,0,0.1) 0px 18px 36px -18px`

### Badges
- Success: `rgba(21,190,83,0.2)` bg, `#108c3d` text, 4px radius

## 5. Layout Principles

### Spacing System
- Base unit: 8px
- Scale: 4px, 8px, 12px, 16px, 24px, 32px, 48px, 64px

### Grid
- Max content width: ~1080px
- Hero: centered single-column
- Features: 2-3 column grids
- Dark sections (`#1c1e54`) alternate with white for rhythm

### Border Radius Scale
- Standard: 4px (buttons, inputs, badges)
- Comfortable: 5-6px (cards, containers)
- Large: 8px (featured elements)

## 6. Depth & Elevation

| Level | Shadow | Use |
|-------|--------|-----|
| Flat | None | Page background |
| Ambient | `rgba(23,23,23,0.06) 0px 3px 6px` | Subtle lift |
| Standard | `rgba(23,23,23,0.08) 0px 15px 35px` | Cards |
| Elevated | `rgba(50,50,93,0.25) 0px 30px 45px -30px, rgba(0,0,0,0.1) 0px 18px 36px -18px` | Featured cards, dropdowns |

## 7. Do's and Don'ts

### Do
- Use deep navy (`#061b31`) for headings, never pure black
- Keep border-radius 4px-8px
- Layer blue-tinted shadows for depth
- Use weight 300 for headlines

### Don't
- Don't use weight 600-700 for headlines
- Don't use large border-radius (12px+, pill shapes)
- Don't use neutral gray shadows
- Don't use pure black for text

## 8. Responsive Behavior

| Breakpoint | Width | Changes |
|------------|-------|---------|
| Mobile | <640px | Single column, 32px headings |
| Tablet | 640-1024px | 2-column grids |
| Desktop | 1024px+ | Full layout, 3-column grids |

## 9. Quick Color Reference

- Primary CTA: `#533afd`
- Background: `#ffffff`
- Heading: `#061b31`
- Body text: `#64748d`
- Border: `#e5edf5`
- Dark section: `#1c1e54`
- Success: `#15be53`
- Accent: `#ea2261`, `#f96bee`
