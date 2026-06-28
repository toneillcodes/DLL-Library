# Binary Specification: OfflineSetupProvider.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\Dism\OfflineSetupProvider.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `83e8e510402f6709fa38de109d8d394eaa49fa742ad8f21bbc9c06591addde75`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DLLGetDISMProviderCLSID` | `0x3A00` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllCanUnloadNow` | `0x3A30` | 42 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x3A60` | 302 | UnwindData |  |
| 4 | `DllRegisterServer` | `0x3BD0` | 243 | UnwindData |  |
| 5 | `DllUnregisterServer` | `0x3CD0` | 114 | UnwindData |  |
