# Binary Specification: CoreUIComponents.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\CoreUIComponents.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `88e2232bc44258a9d477a6952d22e0b9a37cb02390f239296e5564128217e962`
* **Total Exported Functions:** 24

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `CoreUIClientCreate` | `0x17580` | 203 | UnwindData |  |
| 4 | `CoreUICreateDuplicateWindowFactory` | `0x256D0` | 2,124 | UnwindData |  |
| 6 | `CoreUICreateICoreWindowFactoryEx` | `0x25FC0` | 440 | UnwindData |  |
| 7 | `CoreUIFactoryCreate` | `0x2AB00` | 88,720 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `CoreUIServerCreate` | `0x40590` | 216 | UnwindData |  |
| 12 | `DllGetActivationFactory` | `0x60D30` | 45 | UnwindData |  |
| 13 | `DllGetClassObject` | `0x60D60` | 172 | UnwindData |  |
| 11 | `DllCanUnloadNow` | `0x67D80` | 74 | UnwindData |  |
| 3 | `CoreUIConfigureTestHost` | `0xB0790` | 483,376 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `CoreUIClientTestCreate` | `0x1267C0` | 215 | UnwindData |  |
| 9 | `CoreUIServerTestCreate` | `0x1268A0` | 172 | UnwindData |  |
| 17 | `MinUserNotifyOneCoreTransformMode` | `0x15FC10` | 69,648 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `MinUserRegisterPointerInputTarget` | `0x170C20` | 222 | UnwindData |  |
| 20 | `MinUserReregisterPointerInputTargets` | `0x170D00` | 102 | UnwindData |  |
| 21 | `MinUserUnregisterPointerInputTarget` | `0x170D70` | 159 | UnwindData |  |
| 23 | `ServiceMain` | `0x170E10` | 305 | UnwindData |  |
| 24 | `SvchostPushServiceGlobals` | `0x170F50` | 3,952 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `CoreUICreateICoreWindowFactory` | `0x171EC0` | 189 | UnwindData |  |
| 10 | `CreateNavigationClientWindowAdapter` | `0x171F80` | 1,287 | UnwindData |  |
| 22 | `RegisterNavigationClientWindowAdapter` | `0x172490` | 627 | UnwindData |  |
| 14 | `MinUserGetInputHost` | `0x172A40` | 74 | UnwindData |  |
| 15 | `MinUserGetInputRoutingInfo` | `0x172A90` | 136 | UnwindData |  |
| 16 | `MinUserInputInitialize` | `0x172B20` | 282 | UnwindData |  |
| 19 | `MinUserRequestViewHitTest` | `0x172C40` | 141 | UnwindData |  |
