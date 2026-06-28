# Binary Specification: VsGraphicsHelper.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\VsGraphicsHelper.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `9aba66217d61fdfc3e7512e91f39a16e5ead7a7ad3cc33f201511923775ae958`
* **Total Exported Functions:** 10

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 8 | `VsgDbgInitDelayed` | `0x2B900` | 184 | UnwindData |  |
| 7 | `VsgDbgInit` | `0x2B9C0` | 57 | UnwindData |  |
| 10 | `VsgDbgUnInit` | `0x2BA00` | 28 | UnwindData |  |
| 9 | `VsgDbgToggleHUD` | `0x2BA20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `VsgDbgCaptureCurrentFrame` | `0x2BA40` | 57 | UnwindData |  |
| 3 | `VsgDbgBeginCapture` | `0x2BA80` | 47 | UnwindData |  |
| 6 | `VsgDbgEndCapture` | `0x2BAB0` | 42 | UnwindData |  |
| 5 | `VsgDbgCopy` | `0x2BAE0` | 112 | UnwindData |  |
| 2 | `VsgDbgAddHUDMessage` | `0x2BB50` | 346,288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `DisableD3DSpy` | `0x80400` | 479,420 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
