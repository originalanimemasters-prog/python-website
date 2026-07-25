import { createContext, useContext, useMemo, useState, type ReactNode } from "react";

interface UIContextValue {
  isSidebarOpen: boolean;
  toggleSidebar: () => void;
  closeSidebar: () => void;
}

const UIContext = createContext<UIContextValue | null>(null);

export function UIProvider({ children }: { children: ReactNode }) {
  const [isSidebarOpen, setIsSidebarOpen] = useState(false);

  const value = useMemo(
    () => ({
      isSidebarOpen,
      toggleSidebar: () => setIsSidebarOpen((prev) => !prev),
      closeSidebar: () => setIsSidebarOpen(false),
    }),
    [isSidebarOpen]
  );

  return <UIContext.Provider value={value}>{children}</UIContext.Provider>;
}

export function useUI() {
  const ctx = useContext(UIContext);
  if (!ctx) throw new Error("useUI must be used within UIProvider");
  return ctx;
}
