# Binary Specification: eapsimextdesktop.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\eapsimextdesktop.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a343d8b19a4705e5efbda35c976689e017fb95f4b53d3c1c2afc371a1bdb3db6`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DllCanUnloadNow` | `0x8130` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllGetClassObject` | `0x8150` | 1,312 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `EapSimExtCallRunWizard` | `0x8670` | 353 | UnwindData |  |
| 5 | `EapSimExtGetIdentityPageGuid` | `0x87E0` | 58 | UnwindData |  |
| 1 | `EapSimExtInvokeUIAndGetConfig` | `0x9520` | 819 | UnwindData |  |
