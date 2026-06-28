# Binary Specification: httpapi.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\httpapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d09f0b393b0c681f8013358bee69d1661c43b14be5e53be20e8aef4e3008de7a`
* **Total Exported Functions:** 49

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 35 | `HttpRemoveUrl` | `0x1010` | 294 | UnwindData |  |
| 36 | `HttpRemoveUrlFromUrlGroup` | `0x1200` | 69 | UnwindData |  |
| 38 | `HttpSendResponseEntityBody` | `0x1350` | 349 | UnwindData |  |
| 17 | `HttpDeleteServiceConfiguration` | `0x14C0` | 313 | UnwindData |  |
| 42 | `HttpSetServiceConfiguration` | `0x1600` | 311 | UnwindData |  |
| 48 | `HttpWaitForDisconnect` | `0x1A50` | 195 | UnwindData |  |
| 21 | `HttpGetCounters` | `0x1B20` | 316 | UnwindData |  |
| 20 | `HttpFlushResponseCache` | `0x1CD0` | 243 | UnwindData |  |
| 34 | `HttpReceiveRequestEntityBody` | `0x1DD0` | 242 | UnwindData |  |
| 29 | `HttpQueryServiceConfiguration` | `0x1F20` | 1,988 | UnwindData |  |
| 37 | `HttpSendHttpResponse` | `0x26F0` | 532 | UnwindData |  |
| 33 | `HttpReceiveHttpRequest` | `0x2910` | 282 | UnwindData |  |
| 23 | `HttpInitialize` | `0x3490` | 238 | UnwindData |  |
| 9 | `HttpCreateHttpHandle` | `0x37F0` | 224 | UnwindData |  |
| 3 | `HttpAddUrlToUrlGroup` | `0x39B0` | 63 | UnwindData |  |
| 12 | `HttpCreateServerSession` | `0x3C30` | 270 | UnwindData |  |
| 45 | `HttpTerminate` | `0x3D50` | 6 | UnwindData |  |
| 13 | `HttpCreateUrlGroup` | `0x4190` | 296 | UnwindData |  |
| 2 | `HttpAddUrl` | `0x42C0` | 284 | UnwindData |  |
| 11 | `HttpCreateRequestQueueEx` | `0x43F0` | 93 | UnwindData |  |
| 7 | `HttpCloseUrlGroup` | `0x4EC0` | 134 | UnwindData |  |
| 19 | `HttpFindUrlGroupId` | `0x4F50` | 224 | UnwindData |  |
| 25 | `HttpPrepareUrl` | `0x5040` | 527 | UnwindData |  |
| 30 | `HttpQueryUrlGroupProperty` | `0x5260` | 193 | UnwindData |  |
| 43 | `HttpSetUrlGroupProperty` | `0x5330` | 216 | UnwindData |  |
| 6 | `HttpCloseServerSession` | `0x5570` | 135 | UnwindData |  |
| 28 | `HttpQueryServerSessionProperty` | `0x5600` | 229 | UnwindData |  |
| 41 | `HttpSetServerSessionProperty` | `0x56F0` | 237 | UnwindData |  |
| 4 | `HttpCancelHttpRequest` | `0x5920` | 108 | UnwindData |  |
| 14 | `HttpDeclarePush` | `0x6010` | 259 | UnwindData |  |
| 15 | `HttpDelegateRequest` | `0x6120` | 184 | UnwindData |  |
| 16 | `HttpDelegateRequestEx` | `0x61E0` | 218 | UnwindData |  |
| 18 | `HttpEvaluateRequest` | `0x62C0` | 132 | UnwindData |  |
| 26 | `HttpQueryRequestProperty` | `0x65C0` | 406 | UnwindData |  |
| 39 | `HttpSetRequestProperty` | `0x6D30` | 304 | UnwindData |  |
| 49 | `HttpWaitForDisconnectEx` | `0x7040` | 170 | UnwindData |  |
| 1 | `HttpAddFragmentToCache` | `0x82D0` | 245 | UnwindData |  |
| 5 | `HttpCloseRequestQueue` | `0x83D0` | 44 | UnwindData |  |
| 10 | `HttpCreateRequestQueue` | `0x8410` | 36 | UnwindData |  |
| 27 | `HttpQueryRequestQueueProperty` | `0x8440` | 200 | UnwindData |  |
| 31 | `HttpReadFragmentFromCache` | `0x8510` | 245 | UnwindData |  |
| 32 | `HttpReceiveClientCertificate` | `0x8610` | 191 | UnwindData |  |
| 40 | `HttpSetRequestQueueProperty` | `0x86E0` | 177 | UnwindData |  |
| 44 | `HttpShutdownRequestQueue` | `0x87A0` | 42 | UnwindData |  |
| 47 | `HttpWaitForDemandStart` | `0x87D0` | 44 | UnwindData |  |
| 24 | `HttpIsFeatureSupported` | `0x92F0` | 164 | UnwindData |  |
| 46 | `HttpUpdateServiceConfiguration` | `0x93A0` | 410 | UnwindData |  |
| 8 | `HttpControlService` | `0xA2E0` | 177 | UnwindData |  |
| 22 | `HttpGetExtension` | `0xA570` | 175 | UnwindData |  |
