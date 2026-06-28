# Binary Specification: upnphost.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\upnphost.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ed3c2979a03b07c700911854f60870d7243a2b80cf0cb5aae6d3e1ccf7920a4f`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `DllGetClassObject` | `0x33A20` | 120 | UnwindData |  |
| 2 | `DllCanUnloadNow` | `0x35060` | 35,072 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllRegisterServer` | `0x3D960` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DllUnregisterServer` | `0x3D960` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `ServiceMain` | `0x3D970` | 35,600 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `SvchostPushServiceGlobals` | `0x46480` | 69,900 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
