module Jekyll
  class AuthorLinks < Liquid::Tag
    def initialize(tag_name, author_keys, tokens)
      super
      @author_keys = author_keys.strip.split(',').map(&:strip)
    end

    def render(context)
      site = context.registers[:site]
      authors_data = site.data['authors']['authors']
      
      author_links = @author_keys.map do |key|
        author = authors_data[key]
        if author && author['url']
          "[#{author['name']}](#{author['url']})"
        else
          author ? author['name'] : key
        end
      end
      
      author_links.join(', ')
    end
  end
end

Liquid::Template.register_tag('author_links', Jekyll::AuthorLinks) 