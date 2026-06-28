# Binary Specification: MsuProvider.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\Dism\MsuProvider.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `b56967fb6bb0e4cf7ae0573e7a15a262158755562ad441e7eede414af03d29c7`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DLLGetDISMProviderCLSID` | `0x39E0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllCanUnloadNow` | `0x3A10` | 42 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x3A40` | 302 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x3BB0` | 243 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x3CB0` | 114 | UnwindData |  |
