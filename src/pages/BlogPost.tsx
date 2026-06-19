import { useParams, Link, useLocation } from 'react-router-dom'
import { getBlogPost } from '../blog/posts'
import SEO from '../components/SEO'
import { blogPostSchema } from '../components/schema'

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
    <>
      <SEO
        title={post.title}
        description={post.excerpt}
        canonical={`/blog/posts/${post.slug}`}
        ogType="article"
        schema={blogPostSchema(post.title, post.excerpt, post.date, post.slug, post.category)}
      />
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

          {post.content ? (
            <div className="prose prose-invert max-w-none old-site-content text-sm leading-relaxed border-t border-gray-800/50 pt-10"
              dangerouslySetInnerHTML={{ __html: post.content }} />
          ) : (
            <div className="text-center py-12 border-t border-gray-800/50">
              <p className="text-muted">Članak je u pripremi.</p>
            </div>
          )}

          {/* CTA after article */}
          <div className="mt-12 p-6 bg-gradient-to-r from-[#00736a]/10 to-[#0f1629] border border-[#00736a]/20 rounded-xl text-center">
            <h3 className="text-white font-semibold mb-2">Trebate pomoć?</h3>
            <p className="text-sm text-muted mb-4">BIXIE tim je tu da vam pomogne sa implementacijom. Zakažite besplatne konsultacije.</p>
            <Link to={l('/contact')} className="inline-block bg-[#00736a] text-white px-6 py-2.5 rounded-lg text-sm font-medium hover:bg-[#008a7f] transition-all">
              Zakažite konsultacije
            </Link>
          </div>
        </article>
      </div>
    </>
  )
}
