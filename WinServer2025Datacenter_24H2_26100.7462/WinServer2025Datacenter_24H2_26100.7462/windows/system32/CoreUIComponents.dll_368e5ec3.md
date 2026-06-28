# Binary Specification: CoreUIComponents.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\CoreUIComponents.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `368e5ec35696ba94422ad965577ef6021cbc837d20d6215b8b3e38eb268afd6a`
* **Total Exported Functions:** 24

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `CoreUIClientCreate` | `0x17580` | 203 | UnwindData |  |
| 4 | `CoreUICreateDuplicateWindowFactory` | `0x256D0` | 2,124 | UnwindData |  |
| 6 | `CoreUICreateICoreWindowFactoryEx` | `0x25FC0` | 440 | UnwindData |  |
| 7 | `CoreUIFactoryCreate` | `0x2AB00` | 88,576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `CoreUIServerCreate` | `0x40500` | 216 | UnwindData |  |
| 12 | `DllGetActivationFactory` | `0x610E0` | 45 | UnwindData |  |
| 13 | `DllGetClassObject` | `0x61110` | 172 | UnwindData |  |
| 11 | `DllCanUnloadNow` | `0x67F60` | 74 | UnwindData |  |
| 3 | `CoreUIConfigureTestHost` | `0xB05A0` | 482,272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `CoreUIClientTestCreate` | `0x126180` | 215 | UnwindData |  |
| 9 | `CoreUIServerTestCreate` | `0x126260` | 172 | UnwindData |  |
| 17 | `MinUserNotifyOneCoreTransformMode` | `0x15F400` | 69,744 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `MinUserRegisterPointerInputTarget` | `0x170470` | 222 | UnwindData |  |
| 20 | `MinUserReregisterPointerInputTargets` | `0x170550` | 102 | UnwindData |  |
| 21 | `MinUserUnregisterPointerInputTarget` | `0x1705C0` | 159 | UnwindData |  |
| 23 | `ServiceMain` | `0x170660` | 305 | UnwindData |  |
| 24 | `SvchostPushServiceGlobals` | `0x1707A0` | 3,952 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `CoreUICreateICoreWindowFactory` | `0x171710` | 189 | UnwindData |  |
| 10 | `CreateNavigationClientWindowAdapter` | `0x1717D0` | 1,287 | UnwindData |  |
| 22 | `RegisterNavigationClientWindowAdapter` | `0x171CE0` | 627 | UnwindData |  |
| 14 | `MinUserGetInputHost` | `0x172290` | 74 | UnwindData |  |
| 15 | `MinUserGetInputRoutingInfo` | `0x1722E0` | 136 | UnwindData |  |
| 16 | `MinUserInputInitialize` | `0x172370` | 282 | UnwindData |  |
| 19 | `MinUserRequestViewHitTest` | `0x172490` | 141 | UnwindData |  |
