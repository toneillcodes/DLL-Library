# Binary Specification: wdag.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\Microsoft-Edge-WebView\wdag.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `289ae01f11e7a492d6b2b08755a2105bf61c9fa968d8b8e39bc1b6ce82ec5f62`
* **Total Exported Functions:** 12

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 6 | `?WdagSuppressHvsiSplashDialog@@YAXXZ` | `0x3B80` | 60 | UnwindData |  |
| 12 | `WdagSuppressHvsiSplashDialog` | `0x3B80` | 60 | UnwindData |  |
| 4 | `?WdagGetHvSocketCapability@@YAPEB_WXZ` | `0x3BC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `WdagGetHvSocketCapability` | `0x3BC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `?WdagGetHvSocketGuid@@YA?AU_GUID@@W4Channel@internals@wdag@@@Z` | `0x3BD0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `WdagGetHvSocketGuid` | `0x3BD0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `?WdagDestroyContainerProxy@@YAXPEAVContainer@internals@wdag@@@Z` | `0x3C60` | 54,720 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `WdagDestroyContainerProxy` | `0x3C60` | 54,720 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `?WdagCreateContainerProxy@@YAPEAVContainer@internals@wdag@@PEAUErrorHandler@23@PEB_W1_N111@Z` | `0x11220` | 289 | UnwindData |  |
| 7 | `WdagCreateContainerProxy` | `0x11220` | 289 | UnwindData |  |
| 3 | `?WdagFileHasMarkOfTheContainer@@YA_NPEB_W@Z` | `0x114B0` | 188 | UnwindData |  |
| 9 | `WdagFileHasMarkOfTheContainer` | `0x114B0` | 188 | UnwindData |  |
