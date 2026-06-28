# Binary Specification: WpdFs.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\wpdfs.inf_amd64_4c800bb8291de301\WpdFs.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `0c1bb98cf61abbe4b24ca88caeef9612f2660ac21182f0046a86d3cede2aff59`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x5C70` | 42 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x5CA0` | 512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllRegisterServer` | `0x5EA0` | 92 | UnwindData |  |
| 4 | `DllUnregisterServer` | `0x5F10` | 89 | UnwindData |  |
| 5 | `Microsoft_WDF_UMDF_Version` | `0x37BE8` | 0 | Indeterminate |  |
