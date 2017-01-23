library rss_reader.app_component;

import 'package:angular2/core.dart';
import 'package:angular2/router.dart';

import 'package:angular2_components/angular2_components.dart';

import 'package:rss_reader/components/search_component.dart';
import 'package:rss_reader/components/article_component.dart';

@Component(
  selector: 'bbcworldnews-app',
  styleUrls: const ['app_component.css'],
  templateUrl: 'app_component.html',
  directives: const [materialDirectives, ROUTER_DIRECTIVES],
  providers: const [materialProviders, ROUTER_PROVIDERS],
)
@RouteConfig(const [
  const Route(
      path: '/search',
      name: 'Search',
      component: SearchComponent,
      useAsDefault: true),
  const Route(
      path: '/article/:id',
      name: 'Article',
      component: ArticleComponent,
      useAsDefault: false)
])
class AppComponent {
}
