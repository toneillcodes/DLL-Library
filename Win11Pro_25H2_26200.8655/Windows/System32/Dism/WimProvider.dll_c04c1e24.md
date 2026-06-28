# Binary Specification: WimProvider.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\Dism\WimProvider.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `c04c1e243ed745ba9ad8f2e012faae076df40c3bcc9b397e1caf0b5d1e72e176`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DLLGetDISMProviderCLSID` | `0x82D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllCanUnloadNow` | `0x8300` | 42 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x8330` | 302 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x84D0` | 243 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x85D0` | 114 | UnwindData |  |
