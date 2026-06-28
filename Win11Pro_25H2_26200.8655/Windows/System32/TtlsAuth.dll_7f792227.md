# Binary Specification: TtlsAuth.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\TtlsAuth.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `7f792227e402ee439a9993fcf9af9746654762136ca2d4d15dcea45e75ee7474`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 7 | `EapPeerGetInfo` | `0xBC40` | 169 | UnwindData |  |
| 6 | `EapPeerFreeMemory` | `0xD1A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `EapPeerFreeErrorMemory` | `0xD1B0` | 51 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x10690` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x106B0` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0x108A0` | 91 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0x10910` | 17 | UnwindData |  |
