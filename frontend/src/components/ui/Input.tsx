import { forwardRef, type InputHTMLAttributes } from "react";
import { cn } from "@/utils/cn";

export interface InputProps extends InputHTMLAttributes<HTMLInputElement> {
  hasError?: boolean;
}

const Input = forwardRef<HTMLInputElement, InputProps>(({ className, hasError, ...props }, ref) => {
  return (
    <input
      ref={ref}
      className={cn(
        "flex h-11 w-full rounded-xl border bg-surface/80 px-4 text-sm text-foreground placeholder:text-muted-foreground focus-ring transition-colors",
        hasError ? "border-danger" : "border-border focus-visible:border-primary",
        className
      )}
      {...props}
    />
  );
});
Input.displayName = "Input";

export { Input };
