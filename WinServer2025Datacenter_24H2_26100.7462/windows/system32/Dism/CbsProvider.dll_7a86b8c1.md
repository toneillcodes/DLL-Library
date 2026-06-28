# Binary Specification: CbsProvider.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\Dism\CbsProvider.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `7a86b8c15ba8753163dee8182f0f83fa9a325c94b7c9cf1d32c12b72616ad5b3`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DLLGetDISMProviderCLSID` | `0x5450` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllCanUnloadNow` | `0x5480` | 42 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x54B0` | 302 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x5620` | 243 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x5720` | 114 | UnwindData |  |
