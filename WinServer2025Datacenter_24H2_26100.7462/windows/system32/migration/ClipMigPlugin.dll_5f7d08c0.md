# Binary Specification: ClipMigPlugin.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\migration\ClipMigPlugin.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `5f7d08c0fd558db0cefc27919735a77ba92a530ce0b1a10aca301ec27cd04559`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x67C0` | 42 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x67F0` | 302 | UnwindData |  |
| 3 | `DllMain` | `0x6930` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllRegisterServer` | `0x6950` | 293 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x6A80` | 151 | UnwindData |  |
