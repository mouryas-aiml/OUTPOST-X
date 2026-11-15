/**
 * Shared OUTPOST-X mark used by the home page and mission-control shell.
 * also appear on every other page — "without a header, just the logo," i.e. the mark itself,
 * not Home's full nav bar (Launch Windows / Launch Outpost, which only make sense on Home).
 *
 * A separate, small component rather than reusing `modern-hero.tsx`'s own `Nav` brand markup
 * directly: that one is styled for the Home hero's dark background (white text, a translucent
 * dark pill) and sits inside a component file that isn't otherwise imported outside Home. Every
 * other page runs on the app shell's light `--shell-bg`, so this needs the shell's own
 * dark-on-light tokens instead — a real, deliberate restyle, not a copy-paste.
 */
export function BrandMark() {
  return (
    <div className="app-brand">
      <img src="/branding/outpost-x-logo.svg" alt="OUTPOST-X" className="app-brand-logo" />
    </div>
  );
}
