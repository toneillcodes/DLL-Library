# Binary Specification: AppxProvider.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\Dism\AppxProvider.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `1e48c455a347ad6b638923df203c9c722f5c03f9fd69a7ed1fdfee668c9bfec8`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DLLGetDISMProviderCLSID` | `0x4C80` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllCanUnloadNow` | `0x4CB0` | 42 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x4CE0` | 302 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x4E80` | 243 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x4F80` | 114 | UnwindData |  |
