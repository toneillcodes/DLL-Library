# Binary Specification: hascsp.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\hascsp.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `b39f2d150cfbafffb019b8d6f561cc9f227077ecda4ad3992542a51e81b4853f`
* **Total Exported Functions:** 11

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `PolicyManager_PreCheck` | `0x2C40` | 124 | UnwindData |  |
| 10 | `DllRegisterServer` | `0x4F30` | 72,864 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `DllUnregisterServer` | `0x4F30` | 72,864 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `DllCanUnloadNow` | `0x16BD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `DllGetClassObject` | `0x16BF0` | 214 | UnwindData |  |
| 9 | `DllMain` | `0x16CD0` | 235 | UnwindData |  |
| 1 | `GetForceRetrieve` | `0x17180` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `GetHealthCert` | `0x171A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `GetNonce` | `0x171C0` | 574 | UnwindData |  |
| 5 | `SetForceRetrieve` | `0x175F0` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `SetNonce` | `0x17760` | 353 | UnwindData |  |
