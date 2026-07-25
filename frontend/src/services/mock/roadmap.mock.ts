import type { RoadmapTrack } from "@/types";

export function getMockRoadmap(moduleSlug: string): RoadmapTrack | null {
  if (moduleSlug !== "python") return null;

  return {
    moduleSlug: "python",
    title: "Python Roadmap",
    description: "A linear path from core syntax to object-oriented programming and error handling.",
    nodes: [
      { id: "n1", title: "Fundamentals", status: "completed", lessonCount: 4, category: "Variables · Types · Operators · Strings" },
      { id: "n2", title: "Collections", status: "completed", lessonCount: 4, category: "Lists · Tuples · Sets · Dictionaries" },
      { id: "n3", title: "Control Flow", status: "in-progress", lessonCount: 3, category: "If/Else · Loops · Functions" },
      { id: "n4", title: "Object-Oriented Python", status: "locked", lessonCount: 1, category: "Classes · Inheritance" },
      { id: "n5", title: "Working with Files & Errors", status: "locked", lessonCount: 2, category: "File Handling · Exceptions" },
    ],
  };
}
