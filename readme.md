# AFAD API Hizmeti

T.C. İçişleri Bakanlığı Afet ve Acil Durum Yönetimi Başkanlığı web sitesinden çekilen verilerle sunulan gayriresmi bir API servisidir.

## Açık Endpointler

Herhangi bir kimlik doğrulama gerektirmeyen endpointler.

-   [Depremler](https://afad-api.vercel.app/) : `GET /`
-   [Son Deprem](https://afad-api.vercel.app/son-deprem/) : `GET /son-deprem/`
-   [Yer](https://afad-api.vercel.app/yer/hatay) : `GET /yer/<string:yer>/`
