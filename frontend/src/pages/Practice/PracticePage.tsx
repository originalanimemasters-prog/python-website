import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { Play, Send } from "lucide-react";
import { Badge } from "@/components/ui/Badge";
import { Button } from "@/components/ui/Button";
import { Skeleton } from "@/components/ui/Skeleton";
import { ErrorState } from "@/components/common/ErrorState";
import { CodeEditor } from "@/components/editor/CodeEditor";
import { ConsoleOutput } from "@/components/editor/ConsoleOutput";
import { TestCasePanel } from "@/components/editor/TestCasePanel";
import { usePracticeQuestion, useRunCode, useSubmitCode } from "@/hooks/usePractice";

const DIFFICULTY_VARIANT = { beginner: "success", intermediate: "warning", advanced: "danger" } as const;

export default function PracticePage() {
  const { questionId = "reverse-string" } = useParams();
  const { data: question, isLoading, isError, refetch } = usePracticeQuestion(questionId);
  const [code, setCode] = useState("");

  const runMutation = useRunCode(questionId);
  const submitMutation = useSubmitCode(questionId);

  useEffect(() => {
    if (question) setCode(question.starterCode);
  }, [question]);

  if (isLoading) {
    return (
      <div className="grid gap-4 p-6 lg:grid-cols-2">
        <Skeleton className="h-[70vh] w-full" />
        <Skeleton className="h-[70vh] w-full" />
      </div>
    );
  }

  if (isError || !question) {
    return (
      <div className="p-6">
        <ErrorState onRetry={() => refetch()} />
      </div>
    );
  }

  const result = submitMutation.data ?? runMutation.data ?? null;

  return (
    <div className="grid h-[calc(100vh-4rem)] grid-cols-1 lg:grid-cols-2">
      <div className="overflow-y-auto border-r border-border/60 p-6">
        <div className="mb-3 flex items-center gap-2">
          <Badge variant={DIFFICULTY_VARIANT[question.difficulty]}>{question.difficulty}</Badge>
        </div>
        <h1 className="mb-4 font-display text-2xl font-bold">{question.title}</h1>
        <p className="mb-6 leading-relaxed text-muted-foreground">{question.promptMd}</p>
        <TestCasePanel testCases={question.testCases} />
      </div>

      <div className="flex flex-col p-6">
        <div className="mb-3 flex items-center justify-between">
          <span className="text-xs font-semibold uppercase tracking-wider text-muted-foreground">
            {question.language}
          </span>
          <div className="flex gap-2">
            <Button
              variant="secondary"
              size="sm"
              onClick={() => runMutation.mutate(code)}
              disabled={runMutation.isPending}
            >
              <Play className="h-3.5 w-3.5" /> {runMutation.isPending ? "Running..." : "Run"}
            </Button>
            <Button size="sm" onClick={() => submitMutation.mutate(code)} disabled={submitMutation.isPending}>
              <Send className="h-3.5 w-3.5" /> {submitMutation.isPending ? "Submitting..." : "Submit"}
            </Button>
          </div>
        </div>

        <div className="mb-4 h-[45%] min-h-[260px]">
          <CodeEditor value={code} onChange={setCode} language={question.language} />
        </div>

        <div className="flex-1">
          <ConsoleOutput result={result} />
        </div>
      </div>
    </div>
  );
}
