# Binary Specification: WimProvider.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\Dism\WimProvider.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `6cdfa4d5c0df579efc667abbb6ea623bd464d3c93c1f02a63b86a774955d2ca4`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DLLGetDISMProviderCLSID` | `0x82D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllCanUnloadNow` | `0x8300` | 42 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x8330` | 302 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x84D0` | 243 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x85D0` | 114 | UnwindData |  |
