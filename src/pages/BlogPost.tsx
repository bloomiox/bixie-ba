import { useParams, Link, useLocation } from 'react-router-dom'
import { getBlogPost } from '../blog/posts'

export default function BlogPost() {
  const { slug } = useParams()
  const location = useLocation()
  const lang = location.pathname.startsWith('/en') ? 'en' : location.pathname.startsWith('/de') ? 'de' : 'bs'

  const l = (p: string) => (lang === 'bs' ? p : `/${lang}${p}`)

  if (!slug) return null
  const post = getBlogPost(slug)

  if (!post) {
    return (
      <div className="max-w-4xl mx-auto px-4 py-20 text-center">
        <h1 className="text-2xl text-white mb-4">Članak nije pronađen</h1>
        <Link to={l('/blog')} className="text-[#00736a] hover:underline">← Nazad na blog</Link>
      </div>
    )
  }

  return (
    <div className="max-w-3xl mx-auto px-4 py-20">
      <Link to={l('/blog')} className="text-sm text-muted hover:text-white transition-colors mb-8 inline-block">← Nazad na blog</Link>
      <article>
        <div className="flex items-center gap-3 text-xs text-muted mb-4">
          <span className="bg-[#00736a]/10 text-[#00736a] px-2 py-1 rounded">{post.category}</span>
          <span>{post.date}</span>
          <span>·</span>
          <span>{post.readTime}</span>
        </div>
        <h1 className="text-3xl md:text-4xl font-bold text-white mb-8 leading-tight">{post.title}</h1>
        <p className="text-lg text-muted mb-10 leading-relaxed">{post.excerpt}</p>

        <div className="prose prose-invert max-w-none text-muted text-sm leading-relaxed space-y-4 border-t border-gray-800/50 pt-10">
          <p>Content coming soon — ovaj članak je u pripremi za novu React platformu. Prenosimo sav sadržaj sa stare stranice.</p>
          <p>U međuvremenu, <Link to={l('/contact')} className="text-[#00736a] hover:underline">kontaktirajte nas</Link> za više informacija o temi.</p>
        </div>
      </article>
    </div>
  )
}
