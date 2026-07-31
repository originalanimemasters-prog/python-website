import {
  createContext,
  useContext,
  useMemo,
  useState,
  useEffect,
  type ReactNode,
} from "react";

interface AuthContextValue {
  isAuthenticated: boolean;
  accessToken: string | null;
  signIn: (access: string, refresh: string) => void;
  signOut: () => Promise<void>;
}

const AuthContext = createContext<AuthContextValue | null>(null);

export function AuthProvider({ children }: { children: ReactNode }) {
  const [accessToken, setAccessToken] = useState<string | null>(
    localStorage.getItem("access_token")
  );

  useEffect(() => {
    const token = localStorage.getItem("access_token");

    if (token) {
      setAccessToken(token);
    }
  }, []);

  const signIn = (access: string, refresh: string) => {
    localStorage.setItem("access_token", access);
    localStorage.setItem("refresh_token", refresh);

    setAccessToken(access);
  };

  const signOut = async () => {
  const refresh = localStorage.getItem("refresh_token");

  try {
    if (refresh) {
      await fetch("http://127.0.0.1:8000/api/auth/logout/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${accessToken}`,
        },
        body: JSON.stringify({
          refresh,
        }),
      });
    }
  } catch (error) {
    console.error("Logout failed:", error);
  } finally {
    localStorage.removeItem("access_token");
    localStorage.removeItem("refresh_token");

    setAccessToken(null);
  }
};

  const value = useMemo(
    () => ({
      isAuthenticated: !!accessToken,
      accessToken,
      signIn,
      signOut,
    }),
    [accessToken]
  );

  return (
    <AuthContext.Provider value={value}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  const context = useContext(AuthContext);

  if (!context) {
    throw new Error("useAuth must be used within AuthProvider");
  }

  return context;
}