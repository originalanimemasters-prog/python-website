import { useState } from "react";
import { Check, Copy } from "lucide-react";

export function CodeBlock({ code, language = "python" }: { code: string; language?: string }) {
  const [copied, setCopied] = useState(false);

  const handleCopy = async () => {
    await navigator.clipboard.writeText(code);
    setCopied(true);
    setTimeout(() => setCopied(false), 1500);
  };

  return (
    <div className="overflow-hidden rounded-xl border border-border bg-[#0d1117]">
      <div className="flex items-center justify-between border-b border-border/60 px-4 py-2">
        <span className="text-xs font-medium text-muted-foreground">{language}</span>
        <button
          onClick={handleCopy}
          className="focus-ring flex items-center gap-1.5 rounded-md px-2 py-1 text-xs text-muted-foreground transition-colors hover:bg-surface-hover hover:text-foreground"
        >
          {copied ? <Check className="h-3.5 w-3.5 text-success" /> : <Copy className="h-3.5 w-3.5" />}
          {copied ? "Copied" : "Copy"}
        </button>
      </div>
      <pre className="overflow-x-auto p-4 text-sm leading-relaxed">
        <code className="font-mono text-[#e6edf3]">{code}</code>
      </pre>
    </div>
  );
}
