import { Link } from "react-router-dom";
import { motion } from "framer-motion";
import { ArrowRight, Terminal } from "lucide-react";
import { Button } from "@/components/ui/Button";
import { ROUTES } from "@/utils/constants";

export function Hero() {
  return (
    <section className="relative overflow-hidden bg-glow-radial pb-20 pt-20 sm:pt-28">
      <div className="container grid items-center gap-12 lg:grid-cols-2">
        <motion.div
          initial={{ opacity: 0, y: 16 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6 }}
          className="flex flex-col gap-6"
        >
          <span className="w-fit rounded-full border border-border bg-surface px-3 py-1 text-xs font-medium text-muted-foreground">
            Now teaching Python · more modules coming
          </span>
          <h1 className="text-4xl font-bold leading-[1.1] sm:text-5xl lg:text-6xl">
            Learn to code by <span className="gradient-text">actually building</span> it.
          </h1>
          <p className="max-w-lg text-lg text-muted-foreground">
            DevForge turns programming concepts into a guided, hands-on path — lessons you read,
            code you run, and a roadmap that shows exactly what's next.
          </p>
          <div className="flex flex-wrap gap-3">
            <Button size="lg" asChild>
              <Link to={ROUTES.signup}>
                Start learning free <ArrowRight className="h-4 w-4" />
              </Link>
            </Button>
            <Button size="lg" variant="secondary" asChild>
              <Link to={ROUTES.pythonRoadmap}>View the roadmap</Link>
            </Button>
          </div>
        </motion.div>

        <motion.div
          initial={{ opacity: 0, scale: 0.96 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ duration: 0.6, delay: 0.15 }}
          className="glass-panel rounded-2xl p-1"
        >
          <div className="flex items-center gap-1.5 border-b border-border/60 px-4 py-3">
            <span className="h-2.5 w-2.5 rounded-full bg-danger/70" />
            <span className="h-2.5 w-2.5 rounded-full bg-warning/70" />
            <span className="h-2.5 w-2.5 rounded-full bg-success/70" />
            <span className="ml-2 flex items-center gap-1.5 text-xs text-muted-foreground">
              <Terminal className="h-3 w-3" /> lists.py
            </span>
          </div>
          <pre className="overflow-x-auto p-5 font-mono text-sm leading-relaxed text-[#e6edf3]">
{`nums = [3, 1, 4, 1, 5]
nums.append(9)
nums.sort()

print(nums)
# [1, 1, 3, 4, 5, 9]`}
          </pre>
        </motion.div>
      </div>
    </section>
  );
}
