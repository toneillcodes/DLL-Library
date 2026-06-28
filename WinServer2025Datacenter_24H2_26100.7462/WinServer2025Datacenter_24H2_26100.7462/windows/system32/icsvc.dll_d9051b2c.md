# Binary Specification: icsvc.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\icsvc.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d9051b2c8d77b272b16075a8f40d912e70dffc6173632decce533f9bb4235f04`
* **Total Exported Functions:** 8

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllRegisterServer` | `0x60E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllUnregisterServer` | `0x60E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `GuestInterfaceServiceMain` | `0x60F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `HeartbeatServiceMain` | `0x6110` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `KvpexchangeServiceMain` | `0x6120` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `ShutdownServiceMain` | `0x6140` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `TimesyncServiceMain` | `0x6160` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `VMSessionServiceMain` | `0x6180` | 183,788 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
