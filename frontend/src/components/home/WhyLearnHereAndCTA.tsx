import { Link } from "react-router-dom";
import { Check, X } from "lucide-react";
import { Card, CardContent } from "@/components/ui/Card";
import { Button } from "@/components/ui/Button";
import { SectionHeading } from "@/components/common/PageContainer";
import { ROUTES } from "@/utils/constants";

const COMPARISON = [
  { label: "Structured, sequential path", devforge: true, scattered: false },
  { label: "Run code in the same page you're reading", devforge: true, scattered: false },
  { label: "Tests grade your solution, not just your memory", devforge: true, scattered: false },
  { label: "One consistent format across every topic", devforge: true, scattered: false },
];

export function WhyLearnHere() {
  return (
    <section className="py-20">
      <div className="container">
        <SectionHeading align="center" eyebrow="Why learn here" title="Tutorials teach. DevForge builds habits." />
        <div className="mx-auto mt-10 grid max-w-2xl gap-4">
          {COMPARISON.map((row) => (
            <Card key={row.label}>
              <CardContent className="flex items-center justify-between gap-4 p-4">
                <span className="text-sm">{row.label}</span>
                <div className="flex items-center gap-6 text-xs">
                  <span className="flex items-center gap-1.5 text-success">
                    <Check className="h-4 w-4" /> DevForge
                  </span>
                  <span className="flex items-center gap-1.5 text-muted-foreground">
                    <X className="h-4 w-4" /> Scattered videos
                  </span>
                </div>
              </CardContent>
            </Card>
          ))}
        </div>
      </div>
    </section>
  );
}

export function CTA() {
  return (
    <section className="py-20">
      <div className="container">
        <Card className="overflow-hidden border-primary/30 bg-brand-gradient-soft">
          <CardContent className="flex flex-col items-center gap-5 p-12 text-center">
            <h2 className="max-w-lg text-3xl font-bold sm:text-4xl">
              Your first lesson takes <span className="gradient-text">8 minutes.</span>
            </h2>
            <p className="max-w-md text-muted-foreground">
              No setup, no signup wall to try it — jump into Variables and see how it feels.
            </p>
            <Button size="lg" asChild>
              <Link to={ROUTES.signup}>Create your free account</Link>
            </Button>
          </CardContent>
        </Card>
      </div>
    </section>
  );
}
