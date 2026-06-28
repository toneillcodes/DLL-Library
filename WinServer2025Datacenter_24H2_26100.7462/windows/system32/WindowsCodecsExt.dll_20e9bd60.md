# Binary Specification: WindowsCodecsExt.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\WindowsCodecsExt.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `20e9bd6028d2618e81e10cf652798ce94c8516488eb49ab031adcd7f3d8753c1`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DllGetClassObject` | `0x85E0` | 28 | UnwindData |  |
| 4 | `WICCreateColorTransform_Proxy` | `0x8F50` | 90 | UnwindData |  |
| 3 | `IWICColorTransform_Initialize_Proxy` | `0x108C0` | 60 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x15960` | 143,916 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
