# Binary Specification: SDDS.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\SDDS.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `94331ba916f5feaa77e4b1b57a9fa2936cc45389903d31f8f884a4e949b11376`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0xA410` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0xA430` | 1,536 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `SDDSCreateChxDictionary` | `0xAA30` | 147 | UnwindData |  |
| 4 | `SDDSGetCharacterMappingObject` | `0xAAD0` | 282 | UnwindData |  |
