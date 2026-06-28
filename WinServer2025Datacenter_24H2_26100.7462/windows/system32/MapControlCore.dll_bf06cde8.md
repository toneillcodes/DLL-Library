# Binary Specification: MapControlCore.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\MapControlCore.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `bf06cde814c3010cc587155ed9d147db5313a70aab903943f5e1394f090f50c7`
* **Total Exported Functions:** 250

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 180 | `?GetUserGeoRegion@MapsSettings@@SAJPEAPEAUHSTRING__@@@Z` | `0x1880` | 302 | UnwindData |  |
| 16 | `??0GeoCoordinates@core@@QEAA@NN@Z` | `0x2060` | 164 | UnwindData |  |
| 244 | `?UnregisterListener@SuspendResumeDispatcher@@SAXPEAVISuspendResumeListener@@@Z` | `0x2460` | 167 | UnwindData |  |
| 9 | `??0?$BackedType@VGeoCoordinates@ngeo@Microsoft@@@core@@QEAA@XZ` | `0x29E0` | 31 | UnwindData |  |
| 33 | `??1?$BackedType@V?$shared_ptr@VIManeuver@msnma@@@std@@@core@@QEAA@XZ` | `0x2A10` | 24 | UnwindData |  |
| 34 | `??1?$BackedType@V?$shared_ptr@VIRoute@msnma@@@std@@@core@@QEAA@XZ` | `0x2A10` | 24 | UnwindData |  |
| 38 | `??1GeoCoordinates@core@@UEAA@XZ` | `0x2A90` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 225 | `?SetBackingObject@?$BackedType@VGeoCoordinates@ngeo@Microsoft@@@core@@QEAAXAEBVGeoCoordinates@ngeo@Microsoft@@@Z` | `0x2BC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `??1?$BackedType@VGeoCoordinates@ngeo@Microsoft@@@core@@QEAA@XZ` | `0x2BE0` | 21,200 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 220 | `?RestrictedAPIAccessCheck@ApiAccessCheck@@SAJXZ` | `0x7EB0` | 523 | UnwindData |  |
| 1 | `??0?$BackedType@V?$shared_ptr@VIManeuver@msnma@@@std@@@core@@QEAA@$$QEAV01@@Z` | `0x9B70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `??0?$BackedType@V?$shared_ptr@VIRoute@msnma@@@std@@@core@@QEAA@$$QEAV01@@Z` | `0x9B70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `??0?$BackedType@V?$shared_ptr@VIManeuver@msnma@@@std@@@core@@QEAA@AEBV01@@Z` | `0x9BA0` | 18 | UnwindData |  |
| 5 | `??0?$BackedType@V?$shared_ptr@VIRoute@msnma@@@std@@@core@@QEAA@AEBV01@@Z` | `0x9BA0` | 18 | UnwindData |  |
| 3 | `??0?$BackedType@V?$shared_ptr@VIManeuver@msnma@@@std@@@core@@QEAA@XZ` | `0x9BC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `??0?$BackedType@V?$shared_ptr@VIRoute@msnma@@@std@@@core@@QEAA@XZ` | `0x9BC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `??0?$BackedType@VGeoCoordinates@ngeo@Microsoft@@@core@@QEAA@$$QEAV01@@Z` | `0x9BE0` | 31 | UnwindData |  |
| 8 | `??0?$BackedType@VGeoCoordinates@ngeo@Microsoft@@@core@@QEAA@AEBV01@@Z` | `0x9C10` | 31 | UnwindData |  |
| 10 | `??0?$BackedType@VGeoRect@ngeo@Microsoft@@@core@@QEAA@$$QEAV01@@Z` | `0x9C40` | 31 | UnwindData |  |
| 11 | `??0?$BackedType@VGeoRect@ngeo@Microsoft@@@core@@QEAA@AEBV01@@Z` | `0x9C70` | 31 | UnwindData |  |
| 12 | `??0?$BackedType@VGeoRect@ngeo@Microsoft@@@core@@QEAA@XZ` | `0x9CA0` | 31 | UnwindData |  |
| 14 | `??0DoublePoint@core@@QEAA@NN@Z` | `0x9D40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `??0GeoCoordinates@core@@QEAA@AEBV01@@Z` | `0x9D60` | 49 | UnwindData |  |
| 17 | `??0GeoCoordinates@core@@QEAA@XZ` | `0x9DA0` | 50 | UnwindData |  |
| 18 | `??0GeoRect@core@@QEAA@AEBV01@@Z` | `0x9DE0` | 49 | UnwindData |  |
| 19 | `??0GeoRect@core@@QEAA@NNNN@Z` | `0x9E20` | 191 | UnwindData |  |
| 20 | `??0GeoRect@core@@QEAA@PEBVGeoCoordinates@1@0@Z` | `0x9EF0` | 147 | UnwindData |  |
| 21 | `??0GeoRect@core@@QEAA@XZ` | `0x9F90` | 50 | UnwindData |  |
| 26 | `??0Route@core@@QEAA@AEBV01@@Z` | `0xA030` | 50 | UnwindData |  |
| 28 | `??0RouteLeg@core@@QEAA@AEBV01@@Z` | `0xA070` | 307 | UnwindData |  |
| 30 | `??0RouteManeuver@core@@QEAA@AEBV01@@Z` | `0xA1B0` | 106 | UnwindData |  |
| 36 | `??1?$BackedType@VGeoRect@ngeo@Microsoft@@@core@@QEAA@XZ` | `0xA220` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `??1GeoRect@core@@UEAA@XZ` | `0xA2A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `??4?$BackedType@V?$shared_ptr@VIManeuver@msnma@@@std@@@core@@QEAAAEAV01@$$QEAV01@@Z` | `0xA2D0` | 56 | UnwindData |  |
| 47 | `??4?$BackedType@V?$shared_ptr@VIManeuver@msnma@@@std@@@core@@QEAAAEAV01@AEBV01@@Z` | `0xA310` | 24 | UnwindData |  |
| 49 | `??4?$BackedType@V?$shared_ptr@VIRoute@msnma@@@std@@@core@@QEAAAEAV01@AEBV01@@Z` | `0xA310` | 24 | UnwindData |  |
| 48 | `??4?$BackedType@V?$shared_ptr@VIRoute@msnma@@@std@@@core@@QEAAAEAV01@$$QEAV01@@Z` | `0xA330` | 24 | UnwindData |  |
| 50 | `??4?$BackedType@VGeoCoordinates@ngeo@Microsoft@@@core@@QEAAAEAV01@$$QEAV01@@Z` | `0xA350` | 31 | UnwindData |  |
| 51 | `??4?$BackedType@VGeoCoordinates@ngeo@Microsoft@@@core@@QEAAAEAV01@AEBV01@@Z` | `0xA380` | 31 | UnwindData |  |
| 52 | `??4?$BackedType@VGeoRect@ngeo@Microsoft@@@core@@QEAAAEAV01@$$QEAV01@@Z` | `0xA3B0` | 31 | UnwindData |  |
| 53 | `??4?$BackedType@VGeoRect@ngeo@Microsoft@@@core@@QEAAAEAV01@AEBV01@@Z` | `0xA3E0` | 31 | UnwindData |  |
| 54 | `??4DoublePoint@core@@QEAAAEAU01@$$QEAU01@@Z` | `0xA500` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `??4DoublePoint@core@@QEAAAEAU01@AEBU01@@Z` | `0xA520` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `??4GeoCoordinates@core@@QEAAAEAV01@AEBV01@@Z` | `0xA540` | 39 | UnwindData |  |
| 57 | `??4GeoRect@core@@QEAAAEAV01@AEBV01@@Z` | `0xA570` | 39 | UnwindData |  |
| 60 | `??4Route@core@@QEAAAEAV01@AEBV01@@Z` | `0xA600` | 50 | UnwindData |  |
| 61 | `??4RouteLeg@core@@QEAAAEAV01@AEBV01@@Z` | `0xA640` | 96 | UnwindData |  |
| 62 | `??4RouteManeuver@core@@QEAAAEAV01@AEBV01@@Z` | `0xA6B0` | 88 | UnwindData |  |
| 63 | `??8DoublePoint@core@@QEBA_NAEBU01@@Z` | `0xA710` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `??8GeoCoordinates@core@@QEBA_NAEBV01@@Z` | `0xA740` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `??9DoublePoint@core@@QEBA_NAEBU01@@Z` | `0xA760` | 17 | UnwindData |  |
| 66 | `??9GeoCoordinates@core@@QEBA_NAEBV01@@Z` | `0xA780` | 32 | UnwindData |  |
| 78 | `??_FDoublePoint@core@@QEAAXXZ` | `0xAA80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 79 | `?CalculateGeoRect@GeoRect@core@@SAJAEAV?$vector@PEAVGeoCoordinates@core@@V?$allocator@PEAVGeoCoordinates@core@@@std@@@std@@PEAV12@@Z` | `0xAAA0` | 634 | UnwindData |  |
| 85 | `?Contains@GeoRect@core@@QEAA_NPEBVGeoCoordinates@2@@Z` | `0xAD20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `?CopyFrom@GeoRect@core@@QEAAXAEBV12@@Z` | `0xAD40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 92 | `?GetAltitude@GeoCoordinates@core@@UEBANXZ` | `0xAD60` | 30 | UnwindData |  |
| 95 | `?GetBackingObjectRef@?$BackedType@VGeoCoordinates@ngeo@Microsoft@@@core@@IEAAAEAVGeoCoordinates@ngeo@Microsoft@@XZ` | `0xAD90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 96 | `?GetBackingObjectRef@?$BackedType@VGeoCoordinates@ngeo@Microsoft@@@core@@QEBAAEBVGeoCoordinates@ngeo@Microsoft@@XZ` | `0xAD90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `?GetBackingObjectRef@?$BackedType@VGeoRect@ngeo@Microsoft@@@core@@IEAAAEAVGeoRect@ngeo@Microsoft@@XZ` | `0xAD90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 98 | `?GetBackingObjectRef@?$BackedType@VGeoRect@ngeo@Microsoft@@@core@@QEBAAEBVGeoRect@ngeo@Microsoft@@XZ` | `0xAD90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 101 | `?GetBottom@GeoRect@core@@QEBANXZ` | `0xADA0` | 42 | UnwindData |  |
| 102 | `?GetBottomRight@GeoRect@core@@QEBAJPEAVGeoCoordinates@2@@Z` | `0xADD0` | 106 | UnwindData |  |
| 105 | `?GetCenter@GeoRect@core@@QEBAJPEAVGeoCoordinates@2@@Z` | `0xAE40` | 128 | UnwindData |  |
| 129 | `?GetInflatedGeoRect@GeoRect@core@@QEBA?AV12@XZ` | `0xAED0` | 160 | UnwindData |  |
| 136 | `?GetLatitude@GeoCoordinates@core@@UEBANXZ` | `0xAF80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 138 | `?GetLeft@GeoRect@core@@QEBANXZ` | `0xAFA0` | 42 | UnwindData |  |
| 145 | `?GetLongitude@GeoCoordinates@core@@UEBANXZ` | `0xAFD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 152 | `?GetMaxLatitude@GeoCoordinates@core@@SANXZ` | `0xAFF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 153 | `?GetMaxLongitude@GeoCoordinates@core@@SANXZ` | `0xB000` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 154 | `?GetMinLatitude@GeoCoordinates@core@@SANXZ` | `0xB010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 155 | `?GetMinLongitude@GeoCoordinates@core@@SANXZ` | `0xB020` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 162 | `?GetRight@GeoRect@core@@QEBANXZ` | `0xB030` | 42 | UnwindData |  |
| 172 | `?GetTop@GeoRect@core@@QEBANXZ` | `0xB060` | 42 | UnwindData |  |
| 173 | `?GetTopLeft@GeoRect@core@@QEBAJPEAVGeoCoordinates@2@@Z` | `0xB090` | 106 | UnwindData |  |
| 199 | `?Intersects@GeoRect@core@@QEAA_NPEBV12@@Z` | `0xB100` | 565 | UnwindData |  |
| 202 | `?IsDegenerate@GeoRect@core@@QEBA_NXZ` | `0xB340` | 124 | UnwindData |  |
| 209 | `?IsValid@GeoCoordinates@core@@UEBA_NXZ` | `0xB3D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 210 | `?IsValid@GeoRect@core@@UEBA_NXZ` | `0xB3F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 222 | `?SetAltitude@GeoCoordinates@core@@UEAAXN@Z` | `0xB410` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 226 | `?SetBackingObject@?$BackedType@VGeoRect@ngeo@Microsoft@@@core@@QEAAXAEBVGeoRect@ngeo@Microsoft@@@Z` | `0xB430` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 235 | `?SetLatitude@GeoCoordinates@core@@UEAAXN@Z` | `0xB450` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 237 | `?SetLongitude@GeoCoordinates@core@@UEAAXN@Z` | `0xB470` | 3,616 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 99 | `?GetBingAuthenticationKey@MapsSettings@@SAJPEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0xC290` | 143 | UnwindData |  |
| 100 | `?GetBingMapsKey@MapsSettings@@SAJPEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0xC330` | 141 | UnwindData |  |
| 109 | `?GetDataAttribution@MapsSettings@@SAJPEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0xC3D0` | 231 | UnwindData |  |
| 110 | `?GetDefaultCenterFromTimezone@MapsSettings@@SAPEBVGeoCoordinates@core@@XZ` | `0xC630` | 228 | UnwindData |  |
| 117 | `?GetEnableManeuverCondensing@MapsSettings@@SA_NXZ` | `0xC720` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 135 | `?GetKeyValidationStatus@MapsSettings@@SAJPEAH@Z` | `0xC730` | 114 | UnwindData |  |
| 143 | `?GetLimitNetworkUsage@MapsSettings@@SAJPEA_N@Z` | `0xC7B0` | 114 | UnwindData |  |
| 144 | `?GetLocaleMapConfiguration@MapsSettings@@SAJPEAPEAUILocaleMapConfiguration@@@Z` | `0xC830` | 231 | UnwindData |  |
| 181 | `?GetUserGeoRegion@MapsSettings@@SAJPEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0xC920` | 138 | UnwindData |  |
| 182 | `?GetUserGeoRegionAsThreeLetterCode@MapsSettings@@SAJPEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0xC9B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 183 | `?GetUserPreferredUILanguage@MapsSettings@@SAJPEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0xC9C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 184 | `?GetUserProfileLanguage@MapsSettings@@SAJPEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0xC9D0` | 245 | UnwindData |  |
| 185 | `?GetUserProfileLanguages@MapsSettings@@SAJPEAPEAUHSTRING__@@@Z` | `0xCAD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 186 | `?GetUserProfileLanguages@MapsSettings@@SAJPEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0xCAE0` | 138 | UnwindData |  |
| 200 | `?IsChinaVariant@MapsSettings@@SA_NXZ` | `0xCBC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 206 | `?IsOldChinaRegKeySet@MapsSettings@@SA_NXZ` | `0xCBD0` | 103 | UnwindData |  |
| 213 | `?IsWatermarkEnabled@MapsSettings@@SA_NXZ` | `0xCC40` | 67 | UnwindData |  |
| 227 | `?SetBingAuthenticationKey@MapsSettings@@SAJAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0xCC90` | 134 | UnwindData |  |
| 228 | `?SetBingMapsKey@MapsSettings@@SAJAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0xCD20` | 252 | UnwindData |  |
| 231 | `?SetEnableManeuverCondensing@MapsSettings@@SAX_N@Z` | `0xCE30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 234 | `?SetKeyValidationStatus@MapsSettings@@SAJH@Z` | `0xCE40` | 85 | UnwindData |  |
| 236 | `?SetLimitNetworkUsage@MapsSettings@@SAJ_N@Z` | `0xCEA0` | 61 | UnwindData |  |
| 156 | `GetMosThreadInstance` | `0xE1B0` | 82 | UnwindData |  |
| 157 | `GetMosThreadInstanceWithoutWait` | `0xE210` | 82 | UnwindData |  |
| 205 | `IsMosThread` | `0xE590` | 47 | UnwindData |  |
| 245 | `WaitForMosThreadToClose` | `0xEF40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 246 | `?WaitOnClose@MosThread@@SAXXZ` | `0xEF50` | 133 | UnwindData |  |
| 160 | `?GetResultSqmId@OperationAdapterCore@@MEBAKXZ` | `0xF100` | 1,632 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `??0OperationAdapterCore@@IEAA@XZ` | `0xF760` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `??0OperationAdapterCore@@QEAA@AEBV0@@Z` | `0xF780` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `??0QueryAdapterCore@@QEAA@AEBV0@@Z` | `0xF7B0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `??1OperationAdapterCore@@MEAA@XZ` | `0xF7F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `??1QueryAdapterCore@@MEAA@XZ` | `0xF7F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `??4OperationAdapterCore@@QEAAAEAV0@AEBV0@@Z` | `0xF810` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `??4QueryAdapterCore@@QEAAAEAV0@AEBV0@@Z` | `0xF830` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 120 | `?GetErrorCode@OperationAdapterCore@@QEBAJXZ` | `0xF960` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 122 | `?GetGenerationNumber@?$UIThreadCore@UIRouterUI@@@@UEBAJXZ` | `0xF970` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 130 | `?GetInstanceId@OperationAdapterCore@@QEBAHXZ` | `0xF970` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 158 | `?GetProgress@OperationAdapterCore@@QEBAKXZ` | `0xF980` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 219 | `?ResetProgress@OperationAdapterCore@@IEAAXXZ` | `0xF990` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 232 | `?SetErrorCode@OperationAdapterCore@@IEAAXJ@Z` | `0xF9B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 233 | `?SetInstanceId@OperationAdapterCore@@IEAAXH@Z` | `0xF9C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 238 | `?SetProgress@OperationAdapterCore@@MEAAXK@Z` | `0xF9D0` | 30 | UnwindData |  |
| 24 | `??0QueryAdapterCore@@IEAA@XZ` | `0xFA00` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 140 | `?GetLegCount@Route@core@@UEBAKXZ` | `0xFA30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 167 | `?GetStatus@QueryAdapterCore@@QEBA?AW4QueryStatus@@XZ` | `0xFA30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 239 | `?SetProgress@QueryAdapterCore@@MEAAXK@Z` | `0xFA40` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 241 | `?SetStatus@QueryAdapterCore@@IEAAXW4QueryStatus@@@Z` | `0xFA70` | 1,424 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `??0?$UIThreadCore@UIRouterUI@@@@IEAA@XZ` | `0x10000` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `??0RouterAdapterCore@@IEAA@XZ` | `0x10030` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `??1?$UIThreadCore@UIRouterUI@@@@MEAA@XZ` | `0x100E0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `??1RouterAdapterCore@@MEAA@XZ` | `0x10150` | 99 | UnwindData |  |
| 80 | `?CalculateRoute@RouterAdapterCore@@QEAAJ$$QEAV?$vector@URoutePoint@engine@@V?$allocator@URoutePoint@engine@@@std@@@std@@W4TravelMode@engine@@W4RouteOptimization@5@KIPEAURouteOptions@5@@Z` | `0x10460` | 50 | UnwindData |  |
| 81 | `?CalculateRoute@RouterAdapterCore@@QEAAJ$$QEAV?$vector@URoutePoint@engine@@V?$allocator@URoutePoint@engine@@@std@@@std@@W4TravelMode@engine@@W4RouteOptimization@5@KI_JPEAURouteOptions@5@@Z` | `0x104A0` | 832 | UnwindData |  |
| 82 | `?CalculateRoute@RouterAdapterCore@@QEAAJAEBV?$vector@VGeoCoordinates@core@@V?$allocator@VGeoCoordinates@core@@@std@@@std@@W4TravelMode@engine@@W4RouteOptimization@5@KPEAURouteOptions@5@@Z` | `0x107F0` | 39 | UnwindData |  |
| 83 | `?CalculateRoute@RouterAdapterCore@@QEAAJAEBV?$vector@VGeoCoordinates@core@@V?$allocator@VGeoCoordinates@core@@@std@@@std@@W4TravelMode@engine@@W4RouteOptimization@5@K_JPEAURouteOptions@5@@Z` | `0x10820` | 389 | UnwindData |  |
| 84 | `?Cancel@RouterAdapterCore@@QEAAXXZ` | `0x109B0` | 144 | UnwindData |  |
| 89 | `?GetAlternateRoute@RouterAdapterCore@@QEAAJIPEAVRoute@core@@@Z` | `0x10B10` | 167 | UnwindData |  |
| 90 | `?GetAlternateRouteCount@RouterAdapterCore@@QEAAJPEAI@Z` | `0x10BC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | `?GetAlternateRouteViolatedOption@RouterAdapterCore@@QEAAJIPEAH@Z` | `0x10BE0` | 139 | UnwindData |  |
| 106 | `?GetConnectivityType@RouterAdapterCore@@QEAAJPEAW4ConnectivityType@engine@@@Z` | `0x10C80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 159 | `?GetProvider@RouterAdapterCore@@QEAAJPEAW4Provider@engine@@@Z` | `0x10CA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 161 | `?GetResultSqmId@RouterAdapterCore@@UEBAKXZ` | `0x10CC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 163 | `?GetRoute@RouterAdapterCore@@QEAAJPEAVRoute@core@@@Z` | `0x10CD0` | 87 | UnwindData |  |
| 188 | `?GetViolatedOptions@RouterAdapterCore@@QEAAJPEAH@Z` | `0x10D30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 189 | `?IncrementGeneration@?$UIThreadCore@UIRouterUI@@@@IEAAJXZ` | `0x10D50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 190 | `?Initialize@?$UIThreadCore@UIRouterUI@@@@IEAAJV?$unique_ptr@UIThreadSignal@@U?$destroy_delete@UIThreadSignal@@@@@std@@@Z` | `0x10D70` | 192 | UnwindData |  |
| 204 | `?IsDispatchEnabled@?$UIThreadCore@UIRouterUI@@@@IEAA_NXZ` | `0x10E70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 214 | `?OnRouteDone@RouterAdapterCore@@UEAAXAEBURouteResult@engine@@@Z` | `0x10E80` | 262 | UnwindData |  |
| 215 | `?OnRouteProgress@RouterAdapterCore@@UEAAXK@Z` | `0x10F90` | 71 | UnwindData |  |
| 216 | `?Post@?$UIThreadCore@UIRouterUI@@@@UEAAXPEAV?$TDispatchItem@UIRouterUI@@@@@Z` | `0x10FE0` | 131 | UnwindData |  |
| 217 | `?ProcessDispatchQueue@?$UIThreadCore@UIRouterUI@@@@QEAAXPEAUIRouterUI@@@Z` | `0x11070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 230 | `?SetDispatchEnabled@?$UIThreadCore@UIRouterUI@@@@IEAAX_N@Z` | `0x11080` | 688 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 247 | `?_CoreInitialize@RouterAdapterCore@@IEAAJHV?$unique_ptr@UIThreadSignal@@U?$destroy_delete@UIThreadSignal@@@@@std@@@Z` | `0x11330` | 407 | UnwindData |  |
| 248 | `?_CoreUninitialize@RouterAdapterCore@@IEAAXXZ` | `0x114D0` | 158 | UnwindData |  |
| 27 | `??0Route@core@@QEAA@XZ` | `0x12100` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `??0RouteLeg@core@@QEAA@XZ` | `0x12130` | 88 | UnwindData |  |
| 31 | `??0RouteManeuver@core@@QEAA@XZ` | `0x12190` | 60 | UnwindData |  |
| 42 | `??1Route@core@@UEAA@XZ` | `0x12260` | 34 | UnwindData |  |
| 43 | `??1RouteLeg@core@@UEAA@XZ` | `0x12290` | 74 | UnwindData |  |
| 44 | `??1RouteManeuver@core@@UEAA@XZ` | `0x122E0` | 58 | UnwindData |  |
| 87 | `?Deserialize@Route@core@@SAJAEAV?$basic_istream@DU?$char_traits@D@std@@@std@@PEAV12@@Z` | `0x123E0` | 621 | UnwindData |  |
| 88 | `?FormatString@RouteManeuver@core@@SAJAEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@KZZ` | `0x12660` | 352 | UnwindData |  |
| 93 | `?GetBackingObject@?$BackedType@V?$shared_ptr@VIManeuver@msnma@@@std@@@core@@QEBA?AV?$shared_ptr@VIManeuver@msnma@@@std@@XZ` | `0x127D0` | 27 | UnwindData |  |
| 94 | `?GetBackingObject@?$BackedType@V?$shared_ptr@VIRoute@msnma@@@std@@@core@@QEBA?AV?$shared_ptr@VIRoute@msnma@@@std@@XZ` | `0x127D0` | 27 | UnwindData |  |
| 103 | `?GetBoundingBox@Route@core@@UEBAJPEAVGeoRect@2@@Z` | `0x12800` | 262 | UnwindData |  |
| 104 | `?GetBoundingBox@RouteLeg@core@@UEBAJPEAVGeoRect@2@@Z` | `0x12910` | 168 | UnwindData |  |
| 107 | `?GetContinueFreewayInstruction@RouteManeuver@core@@AEBAJAEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x129C0` | 287 | UnwindData |  |
| 108 | `?GetCurrentRoadName@RouteManeuver@core@@QEBAJAEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x12AF0` | 212 | UnwindData |  |
| 111 | `?GetDistanceInMetersFromPreviousManeuver@RouteManeuver@core@@QEBAKXZ` | `0x12BD0` | 33 | UnwindData |  |
| 112 | `?GetDistanceInMetersToNextManeuver@RouteManeuver@core@@QEBAKXZ` | `0x12C00` | 33 | UnwindData |  |
| 113 | `?GetDurationInSeconds@Route@core@@UEBAKXZ` | `0x12C30` | 142 | UnwindData |  |
| 114 | `?GetDurationInSeconds@RouteLeg@core@@UEBAKXZ` | `0x12CD0` | 190 | UnwindData |  |
| 115 | `?GetDurationWithoutTrafficInSeconds@Route@core@@UEBAKXZ` | `0x12DA0` | 142 | UnwindData |  |
| 116 | `?GetDurationWithoutTrafficInSeconds@RouteLeg@core@@UEBAKXZ` | `0x12E40` | 190 | UnwindData |  |
| 118 | `?GetEndInstruction@RouteManeuver@core@@AEBAJAEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x12F10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `?GetEnterFreewayInstruction@RouteManeuver@core@@AEBAJAEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x12F20` | 800 | UnwindData |  |
| 121 | `?GetFreewayExitNumber@RouteManeuver@core@@QEBAJAEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x13250` | 43 | UnwindData |  |
| 123 | `?GetGeometryCoordinates@Route@core@@UEBAJKPEAVGeoCoordinates@2@@Z` | `0x13510` | 361 | UnwindData |  |
| 124 | `?GetGeometryCoordinates@RouteLeg@core@@UEBAJKPEAVGeoCoordinates@2@@Z` | `0x13680` | 222 | UnwindData |  |
| 125 | `?GetGeometryCoordinatesCount@Route@core@@UEBAKXZ` | `0x13770` | 142 | UnwindData |  |
| 126 | `?GetGeometryCoordinatesCount@RouteLeg@core@@UEBAKXZ` | `0x13810` | 95 | UnwindData |  |
| 127 | `?GetGoStraightInstruction@RouteManeuver@core@@AEBAJAEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x13880` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 128 | `?GetHeading@RouteManeuver@core@@QEBA?AW4CompassHeading@2@XZ` | `0x138A0` | 94 | UnwindData |  |
| 131 | `?GetInstructionText@RouteManeuver@core@@QEBAJAEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x13910` | 43 | UnwindData |  |
| 132 | `?GetInstructionTextFromBacking@RouteManeuver@core@@AEBAJAEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@0@Z` | `0x13950` | 224 | UnwindData |  |
| 133 | `?GetInstructionWithTarget@RouteManeuver@core@@AEBAJKAEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x13A40` | 85 | UnwindData |  |
| 134 | `?GetInstructionWithTargetAndReplacement@RouteManeuver@core@@AEBAJKAEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@0@Z` | `0x13AA0` | 191 | UnwindData |  |
| 137 | `?GetLeaveFreewayInstruction@RouteManeuver@core@@AEBAJAEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@0@Z` | `0x13B70` | 1,490 | UnwindData |  |
| 139 | `?GetLeg@Route@core@@UEBAJKPEAVRouteLeg@2@@Z` | `0x14150` | 281 | UnwindData |  |
| 141 | `?GetLengthInMeters@Route@core@@UEBAKXZ` | `0x14270` | 142 | UnwindData |  |
| 142 | `?GetLengthInMeters@RouteLeg@core@@UEBAKXZ` | `0x14310` | 190 | UnwindData |  |
| 146 | `?GetManeuver@RouteLeg@core@@UEBAJKPEAVRouteManeuver@2@@Z` | `0x143E0` | 375 | UnwindData |  |
| 147 | `?GetManeuverCount@RouteLeg@core@@UEBAKXZ` | `0x14560` | 84 | UnwindData |  |
| 148 | `?GetManeuverNotice@RouteManeuver@core@@QEBAJPEAH@Z` | `0x145C0` | 422 | UnwindData |  |
| 149 | `?GetManeuverType@RouteManeuver@core@@QEBA?AW4RouteManeuverType@2@XZ` | `0x14770` | 1,043 | UnwindData |  |
| 150 | `?GetManeuverWarningCount@RouteManeuver@core@@QEBAKXZ` | `0x14B90` | 116 | UnwindData |  |
| 151 | `?GetManeuverWarnings@RouteManeuver@core@@QEBAAEBVIItineraryWarning@msnma@@K@Z` | `0x14C10` | 152 | UnwindData |  |
| 164 | `?GetSnappedCompassHeading@RouteManeuver@core@@CA?AW4CompassHeading@2@K@Z` | `0x14D50` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 165 | `?GetStartCoordinates@RouteManeuver@core@@QEBAJPEAVGeoCoordinates@2@@Z` | `0x14E40` | 250 | UnwindData |  |
| 166 | `?GetStartInstruction@RouteManeuver@core@@AEBAJAEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x14F40` | 276 | UnwindData |  |
| 168 | `?GetStopoverInstruction@RouteManeuver@core@@AEBAJAEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x15060` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 169 | `?GetStringResource@RouteManeuver@core@@SAJKAEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x15070` | 330 | UnwindData |  |
| 170 | `?GetTakeFerryInstruction@RouteManeuver@core@@AEBAJAEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x151C0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 171 | `?GetTargetRoadName@RouteManeuver@core@@QEBAJAEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x15250` | 199 | UnwindData |  |
| 174 | `?GetTrafficCircleExitNumber@RouteManeuver@core@@QEBAKXZ` | `0x15320` | 248 | UnwindData |  |
| 175 | `?GetTrafficCircleInstruction@RouteManeuver@core@@AEBAJAEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x15420` | 184 | UnwindData |  |
| 176 | `?GetTrafficCongestion@Route@core@@UEBA?AW4TrafficCongestionType@IRoute@msnma@@XZ` | `0x154E0` | 202 | UnwindData |  |
| 177 | `?GetTrafficCongestion@RouteLeg@core@@UEBA?AW4TrafficCongestionType@IRoute@msnma@@XZ` | `0x155B0` | 193 | UnwindData |  |
| 178 | `?GetTurnInstruction@RouteManeuver@core@@AEBAJAEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x15680` | 741 | UnwindData |  |
| 179 | `?GetUndefinedInstruction@RouteManeuver@core@@AEBAJAEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x15970` | 49 | UnwindData |  |
| 187 | `?GetUturnInstruction@RouteManeuver@core@@AEBAJAEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x159B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 191 | `?Initialize@Route@core@@QEAAJV?$shared_ptr@VIRoute@msnma@@@std@@@Z` | `0x159D0` | 299 | UnwindData |  |
| 192 | `?Initialize@RouteLeg@core@@AEAAJV?$shared_ptr@VIRoute@msnma@@@std@@K@Z` | `0x15B10` | 375 | UnwindData |  |
| 193 | `?Initialize@RouteManeuver@core@@AEAAJAEBV?$vector@V?$shared_ptr@VIManeuver@msnma@@@std@@V?$allocator@V?$shared_ptr@VIManeuver@msnma@@@std@@@2@@std@@H@Z` | `0x15C90` | 347 | UnwindData |  |
| 194 | `?InitializeGeometryCoordinates@RouteLeg@core@@AEAAJXZ` | `0x15E00` | 350 | UnwindData |  |
| 195 | `?InitializeInstructionText@RouteManeuver@core@@AEBAJAEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@0@Z` | `0x15F70` | 1,522 | UnwindData |  |
| 196 | `?InitializeLegs@Route@core@@AEAAJXZ` | `0x16570` | 303 | UnwindData |  |
| 197 | `?InitializeManeuverCondensingContexts@RouteLeg@core@@AEAAJ_N@Z` | `0x166B0` | 777 | UnwindData |  |
| 198 | `?InitializeManeuvers@RouteLeg@core@@AEAAJXZ` | `0x169C0` | 371 | UnwindData |  |
| 203 | `?IsDeserialized@Route@core@@QEBA_NXZ` | `0x16B40` | 145 | UnwindData |  |
| 211 | `?IsValid@Route@core@@QEBA_NXZ` | `0x16CB0` | 275 | UnwindData |  |
| 212 | `?IsValid@RouteLeg@core@@AEBA_NXZ` | `0x16DD0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 221 | `?Serialize@Route@core@@QEBAJAEAV?$basic_ostream@DU?$char_traits@D@std@@@std@@@Z` | `0x16E80` | 378 | UnwindData |  |
| 223 | `?SetBackingObject@?$BackedType@V?$shared_ptr@VIManeuver@msnma@@@std@@@core@@QEAAXAEBV?$shared_ptr@VIManeuver@msnma@@@std@@@Z` | `0x17000` | 6,480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 224 | `?SetBackingObject@?$BackedType@V?$shared_ptr@VIRoute@msnma@@@std@@@core@@QEAAXAEBV?$shared_ptr@VIRoute@msnma@@@std@@@Z` | `0x17000` | 6,480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 218 | `?RegisterListener@SuspendResumeDispatcher@@SAJPEAVISuspendResumeListener@@PEA_N@Z` | `0x18950` | 271 | UnwindData |  |
| 201 | `IsDebugThread` | `0x18B80` | 31 | UnwindData |  |
| 207 | `IsRenderThread` | `0x18BB0` | 31 | UnwindData |  |
| 208 | `IsUIThread` | `0x18BE0` | 62 | UnwindData |  |
| 229 | `SetDebugThreadId` | `0x18F90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 240 | `SetRenderThreadId` | `0x18FA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 242 | `SetUIThreadChecksEnabled` | `0x18FB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 243 | `SetUIThreadId` | `0x18FC0` | 28,888 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `??_7GeoCoordinates@core@@6B@` | `0x20098` | 344 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `??_7Route@core@@6B@` | `0x201F0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `??_7RouteLeg@core@@6B@` | `0x20240` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `??_7RouteManeuver@core@@6B@` | `0x20290` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `??_7GeoRect@core@@6B@` | `0x20298` | 248 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `??_7QueryAdapterCore@@6B@` | `0x20390` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 70 | `??_7OperationAdapterCore@@6B@` | `0x203C0` | 72 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `??_7?$UIThreadCore@UIRouterUI@@@@6B@` | `0x20408` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `??_7RouterAdapterCore@@6B?$UIThreadCore@UIRouterUI@@@@@` | `0x20448` | 24 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `??_7RouterAdapterCore@@6BIRouterUI@@@` | `0x20460` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `??_7RouterAdapterCore@@6BQueryAdapterCore@@@` | `0x20470` | 77,972 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 249 | `?c_DefaultDrivingRouteOptions@RouterAdapterCore@@2URouteOptions@engine@@B` | `0x33504` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 250 | `?c_DefaultWalkingRouteOptions@RouterAdapterCore@@2URouteOptions@engine@@B` | `0x3350C` | 0 | Indeterminate |  |
