import 'package:angular2/platform/browser.dart';
import 'package:angular2/core.dart';
import 'package:http/http.dart' as http;
import 'package:http/browser_client.dart';
import 'package:rss_reader/components/app_component.dart';

main() {
  bootstrap(AppComponent,
    [provide(http.Client, useFactory: () => new BrowserClient(), deps: [])
  ]);
}