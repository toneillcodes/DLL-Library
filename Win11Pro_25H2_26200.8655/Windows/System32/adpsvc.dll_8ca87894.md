# Binary Specification: adpsvc.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\adpsvc.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `8ca8789466533fb70e8eb463feade67402e531a8233c9f7465176d653e8e9737`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `DllCanUnloadNow` | `0x8480` | 157 | UnwindData |  |
| 4 | `DllGetActivationFactory` | `0x8530` | 343 | UnwindData |  |
| 1 | `ServiceMain` | `0xAFD0` | 308 | UnwindData |  |
| 2 | `SvchostPushServiceGlobals` | `0xB5C0` | 796,316 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
