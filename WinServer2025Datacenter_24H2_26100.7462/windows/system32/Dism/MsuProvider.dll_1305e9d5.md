# Binary Specification: MsuProvider.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\Dism\MsuProvider.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `1305e9d57a28b3046871fee271dbc4dc319912853cd7d944d1960c46d8f774ea`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DLLGetDISMProviderCLSID` | `0x39E0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllCanUnloadNow` | `0x3A10` | 42 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x3A40` | 302 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x3BB0` | 243 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x3CB0` | 114 | UnwindData |  |
