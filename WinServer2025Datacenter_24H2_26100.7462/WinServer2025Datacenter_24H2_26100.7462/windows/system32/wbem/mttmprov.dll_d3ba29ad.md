# Binary Specification: mttmprov.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wbem\mttmprov.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d3ba29ad1066228f2d776c28c69157212ba75cece21ed88374801f146a0c5f36`
* **Total Exported Functions:** 11

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 8 | `MI_Main` | `0x2380` | 2,224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllCanUnloadNow` | `0x2C30` | 47 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x2C70` | 119 | UnwindData |  |
| 4 | `DllMain` | `0x2CF0` | 82 | UnwindData |  |
| 5 | `DllRegisterServer` | `0x2D50` | 72 | UnwindData |  |
| 6 | `DllUnregisterServer` | `0x2DA0` | 65 | UnwindData |  |
| 7 | `GetProviderClassID` | `0x2FC0` | 164,752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `CommonTraps` | `0x2B350` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `TaskManagerTraps` | `0x2B3C0` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `NITS_STUB` | `0x2B530` | 107,368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `NITS_PRESENCE_STUB` | `0x45898` | 0 | Indeterminate |  |
