import { FlaskConical } from "lucide-react";
import type { TestCase } from "@/types";

export function TestCasePanel({ testCases }: { testCases: TestCase[] }) {
  const visible = testCases.filter((tc) => tc.isSample);
  const hiddenCount = testCases.length - visible.length;

  return (
    <div className="flex flex-col gap-3">
      <div className="flex items-center gap-2 text-sm font-semibold">
        <FlaskConical className="h-4 w-4 text-primary" /> Test Cases
      </div>
      {visible.map((tc, i) => (
        <div key={tc.id} className="rounded-xl border border-border bg-surface p-3 text-sm">
          <p className="mb-1 text-xs font-semibold text-muted-foreground">Case {i + 1}</p>
          <p className="font-mono text-xs">
            <span className="text-muted-foreground">Input:</span> {tc.input}
          </p>
          <p className="font-mono text-xs">
            <span className="text-muted-foreground">Expected:</span> {tc.expectedOutput}
          </p>
        </div>
      ))}
      {hiddenCount > 0 && (
        <p className="text-xs text-muted-foreground">+ {hiddenCount} hidden test case(s) run on submit.</p>
      )}
    </div>
  );
}
