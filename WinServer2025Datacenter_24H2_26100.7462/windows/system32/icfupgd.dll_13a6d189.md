# Binary Specification: icfupgd.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\icfupgd.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `13a6d189e905376306ab53cf16e7a9eefa4e6919e55906a7def36fb823cf94fe`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0xE480` | 42 | UnwindData |  |
| 2 | `DllGetClassObject` | `0xE4B0` | 103 | UnwindData |  |
| 3 | `DllMain` | `0xE600` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllRegisterServer` | `0xE620` | 335 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0xE780` | 29,852 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
