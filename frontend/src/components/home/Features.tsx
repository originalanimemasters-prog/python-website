import { Code2, Gauge, LayoutList, Map, MessageSquareCode, Trophy } from "lucide-react";
import { FeatureCard } from "@/components/cards/FeatureCard";
import { SectionHeading } from "@/components/common/PageContainer";

const FEATURES = [
  { icon: Map, title: "Guided roadmaps", description: "Every module is a clear sequence, not a maze — always know what's next." },
  { icon: Code2, title: "Run real code", description: "An in-browser editor with instant output for every lesson and exercise." },
  { icon: LayoutList, title: "Bite-sized lessons", description: "Concepts broken into focused 8–15 minute lessons you can finish on a break." },
  { icon: Trophy, title: "Practice with tests", description: "Solve problems against real test cases, not just multiple choice." },
  { icon: Gauge, title: "Track your progress", description: "Streaks, badges, and a dashboard that shows exactly how far you've come." },
  { icon: MessageSquareCode, title: "Built for developers", description: "No fluff — explanations written the way engineers actually talk." },
];

export function Features() {
  return (
    <section className="py-20">
      <div className="container">
        <SectionHeading
          eyebrow="Why DevForge"
          title="Everything you need, nothing you don't"
          description="A focused learning experience built around reading, writing, and running real code."
        />
        <div className="mt-10 grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
          {FEATURES.map((feature) => (
            <FeatureCard key={feature.title} {...feature} />
          ))}
        </div>
      </div>
    </section>
  );
}
