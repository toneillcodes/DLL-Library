# Binary Specification: FolderProvider.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\Dism\FolderProvider.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `15fdb10189ad2b09756300d0989952ce03c3cbea9d0c889adbd0dc5000f3c9cc`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DLLGetDISMProviderCLSID` | `0x3830` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllCanUnloadNow` | `0x3860` | 42 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x3890` | 302 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x3A00` | 243 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x3B00` | 114 | UnwindData |  |
