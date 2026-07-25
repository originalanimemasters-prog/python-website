import { Hero } from "@/components/home/Hero";
import { Features } from "@/components/home/Features";
import { RoadmapPreview } from "@/components/home/RoadmapPreview";
import { WhyLearnHere, CTA } from "@/components/home/WhyLearnHereAndCTA";

export default function HomePage() {
  return (
    <>
      <Hero />
      <Features />
      <RoadmapPreview />
      <WhyLearnHere />
      <CTA />
    </>
  );
}
