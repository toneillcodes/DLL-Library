# Binary Specification: eapsimextdesktop.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\eapsimextdesktop.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `dbd69bed450fd231a7e4ee1dc7379e275212d3eedfdaac3d53e472fd80fa15d6`
* **Total Exported Functions:** 5

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | `DllCanUnloadNow` | `0x8120` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllGetClassObject` | `0x8140` | 1,312 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `EapSimExtCallRunWizard` | `0x8660` | 353 | UnwindData |  |
| 5 | `EapSimExtGetIdentityPageGuid` | `0x87D0` | 58 | UnwindData |  |
| 1 | `EapSimExtInvokeUIAndGetConfig` | `0x9510` | 819 | UnwindData |  |
