library rss_reader.article_service;

import 'dart:async';
import 'dart:convert';

import 'package:angular2/core.dart';
import 'package:http/http.dart' as http;


import 'package:rss_reader/article.dart';

@Injectable()
class ArticleService {
  final http.Client _http;

  ArticleService(this._http);

  Future<Article> get(guid) async {
    final response = await _http.get('/article/?guid=${Uri.encodeQueryComponent(guid)}');

    return new Article.fromJson(_extractData(response));
  }

  Future<List<Article>> search(keywords) async {
    final response = await _http.get('/articles/?keywords=${Uri.encodeQueryComponent(keywords)}');

    return _extractData(response)
        .map((json) => new Article.fromJson(json))
        .toList();
  }

  _extractData(http.Response resp) => JSON.decode(resp.body);

  Future<List<Article>> getAllArticles() async {
    final response = await _http.get('/articles');

    return _extractData(response)
        .map((json) => new Article.fromJson(json))
        .toList();
  }
}