# Binary Specification: icsvc.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\icsvc.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `e71e349ffed7b2588753c6cbc72cecfc67ea846ab3d3c86a408eff27043fe14f`
* **Total Exported Functions:** 8

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllRegisterServer` | `0x5FE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllUnregisterServer` | `0x5FE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `GuestInterfaceServiceMain` | `0x5FF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `HeartbeatServiceMain` | `0x6010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `KvpexchangeServiceMain` | `0x6020` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `ShutdownServiceMain` | `0x6040` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `TimesyncServiceMain` | `0x6060` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `VMSessionServiceMain` | `0x6080` | 166,108 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
