library rss_reader.article;

class Article {
  final String guid;
  final String title;
  final String thumbnail;
  final String description;
  final String link;

  Article(this.guid, this.title, this.thumbnail, this.description, this.link);
  factory Article.fromJson(Map json) {

    return new Article(
      json.putIfAbsent('guid', () => ''),
      json.putIfAbsent('title', () => ''),
      json.putIfAbsent('thumbnail', () => ''),
      json.putIfAbsent('description', () => ''),
      json.putIfAbsent('link', () => '')
    );
  }
}