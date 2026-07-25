import { useState } from "react";
import { useParams } from "react-router-dom";
import { CheckCircle2, XCircle, RotateCcw } from "lucide-react";
import { Card, CardContent } from "@/components/ui/Card";
import { Button } from "@/components/ui/Button";
import { Skeleton } from "@/components/ui/Skeleton";
import { ErrorState } from "@/components/common/ErrorState";
import { useQuizData } from "@/hooks/useQuiz";
import { cn } from "@/utils/cn";

export default function QuizPage() {
  const { quizId = "python-fundamentals" } = useParams();
  const { data: quiz, isLoading, isError, refetch } = useQuizData(quizId);
  const [answers, setAnswers] = useState<Record<string, string>>({});
  const [submitted, setSubmitted] = useState(false);

  if (isLoading) {
    return (
      <div className="container flex flex-col gap-4 py-12">
        {Array.from({ length: 3 }).map((_, i) => (
          <Skeleton key={i} className="h-32 w-full" />
        ))}
      </div>
    );
  }

  if (isError || !quiz) {
    return (
      <div className="container py-12">
        <ErrorState onRetry={() => refetch()} />
      </div>
    );
  }

  const score = quiz.questions.filter((q) => answers[q.id] === q.correctOptionId).length;
  const allAnswered = quiz.questions.every((q) => answers[q.id]);

  const reset = () => {
    setAnswers({});
    setSubmitted(false);
  };

  return (
    <div className="container flex flex-col gap-6 py-12">
      <div>
        <h1 className="font-display text-2xl font-bold sm:text-3xl">{quiz.title}</h1>
        <p className="text-sm text-muted-foreground">{quiz.questions.length} questions</p>
      </div>

      {submitted && (
        <Card className="border-primary/30 bg-brand-gradient-soft">
          <CardContent className="flex items-center justify-between p-5">
            <p className="font-display font-semibold">
              You scored {score}/{quiz.questions.length}
            </p>
            <Button variant="secondary" size="sm" onClick={reset}>
              <RotateCcw className="h-3.5 w-3.5" /> Retake quiz
            </Button>
          </CardContent>
        </Card>
      )}

      <div className="flex flex-col gap-5">
        {quiz.questions.map((q, qi) => {
          const selected = answers[q.id];
          const isCorrect = selected === q.correctOptionId;

          return (
            <Card key={q.id}>
              <CardContent className="p-5">
                <p className="mb-4 font-medium">
                  {qi + 1}. {q.prompt}
                </p>
                <div className="flex flex-col gap-2">
                  {q.options.map((opt) => {
                    const isSelected = selected === opt.id;
                    const showResult = submitted;
                    return (
                      <button
                        key={opt.id}
                        onClick={() => !submitted && setAnswers((prev) => ({ ...prev, [q.id]: opt.id }))}
                        disabled={submitted}
                        className={cn(
                          "flex items-center justify-between rounded-xl border px-4 py-2.5 text-left text-sm transition-colors focus-ring",
                          isSelected ? "border-primary bg-brand-gradient-soft" : "border-border hover:bg-surface-hover",
                          showResult && opt.id === q.correctOptionId && "border-success bg-success/10",
                          showResult && isSelected && !isCorrect && "border-danger bg-danger/10"
                        )}
                      >
                        {opt.label}
                        {showResult && opt.id === q.correctOptionId && <CheckCircle2 className="h-4 w-4 text-success" />}
                        {showResult && isSelected && !isCorrect && <XCircle className="h-4 w-4 text-danger" />}
                      </button>
                    );
                  })}
                </div>
                {submitted && (
                  <p className="mt-3 text-xs text-muted-foreground">{q.explanation}</p>
                )}
              </CardContent>
            </Card>
          );
        })}
      </div>

      {!submitted && (
        <Button className="w-fit" disabled={!allAnswered} onClick={() => setSubmitted(true)}>
          Submit quiz
        </Button>
      )}
    </div>
  );
}
