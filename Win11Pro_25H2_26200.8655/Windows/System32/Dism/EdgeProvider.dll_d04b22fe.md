# Binary Specification: EdgeProvider.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\Dism\EdgeProvider.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d04b22fe0f259207f744d25f2acfa53cca4567dba2627f98b7193cc24d4cccfe`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DLLGetDISMProviderCLSID` | `0x3F40` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllCanUnloadNow` | `0x3F70` | 42 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x3FA0` | 302 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x4110` | 243 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x4210` | 114 | UnwindData |  |
