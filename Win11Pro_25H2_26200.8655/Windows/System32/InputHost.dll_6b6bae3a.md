# Binary Specification: InputHost.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\InputHost.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `6b6bae3ada7f250b872cc5ab3968b5992451425b69691256c2429058af3f3271`
* **Total Exported Functions:** 33

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2629 | `DllGetActivationFactory` | `0x320F0` | 1,068 | UnwindData |  |
| 2601 | *Ordinal Only* | `0x38CC0` | 63 | UnwindData |  |
| 2605 | *Ordinal Only* | `0x38ED0` | 97 | UnwindData |  |
| 2604 | *Ordinal Only* | `0x39760` | 159 | UnwindData |  |
| 2628 | `DllCanUnloadNow` | `0x3EE70` | 101 | UnwindData |  |
| 2622 | `CreateInputDeviceWatcher` | `0x4F860` | 112 | UnwindData |  |
| 2615 | `SetInputFocus` | `0x53FA0` | 29,520 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2624 | `CreateInputHostForProcess` | `0x5B2F0` | 132 | UnwindData |  |
| 2620 | `CreateGenericInputHost` | `0x62AA0` | 16,960 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2611 | `CreateDragOperationPrivate` | `0x66CE0` | 5,744 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2612 | `CreatePointerInputHost` | `0x66CE0` | 5,744 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2613 | `CreateTouchInputHost` | `0x66CE0` | 5,744 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2614 | `SetInputDeviceIndicatorState` | `0x66CE0` | 5,744 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2616 | `TouchInputHostCreate` | `0x66CE0` | 5,744 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2617 | `CreateComboButtonProxy` | `0x68350` | 207 | UnwindData |  |
| 2623 | `CreateInputHost` | `0x68A80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2626 | `CreateMPCManagerClient` | `0x68A90` | 440 | UnwindData |  |
| 2627 | `CreateViewHitTestRequestClient` | `0x68C50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2631 | `SetInputButtonEnabledOnIdle` | `0x68C60` | 118 | UnwindData |  |
| 2632 | `SetInputDeviceRepeatParameters` | `0x68CE0` | 123 | UnwindData |  |
| 2633 | `ViewHitTestClientCreate` | `0x68D70` | 1,936 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2610 | *Ordinal Only* | `0x69500` | 316 | UnwindData |  |
| 2608 | *Ordinal Only* | `0x69650` | 357 | UnwindData |  |
| 2602 | *Ordinal Only* | `0x697C0` | 101 | UnwindData |  |
| 2603 | *Ordinal Only* | `0x69830` | 101 | UnwindData |  |
| 2607 | *Ordinal Only* | `0x698A0` | 221 | UnwindData |  |
| 2609 | *Ordinal Only* | `0x69990` | 350 | UnwindData |  |
| 2606 | *Ordinal Only* | `0x69B00` | 104 | UnwindData |  |
| 2618 | `CreateCursorClient` | `0x69B70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2619 | `CreateCursorManager` | `0x69B80` | 51 | UnwindData |  |
| 2630 | `DllGetClassObject` | `0x7A750` | 69 | UnwindData |  |
| 2625 | `CreateInputSystemClientConnection` | `0x7AC90` | 111 | UnwindData |  |
| 2621 | `CreateHeatGripServiceClient` | `0x14D2E0` | 201 | UnwindData |  |
