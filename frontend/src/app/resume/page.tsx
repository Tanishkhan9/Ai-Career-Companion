import React, { useState } from 'react'

export default function ResumeUpload() {
  const [file, setFile] = useState<File | null>(null)
  const [message, setMessage] = useState<string | null>(null)

  const onFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files.length > 0) setFile(e.target.files[0])
  }

  const onSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    if (!file) return setMessage('Please select a file')
    const form = new FormData()
    form.append('file', file)
    try {
      const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/resume/upload`, {
        method: 'POST',
        body: form,
      })
      const data = await res.json()
      if (!res.ok) throw new Error(data.detail || 'Upload failed')
      setMessage('Upload successful: ' + (data.filename || ''))
    } catch (err: any) {
      setMessage(err.message)
    }
  }

  return (
    <div className="max-w-2xl mx-auto p-6">
      <h1 className="text-2xl font-bold mb-4">Upload Resume</h1>
      <form onSubmit={onSubmit} className="flex flex-col gap-4">
        <input type="file" accept=".pdf,.doc,.docx" onChange={onFileChange} />
        <button className="px-4 py-2 bg-blue-600 text-white rounded">Upload</button>
      </form>
      {message && <p className="mt-4">{message}</p>}
    </div>
  )
}
