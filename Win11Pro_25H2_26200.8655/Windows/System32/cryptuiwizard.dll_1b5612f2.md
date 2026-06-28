# Binary Specification: cryptuiwizard.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\cryptuiwizard.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `1b5612f280b6f581ed52079d47790c77dacc4f23af318ffc09b0b346b05e2681`
* **Total Exported Functions:** 8

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 8 | `DllMain` | `0x1F40` | 106 | UnwindData |  |
| 1 | `GetFunctionTable` | `0x1FB0` | 18,368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `CryptUIWizBuildCTL` | `0x6770` | 4,737 | UnwindData |  |
| 3 | `CryptUIWizDigitalSign` | `0xE5C0` | 749 | UnwindData |  |
| 5 | `CryptUIWizFreeDigitalSignContext` | `0xE8C0` | 50 | UnwindData |  |
| 4 | `CryptUIWizExport` | `0x153F0` | 1,298 | UnwindData |  |
| 6 | `CryptUIWizImport` | `0x19330` | 46 | UnwindData |  |
| 7 | `CryptUIWizImportInternal` | `0x19370` | 4,079 | UnwindData |  |
