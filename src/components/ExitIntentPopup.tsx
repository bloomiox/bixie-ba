import { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'

export default function ExitIntentPopup() {
  const [visible, setVisible] = useState(false)
  const [dismissed, setDismissed] = useState(false)

  useEffect(() => {
    let timeout: ReturnType<typeof setTimeout>
    let fired = false

    const handleMouseLeave = (e: MouseEvent) => {
      if (fired || dismissed) return
      if (e.clientY <= 0) {
        fired = true
        timeout = setTimeout(() => setVisible(true), 100)
      }
    }

    document.addEventListener('mouseleave', handleMouseLeave)
    return () => {
      document.removeEventListener('mouseleave', handleMouseLeave)
      clearTimeout(timeout)
    }
  }, [dismissed])

  if (!visible) return null

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/60 backdrop-blur-sm" onClick={() => setVisible(false)}>
      <div className="bg-[#0f1629] border border-gray-700 rounded-2xl p-8 max-w-md mx-4 shadow-2xl" onClick={e => e.stopPropagation()}>
        <button onClick={() => setVisible(false)} className="float-right text-gray-500 hover:text-white transition-colors text-lg">&times;</button>
        <div className="text-center">
          <div className="text-4xl mb-4">🎯</div>
          <h3 className="text-xl font-bold text-white mb-2">Besplatan CRM audit</h3>
          <p className="text-sm text-muted mb-6">
            Ostavite nam kontakt i napravit ćemo besplatnu analizu vašeg poslovanja — u roku 24h dobijate prijedlog optimalnog rješenja.
          </p>
          <div className="space-y-3">
            <Link to="/contact"
              onClick={() => { setVisible(false); setDismissed(true) }}
              className="block bg-[#00736a] text-white px-6 py-3 rounded-xl font-medium hover:bg-[#008a7f] transition-all">
              Zakažite besplatne konsultacije
            </Link>
            <button onClick={() => { setVisible(false); setDismissed(true) }}
              className="text-sm text-muted hover:text-white transition-colors">
              Ne, hvala
            </button>
          </div>
          <p className="text-[10px] text-muted mt-4">Bez obaveze · Odgovaramo u roku 24h</p>
        </div>
      </div>
    </div>
  )
}
