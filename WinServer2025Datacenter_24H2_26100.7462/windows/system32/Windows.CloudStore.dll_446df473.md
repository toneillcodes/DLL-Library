# Binary Specification: Windows.CloudStore.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\Windows.CloudStore.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `446df473afa7fcd15f6cfb9605fedb6ada2d42c0ed5902afb297c0ed10a4343e`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DllGetActivationFactory` | `0x6F1A0` | 79 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x6F200` | 107 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x6F450` | 221 | UnwindData |  |
| 4 | `GetProxyDllInfo` | `0xC0B60` | 1,332,572 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
