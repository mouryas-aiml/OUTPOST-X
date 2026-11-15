import { TEAM_CONFIG } from "../config/team.js";

export interface AppFooterProps {
  onOpenCredits?: (() => void) | undefined;
  onOpenDataPassport?: (() => void) | undefined;
  onOpenDataSources?: (() => void) | undefined;
  className?: string | undefined;
}

export function AppFooter({
  onOpenCredits,
  className,
}: AppFooterProps) {
  return (
    <footer className={`app-footer ${className ?? ""}`} role="contentinfo" aria-label="OUTPOST-X Footer">
      <div className="app-footer-inner app-footer-container">
        {/* Left – Branding */}
        <div className="app-footer-brand app-footer-brand-col">
          <img src="/branding/outpost-x-logo.svg" alt="OUTPOST-X" className="app-footer-logo" />
          <p className="app-footer-tagline">{TEAM_CONFIG.tagline}</p>
        </div>

        {/* Centre – Built by TensorMinds */}
        <div className="app-footer-team app-footer-team-col">
          <h4 className="app-footer-col-title">
            BUILT BY <span className="app-footer-team-highlight">{TEAM_CONFIG.teamName}</span>
          </h4>
          <ul className="app-footer-team-list">
            {TEAM_CONFIG.members.map((member) => (
              <li key={member.name} className="app-footer-team-item">
                <a
                  href={member.linkedin}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="app-footer-member-link"
                  title={`${member.name} — LinkedIn`}
                >
                  <span className="app-footer-member-name">{member.name}</span>
                  <svg
                    className="app-footer-ext-icon"
                    viewBox="0 0 24 24"
                    width="11"
                    height="11"
                    fill="none"
                    stroke="currentColor"
                    strokeWidth="2"
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    aria-hidden="true"
                  >
                    <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6" />
                    <polyline points="15 3 21 3 21 9" />
                    <line x1="10" y1="14" x2="21" y2="3" />
                  </svg>
                </a>
              </li>
            ))}
          </ul>
        </div>

        {/* Right – Navigation & Mission Data */}
        <div className="app-footer-links app-footer-links-col">
          <h4 className="app-footer-col-title">NAVIGATION &amp; MISSION DATA</h4>
          <nav aria-label="Footer navigation" className="app-footer-links-list">
            <a href="/about.html" className="app-footer-link">
              Mission Overview &amp; About
            </a>
            {onOpenCredits ? (
              <button type="button" className="app-footer-link app-footer-link-btn" onClick={onOpenCredits}>
                Credits &amp; Licenses
              </button>
            ) : (
              <a href="/about.html#credits" className="app-footer-link">
                Credits &amp; Licenses
              </a>
            )}
          </nav>
        </div>
      </div>

      {/* Bottom Bar */}
      <div className="app-footer-bottom app-footer-bottom-bar">
        <div className="app-footer-bottom-content">
          <p className="app-footer-copyright">
            &copy; {TEAM_CONFIG.year} {TEAM_CONFIG.projectName}. All rights reserved. Not affiliated with or endorsed by NASA.
          </p>
          <p className="app-footer-attribution">
            {TEAM_CONFIG.nasaAttribution}
          </p>
        </div>
      </div>
    </footer>
  );
}
