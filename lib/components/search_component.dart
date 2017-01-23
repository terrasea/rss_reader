library rss_reader.search_component;

import 'dart:async';

import 'package:angular2/core.dart';
import 'package:angular2/router.dart';

import 'package:angular2_components/angular2_components.dart';

import 'package:rss_reader/article.dart';
import 'package:rss_reader/services/article_service.dart';

@Component(
  selector: 'article-search',
  styleUrls: const ['search_component.css'],
  templateUrl: 'search_component.html',
  directives: const [materialDirectives],
  providers: const [ArticleService, materialProviders],
)
class SearchComponent implements OnInit {
  List<Article> articles;

  String keywords = '';

  final Router _router;
  final ArticleService _articleService;

  SearchComponent(this._router, this._articleService);

  Future<Null> ngOnInit() async {
    articles = (await _articleService.getAllArticles());
  }

  updateKeywords(value) {
    keywords = value;
  }

  Future<Null> search() async {
    print(keywords);
    articles = (await _articleService.search(keywords));
  }

  void viewArticle(Article article) {
    var link = [
      'Article',
      {'id': article.guid}
    ];
    _router.navigate(link);
  }
}