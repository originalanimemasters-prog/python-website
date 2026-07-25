import { Link } from "react-router-dom";
import { ArrowRight } from "lucide-react";
import { RoadmapNodeCard } from "@/components/cards/RoadmapNodeCard";
import { SectionHeading } from "@/components/common/PageContainer";
import { Button } from "@/components/ui/Button";
import { getMockRoadmap } from "@/services/mock/roadmap.mock";
import { ROUTES } from "@/utils/constants";

export function RoadmapPreview() {
  const roadmap = getMockRoadmap("python");
  if (!roadmap) return null;

  return (
    <section className="py-20">
      <div className="container grid gap-12 lg:grid-cols-[1fr_1.2fr] lg:items-center">
        <div className="flex flex-col gap-5">
          <SectionHeading
            eyebrow="The Python Roadmap"
            title="A path, not a pile of videos"
            description="Every lesson has a place in the sequence. You always know what you've mastered and exactly what's next."
          />
          <Button variant="secondary" className="w-fit" asChild>
            <Link to={ROUTES.pythonRoadmap}>
              Explore the full roadmap <ArrowRight className="h-4 w-4" />
            </Link>
          </Button>
        </div>

        <div className="glass-panel rounded-2xl p-6">
          {roadmap.nodes.map((node, i) => (
            <RoadmapNodeCard key={node.id} node={node} index={i} />
          ))}
        </div>
      </div>
    </section>
  );
}
