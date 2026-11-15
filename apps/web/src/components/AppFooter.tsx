import { TEAM_CONFIG } from "../config/team.js";

export interface AppFooterProps {
  onOpenCredits?: (() => void) | undefined;
  onOpenDataPassport?: (() => void) | undefined;
  onOpenDataSources?: (() => void) | undefined;
  className?: string | undefined;
}

export function AppFooter({
  onOpenCredits,
  onOpenDataPassport,
  onOpenDataSources,
  className,
}: AppFooterProps) {
  return (
    <footer className={`app-footer ${className ?? ""}`} role="contentinfo" aria-label="OUTPOST-X Footer">
      <div className="app-footer-inner app-footer-container">
        <div className="app-footer-brand app-footer-brand-col">
          <img src="/branding/outpost-x-logo.svg" alt="OUTPOST-X" className="app-footer-logo" />
          <p className="app-footer-tagline">{TEAM_CONFIG.tagline}</p>
          <p className="app-footer-mission-sub">
            Advanced planetary habitat simulation grounded in authenticated NASA exploration datasets,
            life-support architectures, and orbital mechanics.
          </p>
        </div>

        <div className="app-footer-team app-footer-team-col">
          <h4 className="app-footer-col-title app-footer-team-label">
            Built by <strong className="app-footer-team-highlight">{TEAM_CONFIG.teamName}</strong>
          </h4>
          <p className="app-footer-team-desc">Mission Engineering & Operations:</p>
          <ul className="app-footer-members app-footer-team-list">
            {TEAM_CONFIG.members.map((member, idx) => (
              <li key={member.name} className="app-footer-member app-footer-team-item">
                <span className="app-footer-member-badge">0{idx + 1}</span>
                <span className="app-footer-member-name">{member.name}</span>
                {member.role && <span className="app-footer-member-role">{member.role}</span>}
              </li>
            ))}
          </ul>
        </div>

        <div className="app-footer-links app-footer-links-col">
          <h4 className="app-footer-col-title">Navigation & Mission Data</h4>
          <nav aria-label="Footer navigation" className="app-footer-links-list">
            <a href="/about.html" className="app-footer-link">
              Mission Overview & About
            </a>
            {onOpenDataSources && (
              <button type="button" className="app-footer-link app-footer-link-btn" onClick={onOpenDataSources}>
                NASA Data Sources
              </button>
            )}
            {onOpenDataPassport && (
              <button type="button" className="app-footer-link app-footer-link-btn" onClick={onOpenDataPassport}>
                Science Data Passport
              </button>
            )}
            {onOpenCredits && (
              <button type="button" className="app-footer-link app-footer-link-btn" onClick={onOpenCredits}>
                Credits &amp; Licenses
              </button>
            )}
          </nav>
        </div>
      </div>

      <div className="app-footer-bottom app-footer-bottom-bar">
        <div className="app-footer-bottom-content">
          <p className="app-footer-copyright">
            &copy; {TEAM_CONFIG.year} {TEAM_CONFIG.projectName}. All rights reserved.
            Not affiliated with or endorsed by NASA.
          </p>
          <p className="app-footer-nasa app-footer-attribution">
            {TEAM_CONFIG.nasaAttribution}{" "}
            <a href={TEAM_CONFIG.nasaDataUrl} className="app-footer-link">Data Sources</a>
          </p>
        </div>
      </div>
    </footer>
  );
}
