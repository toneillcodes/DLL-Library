# Binary Specification: InputHost.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\InputHost.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `1079baf21b98d82ac6e4e87334524fe392c6c30b338b20c2bdf09b6da9beda28`
* **Total Exported Functions:** 33

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2629 | `DllGetActivationFactory` | `0x2FBC0` | 1,068 | UnwindData |  |
| 2601 | *Ordinal Only* | `0x36770` | 63 | UnwindData |  |
| 2605 | *Ordinal Only* | `0x36980` | 97 | UnwindData |  |
| 2604 | *Ordinal Only* | `0x38530` | 159 | UnwindData |  |
| 2628 | `DllCanUnloadNow` | `0x40660` | 101 | UnwindData |  |
| 2622 | `CreateInputDeviceWatcher` | `0x50890` | 112 | UnwindData |  |
| 2615 | `SetInputFocus` | `0x54AA0` | 28,720 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2624 | `CreateInputHostForProcess` | `0x5BAD0` | 132 | UnwindData |  |
| 2620 | `CreateGenericInputHost` | `0x63260` | 16,944 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2611 | `CreateDragOperationPrivate` | `0x67490` | 5,744 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2612 | `CreatePointerInputHost` | `0x67490` | 5,744 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2613 | `CreateTouchInputHost` | `0x67490` | 5,744 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2614 | `SetInputDeviceIndicatorState` | `0x67490` | 5,744 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2616 | `TouchInputHostCreate` | `0x67490` | 5,744 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2617 | `CreateComboButtonProxy` | `0x68B00` | 207 | UnwindData |  |
| 2623 | `CreateInputHost` | `0x69230` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2626 | `CreateMPCManagerClient` | `0x69240` | 440 | UnwindData |  |
| 2627 | `CreateViewHitTestRequestClient` | `0x69400` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2631 | `SetInputButtonEnabledOnIdle` | `0x69410` | 118 | UnwindData |  |
| 2632 | `SetInputDeviceRepeatParameters` | `0x69490` | 123 | UnwindData |  |
| 2633 | `ViewHitTestClientCreate` | `0x69520` | 1,936 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2610 | *Ordinal Only* | `0x69CB0` | 316 | UnwindData |  |
| 2608 | *Ordinal Only* | `0x69E00` | 357 | UnwindData |  |
| 2602 | *Ordinal Only* | `0x69F70` | 101 | UnwindData |  |
| 2603 | *Ordinal Only* | `0x69FE0` | 101 | UnwindData |  |
| 2607 | *Ordinal Only* | `0x6A050` | 221 | UnwindData |  |
| 2609 | *Ordinal Only* | `0x6A140` | 350 | UnwindData |  |
| 2606 | *Ordinal Only* | `0x6A2B0` | 104 | UnwindData |  |
| 2618 | `CreateCursorClient` | `0x6A320` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2619 | `CreateCursorManager` | `0x6A330` | 51 | UnwindData |  |
| 2630 | `DllGetClassObject` | `0x7AA90` | 69 | UnwindData |  |
| 2625 | `CreateInputSystemClientConnection` | `0x7AF70` | 111 | UnwindData |  |
| 2621 | `CreateHeatGripServiceClient` | `0x14D900` | 201 | UnwindData |  |
