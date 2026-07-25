import type { ReactNode } from "react";
import { cn } from "@/utils/cn";

export function PageContainer({ children, className }: { children: ReactNode; className?: string }) {
  return <div className={cn("container", className)}>{children}</div>;
}

export function SectionHeading({
  eyebrow,
  title,
  description,
  align = "left",
}: {
  eyebrow?: string;
  title: string;
  description?: string;
  align?: "left" | "center";
}) {
  return (
    <div className={cn("flex flex-col gap-3", align === "center" && "items-center text-center")}>
      {eyebrow && (
        <span className="text-xs font-semibold uppercase tracking-[0.2em] text-primary">{eyebrow}</span>
      )}
      <h2 className="text-3xl font-bold sm:text-4xl">{title}</h2>
      {description && <p className="max-w-2xl text-muted-foreground">{description}</p>}
    </div>
  );
}
