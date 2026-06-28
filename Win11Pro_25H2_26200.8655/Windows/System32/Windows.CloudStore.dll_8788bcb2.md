# Binary Specification: Windows.CloudStore.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\Windows.CloudStore.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `8788bcb2b6ca3a5e010ade22fc5cce133b69c87f94e8d777f38c6c98053d73a7`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DllGetActivationFactory` | `0x6EBF0` | 79 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x6EC50` | 107 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x6EEA0` | 221 | UnwindData |  |
| 4 | `GetProxyDllInfo` | `0xBFCE0` | 1,329,036 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
