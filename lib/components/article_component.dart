library rss_reader.article_component;

import 'dart:async';

import 'package:angular2/core.dart';
import 'package:angular2/router.dart';
import 'package:angular2/platform/common.dart';

import 'package:angular2_components/angular2_components.dart';

import 'package:rss_reader/article.dart';
import 'package:rss_reader/services/article_service.dart';

@Component(
  selector: 'article-view',
  styleUrls: const ['article_component.css'],
  templateUrl: 'article_component.html',
  directives: const [materialDirectives],
  providers: const [ArticleService, materialProviders],
)
class ArticleComponent implements OnInit {
  Article article;

  String get link => article.link;

  final ArticleService _articleService;
  final RouteParams _routeParams;
  final Location _location;

  ArticleComponent(this._articleService, this._routeParams, this._location);

  Future<Null> ngOnInit() async {
    var _id = _routeParams.get('id');
    article = await _articleService.get(_id);
  }

  void goBack() => _location.back();
}