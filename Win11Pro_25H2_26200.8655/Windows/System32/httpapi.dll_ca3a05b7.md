# Binary Specification: httpapi.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\httpapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ca3a05b7e413e45dc71fbb4649b68493a2582726f368b0b34438b9e47d6f835f`
* **Total Exported Functions:** 49

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 35 | `HttpRemoveUrl` | `0x1010` | 304 | UnwindData |  |
| 36 | `HttpRemoveUrlFromUrlGroup` | `0x1210` | 69 | UnwindData |  |
| 38 | `HttpSendResponseEntityBody` | `0x1360` | 349 | UnwindData |  |
| 17 | `HttpDeleteServiceConfiguration` | `0x14D0` | 313 | UnwindData |  |
| 42 | `HttpSetServiceConfiguration` | `0x1610` | 311 | UnwindData |  |
| 48 | `HttpWaitForDisconnect` | `0x1A60` | 185 | UnwindData |  |
| 21 | `HttpGetCounters` | `0x1B20` | 320 | UnwindData |  |
| 20 | `HttpFlushResponseCache` | `0x1CD0` | 246 | UnwindData |  |
| 34 | `HttpReceiveRequestEntityBody` | `0x1DD0` | 244 | UnwindData |  |
| 29 | `HttpQueryServiceConfiguration` | `0x1F20` | 2,004 | UnwindData |  |
| 37 | `HttpSendHttpResponse` | `0x2700` | 537 | UnwindData |  |
| 33 | `HttpReceiveHttpRequest` | `0x2920` | 284 | UnwindData |  |
| 23 | `HttpInitialize` | `0x34C0` | 245 | UnwindData |  |
| 9 | `HttpCreateHttpHandle` | `0x3780` | 229 | UnwindData |  |
| 3 | `HttpAddUrlToUrlGroup` | `0x3870` | 63 | UnwindData |  |
| 12 | `HttpCreateServerSession` | `0x3AF0` | 283 | UnwindData |  |
| 45 | `HttpTerminate` | `0x3C20` | 6 | UnwindData |  |
| 13 | `HttpCreateUrlGroup` | `0x4070` | 301 | UnwindData |  |
| 2 | `HttpAddUrl` | `0x41B0` | 291 | UnwindData |  |
| 11 | `HttpCreateRequestQueueEx` | `0x42E0` | 93 | UnwindData |  |
| 7 | `HttpCloseUrlGroup` | `0x4DD0` | 134 | UnwindData |  |
| 19 | `HttpFindUrlGroupId` | `0x4E60` | 225 | UnwindData |  |
| 25 | `HttpPrepareUrl` | `0x4F50` | 535 | UnwindData |  |
| 30 | `HttpQueryUrlGroupProperty` | `0x5170` | 194 | UnwindData |  |
| 43 | `HttpSetUrlGroupProperty` | `0x5240` | 217 | UnwindData |  |
| 6 | `HttpCloseServerSession` | `0x5480` | 135 | UnwindData |  |
| 28 | `HttpQueryServerSessionProperty` | `0x5510` | 233 | UnwindData |  |
| 41 | `HttpSetServerSessionProperty` | `0x5600` | 243 | UnwindData |  |
| 4 | `HttpCancelHttpRequest` | `0x5830` | 108 | UnwindData |  |
| 14 | `HttpDeclarePush` | `0x5F10` | 261 | UnwindData |  |
| 15 | `HttpDelegateRequest` | `0x6020` | 191 | UnwindData |  |
| 16 | `HttpDelegateRequestEx` | `0x60F0` | 225 | UnwindData |  |
| 18 | `HttpEvaluateRequest` | `0x61E0` | 134 | UnwindData |  |
| 26 | `HttpQueryRequestProperty` | `0x64E0` | 399 | UnwindData |  |
| 39 | `HttpSetRequestProperty` | `0x6CA0` | 299 | UnwindData |  |
| 49 | `HttpWaitForDisconnectEx` | `0x6FB0` | 174 | UnwindData |  |
| 1 | `HttpAddFragmentToCache` | `0x8480` | 248 | UnwindData |  |
| 5 | `HttpCloseRequestQueue` | `0x8580` | 44 | UnwindData |  |
| 10 | `HttpCreateRequestQueue` | `0x85C0` | 36 | UnwindData |  |
| 27 | `HttpQueryRequestQueueProperty` | `0x85F0` | 205 | UnwindData |  |
| 31 | `HttpReadFragmentFromCache` | `0x86D0` | 250 | UnwindData |  |
| 32 | `HttpReceiveClientCertificate` | `0x87D0` | 193 | UnwindData |  |
| 40 | `HttpSetRequestQueueProperty` | `0x88A0` | 182 | UnwindData |  |
| 44 | `HttpShutdownRequestQueue` | `0x8960` | 42 | UnwindData |  |
| 47 | `HttpWaitForDemandStart` | `0x8990` | 44 | UnwindData |  |
| 24 | `HttpIsFeatureSupported` | `0x94E0` | 174 | UnwindData |  |
| 46 | `HttpUpdateServiceConfiguration` | `0x95A0` | 410 | UnwindData |  |
| 8 | `HttpControlService` | `0xA4F0` | 180 | UnwindData |  |
| 22 | `HttpGetExtension` | `0xA790` | 188 | UnwindData |  |
