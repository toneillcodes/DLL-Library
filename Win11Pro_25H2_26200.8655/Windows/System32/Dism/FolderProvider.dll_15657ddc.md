# Binary Specification: FolderProvider.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\Dism\FolderProvider.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `15657ddc03eec6003eac1ba917277cd04409fb50c7afd6cb4641c7ee1fbe6638`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DLLGetDISMProviderCLSID` | `0x3830` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllCanUnloadNow` | `0x3860` | 42 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x3890` | 302 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x3A00` | 243 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x3B00` | 114 | UnwindData |  |
