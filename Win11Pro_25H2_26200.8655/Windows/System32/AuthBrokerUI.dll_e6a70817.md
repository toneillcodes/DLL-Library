# Binary Specification: AuthBrokerUI.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\AuthBrokerUI.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `e6a70817fb605c6d0bd60736c31e479449101c9ee569369f6c5cb0250aef7fe4`
* **Total Exported Functions:** 9

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `CreateWndMgmt` | `0x2CE0` | 168 | UnwindData |  |
| 2 | `DirectUIInitProc` | `0x2D90` | 45 | UnwindData |  |
| 3 | `DirectUIInitThread` | `0x2DD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DirectUIUnInitProc` | `0x2DF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `DirectUIUnInitThread` | `0x2E10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `FreeWndMgmt` | `0x2E30` | 69 | UnwindData |  |
| 7 | `WabCreateWebRuntimeCoreControl` | `0x3610` | 145 | UnwindData |  |
| 8 | `WabCreateWebRuntimeCoreVisualViewport` | `0x36B0` | 145 | UnwindData |  |
| 9 | `WabImmDisableLegacyIME` | `0x3750` | 60,364 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
