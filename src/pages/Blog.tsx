import { Link, useLocation } from 'react-router-dom'
import { getAllBlogPosts } from '../blog/posts'

export default function Blog() {
  const location = useLocation()
  const lang = location.pathname.startsWith('/en') ? 'en' : location.pathname.startsWith('/de') ? 'de' : 'bs'
  const posts = getAllBlogPosts()

  const l = (p: string) => (lang === 'bs' ? p : `/${lang}${p}`)

  const categories = [...new Set(posts.map(p => p.category))]

  return (
    <div className="max-w-4xl mx-auto px-4 py-20">
      <h1 className="text-4xl font-bold text-white mb-4">Blog</h1>
      <p className="text-muted mb-12 max-w-xl">Najnoviji članci o AI agentima, CRM sistemima i digitalnoj transformaciji.</p>

      <div className="flex flex-wrap gap-2 mb-10">
        {categories.map(cat => (
          <span key={cat} className="text-xs px-3 py-1.5 bg-[#0f1629] border border-gray-800 rounded-full text-muted">{cat}</span>
        ))}
      </div>

      <div className="space-y-6">
        {posts.map(post => (
          <Link key={post.slug} to={l(`/blog/posts/${post.slug}`)}
            className="block bg-[#0f1629] border border-gray-800 rounded-xl p-6 hover:border-[#00736a]/30 transition-all group">
            <div className="flex items-start justify-between gap-4 mb-3">
              <h2 className="text-lg font-semibold text-white group-hover:text-[#00736a] transition-colors">{post.title}</h2>
              <span className="text-[10px] uppercase tracking-wider text-muted bg-white/5 px-2 py-1 rounded shrink-0">{post.category}</span>
            </div>
            <p className="text-sm text-muted leading-relaxed mb-3">{post.excerpt}</p>
            <div className="flex items-center gap-4 text-xs text-muted">
              <span>{post.date}</span>
              <span>·</span>
              <span>{post.readTime}</span>
            </div>
          </Link>
        ))}
      </div>
    </div>
  )
}
