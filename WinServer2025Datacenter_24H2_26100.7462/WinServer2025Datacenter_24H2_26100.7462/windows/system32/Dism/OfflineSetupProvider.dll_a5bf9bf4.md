# Binary Specification: OfflineSetupProvider.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\Dism\OfflineSetupProvider.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a5bf9bf4315b1262cd0b03a5c1f7846f2c8db57d84cd0f2ea3b9d2e746a2fde0`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DLLGetDISMProviderCLSID` | `0x3A00` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllCanUnloadNow` | `0x3A30` | 42 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x3A60` | 302 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x3BD0` | 243 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x3CD0` | 114 | UnwindData |  |
