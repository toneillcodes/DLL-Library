# Binary Specification: CoreMas.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\CoreMas.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a167ee305146f44f4936cab50e29a391680ba63214f38e67627d5f4b1e1ddcf2`
* **Total Exported Functions:** 12

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 11 | `RunUnimicProcessor` | `0x19470` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `CreateUnimicFilter` | `0x19490` | 9,668 | UnwindData |  |
| 5 | `GetUnimicFilterInputPortCount` | `0x1D820` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `GetUnimicProcessorInputChannelCount` | `0x1D820` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `GetUnimicProcessorOutputChannelCount` | `0x1D840` | 73,488 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `SetUnimicFilterInputPort` | `0x1D840` | 73,488 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `CreateUnimicProcessor` | `0x2F750` | 97 | UnwindData |  |
| 3 | `DeleteUnimicFilter` | `0x2F7C0` | 31 | UnwindData |  |
| 4 | `DeleteUnimicProcessor` | `0x2F7F0` | 69 | UnwindData |  |
| 6 | `GetUnimicFilterOutputPort` | `0x2F840` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `GetUnimicFilterOutputPortCount` | `0x2F860` | 9,028 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `GetUnimicProcessorDelay` | `0x2F860` | 9,028 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |
