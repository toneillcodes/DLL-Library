# Binary Specification: ninput.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\ninput.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `42f66d8f2af0ae8daeadb146aebb1fded27182dc71df1b575b248f9856f8a757`
* **Total Exported Functions:** 40

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `CreateInteractionContext` | `0xD8F0` | 249 | UnwindData |  |
| 21 | `ResetInteractionContext` | `0xF780` | 2,160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `SetInteractionConfigurationInteractionContext` | `0xFFF0` | 48 | UnwindData |  |
| 26 | `SetMouseWheelParameterInteractionContext` | `0x12CB0` | 358 | UnwindData |  |
| 2500 | *Ordinal Only* | `0x133E0` | 1,760 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `StopInteractionContext` | `0x13AC0` | 183 | UnwindData |  |
| 2502 | *Ordinal Only* | `0x13B80` | 210 | UnwindData |  |
| 2505 | *Ordinal Only* | `0x13F50` | 1,171 | UnwindData |  |
| 12 | `GetStateInteractionContext` | `0x14550` | 541 | UnwindData |  |
| 1 | `DefaultInputHandler` | `0x15330` | 10 | UnwindData |  |
| 5 | `DestroyInteractionContext` | `0x2E860` | 98 | UnwindData |  |
| 15 | `ProcessBufferedPacketsInteractionContext` | `0x2EE20` | 221 | UnwindData |  |
| 2 | `AddPointerInteractionContext` | `0x36160` | 70 | UnwindData |  |
| 20 | `RemovePointerInteractionContext` | `0x39F20` | 88 | UnwindData |  |
| 18 | `RegisterOutputCallbackInteractionContext` | `0x3BAD0` | 3,536 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `GetInteractionConfigurationInteractionContext` | `0x3C8A0` | 123 | UnwindData |  |
| 28 | `SetPropertyInteractionContext` | `0x3CB50` | 1,520 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2506 | *Ordinal Only* | `0x3D140` | 1,111 | UnwindData |  |
| 19 | `RegisterOutputCallbackInteractionContext2` | `0x3D600` | 7,056 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `SetInertiaParameterInteractionContext` | `0x3F190` | 3,712 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `SetTranslationParameterInteractionContext` | `0x40010` | 2,976 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `SetHoldParameterInteractionContext` | `0x40BB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2501 | *Ordinal Only* | `0x40BD0` | 111 | UnwindData |  |
| 3 | `BufferPointerPacketsInteractionContext` | `0x42D30` | 30 | UnwindData |  |
| 17 | `ProcessPointerFramesInteractionContext` | `0x42D60` | 35 | UnwindData |  |
| 2508 | *Ordinal Only* | `0x4EF40` | 347 | UnwindData |  |
| 6 | `GetCrossSlideParameterInteractionContext` | `0x4F240` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `GetHoldParameterInteractionContext` | `0x4F270` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `GetInertiaParameterInteractionContext` | `0x4F2A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `GetMouseWheelParameterInteractionContext` | `0x4F2D0` | 147 | UnwindData |  |
| 11 | `GetPropertyInteractionContext` | `0x4F370` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `GetTapParameterInteractionContext` | `0x4F3C0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `GetTranslationParameterInteractionContext` | `0x4F440` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `ProcessInertiaInteractionContext` | `0x4F4C0` | 87 | UnwindData |  |
| 2507 | *Ordinal Only* | `0x4F520` | 372 | UnwindData |  |
| 22 | `SetCrossSlideParametersInteractionContext` | `0x4F900` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2504 | *Ordinal Only* | `0x4F950` | 108 | UnwindData |  |
| 27 | `SetPivotInteractionContext` | `0x4F9D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `SetTapParameterInteractionContext` | `0x4F9F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2503 | *Ordinal Only* | `0x4FA20` | 286 | UnwindData |  |
