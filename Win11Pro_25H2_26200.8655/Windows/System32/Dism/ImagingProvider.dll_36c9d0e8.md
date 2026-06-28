# Binary Specification: ImagingProvider.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\Dism\ImagingProvider.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `36c9d0e8a41d5e9439df1e512a0a5613a2c65a095b9beeb8b76ecbff0250c818`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DLLGetDISMProviderCLSID` | `0x3A30` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllCanUnloadNow` | `0x3A60` | 42 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x3A90` | 302 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x3C00` | 243 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x3D00` | 114 | UnwindData |  |
