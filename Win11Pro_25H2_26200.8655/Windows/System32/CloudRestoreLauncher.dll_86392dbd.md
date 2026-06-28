# Binary Specification: CloudRestoreLauncher.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\CloudRestoreLauncher.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `86392dbd81411c96a12230f7a56dc2bf0a50eb31f1f9023af6829f014a8cc126`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `DllCanUnloadNow` | `0x26F60` | 86 | UnwindData |  |
| 5 | `DllGetClassObject` | `0x26FC0` | 199 | UnwindData |  |
| 4 | `DllGetActivationFactory` | `0x274D0` | 195 | UnwindData |  |
| 1 | `ServiceMain` | `0x283F0` | 64 | UnwindData |  |
| 2 | `SvchostPushServiceGlobals` | `0x28440` | 1,071,309 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
