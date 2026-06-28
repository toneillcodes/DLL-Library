# Binary Specification: upnphost.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\upnphost.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `1654eeb5a4047c35af8eac84f54f6da79bb8ba1274d833d39b566075998b72f8`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `DllGetClassObject` | `0x35880` | 120 | UnwindData |  |
| 2 | `DllCanUnloadNow` | `0x36DC0` | 28,160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllRegisterServer` | `0x3DBC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DllUnregisterServer` | `0x3DBC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `ServiceMain` | `0x3DBD0` | 13,904 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `SvchostPushServiceGlobals` | `0x41220` | 97,852 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
