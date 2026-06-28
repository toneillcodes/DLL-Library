# Binary Specification: LanguageComponentsInstaller.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\LanguageComponentsInstaller.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `4bdf5666753a9632dde959f849219adff0eaaad9f604ef82f1914c918bdea7af`
* **Total Exported Functions:** 7

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `DllRegisterServer` | `0x18CB0` | 40,144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0x18CB0` | 40,144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DllCanUnloadNow` | `0x22980` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x229A0` | 184 | UnwindData |  |
| 5 | `GetUnusedLanguageFeatures` | `0x22A90` | 1,391 | UnwindData |  |
| 6 | `RequestFeaturesInstallation` | `0x25790` | 778 | UnwindData |  |
| 7 | `RequestFeaturesUninstallation` | `0x25AA0` | 481 | UnwindData |  |
