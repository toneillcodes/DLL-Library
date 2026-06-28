# Binary Specification: dinput.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\dinput.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `262c4b8e112fdce256fa10f071a6e871e3fe958762db872a7f915e9ff43a8e71`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DirectInputCreateA` | `0xD550` | 41 | UnwindData |  |
| 2 | `DirectInputCreateEx` | `0xD580` | 202 | UnwindData |  |
| 3 | `DirectInputCreateW` | `0xD710` | 41 | UnwindData |  |
| 4 | `DllCanUnloadNow` | `0xD740` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DllGetClassObject` | `0xD850` | 171 | UnwindData |  |
| 6 | `DllRegisterServer` | `0x1BB30` | 624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `DllUnregisterServer` | `0x1BDA0` | 21,197 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
