require 'json'
require 'yaml'
require 'fileutils'

Jekyll::Hooks.register :posts, :post_write do |post|
  if post.data['layout'] == 'qotd'
    permalink_parts = post.data['permalink'].split('/')

    permalink_parts.delete('quotes')
    
    permalink_parts.delete_at(permalink_parts.index('qotd') + 1)
    
    json_file_path = File.join('_site', '/api' + permalink_parts.join('/') + '.json')

    FileUtils.mkdir_p(File.dirname(json_file_path))

    quote_info = {
      'quote' => post.data['quote'],
      'date' => post.data['date'],
      'number' => post.data['number'],
      'saidby' => post.data['saidby'],
      'submitter' => post.data['submitter'],
      'level' => post.data['level'],
      'context' => post.data['context'],
      'notes' => post.data['notes'],
      'tags' => post.data['tags'],
      'discord' => post.data['discord'],
      'image' => json_file_path.sub('/api', '/archive/img').sub('.json', '.png').sub('_site', 'https://[TOKEN]-secure.yeahgames.net')
    }    

    File.write(json_file_path, JSON.pretty_generate(quote_info))
  end
end
