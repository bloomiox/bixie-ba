# BIXIE Komponente — Dizajn Sistem

> **Stack:** React + TypeScript + Tailwind CSS
> **Tema:** Dark only

---

## Dugmad

### Primarno (CTA)
```tsx
<button className="bg-accent hover:bg-accent-hover text-white rounded-md transition-all duration-200">
  Početak
</button>
```

### Sekundarno
```tsx
<button className="bg-surface border border-border text-text-primary hover:bg-elevated rounded-md transition-all duration-200">
  Saznaj više
</button>
```

---

## Kartice

```tsx
<div className="bg-card border border-border rounded-lg p-6 shadow-card hover:border-accent/30 transition-all duration-200">
  ...
</div>
```

---

## Navigacija

```tsx
<nav className="fixed top-0 w-full bg-bg-nav backdrop-blur-md border-b border-border z-nav">
  ...
</nav>
```

---

## Gradient naslov

```tsx
<h2 className="gradient-text text-3xl font-bold">
  {/* gradient: 135deg #00736a → #00a396 */}
  AI Solutions
</h2>
```

---

## Tipografska hijerarhija

| Nivo | Veličina | Težina | Boja |
|------|----------|--------|------|
| h1 | 2.25rem+ | Bold | `var(--text-primary)` |
| h2 | 1.5rem | Semibold | `var(--text-primary)` |
| h3 | 1.25rem | Medium | `var(--text-primary)` |
| Body | 1rem | Normal | `var(--text-secondary)` |
| Muted | 0.875rem | Normal | `var(--text-muted)` |
