# Binary Specification: LogProvider.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\Dism\LogProvider.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `b0de9f08a1f31aa38aad20807561a16bca7e76ebea5d5a7397097a494ab14018`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DLLGetDISMProviderCLSID` | `0x3870` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllCanUnloadNow` | `0x38A0` | 42 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x38D0` | 302 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x3A40` | 243 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x3B40` | 114 | UnwindData |  |
