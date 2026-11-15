import React, { useEffect, useRef } from "react";
import "./SpaceBackground.css";

interface Star {
  x: number;
  y: number;
  z: number;
  pz: number;
  size: number;
  color: string;
  twinklePhase: number;
  twinkleSpeed: number;
}

const STAR_COLORS = [
  "#ffffff",
  "#ffffff",
  "#ffffff",
  "#e0f2fe",
  "#7dd3fc",
  "#38bdf8",
  "#c084fc",
  "#fcd34d",
];

export const SpaceBackground: React.FC = () => {
  const canvasRef = useRef<HTMLCanvasElement | null>(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    const ctx = canvas.getContext("2d", { alpha: false });
    if (!ctx) return;

    let animationFrameId: number;
    let width = (canvas.width = window.innerWidth);
    let height = (canvas.height = window.innerHeight);

    const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

    // Star configuration
    const NUM_STARS = Math.min(1200, Math.floor((width * height) / 1000));
    const MAX_DEPTH = 1500;
    const SPEED = prefersReducedMotion ? 0 : 0.65;

    const stars: Star[] = [];
    for (let i = 0; i < NUM_STARS; i++) {
      stars.push({
        x: (Math.random() - 0.5) * width * 2,
        y: (Math.random() - 0.5) * height * 2,
        z: Math.random() * MAX_DEPTH,
        pz: MAX_DEPTH,
        size: Math.random() * 1.5 + 0.5,
        color: STAR_COLORS[Math.floor(Math.random() * STAR_COLORS.length)] ?? "#ffffff",
        twinklePhase: Math.random() * Math.PI * 2,
        twinkleSpeed: Math.random() * 0.03 + 0.01,
      });
    }

    // Parallax mouse tracking
    let targetMouseX = 0;
    let targetMouseY = 0;
    let currentMouseX = 0;
    let currentMouseY = 0;

    const handleMouseMove = (e: MouseEvent) => {
      targetMouseX = (e.clientX - width / 2) * 0.05;
      targetMouseY = (e.clientY - height / 2) * 0.05;
    };

    window.addEventListener("mousemove", handleMouseMove, { passive: true });

    const handleResize = () => {
      if (!canvas) return;
      width = canvas.width = window.innerWidth;
      height = canvas.height = window.innerHeight;
    };

    window.addEventListener("resize", handleResize, { passive: true });

    let isTabVisible = !document.hidden;
    const handleVisibilityChange = () => {
      isTabVisible = !document.hidden;
    };
    document.addEventListener("visibilitychange", handleVisibilityChange);

    const render = () => {
      if (!isTabVisible) {
        animationFrameId = requestAnimationFrame(render);
        return;
      }

      // Smooth mouse lerp
      currentMouseX += (targetMouseX - currentMouseX) * 0.05;
      currentMouseY += (targetMouseY - currentMouseY) * 0.05;

      // Deep space base clear
      ctx.fillStyle = "#050816";
      ctx.fillRect(0, 0, width, height);

      // Subtle dynamic nebula gradients
      const cx = width / 2 + currentMouseX * 2;
      const cy = height / 2 + currentMouseY * 2;

      const grad1 = ctx.createRadialGradient(cx * 0.6, cy * 0.4, 40, cx * 0.6, cy * 0.4, width * 0.65);
      grad1.addColorStop(0, "rgba(14, 116, 144, 0.12)");
      grad1.addColorStop(0.6, "rgba(2, 44, 80, 0.06)");
      grad1.addColorStop(1, "transparent");
      ctx.fillStyle = grad1;
      ctx.fillRect(0, 0, width, height);

      const grad2 = ctx.createRadialGradient(cx * 1.3, cy * 1.2, 50, cx * 1.3, cy * 1.2, width * 0.6);
      grad2.addColorStop(0, "rgba(91, 33, 182, 0.09)");
      grad2.addColorStop(0.5, "rgba(49, 16, 102, 0.04)");
      grad2.addColorStop(1, "transparent");
      ctx.fillStyle = grad2;
      ctx.fillRect(0, 0, width, height);

      const fov = 350;

      for (let i = 0; i < stars.length; i++) {
        const star = stars[i]!;

        if (!prefersReducedMotion) {
          star.pz = star.z;
          star.z -= SPEED;

          if (star.z <= 0) {
            star.z = MAX_DEPTH;
            star.pz = MAX_DEPTH;
            star.x = (Math.random() - 0.5) * width * 2;
            star.y = (Math.random() - 0.5) * height * 2;
          }
        }

        const k = fov / star.z;
        const sx = star.x * k + width / 2 + currentMouseX;
        const sy = star.y * k + height / 2 + currentMouseY;

        if (sx < -20 || sx > width + 20 || sy < -20 || sy > height + 20) {
          continue;
        }

        // Depth & Twinkle calculation
        const depthAlpha = Math.min(1, Math.max(0.1, 1 - star.z / MAX_DEPTH));
        star.twinklePhase += star.twinkleSpeed;
        const twinkle = Math.sin(star.twinklePhase) * 0.25;
        const alpha = Math.min(1, Math.max(0.15, depthAlpha + twinkle));

        const radius = Math.max(0.6, star.size * k * 0.85);

        ctx.beginPath();
        ctx.arc(sx, sy, Math.min(radius, 3), 0, Math.PI * 2);
        ctx.fillStyle = star.color;
        ctx.globalAlpha = alpha;
        ctx.fill();

        // Subtle motion streak for near fast stars
        if (!prefersReducedMotion && star.z < MAX_DEPTH * 0.5) {
          const pk = fov / star.pz;
          const px = star.x * pk + width / 2 + currentMouseX;
          const py = star.y * pk + height / 2 + currentMouseY;

          ctx.beginPath();
          ctx.moveTo(px, py);
          ctx.lineTo(sx, sy);
          ctx.strokeStyle = star.color;
          ctx.globalAlpha = alpha * 0.35;
          ctx.lineWidth = radius * 0.6;
          ctx.stroke();
        }
      }

      ctx.globalAlpha = 1.0;

      if (!prefersReducedMotion) {
        animationFrameId = requestAnimationFrame(render);
      }
    };

    render();

    return () => {
      cancelAnimationFrame(animationFrameId);
      window.removeEventListener("mousemove", handleMouseMove);
      window.removeEventListener("resize", handleResize);
      document.removeEventListener("visibilitychange", handleVisibilityChange);
    };
  }, []);

  return (
    <div className="space-bg-container" aria-hidden="true">
      <canvas ref={canvasRef} className="space-bg-canvas" />
      <div className="space-bg-overlay" />
    </div>
  );
};
