"use client"
import { useEffect } from 'react'
import { useRouter } from 'next/navigation'

const DEMO_MODE = process.env.NEXT_PUBLIC_DEMO_MODE === 'true'

export function useAuthRedirect() {
  const router = useRouter()
  useEffect(() => {
    if (DEMO_MODE) return
    const token = localStorage.getItem('token')
    if (!token) router.replace('/auth/login')
  }, [router])
}

export function getAuthToken(): string | null {
  if (typeof window === 'undefined') return null
  return localStorage.getItem('token')
}

