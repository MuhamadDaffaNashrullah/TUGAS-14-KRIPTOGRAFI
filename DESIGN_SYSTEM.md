# CipherFlow Design System

## Spacing Scale (Presisi & Konsisten)

### Mobile (< 640px)
- **Container padding**: `px-4` (1rem / 16px)
- **Section padding**: `py-12` (3rem / 48px)
- **Card padding**: `p-4` (1rem / 16px)
- **Element gap**: `gap-3` (0.75rem / 12px)
- **Small gap**: `gap-2` (0.5rem / 8px)

### Tablet (640px - 1024px)
- **Container padding**: `px-6` (1.5rem / 24px)
- **Section padding**: `py-16` (4rem / 64px)
- **Card padding**: `p-6` (1.5rem / 24px)
- **Element gap**: `gap-4` (1rem / 16px)
- **Small gap**: `gap-2.5` (0.625rem / 10px)

### Desktop (> 1024px)
- **Container padding**: `px-8` (2rem / 32px)
- **Section padding**: `py-24` (6rem / 96px)
- **Card padding**: `p-8` (2rem / 32px)
- **Element gap**: `gap-6` (1.5rem / 24px)
- **Small gap**: `gap-3` (0.75rem / 12px)

## Typography Scale

### Headings
```
H1: text-3xl sm:text-4xl md:text-5xl (30px → 36px → 48px)
H2: text-2xl sm:text-3xl md:text-4xl (24px → 30px → 36px)
H3: text-xl sm:text-2xl (20px → 24px)
H4: text-lg sm:text-xl (18px → 20px)
```

### Body Text
```
Large: text-base sm:text-lg (16px → 18px)
Normal: text-sm sm:text-base (14px → 16px)
Small: text-xs sm:text-sm (12px → 14px)
Tiny: text-[10px] sm:text-xs (10px → 12px)
```

### Mono Text
```
Large: text-sm sm:text-base font-mono
Normal: text-xs sm:text-sm font-mono
Small: text-[10px] sm:text-xs font-mono
```

## Border Radius

### Components
- **Buttons**: `rounded-lg` (8px)
- **Cards**: `rounded-2xl sm:rounded-3xl` (16px → 24px)
- **Inputs**: `rounded-xl` (12px)
- **Small elements**: `rounded-lg` (8px)
- **Badges**: `rounded-full`

## Icon Sizes

```
Tiny: w-3 h-3 sm:w-3.5 sm:h-3.5 (12px → 14px)
Small: w-3.5 h-3.5 sm:w-4 sm:h-4 (14px → 16px)
Normal: w-4 h-4 sm:w-5 sm:h-5 (16px → 20px)
Large: w-5 h-5 sm:w-6 sm:h-6 (20px → 24px)
```

## Button Sizes

```
Small: px-3 sm:px-4 py-2 sm:py-2.5 text-xs sm:text-sm
Medium: px-4 sm:px-6 py-2.5 sm:py-3 text-sm sm:text-base
Large: px-6 sm:px-8 py-3 sm:py-4 text-base sm:text-lg
```

## Grid Layouts

### Feature Cards
```
Mobile: grid-cols-1
Tablet: md:grid-cols-2
Desktop: lg:grid-cols-3
```

### Stats
```
Mobile: grid-cols-2
Tablet: sm:grid-cols-4
```

### Form Inputs
```
Mobile: grid-cols-1
Desktop: lg:grid-cols-2
```

## Color Tokens

### Background
- `bg-bg`: #0B0F14 (main background)
- `bg-surface`: #121821 (cards, panels)
- `bg-surface-secondary`: #1A222D (nested elements)

### Text
- `text-text`: #F8FAFC (primary text)
- `text-muted`: #94A3B8 (secondary text)

### Accent
- `text-primary`: #5EE6A6 (primary accent - green)
- `text-accent`: #FF8A5C (secondary accent - orange)

### Borders
- `border-white/6`: rgba(255, 255, 255, 0.06) (subtle)
- `border-white/8`: rgba(255, 255, 255, 0.08) (normal)
- `border-white/10`: rgba(255, 255, 255, 0.10) (prominent)
- `border-primary/20`: rgba(94, 230, 166, 0.20) (accent)

## Breakpoints

```css
sm: 640px   /* Small tablets */
md: 768px   /* Tablets */
lg: 1024px  /* Small laptops */
xl: 1280px  /* Desktops */
2xl: 1536px /* Large desktops */
```

## Z-Index Layers

```
-1: Background animations
0: Base content
10: Cards, panels
20: Dropdowns
30: Sticky headers
40: Modals backdrop
50: Modals, mobile menus
9999: Noise overlay
```

## Animation Timing

```
Fast: duration-200
Normal: duration-300
Slow: duration-500
```

## Shadow Hierarchy

```
Subtle: shadow-sm
Normal: shadow-md
Elevated: shadow-lg
Floating: shadow-xl
Glow: shadow-[0_0_20px_rgba(94,230,166,0.15)]
```
