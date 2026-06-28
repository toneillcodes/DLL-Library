# Binary Specification: FfuProvider.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\Dism\FfuProvider.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `87882c399d2882083fa737a1fdb1e53c8c1e0d8bdb115a24c113b8807b57e53e`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DLLGetDISMProviderCLSID` | `0x4160` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllCanUnloadNow` | `0x4190` | 42 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x41C0` | 302 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x4330` | 243 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x4430` | 114 | UnwindData |  |
