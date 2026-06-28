# Binary Specification: AuthBrokerUI.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\AuthBrokerUI.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `7dd5752215a1f1b8dcba4661e983405f50ec40eef338a18ce9dc7f97374151e3`
* **Total Exported Functions:** 9

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `CreateWndMgmt` | `0x3980` | 168 | UnwindData |  |
| 2 | `DirectUIInitProc` | `0x3A30` | 45 | UnwindData |  |
| 3 | `DirectUIInitThread` | `0x3A70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DirectUIUnInitProc` | `0x3A90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DirectUIUnInitThread` | `0x3AB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `FreeWndMgmt` | `0x3AD0` | 69 | UnwindData |  |
| 7 | `WabCreateWebRuntimeCoreControl` | `0x42B0` | 145 | UnwindData |  |
| 8 | `WabCreateWebRuntimeCoreVisualViewport` | `0x4350` | 145 | UnwindData |  |
| 9 | `WabImmDisableLegacyIME` | `0x43F0` | 73,748 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
