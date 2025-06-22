module Jekyll
  module AuthorFilters
    def author_links(author_string)
      return author_string unless author_string.is_a?(String)
      
      # Load authors data
      authors_data = @context.registers[:site].data['authors']['authors']
      
      # Split authors by comma
      authors = author_string.split(',').map(&:strip)
      
      # Process each author
      linked_authors = authors.map do |author|
        # Try to find matching author in data
        matching_author = authors_data.find { |key, data| data['name'] == author }
        
        if matching_author
          author_data = matching_author[1]
          if author_data['url']
            "[#{author}](#{author_data['url']})"
          else
            author
          end
        else
          author
        end
      end
      
      linked_authors.join(', ')
    end
  end
end

Liquid::Template.register_filter(Jekyll::AuthorFilters) 