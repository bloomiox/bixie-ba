import { Routes, Route } from 'react-router-dom'
import Layout from './components/Layout'
import Home from './pages/Home'
import About from './pages/About'
import Contact from './pages/Contact'
import FAQ from './pages/FAQ'
import Privacy from './pages/Privacy'
import Blog from './pages/Blog'
import BlogPost from './pages/BlogPost'
import ServicesCRM from './pages/ServicesCRM'
import ServicesAIAgents from './pages/ServicesAIAgents'
import ServicesDigitalTransformation from './pages/ServicesDigitalTransformation'
import ServicesRPA from './pages/ServicesRPA'
import CaseStudies from './pages/CaseStudies'
import AIProviders from './pages/AIProviders'

export default function App() {
  return (
    <Routes>
      <Route element={<Layout />}>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/contact" element={<Contact />} />
        <Route path="/faq" element={<FAQ />} />
        <Route path="/privacy" element={<Privacy />} />
        <Route path="/blog" element={<Blog />} />
        <Route path="/blog/posts/:slug" element={<BlogPost />} />
        <Route path="/services/crm" element={<ServicesCRM />} />
        <Route path="/services/ai-agents" element={<ServicesAIAgents />} />
        <Route path="/services/digital-transformation" element={<ServicesDigitalTransformation />} />
        <Route path="/services/rpa" element={<ServicesRPA />} />
        <Route path="/case-studies" element={<CaseStudies />} />
        <Route path="/ai-providers" element={<AIProviders />} />
        {/* Language prefixes */}
        <Route path="/:lang/about" element={<About />} />
        <Route path="/:lang/contact" element={<Contact />} />
        <Route path="/:lang/faq" element={<FAQ />} />
        <Route path="/:lang/privacy" element={<Privacy />} />
        <Route path="/:lang/blog" element={<Blog />} />
        <Route path="/:lang/blog/posts/:slug" element={<BlogPost />} />
        <Route path="/:lang/services/crm" element={<ServicesCRM />} />
        <Route path="/:lang/services/ai-agents" element={<ServicesAIAgents />} />
        <Route path="/:lang/services/digital-transformation" element={<ServicesDigitalTransformation />} />
        <Route path="/:lang/services/rpa" element={<ServicesRPA />} />
        <Route path="/:lang/case-studies" element={<CaseStudies />} />
        <Route path="/:lang/ai-providers" element={<AIProviders />} />
      </Route>
    </Routes>
  )
}
