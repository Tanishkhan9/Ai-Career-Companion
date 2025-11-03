export async function uploadResume(file: File) {
  const form = new FormData()
  form.append('file', file)
  const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/resume/upload`, {
    method: 'POST',
    body: form,
  })
  if (!res.ok) throw new Error('Upload failed')
  return res.json()
}
