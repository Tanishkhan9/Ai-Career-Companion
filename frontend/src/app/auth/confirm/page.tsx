"use client";

import { Suspense, useEffect, useState } from "react";
import { useSearchParams } from "next/navigation";
import { API_BASE } from "@/lib/api";

function ConfirmContent() {
  const [status, setStatus] = useState<string>("verifying");
  const searchParams = useSearchParams();
  const token = searchParams.get("token") || undefined;

  useEffect(() => {
    if (!token) {
      setStatus("missing-token");
      return;
    }

    const verify = async () => {
      try {
        const res = await fetch(`${API_BASE}/users/verify?token=${encodeURIComponent(token)}`);
        if (res.ok) {
          setStatus("success");
        } else {
          const data = await res.json();
          setStatus(data?.detail || "failed");
        }
      } catch (err) {
        setStatus("error");
      }
    };

    verify();
  }, [token]);

  return (
    <div className="min-h-screen flex items-center justify-center">
      <div className="p-6 bg-white rounded shadow w-full max-w-md text-center">
        {status === "verifying" && <p>Verifying your account...</p>}
        {status === "missing-token" && <p>Verification token missing from URL.</p>}
        {status === "success" && <p className="text-green-600">Your account has been verified — you can now log in.</p>}
        {status === "failed" && <p className="text-red-600">Verification failed. The token may be invalid or expired.</p>}
        {status === "error" && <p className="text-red-600">Network error while verifying — try again later.</p>}
        {status !== "verifying" && (
          <div className="mt-4">
            <a href="/auth/login" className="text-blue-600 underline">Go to login</a>
          </div>
        )}
      </div>
    </div>
  );
}

export default function ConfirmPage() {
  return (
    <Suspense fallback={<div className="min-h-screen flex items-center justify-center"><div className="p-6 bg-white rounded shadow w-full max-w-md text-center"><p>Loading...</p></div></div>}>
      <ConfirmContent />
    </Suspense>
  );
}
