# Binary Specification: wdag.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\Microsoft-Edge-WebView\wdag.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `54ca205f4cbb5594a3300f08e7d57c1270f9c755ed8bcf93b5f1444c2d6405fb`
* **Total Exported Functions:** 12

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 6 | `?WdagSuppressHvsiSplashDialog@@YAXXZ` | `0x3940` | 60 | UnwindData |  |
| 12 | `WdagSuppressHvsiSplashDialog` | `0x3940` | 60 | UnwindData |  |
| 4 | `?WdagGetHvSocketCapability@@YAPEB_WXZ` | `0x3980` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `WdagGetHvSocketCapability` | `0x3980` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `?WdagGetHvSocketGuid@@YA?AU_GUID@@W4Channel@internals@wdag@@@Z` | `0x3990` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `WdagGetHvSocketGuid` | `0x3990` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `?WdagDestroyContainerProxy@@YAXPEAVContainer@internals@wdag@@@Z` | `0x3A20` | 49,248 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `WdagDestroyContainerProxy` | `0x3A20` | 49,248 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `?WdagCreateContainerProxy@@YAPEAVContainer@internals@wdag@@PEAUErrorHandler@23@PEB_W1_N111@Z` | `0xFA80` | 324 | UnwindData |  |
| 7 | `WdagCreateContainerProxy` | `0xFA80` | 324 | UnwindData |  |
| 3 | `?WdagFileHasMarkOfTheContainer@@YA_NPEB_W@Z` | `0xFD60` | 187 | UnwindData |  |
| 9 | `WdagFileHasMarkOfTheContainer` | `0xFD60` | 187 | UnwindData |  |
