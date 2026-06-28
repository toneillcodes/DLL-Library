# Binary Specification: wlanui.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wlanui.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `da4b308a96c0d34b88d71d492626b968599f6e97be160fb65e9a7002b35480ff`
* **Total Exported Functions:** 6

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllGetClassObject` | `0x6610` | 281 | UnwindData |  |
| 2 | `WLFreeProfile` | `0x7410` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `WLFreeProfileXml` | `0x7430` | 68,000 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `WLInvokeProfileUI` | `0x17DD0` | 123 | UnwindData |  |
| 5 | `WLInvokeProfileUIFromXMLFile` | `0x17E60` | 278 | UnwindData |  |
| 6 | `WlanUIEditProfile` | `0x17F80` | 762 | UnwindData |  |
