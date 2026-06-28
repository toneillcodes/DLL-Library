# Binary Specification: FXSROUTE.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\FXSROUTE.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ccd68e3a8ed2755a6ee2f1702124f8153a1b54756eb0e156824dc66dd2d1fd25`
* **Total Exported Functions:** 10

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `FaxRouteConfigure` | `0x2D90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `FaxRouteEmail` | `0x2DA0` | 813 | UnwindData |  |
| 3 | `FaxRoutePrint` | `0x30E0` | 629 | UnwindData |  |
| 4 | `FaxRouteStore` | `0x3360` | 1,296 | UnwindData |  |
| 6 | `FaxRouteDeviceChangeNotification` | `0x3E90` | 67 | UnwindData |  |
| 7 | `FaxRouteDeviceEnable` | `0x3EE0` | 260 | UnwindData |  |
| 9 | `FaxRouteInitialize` | `0x3FF0` | 617 | UnwindData |  |
| 5 | `FaxExtInitializeConfig` | `0x7070` | 148 | UnwindData |  |
| 8 | `FaxRouteGetRoutingInfo` | `0x7110` | 530 | UnwindData |  |
| 10 | `FaxRouteSetRoutingInfo` | `0x7330` | 449 | UnwindData |  |
