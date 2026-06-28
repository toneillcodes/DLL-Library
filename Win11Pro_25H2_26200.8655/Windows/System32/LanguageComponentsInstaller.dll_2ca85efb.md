# Binary Specification: LanguageComponentsInstaller.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\LanguageComponentsInstaller.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `2ca85efb88a882daca7df069396db4a669570ea3a73f70a5d5b743d793d9a8eb`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `DllRegisterServer` | `0x184E0` | 39,968 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0x184E0` | 39,968 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DllCanUnloadNow` | `0x22100` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x22120` | 184 | UnwindData |  |
| 5 | `GetUnusedLanguageFeatures` | `0x22210` | 1,391 | UnwindData |  |
| 6 | `RequestFeaturesInstallation` | `0x24F30` | 786 | UnwindData |  |
| 7 | `RequestFeaturesUninstallation` | `0x25250` | 489 | UnwindData |  |
