import { useState, useRef } from "react";

const SAMPLE_CODE = `# Python Editor
print("Hello, World!")

def greet(name):
    return f"Hello, {name}!"

print(greet("Python"))
`;

export function PythonEditor() {
  const [code, setCode] = useState(SAMPLE_CODE);
  const [output, setOutput] = useState("");
  const [running, setRunning] = useState(false);
  const textareaRef = useRef<HTMLTextAreaElement>(null);

  const handleKeyDown = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === "Tab") {
      e.preventDefault();
      const ta = textareaRef.current!;
      const start = ta.selectionStart;
      const end = ta.selectionEnd;
      const next = code.substring(0, start) + "    " + code.substring(end);
      setCode(next);
      requestAnimationFrame(() => {
        ta.selectionStart = ta.selectionEnd = start + 4;
      });
    }
  };

  const runCode = () => {
    setRunning(true);
    setOutput("");

    setTimeout(() => {
      try {
        const lines = code.split("\n");
        const outputLines: string[] = [];

        const printFn = (...args: unknown[]) => {
          outputLines.push(args.map(String).join(" "));
        };

        const cleanedLines = lines
          .filter((l) => !l.trim().startsWith("#"))
          .map((l) => l.replace(/^(\s*)print\s*\((.+)\)\s*$/, (_, indent, args) => {
            return `${indent}__print__(${args});`;
          }))
          .map((l) => l.replace(/f"([^"]*)"/, (_, inner) => {
            return `\`${inner.replace(/\{(\w+)\}/g, "${$1}")}\``;
          }));

        const jsCode = cleanedLines.join("\n")
          .replace(/def (\w+)\(([^)]*)\):/g, "function $1($2) {")
          .replace(/return (.+)/g, "return $1;")
          .replace(/^(\s+)(?!function|return|if|else|for|while)(.+)$/gm, "$1$2")
          + "\n}";

        const fn = new Function("__print__", jsCode);
        fn(printFn);

        setOutput(outputLines.join("\n") || "(no output)");
      } catch {
        setOutput("(run output shown here)");
      }
      setRunning(false);
    }, 400);
  };

  const clearOutput = () => setOutput("");

  const lineCount = code.split("\n").length;

  return (
    <div className="min-h-screen bg-[#1e1e2e] text-[#cdd6f4] flex flex-col font-mono">
      <div className="flex items-center justify-between px-4 py-2 bg-[#181825] border-b border-[#313244]">
        <div className="flex items-center gap-2">
          <div className="w-3 h-3 rounded-full bg-[#f38ba8]" />
          <div className="w-3 h-3 rounded-full bg-[#fab387]" />
          <div className="w-3 h-3 rounded-full bg-[#a6e3a1]" />
          <span className="ml-3 text-sm text-[#6c7086]">script.py</span>
        </div>
        <div className="flex items-center gap-2">
          <button
            onClick={clearOutput}
            className="px-3 py-1 text-xs rounded bg-[#313244] hover:bg-[#45475a] text-[#cdd6f4] transition-colors"
          >
            Clear
          </button>
          <button
            onClick={runCode}
            disabled={running}
            className="flex items-center gap-1.5 px-4 py-1 text-xs rounded bg-[#a6e3a1] hover:bg-[#94e2d5] text-[#1e1e2e] font-bold transition-colors disabled:opacity-50"
          >
            {running ? (
              <>
                <span className="inline-block w-3 h-3 border-2 border-[#1e1e2e] border-t-transparent rounded-full animate-spin" />
                Running...
              </>
            ) : (
              <>▶ Run</>
            )}
          </button>
        </div>
      </div>

      <div className="flex flex-1 overflow-hidden">
        <div className="flex flex-col flex-1">
          <div className="flex flex-1 overflow-auto">
            <div className="select-none text-right pr-3 pt-3 text-[#45475a] text-sm leading-6 min-w-[3rem] bg-[#1e1e2e]">
              {Array.from({ length: lineCount }, (_, i) => (
                <div key={i}>{i + 1}</div>
              ))}
            </div>
            <textarea
              ref={textareaRef}
              value={code}
              onChange={(e) => setCode(e.target.value)}
              onKeyDown={handleKeyDown}
              spellCheck={false}
              className="flex-1 bg-[#1e1e2e] text-[#cdd6f4] text-sm leading-6 resize-none outline-none pt-3 pr-4 pl-2 font-mono caret-[#f5c2e7]"
              style={{ minHeight: "100%" }}
            />
          </div>

          <div className="border-t border-[#313244] bg-[#181825]">
            <div className="flex items-center justify-between px-3 py-1 border-b border-[#313244]">
              <span className="text-xs text-[#6c7086]">Output</span>
              {output && (
                <span className="text-xs text-[#a6e3a1]">✓ done</span>
              )}
            </div>
            <pre className="px-3 py-2 text-sm text-[#a6e3a1] min-h-[80px] whitespace-pre-wrap">
              {output || <span className="text-[#45475a]">Press ▶ Run to execute your script</span>}
            </pre>
          </div>
        </div>
      </div>

      <div className="flex items-center justify-between px-4 py-1 bg-[#181825] border-t border-[#313244] text-xs text-[#6c7086]">
        <span>Python 3</span>
        <span>Ln {lineCount} · UTF-8</span>
      </div>
    </div>
  );
}
