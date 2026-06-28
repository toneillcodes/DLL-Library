# Binary Specification: WindowsCodecsExt.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\WindowsCodecsExt.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `3cb2d54abbde17b2efc712d2eaef925719d06b4de8471e7ae30152005202570d`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DllGetClassObject` | `0x7F80` | 28 | UnwindData |  |
| 4 | `WICCreateColorTransform_Proxy` | `0x88F0` | 90 | UnwindData |  |
| 3 | `IWICColorTransform_Initialize_Proxy` | `0x105F0` | 60 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x15770` | 138,652 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
