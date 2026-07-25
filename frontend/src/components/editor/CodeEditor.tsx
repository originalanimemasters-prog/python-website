import Editor from "@monaco-editor/react";

interface CodeEditorProps {
  value: string;
  onChange: (value: string) => void;
  language?: string;
  height?: string;
}

export function CodeEditor({ value, onChange, language = "python", height = "100%" }: CodeEditorProps) {
  return (
    <div className="h-full overflow-hidden rounded-xl border border-border">
      <Editor
        height={height}
        language={language}
        theme="vs-dark"
        value={value}
        onChange={(val) => onChange(val ?? "")}
        options={{
          fontSize: 14,
          fontFamily: "'JetBrains Mono', monospace",
          minimap: { enabled: false },
          scrollBeyondLastLine: false,
          padding: { top: 16 },
          automaticLayout: true,
          tabSize: 4,
        }}
      />
    </div>
  );
}
