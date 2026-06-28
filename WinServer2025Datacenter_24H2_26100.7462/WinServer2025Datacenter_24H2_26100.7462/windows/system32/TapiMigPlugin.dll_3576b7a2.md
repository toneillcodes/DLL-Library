# Binary Specification: TapiMigPlugin.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\TapiMigPlugin.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `3576b7a2ab8c019dbfd19184058ca018f0dd4edc6d58f7e8cb72116ffbfcaa88`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x8D20` | 42 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x8D50` | 302 | UnwindData |  |
| 3 | `DllMain` | `0x8E90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllRegisterServer` | `0x8EB0` | 293 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x8FE0` | 151 | UnwindData |  |
