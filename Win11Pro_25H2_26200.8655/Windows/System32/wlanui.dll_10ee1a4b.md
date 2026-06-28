# Binary Specification: wlanui.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\wlanui.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `10ee1a4bc4f9e36fd9cfcc4bfa30513c2fecd20f2b07e1a28e8e33c9915685c2`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllGetClassObject` | `0x6610` | 281 | UnwindData |  |
| 2 | `WLFreeProfile` | `0x7410` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `WLFreeProfileXml` | `0x7430` | 68,016 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `WLInvokeProfileUI` | `0x17DE0` | 123 | UnwindData |  |
| 5 | `WLInvokeProfileUIFromXMLFile` | `0x17E70` | 278 | UnwindData |  |
| 6 | `WlanUIEditProfile` | `0x17F90` | 762 | UnwindData |  |
