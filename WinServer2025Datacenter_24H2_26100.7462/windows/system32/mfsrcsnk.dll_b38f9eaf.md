# Binary Specification: mfsrcsnk.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\mfsrcsnk.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `b38f9eaf1cb8bdcb32292b5bf88c750c9a85c656723abcd52a1100a6cf2932a0`
* **Total Exported Functions:** 4

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x7E220` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DllGetClassObject` | `0x7E240` | 67,568 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `MFCreateWAVEMediaSink` | `0x8EA30` | 980 | UnwindData |  |
| 3 | `MFCreateAVIMediaSink` | `0xA9740` | 897 | UnwindData |  |
