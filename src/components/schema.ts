const siteUrl = 'https://bixie.ba'

export const localBusinessSchema = {
  '@context': 'https://schema.org',
  '@type': 'LocalBusiness',
  name: 'BIXIE',
  description: 'CRM implementacija, AI agenti i digitalna transformacija za firme u BiH, Hrvatskoj, Švicarskoj i EU.',
  url: siteUrl,
  telephone: '+38761123456',
  email: 'hello@bixie.ba',
  address: {
    '@type': 'PostalAddress',
    addressLocality: 'Sarajevo',
    addressCountry: 'BA',
  },
  foundingDate: '2011',
  knowsAbout: ['CRM', 'AI Agenti', 'Digitalna Transformacija', 'RPA', 'Bitrix24'],
  areaServed: ['Bosna i Hercegovina', 'Hrvatska', 'Švicarska', 'EU'],
  hasOfferCatalog: {
    '@type': 'OfferCatalog',
    name: 'BIXIE usluge',
    itemListElement: [
      { '@type': 'Offer', itemOffered: { '@type': 'Service', name: 'CRM Implementacija' } },
      { '@type': 'Offer', itemOffered: { '@type': 'Service', name: 'AI Agenti' } },
      { '@type': 'Offer', itemOffered: { '@type': 'Service', name: 'Digitalna Transformacija' } },
      { '@type': 'Offer', itemOffered: { '@type': 'Service', name: 'RPA Automatizacija' } },
    ],
  },
}

export function blogPostSchema(title: string, description: string, date: string, slug: string, category: string) {
  return {
    '@context': 'https://schema.org',
    '@type': 'BlogPosting',
    headline: title,
    description,
    datePublished: date,
    author: {
      '@type': 'Organization',
      name: 'BIXIE',
      url: siteUrl,
    },
    publisher: {
      '@type': 'Organization',
      name: 'BIXIE',
      url: siteUrl,
    },
    url: `${siteUrl}/blog/posts/${slug}`,
    mainEntityOfPage: `${siteUrl}/blog/posts/${slug}`,
    articleSection: category,
    inLanguage: 'bs',
  }
}

export function reviewSchema(reviewerName: string, reviewBody: string, ratingValue: number = 5) {
  return {
    '@context': 'https://schema.org',
    '@type': 'Review',
    itemReviewed: {
      '@type': 'LocalBusiness',
      name: 'BIXIE',
    },
    author: {
      '@type': 'Person',
      name: reviewerName,
    },
    reviewBody,
    reviewRating: {
      '@type': 'Rating',
      ratingValue,
      bestRating: 5,
    },
  }
}

export const faqSchema = (questions: { q: string; a: string }[]) => ({
  '@context': 'https://schema.org',
  '@type': 'FAQPage',
  mainEntity: questions.map(q => ({
    '@type': 'Question',
    name: q.q,
    acceptedAnswer: {
      '@type': 'Answer',
      text: q.a,
    },
  })),
})
