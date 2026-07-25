import { AlertCircle, CheckCircle2, Terminal } from "lucide-react";
import type { RunResult } from "@/types";
import { cn } from "@/utils/cn";

export function ConsoleOutput({ result }: { result: RunResult | null }) {
  if (!result) {
    return (
      <div className="flex h-full flex-col items-center justify-center gap-2 rounded-xl border border-border bg-[#0d1117] p-6 text-center text-muted-foreground">
        <Terminal className="h-5 w-5" />
        <p className="text-sm">Run your code to see output here.</p>
      </div>
    );
  }

  const isSuccess = result.status === "success";

  return (
    <div className="flex h-full flex-col rounded-xl border border-border bg-[#0d1117] p-4 font-mono text-sm">
      <div
        className={cn(
          "mb-3 flex items-center gap-2 text-xs font-semibold",
          isSuccess ? "text-success" : "text-danger"
        )}
      >
        {isSuccess ? <CheckCircle2 className="h-4 w-4" /> : <AlertCircle className="h-4 w-4" />}
        {isSuccess ? "Execution succeeded" : "Execution failed"}
        <span className="ml-auto font-normal text-muted-foreground">{result.runtimeMs}ms</span>
      </div>
      {result.stdout && <pre className="whitespace-pre-wrap text-[#e6edf3]">{result.stdout}</pre>}
      {result.stderr && <pre className="whitespace-pre-wrap text-danger">{result.stderr}</pre>}
      <p className="mt-3 text-xs text-muted-foreground">
        {result.passedTestCases}/{result.totalTestCases} test cases passed
      </p>
    </div>
  );
}
